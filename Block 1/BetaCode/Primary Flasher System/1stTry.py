#This is my first try at control code for the FlasherPi class
import time
import os
import RPi.GPIO as GPIO
import shutil
import math
from lxml import html
import requests

Relay1ControlPin = 24
GPIO.cleanup() #resets GPIO pins to accept button inputs
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Relay1ControlPin, GPIO.OUT) #sets input to GPIO pin#24. Button will be wired to this pin and the ground pin
print GPIO.RPI_INFO #shows the information about the RasPi
response = 1

def GetStatus():
	print "I got run!!"
	page = requests.get('http://192.168.86.114/index.html')
	tree = html.fromstring(page.content)
	SystemState = tree.xpath('//h1/text()')
	print "Recieved System Status", SystemState
GetStatus()
def PingWebServer():
	print "Ping Got Run"
	response = os.system("ping -c 1 " + "192.168.86.114") #this is for home testing, not the actual deployment!!
	if response == 0:
		print 'Webserver is up!'
	else:
		print 'Webserver is down!'

def FlashFailureMode(): #blinks once per second
	while SystemState == 'Fault':
		GetStatus()
		GPIO.output(Relay1ControlPin, 1)
		time.sleep(0.1)
		GPIO.output(Relay1ControlPin, 0)
		time.sleep(1)

def FlashEmergencyMode():
	while SystemState == 'Emergency':
		GetStatus()
                GPIO.output(Relay1ControlPin, 1)
                time.sleep(0.4)
                GPIO.output(Relay1ControlPin, 0)
                time.sleep(0.3)

while True:
	PingWebServer()
	GetStatus()
	if response == 0:
		GetStatus()
		print "This better fucking work", SystemState
		if SystemState == 'Emergency':
			print "Emergency got run"
			FlashEmergencyMode()
		else:
			if (SystemState == 'Nominal'):
				GPIO.output(Relay1ControlPin, 0)
			else: FlashFailureMode()
	else:
		FlashFailureMode()
