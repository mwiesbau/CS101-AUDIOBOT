

import RPi.GPIO as GPIO
import time
import threading

class Motor(threading.Thread):


	def __init__(self, pwmPin, pinRed, pinBlack, pinRotation, name):
		threading.Thread.__init__(self)

		self.pwmPin = pwmPin
		self.pinRed = pinRed
		self.pinBlack = pinBlack
		self.pinRotation = pinRotation
		self.counter = 0
		self.name = name

		# SETUP GPIO PINS FOR THE MOTOR
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pwmPin, GPIO.OUT)
		GPIO.setup(self.pinRed, GPIO.OUT)
		GPIO.setup(self.pinBlack, GPIO.OUT)

		# SETUP GPIO PINS FOR DECODER
		GPIO.setup(self.pinRotation, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		self.rotation = GPIO.input(pinRotation)





	def run(self):
		print("Starting " + self.name + " motor")
		# PULSE WIDTH MODULATION SET TO FREQ 255
		self.pwm = GPIO.PWM(self.pwmPin, 255)


	def countRotations(self, channel):
		self.counter += 1

	def getRotations(self):
		return self.counter

	def resetRotations(self):
		self.counter = 0
		
		
	
	def forward(self, frequency, duty=100):		
		GPIO.add_event_detect(self.pinRotation, GPIO.RISING, callback = self.countRotations)
		self.pwm.start(duty)
		GPIO.output(self.pinRed, GPIO.HIGH)
		GPIO.output(self.pinBlack, GPIO.LOW)
		

	def backward(self, frequency, duty=100):
		GPIO.add_event_detect(self.pinRotation, GPIO.RISING, callback=self.countRotations)
		self.pwm.start(duty)
		GPIO.output(self.pinRed, GPIO.LOW)
		GPIO.output(self.pinBlack, GPIO.HIGH)


	def stop(self):
		self.pwm.stop()

			

def teardown():
	GPIO.cleanup()


if __name__ == "__main__":
	
	# INITIALIZE RIGHT MOTOR

	


	time.sleep(20)
#	rightMotor.stop()
#	leftMotor.stop()
	

#	time.sleep(10)
#	print("exiting")	

	teardown()
	
