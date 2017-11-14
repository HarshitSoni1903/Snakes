#snake game
import pygame
import sys
import random
import time


def showscore(choice=1):
    sfont = pygame.font.SysFont('Magneto Bold', 36)
    s_surface = sfont.render("Score: {0}".format(score), True, red)
    s_rect = s_surface.get_rect()
    if choice==1:
        s_rect.midtop = (80,10)
    else:
        s_rect.midtop = (360, 120)
    playsurface.blit(s_surface, s_rect)

#keeping track of highscores

highscore=[1,2,3,8]

def checkscore():
    highscore.append(score)
    highscore.sort()
    highscore.reverse()
    if len(highscore)>5:
        highscore.pop()

def highscore1():
    checkscore()
    hfont = pygame.font.SysFont('Magneto Bold', 24)
    hfont1 = pygame.font.SysFont('Magneto Bold', 24)
    h_surface = hfont.render("High Score:", True, red)
    h_rect = h_surface.get_rect()
    h_rect.midtop = (360, 160)
    playsurface.blit(h_surface, h_rect)
    print highscore
    for i in range(len(highscore)):
        h_score_surface = hfont1.render("{0}.   {1}".format((i+1),(highscore[i])),True,black)
        h_score_rect = h_score_surface.get_rect()
        h_score_rect.midtop = (360, 190+i*20)
        playsurface.blit(h_score_surface, h_score_rect)

#we need to display gameover on the screen once the game is over.

def gameover():
    #using a font present in the system to stylize the "Game Over!" text

    myfont = pygame.font.SysFont('Magneto Bold',72)
    Font_surface = myfont.render("Game Over!",True,black)
    font_rect = Font_surface.get_rect()
    font_rect.midtop=(360,15)
    playsurface.blit(Font_surface,font_rect)
    showscore(0)
    highscore1()
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit()

def play():

    checkerror = pygame.init()

    if checkerror[1] > 0:
        print("error")
        sys.exit(-1)
    else:
        print("success")

    # window
    global playsurface,red, black, fpsController,snakepos,snakebody,score, highscore,changeto, direcction

    playsurface = pygame.display.set_mode((720, 460))
    pygame.display.set_caption('Sanke Game')

    # color

    red = pygame.Color(255, 0, 0)
    brown = pygame.Color(165, 42, 42)
    green = pygame.Color(0, 255, 0)
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)

    # framecontroller

    fpsController = pygame.time.Clock()

    # positions and directions
    # initial position of snake.
    # Everything is a block of 10x10 pixels
    # Initially snake is a 3 block element

    snakepos = [100, 50]
    snakebody = [[100, 50], [90, 50], [80, 50]]

    # position of food is random at every instant
    # keeping the position of food in a pixel area of 10x10 block
    # it can range anywhere in 720x460
    # but multiplying with 10 makes sure that the food is neer placed aat some random pixel like 422x328
    # which causes dis-alignment
    foodpos = [random.randrange(0, 72) * 10, random.randrange(0, 46) * 10]

    # food has to be spawned only when some flag is true
    # not in some other conditions, like food is already present, or the game has just started and other such situations

    foodspawn = True

    # snake needs some directions to move.
    # initial snake movement is supplied as right

    direction = 'RIGHT'
    changeto = direction

    # every game needs to keep score
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    changeto = 'RIGHT'
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    changeto = 'LEFT'
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    changeto = 'UP'
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    changeto = 'DOWN'
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        #The snake cannot go right if he's already moving left

        if changeto == "RIGHT" and not direction == 'LEFT':
            direction = "RIGHT"
        if changeto == "LEFT" and not direction == 'RIGHT':
            direction = "LEFT"
        if changeto == "DOWN" and not direction == 'UP':
            direction = "DOWN"
        if changeto == "UP" and not direction == 'DOWN':
            direction = "UP"

        #we are moving the snake here!
        if direction == "RIGHT":
            snakepos[0] += 10
        if direction == "LEFT":
            snakepos[0] -= 10
        if direction == "UP":
            snakepos[1] -= 10
        if direction == "DOWN":
            snakepos[1] += 10

        #Snake Body Movement

        snakebody.insert(0,list(snakepos))

        if snakepos[0] == foodpos[0] and snakepos[1] == foodpos[1]:
            foodspawn = False
            score +=1
        else:
            snakebody.pop()

        if foodspawn == False:
            foodpos = [random.randrange(0, 72) * 10, random.randrange(0, 46) * 10]

        foodspawn = True

        #changing the colour of screen!
        playsurface.fill(white)

        #looping throught the coordiates of snake's body to display snake
        for pos in snakebody:
            #we create each block with a square(rectangle)
            pygame.draw.rect(playsurface, green, pygame.Rect(pos[0],pos[1], 10, 10))


        #food!!
        pygame.draw.rect(playsurface, brown, pygame.Rect(foodpos[0], foodpos[1], 10, 10))

        #game over if you hit a wall.  snakepos should be more han atleast one of boundary

        if snakepos[0]>710 or snakepos[0]<0:
            gameover()
        if snakepos[1]>450 or snakepos[1]<0:
            gameover()

        #snake should not eat his own tail

        for block in snakebody[1:]:
            if snakepos[0]== block[0] and snakepos[1]== block[1]:
                gameover()

        #display th score
        showscore()
        #updating the screen
        pygame.display.flip()

        #controlling number of frames

        fpsController.tick(23)

play()
