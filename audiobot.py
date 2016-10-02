import pyaudio
import numpy as np
import sys
import audioop
import math

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True,
                    frames_per_buffer=2**10)

counter = 0

while True:
    counter += 1
    data = np.fromstring(stream.read(2**10),dtype=np.int16)
    rms = audioop.rms(data,2)
    decibel = 20 * math.log10(rms)
    bars = "#" * int((decibel - 35))
    print("%05d %03dDB %s"%(counter,decibel,bars))


stream.stop_stream()
stream.close()
audio.terminate()
