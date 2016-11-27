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
seconds = 300
stage = 0 #0 = orange; 1 = break; 2 = blue

while True:
    counter += 1
    data = np.fromstring(stream.read(2**10),dtype=np.int16)
    rms = audioop.rms(data,2)

   # seconds -= 3
   # if (seconds//10) < 0:
        #stage+=1
       # seconds = 300
    # WEIRD ISSUE ON SOME WINDOWS PC's 
    if rms == 0:
        continue

    #ORANGE TURN#########################
    if 1:
        # SEND THE DB READING TO TIPBOARD ########################################################
        decibel = 20 * math.log10(rms)

        #Take average of decibels #######################################################
     #   avgCount += 1
     #   decibelSum += int(decibel)
      #  avgDecibel = decibelSum / avgCount

        #I figured the car shouldnt move when the room is fairly quiet so I set it up so speed is 0
        #unless the DB is 40 or higher, can be easily adjusted.
        #adjustedDecibel = decibel - threshold
        #if(adjustedDecibel < 0#adjustedDecibel = 0
        #percentSpeed = (adjustedDecibel / maxSpeed)*100
        #if(percentSpeed > highestSpeed):
            #highestSpeed = percentSpeed
        #publish results to tipboard#######################################################   
        publishToTipboard.update_just_value_config("orangenoise", "#FF9618")
        publishToTipboard.update_just_value_config("orangeavg", "#FF9618")
        publishToTipboard.update_big_value_config("orangebigvalue", "#FF9618")
        publishToTipboard.update_big_value("orangebigvalue", "", "Current Speed", \
                                           "{:3.2f}%".format(percentSpeed), "Distance", \
                                           decibelSum/200, "Max Speed", \
                                           int(highestSpeed))
        publishToTipboard.update_just_value("orangeavg", "Average Level", "", str(round(decibel,0)))
        publishToTipboard.update_just_value("orangenoise", "Current Level", "", str(round(decibel,0)))
        publishToTipboard.update_pie_chart("maxspeedpiechart", "Max Speed", "blue", "orange", int(highestSpeed), avgDecibel)
      #  publishToTipboard.update_just_value_config("timer", "#FF9618")
      #  publishToTipboard.update_just_value("timer", "Timer", "", (seconds//10))

    #BLUE TURN########################
    if 2:
        # SEND THE DB READING TO TIPBOARD ########################################################
        decibel = 20 * math.log10(rms)

        #Take average of decibels #######################################################
        #avgCount += 1
        #decibelSum += int(decibel)
        #avgDecibel = decibelSum / avgCount

        #I figured the car shouldnt move when the room is fairly quiet so I set it up so speed is 0
        #unless the DB is 40 or higher, can be easily adjusted.
       # adjustedDecibel = decibel - threshold
        #if(adjustedDecibel < 0):
            #adjustedDecibel = 0
        #percentSpeed = (adjustedDecibel / maxSpeed)*100
        #if(percentSpeed > highestSpeed):
            #highestSpeed = percentSpeed
        #publish results to tipboard#######################################################
        publishToTipboard.update_just_value_config("bluenoise", "blue")
        publishToTipboard.update_just_value_config("blueavg", "blue")
        publishToTipboard.update_big_value_config("bluebigvalue", "blue")
        publishToTipboard.update_big_value("bluebigvalue", "", "Current Speed", \
                                           "{:3.2f}%".format(percentSpeed), "Distance", \
                                           decibelSum/200, "Max Speed", \
                                           int(highestSpeed))
        publishToTipboard.update_just_value("blueavg", "Average Level", "", str(round(decibel,0)))
        publishToTipboard.update_just_value("bluenoise", "Current Level", "", str(round(decibel,0)))
        publishToTipboard.update_pie_chart("maxspeedpiechart", "Max Speed", "blue", "orange", int(highestSpeed), avgDecibel)
      #  publishToTipboard.update_just_value_config("timer", "blue")
       # publishToTipboard.update_just_value("timer", "Timer", "", (seconds//10))

    #BREAK############################
    #elif stage == 1:
      #  publishToTipboard.update_just_value_config("timer", "blue")
      #  publishToTipboard.update_just_value("timer", "Timer", "", (seconds//10)) 
    #########################################################################################


    ## PRINT TO CONSOLE #####
    bars = "#" * int((decibel - 35))
    print("%05d %03dDB %s"%(counter,decibel,bars))
    time.sleep(.1)
    

stream.stop_stream()
stream.close()
audio.terminate()
