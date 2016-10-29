

import RPi.GPIO as GPIO
import time
import threading
from threading import Thread

class Motor():


	
	def __init__(self, pwmPin, pinRed, pinBlack, pinRotation):
		self.pwmPin = pwmPin
		self.pinRed = pinRed
		self.pinBlack = pinBlack
		self.pinRotation = pinRotation
		self.counter = 0
	

		# SETUP GPIO PINS FOR THE MOTOR
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pwmPin, GPIO.OUT)
		GPIO.setup(self.pinRed, GPIO.OUT)
		GPIO.setup(self.pinBlack, GPIO.OUT)

		# SETUP GPIO PINS FOR DECODER
		GPIO.setup(self.pinRotation, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		self.rotation = GPIO.input(pinRotation)

		# PULSE WIDTH MODULATION SET TO FREQ 255
		self.pwm = GPIO.PWM(self.pwmPin, 255)


	def countRotation(self, channel):
		self.counter += 1
		print(self.counter)
		#if self.counter == 10:
		#	self.pwm.stop()

		
		
	
	def forward(self, frequency, duty=100):		
		GPIO.add_event_detect(self.pinRotation, GPIO.RISING, callback = self.countRotation)
		self.pwm.start(duty)
		GPIO.output(self.pinRed, GPIO.HIGH)
		GPIO.output(self.pinBlack, GPIO.LOW)
		

	def backward(self, frequency, duty=100):
		self.pwm.start(duty)
		GPIO.output(self.pinRed, GPIO.LOW)
		GPIO.output(self.pinBlack, GPIO.HIGH)


	def stop(self):
		self.pwm.stop()

			

def teardown():
	GPIO.cleanup()


if __name__ == "__main__":
	
	# INITIALIZE RIGHT MOTOR
	rightMotor = Motor(40, 38, 36, 16)
	rightPWM = rightMotor.backward(255, 30)
	
	# INITIALIZE LEFT MOTOR
	leftMotor = Motor(33, 35, 37, 18)
	leftPWM = leftMotor.backward(255, 30)

	time.sleep(20)
#	rightMotor.stop()
#	leftMotor.stop()
	

#	time.sleep(10)
#	print("exiting")	

	teardown()
	
