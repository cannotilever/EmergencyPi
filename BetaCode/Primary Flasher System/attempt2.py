# This is the second Itteration of the control code for the button control computer
import time
import os
import RPi.GPIO as GPIO
import shutil
import math

GPIO.cleanup() #resets GPIO pins to accept button inputs
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(24, GPIO.IN) #sets input to GPIO pin#24. Button will be wired to this pin and the ground pin
print GPIO.RPI_INFO #shows the information about the RasPi
shutil.copyfile("/home/pi/Programming/WebPages/Nominal.html", "/var/www/html/index.html") #assume system is OK
time.sleep(0.5)
StartUpVar = GPIO.input(24) #we assume that the button is connected and not pressed when the program starts. To detect when the button is pressed, we just detect when button current state != button origional state
TimesButtonWasPressed = 0
CheckForTimer = False
print "The assumed button neutral value is:", StartUpVar
while True:
	if(GPIO.input(24)) != StartUpVar:
		print "Button Press Detected"
		if TimesButtonWasPressed == 0:
			print "Emergency mode detected!"
			shutil.copyfile("/home/pi/Programming/WebPages/Emergency.html", "/var/www/html/index.html")
			TimesButtonWasPressed = 1
			CheckForTimer = True
			TimerStartTime = time.time()
			time.sleep(2)
		else:
			if TimesButtonWasPressed > 0:
				print "Resetting to Nominal."
				shutil.copyfile("/home/pi/Programming/WebPages/Nominal.html", "/var/www/html/index.html")
				TimesButtonWasPressed = 0
				CheckForTimer = False
				time.sleep(2)
	else:
		#print "System has entered Idle Mode."
		if (CheckForTimer == True) and (time.time() - TimerStartTime > 3600):
			shutil.copyfile("/home/pi/Programming/WebPages/Fault.html", "/var/www/html/index.html")
			print "System Fault Detected!"
			break
		#else:
			#print "System Check OK"
print "System has failed, We'll get 'em next time"
