import pyaudio
import numpy as np
import sys


audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True,
                    frames_per_buffer=2**10)


counter = 0

while True:
   # ch = sys.stdin.buffer.read(1)
   # if ch=='\x1b':
   #     exit(0)
    counter += 1
    data = np.fromstring(stream.read(2**10),dtype=np.int16)
    peak = np.average(np.abs(data))*2
    bars = "#" * int(150*peak/2**16)
    print("%05d %05d %s"%(counter,peak,bars))


stream.stop_stream()
stream.close()
audio.terminate()
