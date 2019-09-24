import os
import time
import math
from lxml import html
import requests
import pygame
from pygame.locals import *

#Dynamically Changing Values:
WebServer = '192.168.86.40'
display_width = 1920
display_height = 1080

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue =(57,0,236)

def CheckWebServer():
    global Emergency, status, status2
    page = requests.get('http://' + WebServer + '/generalAlarm.html')
    tree = html.fromstring(page.content)
    status = tree.xpath('//h1/text()')
    page2 = requests.get('http://' + WebServer + '/silentAlarm.html')
    tree2 = html.fromstring(page2.content)
    status2 = tree2.xpath('//h1/text()')
    LastStatus = 'Initializing'
    LastStatus2 = 'Initializing'
    print ("got Status 1", status)
    print ("got Status 2", status2)
    if (status == ['Emergency']) and status2 != ['Emergency']:
        Emergency = True
    if (status2 == ['Emergency']) and status != ['Emergency']:
        Emergency = True
    if (status == ['Emergency']) and status2 == ['Emergency']:
        Emergency = True
    if (status != ['Emergency']) and status2 != ['Emergency']:
        Emergency = False
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def GameLoop(alarm):
    global Emergency
    pygame.init()
    gameDisplay = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Emergency Alert')
    while Emergency:
        CheckWebServer()
        if not Emergency:
            pygame.quit()
            DormentLoop()
        gameDisplay.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf', 55)
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        if alarm == 'General':
            gameDisplay.fill(red)
            TextSurf, TextRect = text_objects('HVRHS EMERGENCY ALERT SYSTEM HAS BEEN ACTIVATED', largeText)
            TextRect.center = ((display_width / 2), (display_height / 2))
            smallTextSurf, smallTextRect = text_objects('Emergency Broadcast System:', smallText)
            smallTextRect.center = ((display_width / 2), (display_height / 4))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(smallTextSurf, smallTextRect)
            pygame.display.update()
            pygame.display.flip()
            pygame.time.wait(500)
        if alarm == 'Silent':
            gameDisplay.fill(blue)
            TextSurf, TextRect = text_objects('Main Office Is In Distress!', largeText)
            TextRect.center = ((display_width / 2), (display_height / 2))
            smallTextSurf, smallTextRect = text_objects('Emergency Broadcast System:', smallText)
            smallTextRect.center = ((display_width / 2), (display_height / 4))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(smallTextSurf, smallTextRect)
            pygame.display.update()
            pygame.display.flip()
            pygame.time.wait(500)
        if alarm == 'Both':
            gameDisplay.fill(white)
            TextSurf, TextRect = text_objects('All Alarms Active!!', largeText)
            TextRect.center = ((display_width / 2), (display_height / 2))
            smallTextSurf, smallTextRect = text_objects('Emergency Broadcast System:', smallText)
            smallTextRect.center = ((display_width / 2), (display_height / 4))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(smallTextSurf, smallTextRect)
            pygame.display.update()
            pygame.display.flip()
            pygame.time.wait(500)
        for event in pygame.event.get():
            if pygame.key.get_pressed()[pygame.K_RETURN]:
                Emergency = False
                pygame.quit()

def DormentLoop():
    while True:
        global Emergency, status, status2
        CheckWebServer()
        CurTime = time.time()
        if (status == ['Emergency']) and status2 != ['Emergency']:
            GameLoop('General')
        if (status2 == ['Emergency']) and status != ['Emergency']:
            GameLoop('Silent')
        if (status == ['Emergency']) and status2 == ['Emergency']:
            GameLoop('All')
        if (status != ['Emergency']) and status2 != ['Emergency']:
            print ("All is Well as of ", CurTime)
            time.sleep(2)
DormentLoop()