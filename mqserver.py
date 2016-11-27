import zmq
import time
from publishToTipboard import update_just_value

context = zmq.Context()

sock = context.socket(zmq.SUB)

topicfilter = "DB"

sock.setsockopt(zmq.SUBSCRIBE, topicfilter)
sock.setsockopt(zmq.CONFLATE, 1)

sock.connect("tcp://127.0.0.1:5101")

while True:
        string = sock.recv()
        _, message = string.split()
        print "Echo: " + message
        update_just_value("rednoise", "TEST", "", message)
