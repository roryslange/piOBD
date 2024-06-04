#created by Rory Lange on Dec 4, 2022
#graphical user interface for a live diagnostic system 


import pygame
from pygame.locals import *

#some colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,128)

#initialize pygame
pygame.init()


#screen size and other important variables
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
screenWidth = screen.get_width()
screenHeight = screen.get_height()
heightCenter = screenHeight/2
textHeight = screenHeight*.75
gauge1X = screenWidth*.25
gauge2X = screenWidth*.5
gauge3X = screenWidth*.75
gaugeRadius = (gauge2X - gauge1X)/2
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 50)
testCounter = 0 #for testing gauges

#function to draw circles and background 
def skeletonGui():
    screen.fill(white)
    pygame.draw.circle(screen, black, (int(gauge1X), int(heightCenter)), int(gaugeRadius), 5)
    pygame.draw.circle(screen, black, (int(gauge2X), int(heightCenter)), int(gaugeRadius), 5)
    pygame.draw.circle(screen, black, (int(gauge3X), int(heightCenter)), int(gaugeRadius), 5)

    gauge1Text = font.render("RPM", True, black)   
    gauge2Text = font.render("SPEED", True, black) 
    gauge3Text = font.render("OIL TEMP", True, black)
    gauge1Location = gauge1Text.get_rect(center=(gauge1X, textHeight))
    gauge2Location = gauge2Text.get_rect(center=(gauge2X, textHeight))
    gauge3Location = gauge3Text.get_rect(center=(gauge3X, textHeight))
    screen.blit(gauge1Text, gauge1Location)
    screen.blit(gauge2Text, gauge2Location)
    screen.blit(gauge3Text, gauge3Location)

#function to put values into the gauges
def guiValues(g1="0000", g2="0000", g3="0000"):
    gauge1Value = font.render(g1, True, black)
    gauge2Value = font.render(g2, True, black)
    gauge3Value = font.render(g3, True, black)
    
    g1ValueLocation = gauge1Value.get_rect(center=(gauge1X, heightCenter))
    g2ValueLocation = gauge2Value.get_rect(center=(gauge2X, heightCenter))
    g3ValueLocation = gauge3Value.get_rect(center=(gauge3X, heightCenter))
    
    screen.blit(gauge1Value, g1ValueLocation)
    screen.blit(gauge2Value, g2ValueLocation)
    screen.blit(gauge3Value, g3ValueLocation)
    


#frame loop
done = False
while not done:
    for event in pygame.event.get(): #loop through events each frame
        if event.type == pygame.QUIT: #done if quit event is triggered
            done = True
        elif event.type == KEYDOWN: #done if escape key is hit
            if event.key == K_ESCAPE:
                done = True


    #reprint skeleton and values each frame
    skeletonGui()
    guiValues(str(testCounter), str(testCounter), str(testCounter))
    
    #update screen
    pygame.display.update()
    pygame.display.flip()
    
    #test counter to test if number print is working properly
    testCounter += 1
    testCounter = testCounter % 99

    #set framerate
    clock.tick(60)


#quit pygame
pygame.quit()

