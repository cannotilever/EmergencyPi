#workstation endpoint security listener
import os
import time
import math
from lxml import html
import requests
import pygame
from pygame.locals import *

global tree, status, Running, tree2, status2, gameDisplay, LastStatus, LastStatus2
WebServer = '192.168.86.40'
page = requests.get('http://' + WebServer + '/generalAlarm.html')
tree = html.fromstring(page.content)
status = tree.xpath('//h1/text()')
page2 = requests.get('http://' + WebServer + '/silentAlarm.html')
tree2 = html.fromstring(page2.content)
status2 = tree2.xpath('//h1/text()')
LastStatus = 'Initializing'
LastStatus2 = 'Initializing'
#pygame.init()
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
    largeText = pygame.font.Font('freesansbold.ttf', 55)
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    smallTextSurf, smallTextRect = text_objects('Emergency Broadcast System:', smallText)
    smallTextRect.center = ((display_width/2),(display_height/4))
    gameDisplay.blit(TextSurf, TextRect)
    gameDisplay.blit(smallTextSurf, smallTextRect)
    pygame.display.update()
    pygame.display.flip()
def DisplayEmergencyScreen():
    pygame.init()
    global gameDisplay
    gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    #gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Emergency Alert')
    gameDisplay.fill(red)
    message_display('HVRHS EMERGENCY ALERT SYSTEM HAS BEEN ACTIVATED')
    print("Message Command Should Have Been Run with This color Code:", red)
def DisplaySilentAlarm():
    global gameDisplay
    pygame.init()
    gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    #gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Emergency Pi Message')
    gameDisplay.fill(blue)
    message_display('Main Office Is In Distress!')

def ClearScreen():
  #  global usepygame
    pygame.quit()
    print("clearscreen Called")

while True:
    #global usepygame
    #global LastStatus, LastStatus2
 #   print("Pygame Status: ", usepygame)
    page = requests.get('http://' + WebServer + '/generalAlarm.html')
    tree = html.fromstring(page.content)
    status = tree.xpath('//h1/text()')
    page2 = requests.get('http://' + WebServer + '/silentAlarm.html')
    tree2 = html.fromstring(page2.content)
    status2 = tree2.xpath('//h1/text()')
    print ("got Status 1", status)
    if (status == ['Emergency']) and status != LastStatus:
        DisplayEmergencyScreen()
    print ("got Status 2", status2)
    if (status2 == ['Emergency']) and status2 != LastStatus2:
        DisplaySilentAlarm()
    print ("Last General Status was:", LastStatus)
    print ("Last Silent Status was:", LastStatus2)
    if(status != ['Emergency']) and (status2 != ['Emergency']) and ((status != LastStatus) or (status2 != LastStatus2)):
        ClearScreen()

    time.sleep(1)
    LastStatus = status
    LastStatus2 = status2
pygame.quit()
quit()
