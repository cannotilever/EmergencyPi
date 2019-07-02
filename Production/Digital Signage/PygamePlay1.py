import pygame
import time

pygame.init()

display_width = 1920
display_height = 1080

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Emergency Pi Message')

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',55)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

def ShowMain():
	gameDisplay.fill(red)
	message_display('HVRHS EMERGENCY ALERT SYSTEM HAS BEEN TRIGGERED')

ShowMain()


time.sleep(5)
pygame.quit()
quit()
