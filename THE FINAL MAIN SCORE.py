#####I got this code from stack overflow


### i have been searching for LITERALLY DAYS on how to get surf to work
####after realizing that surf was a library, i tried to figure out how to import it
## i then searched  on stack overflow, and i got the following code

##gabe will change the variables to fit his code

###importing system, 
##importing pygame
##Importing locals import

import sys
import pygame
from pygame.locals import *


##initializing pygame

pygame.init()
##setting size, height and width
size = width, height = 800,500
##setting screen

#setting caption and font for display
screen = pygame.display.set_mode(size)
pygame.display.set_caption("testing")
myfont = pygame.font.SysFont("monospace", 16)
WHITE = (255,255,255)

score = 0
###setting boolean
##while true is a boolean
while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(WHITE)

    disclaimertext = myfont.render("YEEE I GOT IT TO WORK...", 1, (0,0,0))
    screen.blit(disclaimertext, (5, 480))

    scoretext = myfont.render("Score {0}".format(score), 1, (0,0,0))
    screen.blit(scoretext, (5, 10))
    score += 1


    ###THANK GOD, i have literally worked for 8 hours this weeekend on this, and finally got it

    ##this is satisfying as hell