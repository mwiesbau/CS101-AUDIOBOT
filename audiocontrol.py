import pyaudio
import numpy as np
import audioop
import math
import time
import publishToTipboard

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True,
                    frames_per_buffer=2**10)

counter = 0
avgCount = 0
decibelSum = 0
avgDecibel = 0

while True:
    counter += 1
    data = np.fromstring(stream.read(2**10),dtype=np.int16)
    rms = audioop.rms(data,2)
    

    # WEIRD ISSUE ON SOME WINDOWS PC's 
    if rms == 0:
        continue
    
    # SEND THE DB READING TO TIPBOARD ########################################################
    decibel = 20 * math.log10(rms)
    if decibel > 60:
        publishToTipboard.update_just_value_config("noise", "yellow")
    elif decibel > 75:
        publishToTipboard.update_just_value_config("noise", "red")
    else:
        publishToTipboard.update_just_value_config("noise", "green")

    #Take average of decibels #######################################################
    avgCount += 1
    decibelSum += int(decibel)
    avgDecibel = decibelSum / avgCount

    #publish results to tipboard#######################################################
    
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
