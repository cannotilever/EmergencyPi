# This is the second Itteration of the control code for the button control computer, It supports 2 buttons; 1 for primary alarm system, 1 for silent alarm system
import time
import os
import shutil
import math
import pifacedigitalio as pfio
from subprocess import call

pfio.init()
shutil.copyfile("/home/pi/Programming/WebPages/Nominal.html", "/var/www/html/index.html") #assume system is OK
time.sleep(0.5)
Button1StartUpVar = pfio.digital_read(7) #we assume that the button is connected and not pressed when the program starts. To detect when the button is pressed, we just detect when button current state != button origional state
Button2StartUpVar = pfio.digital_read(6) #silent alarm button
TimesButtonWasPressed = 0
#global CheckForTimer, GeneralAlarm, SilentAlarm, GeneralAlarmLast, SilentAlarmLast, allowSwitcher, AllowSwitcherTimer
CheckForTimer = False
GeneralAlarm = False
SilentAlarm = False
GeneralAlarmLast = False
SilentAlarmLast = False
allowSwitcher = True
AllowSwitcherTimer = time.time()

print "The assumed button 1 neutral value is:", Button1StartUpVar
print "The assumed button 2 neutral value is:", Button2StartUpVar
print "General alarm:", GeneralAlarm
def GeneralAlarmListener():
	global GeneralAlarm
	global AllowSwitcherTimer
	global GeneralAlarmLast
	GeneralAlarmLast = GeneralAlarm
	if((time.time()) - AllowSwitcherTimer) >= 2:
		allowSwitcher = True
	else:
		allowSwitcher = False
	if((pfio.digital_read(7)) != Button1StartUpVar) and allowSwitcher == True:
		AllowSwitcherTimer = time.time()
		print "Button 1 Press Detected!"
		if(GeneralAlarm == False):
			print "triggering emergency mode"
			GeneralAlarm = True
		else:
			print "Deactivating Emergency Mode!"
			GeneralAlarm = False
def SilentAlarmListener():
	global SilentAlarm
	global AllowSwitcherTimer
	global SilentAlarmLast
	SilentAlarmLast = SilentAlarm
        if((time.time()) - AllowSwitcherTimer) >= 2:
                allowSwitcher = True
        else:
                allowSwitcher = False
        if((pfio.digital_read(6)) != Button2StartUpVar) and allowSwitcher == True:
                AllowSwitcherTimer = time.time()
                print "Button 6 Press Detected!"
                if(SilentAlarm == False):
                        print "triggering emergency mode"
			SilentAlarm = True
                else:
                        print "Deactivating Emergency Mode!"
                        SilentAlarm = False
def AlarmResponder(Alarm, Status):
	print "Recieved Data in Responder", Alarm, Status
	if Alarm == "General":
		if (Status == 1):
			shutil.copyfile("/home/pi/Programming/WebPages/Emergency.html", "/var/www/html/generalAlarm.html")
			print "General Alarm set to emergency status."
			pfio.digital_write(0, 1)
		if (Status == 0):
			shutil.copyfile("/home/pi/Programming/WebPages/Nominal.html", "/var/www/html/generalAlarm.html")
			print "Genaral Alarm set to Nominal status"
			pfio.digital_write(0, 0)
		if (Status != 0) and (Status != 1):
			shutil.copyfile("/home/pi/Programming/WebPages/Fault.html", "/var/www/html/generalAlarm.html")
			print "GENERAL ALARM RECIEVED INVALID INPUT:", Status
			pfio.digital_write(0, 0)
	if Alarm == "Silent":
		if Status == "1":
			shutil.copyfile("/home/pi/Programming/WebPages/SilentEmergency.html", "/var/www/html/silentAlarm.html")
			print "Silent Alarm set to emergency status, Shhhhhh."
			call(['espeak "Printer Supply Notification: cyan ink low" 2>/dev/null'], shell=True)
		if Status == "0":
			shutil.copyfile("/home/pi/Programming/WebPages/Nominal.html", "/var/www/html/silentAlarm.html")
			print "Silent Alarm deactivated."
                        call(['espeak "Printer Supply Notification: cyan ink replenished" 2>/dev/null'], shell=True)

while True:
	#global GeneralAlarm, GeneralAlarmLast
	if((time.time()) - AllowSwitcherTimer) >= 2:
		allowSwitcher = True
	else:
                allowSwitcher = False
	#print "AllwSwitchTimer", AllowSwitcherTimer
	#print "Allow Switch", allowSwitcher
	print "calc", (time.time() - AllowSwitcherTimer)
	GeneralAlarmListener()
	SilentAlarmListener()
	time.sleep(0.01)
	if GeneralAlarm != GeneralAlarmLast:
		if GeneralAlarm == True:
			AlarmResponder("General", 1)
		if GeneralAlarm == False:
			AlarmResponder("General", 0)
	if SilentAlarm != SilentAlarmLast:
		if SilentAlarm == True:
			AlarmResponder("Silent", "1")
		if SilentAlarm == False:
			AlarmResponder("Silent", "0")
	time.sleep(0.01)
print "System has failed, We'll get 'em next time"
