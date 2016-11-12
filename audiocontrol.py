import pyaudio
import numpy as np
import audioop
import math
import time
import publishToTipboard

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True,
                    frames_per_buffer=2**10)

threshold = 40.0
counter = 0
avgCount = 0
decibelSum = 0
avgDecibel = 0
percentSpeed = 0
highestSpeed = 0
maxSpeed = 140.0 - threshold
adjustedDecibel = 0.0

while True:
    counter += 1
    data = np.fromstring(stream.read(2**10),dtype=np.int16)
    rms = audioop.rms(data,2)
    

    # WEIRD ISSUE ON SOME WINDOWS PC's 
    if rms == 0:
        continue

    # SEND THE DB READING TO TIPBOARD ########################################################
    decibel = 20 * math.log10(rms)
    publishToTipboard.update_just_value_config("rednoise", "#FF9618")
    publishToTipboard.update_just_value_config("bluenoise", "blue")

    #Take average of decibels #######################################################
    avgCount += 1
    decibelSum += int(decibel)
    avgDecibel = decibelSum / avgCount

    # SEND AVG DB ################################################################
    publishToTipboard.update_just_value_config("redavg", "#FF9618")
    publishToTipboard.update_just_value_config("blueavg", "blue")

    #I figured the car shouldnt move when the room is fairly quiet so I set it up so speed is 0
    #unless the DB is 40 or higher, can be easily adjusted.
    adjustedDecibel = decibel - threshold
    if(adjustedDecibel < 0):
        adjustedDecibel = 0
    percentSpeed = (adjustedDecibel / maxSpeed)*100
    if(percentSpeed > highestSpeed):
        highestSpeed = percentSpeed

    # SEND SPEED(big_data) ################################################################
    publishToTipboard.update_big_value_config("redbigvalue", "#FF9618")
    publishToTipboard.update_big_value_config("bluebigvalue", "blue")



    #publish results to tipboard#######################################################
    publishToTipboard.update_big_value("redbigvalue", "Trump? really?", "Current Speed", \
                                       "{:3.2f}%".format(percentSpeed), "Distance", \
                                       decibelSum/200, "Max Speed", \
                                       int(highestSpeed))
    publishToTipboard.update_big_value("bluebigvalue", "Trump? really?", "Current Speed", \
                                       "{:3.2f}%".format(percentSpeed), "Distance", \
                                       decibelSum/200, "Max Speed", \
                                       int(highestSpeed))
    publishToTipboard.update_just_value("redavg", "Average Level", "Decibel", str(round(avgDecibel,0)))
    publishToTipboard.update_just_value("blueavg", "Average Level", "Decibel", str(round(avgDecibel,0)))
    publishToTipboard.update_just_value("rednoise", "Current Level", "Decibel", str(round(decibel,0)))
    publishToTipboard.update_just_value("bluenoise", "Current Level", "Decibel", str(round(decibel,0)))
    publishToTipboard.update_pie_chart("maxspeedpiechart", "Max Speed", "blue", "orange", int(highestSpeed), avgDecibel)
    publishToTipboard.update_pie_chart("distancepiechart", "Distance", "blue", "orange", \
                                       avgDecibel, int(highestSpeed))
        
    #########################################################################################


    ## PRINT TO CONSOLE #####
    bars = "#" * int((decibel - 35))
    print("%05d %03dDB %s"%(counter,decibel,bars))
    
    
    time.sleep(.1)



stream.stop_stream()
stream.close()
audio.terminate()
