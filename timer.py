import time
import publishToTipboard

#ORANGE TURN
seconds = 30
while seconds >= 0:
    publishToTipboard.update_just_value_config("timer", "#FF9618")
    publishToTipboard.update_just_value("timer", "Timer", "", seconds)
    time.sleep(1)
    seconds -= 1
#BREAK
publishToTipboard.update_state()    
seconds = 15
while seconds >= 0:
    publishToTipboard.update_just_value_config("timer", "black")
    publishToTipboard.update_just_value("timer", "Timer", "", seconds)
    time.sleep(1)
    seconds -= 1
#BLUE TURN
publishToTipboard.update_state()
seconds = 30
while seconds >= 0:
    publishToTipboard.update_just_value_config("timer", "blue")
    publishToTipboard.update_just_value("timer", "Timer", "", seconds)
    time.sleep(1)
    seconds -= 1
