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
    if decibel > 75:
        publishToTipboard.update_just_value_config("noise", "green")
    elif decibel > 60:
        publishToTipboard.update_just_value_config("noise", "yellow")
    else:
        publishToTipboard.update_just_value_config("noise", "red")

    #Take average of decibels #######################################################
    avgCount += 1
    decibelSum += int(decibel)
    avgDecibel = decibelSum / avgCount

    # SEND AVG DB ################################################################
    if avgDecibel > 75:
        publishToTipboard.update_just_value_config("avg", "green")
    elif avgDecibel > 60:
        publishToTipboard.update_just_value_config("avg", "yellow")
    else:
        publishToTipboard.update_just_value_config("avg", "red")

    #I figured the car shouldnt move when the room is fairly quiet so I set it up so speed is 0
    #unless the DB is 40 or higher, can be easily adjusted.
    adjustedDecibel = decibel - threshold
    if(adjustedDecibel < 0):
        adjustedDecibel = 0
    percentSpeed = (adjustedDecibel / maxSpeed)*100
    if(percentSpeed > highestSpeed):
        highestSpeed = percentSpeed

    # SEND SPEED(simple_percent) ################################################################
    if  percentSpeed > 15:
        publishToTipboard.update_simple_percentage_config("simplepercentage", "green")
    elif percentSpeed > 10:
        publishToTipboard.update_siimple_percentage_config("simplepercentage", "yellow")
    else:
        publishToTipboard.update_simple_percentage_config("simplepercentage", "red")

    #publish results to tipboard#######################################################
    publishToTipboard.update_simple_percentage("simplepercentage","Percent Speed", "maybe this tile instead?", \
                                               "{:3.0f}%".format(percentSpeed), "idk", \
                                               "{:3.0f}%".format(highestSpeed), "something", "Highest Speed")
    publishToTipboard.update_big_value("bigvalue", "Trump? really?", "Current Speed", \
                                       "{:3.2f}%".format(percentSpeed), "Upper Left", \
                                       str(round(avgDecibel,0)), "Lower Left", \
                                       str(round(avgDecibel,0)), "Upper Right", \
                                       str(round(avgDecibel,0)), "Lower Right", \
                                       str(round(avgDecibel,0)))
    publishToTipboard.update_just_value("avg", "Average Level", "Decibel", str(round(avgDecibel,0)))
    publishToTipboard.update_just_value("noise", "Current Level", "Decibel", str(round(decibel,0)))
        
    #########################################################################################


    ## PRINT TO CONSOLE #####
    bars = "#" * int((decibel - 35))
    print("%05d %03dDB %s"%(counter,decibel,bars))
    
    
    time.sleep(.1)



stream.stop_stream()
stream.close()
audio.terminate()
