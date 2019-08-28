# This is the third itteration of the Button script. This adds support for toggle buttons and modifies the alarm shutdown behavior.
import time
import os
import shutil
import math
import pifacedigitalio as pfio

pfio.init()
shutil.copyfile("/home/pi/Documents/WebPages/Nominal.html", "/var/www/html/generalAlarm.html") #assume system is OK
shutil.copyfile("/home/pi/Documents/WebPages/Nominal.html", "/var/www/html/silentAlarm.html")
pfio.digital_write(0, 0)
time.sleep(0.5)
Button1StartUpVar = pfio.digital_read(7) #we assume that the button is connected and not pressed when the program starts. To detect when the button is pressed, we just detect when button current state != button origional state
Button2StartUpVar = pfio.digital_read(6) #silent alarm button
TimesButtonWasPressed = 0
#global CheckForTimer, GeneralAlarm, SilentAlarm, GeneralAlarmLast, SilentAlarmLast
CheckForTimer = False
GeneralAlarm = False
SilentAlarm = False
GeneralAlarmLast = False
SilentAlarmLast = False

def GeneralAlarmListener():
        global GeneralAlarm
        if((pfio.digital_read(7)) != Button1StartUpVar):
                #print ("Button 1 Press Detected!")
                #print ("triggering emergency mode")
                GeneralAlarm = True

def SilentAlarmListener():
        global SilentAlarm
        if((pfio.digital_read(6)) != Button2StartUpVar):
                #print ("Button 6 Press Detected!")
                #print ("triggering emergency mode")
                SilentAlarm = True

def AlarmResponder(Alarm):
        #print ("Recieved Data in Responder", Alarm)
        if Alarm == "General":
                shutil.copyfile("/home/pi/Documents/WebPages/Emergency.html", "/var/www/html/generalAlarm.html")
                #print ("General Alarm set to emergency status.")
                pfio.digital_write(0, 1)

        if Alarm == "Silent":
                shutil.copyfile("/home/pi/Documents/WebPages/SilentEmergency.html", "/var/www/html/silentAlarm.html")
                #print ("Silent Alarm set to emergency status, Shhhhhh.")
        if Alarm == "Silent" or Alarm == "General":
                #print ("waiting to be called by clear function")
                exit()

while True:
        GeneralAlarmListener()
        SilentAlarmListener()
        time.sleep(0.01)
        if GeneralAlarm != GeneralAlarmLast:
                AlarmResponder("General")
        if SilentAlarm != SilentAlarmLast:
                AlarmResponder("Silent")
        time.sleep(0.01)
#print ("System has failed, We'll get 'em next time")
