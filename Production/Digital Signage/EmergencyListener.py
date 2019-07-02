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

global tree, status, Running, tree2, status2, gameDisplay

page = requests.get('http://192.168.32.11/generalAlarm.html')
tree = html.fromstring(page.content)
status = tree.xpath('//h1/text()')
page2 = requests.get('http://192.168.32.11/silentAlarm.html')
tree2 = html.fromstring(page2.content)
status2 = tree2.xpath('//h1/text()')
pygame.init()

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
	pygame.quit()
Running = True

while(True):
	page = requests.get('http://192.168.32.11/generalAlarm.html')
	tree = html.fromstring(page.content)
	status = tree.xpath('//h1/text()')
	page2 = requests.get('http://192.168.32.11/silentAlarm.html')
	tree2 = html.fromstring(page2.content)
	status2 = tree2.xpath('//h1/text()')
	print ("got Status 1", status)
	if (status == ['Emergency']):
		DisplayEmergencyScreen()
		call(['espeak "EMERGENCY DETECTED! THIS IS NOT A DRILL!" 2>/dev/null'], shell=True)
	print ("got Status 2", status2)
	if (status2 == ['Emergency']):
		DisplaySilentAlarm()
	if (status != ['Emergency']) and (status2 != ['Emergency']):
		ClearScreen()
	time.sleep(1)
pygame.quit()
quit()
