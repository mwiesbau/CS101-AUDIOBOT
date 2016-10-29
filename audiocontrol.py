import pyaudio
import numpy as np
import sys
import audioop
import math
import time
import publish

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True,
                    frames_per_buffer=2**10)

counter = 0

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
        publish.update_just_value_config("noise", "yellow")
    elif decibel > 75:
        publish.update_just_value_config("noise", "red")
    else:
        publish.update_just_value_config("noise", "green")

    publish.update_just_value("noise", "Current Level", "Decibel", str(round(decibel,0)))
    #########################################################################################


    ## PRINT TO CONSOLE #####
    bars = "#" * int((decibel - 35))
    print("%05d %03dDB %s"%(counter,decibel,bars))
    
    time.sleep(.1)



stream.stop_stream()
stream.close()
audio.terminate()
