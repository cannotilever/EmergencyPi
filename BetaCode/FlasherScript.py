#This is my third try for the Flasher Control Computer Code, as part of the EmergencyPi system
from playsound import playsound
import time
import os
import RPi.GPIO as GPIO
import shutil
import math
from lxml import html
import requests
from subprocess import call

Relay1ControlPin = 15
GPIO.cleanup() #resets GPIO pins to accept button inputs
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Relay1ControlPin, GPIO.OUT) #sets input to GPIO pin#24. Button will be wired to this pin and the ground pin
print GPIO.RPI_INFO #shows the information about the RasPi
loopcounter = 0
page = requests.get('http://192.168.32.11/generalAlarm.html')
tree = html.fromstring(page.content)
status = tree.xpath('//h1/text()')
print "Recieved System Status", status
PingFailedCounter = 0
call(['espeak "Flasher System Started." 2>/dev/null'], shell=True)
def FlashPattern(status):
	if (status == ['Emergency']):
		print "EmergencyGotRun"
		os.system("mpg123 " + "/home/pi/Music/tos_red_alert_2.mp3")
		GPIO.output(Relay1ControlPin, 1)
		PingWebServer()
		CheckForEndOfState()
	if (status == ['Fault']):
		print 'FaultFlash got run'
		call(['espeak "System alert. Repairs needed!" 2>/dev/null'], shell=True)
		GPIO.output(Relay1ControlPin, 1)
		time.sleep(2)
		GPIO.output(Relay1ControlPin, 0)
		time.sleep(0.5)
		CheckForEndOfState()
	if (status == ['Nominal']):
		GPIO.output(Relay1ControlPin, 0)
		time.sleep(0.1)
		CheckForEndOfState()
def CheckForEndOfState():
	global page, tree, status
	page = requests.get('http://192.168.32.11/generalAlarm.html')
	tree = html.fromstring(page.content)
	status = tree.xpath('//h1/text()')
	print "Recieved System Status", status
def PingWebServer():
	response = os.system("ping -c 1 " + "192.168.32.11") #this is for home testing, not the actual deployment!!
        if response == 0:
                print 'Webserver is up!'
		PingFailedCounter = 0
        else:
                print 'Webserver is UnReachable!'
		PingFailedCounter += 1

while True:
	global page, tree, status
        loopcounter += 1 #for experimentation only
	PingWebServer()
	time.sleep(0.05)
	if (PingFailedCounter != 1):
		CheckForEndOfState()
	else:
		PingWebServer()
	FlashPattern(status)
	if (PingFailedCounter >= 5):
		print "Cannot contact server, rebooting."
		call(['espeak "Cannot Contact server, rebooting now" 2>/dev/null'], shell=True)
		time.sleep(5)
		os.system("sudo shutdown now")
	if(status != ['Emergency']) or (status != ['Nominal']):
		status = 'Fault'
print "if you see this, Something is very wrong!!"
