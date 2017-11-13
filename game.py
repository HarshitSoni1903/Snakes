#snake game

import pygame
import sys
import random
import time

checkerror = pygame.init()

if checkerror[1]>0:
    print "error"
    sys.exit(-1)
else:
    print "success"

#window
playsurface = pygame.display.set_mode((720,460))
pygame.display.set_caption('Sanke Game')

#color

red=pygame.Color(255,0,0)
brown=pygame.Color(165,42,42)
green=pygame.Color(0,255,0)
black=pygame.Color(0,0,0)
white=pygame.Color(255,255,255)

#framecontroller

fpsController = pygame.time.Clock()

#positions and directions
    #initial position of snake.
    # Everything is a block of 10x10 pixels
    # Initially snake is a 3 block element

snakepos = [100,50]
snakebody = [[100,50],[90,50],[80,50]]

    #position of food is random at every instant
    #keeping the position of food in a pixel area of 10x10 block
    #it can range anywhere in 720x460
    #but multiplying with 10 makes sure that the food is neer placed aat some random pixel like 422x328
    #which causes dis-alignment
foodpos = [random.randrange(0,72)*10,random.randrange(0,46)*10]

    #food has to be spawned only when some flag is true
    #not in some other conditions, like food is already present, or the game has just started and other such situations

foodspawn = True

    #snake needs some directions to move.
    #initial snake movement is supplied as right

direction = 'RIGHT'
changeto = direction

#we need to display gameover on the screen once the game is over.

def gameover():
    #using a font present in the system to stylize the "Game Over!" text

    myfont = pygame.font.SysFont('Magneto Bold',72)
    Font_surface = myfont.render("Game Over!",True,red)
    font_rect = Font_surface.get_rect()
    font_rect.midtop=(360,100)
    playsurface.blit(Font_surface,font_rect)
    pygame.display.flip()

