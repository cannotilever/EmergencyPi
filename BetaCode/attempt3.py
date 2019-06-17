# This is the second Itteration of the control code for the button control computer
import time
import os
import shutil
import math
import pifacedigitalio as pfio

pfio.init()
shutil.copyfile("/home/pi/Programming/WebPages/Nominal.html", "/var/www/html/index.html") #assume system is OK
time.sleep(0.5)
StartUpVar = pfio.digital_read(7) #we assume that the button is connected and not pressed when the program starts. To detect when the button is pressed, we just detect when button current state != button origional state
TimesButtonWasPressed = 0
CheckForTimer = False
print "The assumed button neutral value is:", StartUpVar
while True:
	if(pfio.digital_read(7)) != StartUpVar:
		print "Button Press Detected"
		if TimesButtonWasPressed == 0:
			print "Emergency mode detected!"
			shutil.copyfile("/home/pi/Programming/WebPages/Emergency.html", "/var/www/html/index.html")
			pfio.digital_write(0, 1)
			TimesButtonWasPressed = 1
			CheckForTimer = True
			TimerStartTime = time.time()
			time.sleep(2)
		else:
			if TimesButtonWasPressed > 0:
				print "Resetting to Nominal."
				shutil.copyfile("/home/pi/Programming/WebPages/Nominal.html", "/var/www/html/index.html")
				pfio.digital_write(0, 0)
				TimesButtonWasPressed = 0
				CheckForTimer = False
				time.sleep(2)
	else:
		#print "System has entered Idle Mode."
		if (CheckForTimer == True) and (time.time() - TimerStartTime > 3600):
			shutil.copyfile("/home/pi/Programming/WebPages/Fault.html", "/var/www/html/index.html")
			print "System Fault Detected!"
			pfio.digital_write(0, 0)
			break
		#else:
			#print "System Check OK"
print "System has failed, We'll get 'em next time"
