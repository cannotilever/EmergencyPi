#workstation endpoint security listener
import os
import time
import shutil
import math
from lxml import html
import requests
from subprocess import call
import pygame
from pygame.locals import *

global tree, status, Running, tree2, status2, gameDisplay, LastStatus, LastStatus2

page = requests.get('http://ubuntuserver01/generalAlarm.html')
tree = html.fromstring(page.content)
status = tree.xpath('//h1/text()')
page2 = requests.get('http://ubuntuserver01/silentAlarm.html')
tree2 = html.fromstring(page2.content)
status2 = tree2.xpath('//h1/text()')
LastStatus = 'Initializing...'
LastStatus2 = 'Initializing...'
pygame.init()
pygame.mixer.init()
Nostromo = pygame.mixer.Sound('../Sounds/DynamicLoad_BSPNostromo_Ripley.023.ogg')

#display Dimensions Depricated
display_width = 1920
display_height = 1080

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue =(57,0,236)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
	global gameDisplay
	#gameDisplay = pygame.display.set_mode((display_width,display_height))
	largeText = pygame.font.Font('freesansbold.ttf',55)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()
	pygame.display.flip()
def DisplayEmergencyScreen():
	pygame.init()
	global gameDisplay
	gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	pygame.display.set_caption('Emergency Pi Message')
	gameDisplay.fill(red)
	Nostromo.play(-1)
	message_display('HVRHS EMERGENCY ALERT SYSTEM HAS BEEN ACTIVATED')
	print("Message Command Should Have Been Run with This color Code:", red)
def DisplaySilentAlarm():
	global gameDisplay
	pygame.init()
	gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	pygame.display.set_caption('Emergency Pi Message')
	gameDisplay.fill(blue)
	message_display('Main Office Is In Distress!')

def ClearScreen():
	Nostromo.stop()
	pygame.quit()
Running = True

while(True):
#	global LastStatus, LastStatus2
	page = requests.get('http://ubuntuserver01/generalAlarm.html')
	tree = html.fromstring(page.content)
	status = tree.xpath('//h1/text()')
	page2 = requests.get('http://ubuntuserver01/silentAlarm.html')
	tree2 = html.fromstring(page2.content)
	status2 = tree2.xpath('//h1/text()')
	print ("got Status 1", status)
	if ((status == ['Emergency']) and status != LastStatus):
		DisplayEmergencyScreen()
		call(['espeak "EMERGENCY DETECTED! THIS IS NOT A DRILL!" 2>/dev/null'], shell=True)
	print ("got Status 2", status2)
	if ((status2 == ['Emergency']) and status2 != LastStatus2):
		DisplaySilentAlarm()
	print ("Last General Status was:", LastStatus)
	print ("Last Silent Status was:", LastStatus2)
	if ((status != ['Emergency']) and (status2 != ['Emergency']) and ((status != LastStatus) or (status2 != LastStatus2))):
		ClearScreen()
	time.sleep(1)
	LastStatus = status
	LastStatus2 = status2
pygame.quit()
quit()
