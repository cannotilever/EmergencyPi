#Emergency Alert System Flasher Control Module: Production Code
import time
import os
import RPi.GPIO as GPIO
import shutil
import math
from lxml import html
import requests
from subprocess import call
WebServer = '10.12.8.203'
Relay1ControlPin = 15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Relay1ControlPin, GPIO.OUT)
print (GPIO.RPI_INFO)
loopcounter = 0
page = requests.get('http://' + WebServer +'/generalAlarm.html')
tree = html.fromstring(page.content)
status = tree.xpath('//h1/text()')
statusLast = 'Initializing...'
def FlashPattern(status):
        global statusLast
        statusLast = status
        if (status == ['Emergency']):
                print ("Emergency Got Run")
                GPIO.output(Relay1ControlPin, 1)
                CheckForEndOfState()
        if (status == ['Fault']):
                print ("FaultFlash got run")
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
        page = requests.get('http://' + WebServer +'/generalAlarm.html')
        tree = html.fromstring(page.content)
        status = tree.xpath('//h1/text()')
        print ("Recieved System Status", status)

while True:
        global page, tree, status
        time.sleep(0.5)
        CheckForEndOfState()
        if(status != statusLast):
                FlashPattern(status)
        if(status != ['Emergency']) or (status != ['Nominal']):
                status = 'Fault'
print ("if you see this, Something is very wrong!!")
