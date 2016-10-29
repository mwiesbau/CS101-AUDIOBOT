from motorcontrol import Motor
import threading
import RPi.GPIO as GPIO
import time
import argparse

def stopRobot():
    GPIO.cleanup()


def setupLeftMotor():
    # INITIALIZE LEFT MOTOR
    leftMotor = Motor(33, 35, 37, 18)     ## SETS THE GPIO PINS
    #leftPWM = leftMotor.backward(255, 30)
    return leftMotor


def setupRightMotor():
    rightMotor = Motor(40, 38, 36, 16)    ## SETS THE GPIO PINS
    #rightPWM = rightMotor.backward(255, 30)


def startRobot(sleeptime, speed):

    leftMotor = setupLeftMotor()

    leftMotor.forward(255, speed)


    try:
        while True:
            print("Left Rotations = " + str(leftMotor.getRotations()))
            time.sleep(sleeptime)



    except KeyboardInterrupt:   # EXIT ON CTRL+C
        stopRobot()
        pass


if __name__ == ("__main__"):

    parser = argparse.ArgumentParser()
    parser.add_argument("sleep", help="sleep time in seconds")
    parser.add_argument("speed", help="wheelspeed")
    args = parser.parse_args()




    startRobot(args.sleep, args.speed)