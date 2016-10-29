from motorcontrol import Motor
import threading
import RPi.GPIO as GPIO
import time
import argparse

def stopRobot():
    GPIO.cleanup()


def setupLeftMotor():
    # INITIALIZE LEFT MOTOR
    leftMotor = Motor(33, 35, 37, 18, "left")     ## SETS THE GPIO PINS
    #leftPWM = leftMotor.backward(255, 30)
    return leftMotor


def setupRightMotor():
    rightMotor = Motor(40, 38, 36, 16, "right")    ## SETS THE GPIO PINS
    #rightPWM = rightMotor.backward(255, 30)
    return rightMotor


def startRobot(sleeptime, pwm, intensity, wheel):


    #if wheel == "left":
    #    cMotor = setupLeftMotor()

    #else:
    leftMotor = setupLeftMotor()
    rightMotor = setupRightMotor()


    leftMotor.forward(pwm, intensity)
    rightMotor.forward(pwm, intensity)

    try:
        while True:


            leftRot = leftMotor.getRotations()
            rightRot = rightMotor.getRotations()

            if leftRot > rightRot:
                rightMotor.increaseForward()

            if leftRot < rightRot:
                rightMotor.decreaseForward()

            print("LR = " + str(leftMotor.getRotations()) + "\tRR = " + str(rightMotor.getRotations()))


            time.sleep(sleeptime)



    except KeyboardInterrupt:   # EXIT ON CTRL+C
        stopRobot()
        pass


if __name__ == ("__main__"):

    parser = argparse.ArgumentParser()
    parser.add_argument("sleep", help="sleep time in seconds")
    parser.add_argument("intensity", help="value from 0 to 100")
    parser.add_argument("pwm", help="pwm value from 0 to 255")
    parser.add_argument("wheel", help="[left, right]")
    args = parser.parse_args()




    startRobot(float(args.sleep), float(args.pwm), float(args.intensity), args.wheel)