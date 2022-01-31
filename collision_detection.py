# PyGame Collision Detection Practice, Johnson Kayln, January 31, 2022, 8:32am v0.0

import pygame, sys, random
from pygame.locals import *

#Setup PyGame
pygame.init()
mainClock = pygame.time.Clock()

#Setup Pygame Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Collision Dection 2022')

#Setup Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Setup the player and food data structures.
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []

for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE),random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE,FOODSIZE))

# Movement Variable
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

# Run the game_loop.
while True:
    #Check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if event.type == KEYDOWN:
        # Change the keyboard variables.
        if event.key == K_LEFT or event.key == K_a:
            moveRight = False
            moveLeft = True
        if event.key == K_RIGHT or event.key == K_d:
            moveRight = False
            moveLeft = True
        if event.key == K_UP or event.key == K_w:
            moveRight = False
            moveLeft = True
        if event.key == K_DOWN or event.key == K_s:
            moveRight = False
            moveLeft = True
    if event.type == KEYUP:
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        # CHeck to see if player has stopped moving.
        if event.key == K_LEFT or event.key == K_a:
            moveLeft = False
        if event.key == K_RIGHT or event.key == K_d:
            moveRight = False
        if event.key == K_UP or event.key == K_w:
            moveUp = False
        if event.key == K_DOWN or event.key == K_s:
            moveDown = False
        if event.key == K_x: # Use x to teleport the player.
            player.top = random.randint(0, WINDOWHEIGHT - player.height)
            player.left = random.randint(0, WINDOWWIDTH - player.width)
    
    if event.type == MOUSEBUTTONUP:
        foods.append(pygame.Rect(event.pos[0],event.pos[1]), FOODSIZE,FOODSIZE))

foodCounter += 1
if foodCounter => NEWFOOD:
    # Add new food.
    foodCounter = 0
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# Draw white backgrojnd on Window Surface
windowSurface.fill(WHITE)


