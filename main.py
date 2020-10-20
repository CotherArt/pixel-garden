# coding: utf-8
__author__ = 'CotherArt'

import pygame
import sys
from time import sleep
from random import randint

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (47,79,79)
GREEN = (0, 128, 0)
MAROON = (128,0,0)
BLUE = (30,144,255)
LIGTH_BLUE =(186, 212, 239)

color_background = LIGTH_BLUE
color_seed = BLACK
color_ground = GRAY

# Constants
WIDTH, HEIGHT = 480, 480
ORIGEN_X, ORIGEN_Y = int(WIDTH/2), int(HEIGHT/2)

# Display properties
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('pixel garden by: CotherArt')
clock = pygame.time.Clock()

pixel_tam = 1
ground_thick = 20
seed_posx = ORIGEN_X
seed_posy = HEIGHT - (ground_thick + pixel_tam)

branch = []

def add_branch():
    global branch
    branch.append(pygame.Rect(seed_posx, seed_posy, pixel_tam, pixel_tam))

def draw_branch():
    for i in branch:
        pygame.draw.rect(screen, color_seed, i)    

def draw_seed():
    pygame.draw.rect(screen, color_seed, pygame.Rect(seed_posx, seed_posy, pixel_tam, pixel_tam))

def draw_ground():
    pygame.draw.rect(screen, color_ground, pygame.Rect(0, HEIGHT-ground_thick, WIDTH, ground_thick))

def grow():
    global seed_posx
    global seed_posy

    seed_posy -= pixel_tam
    if randint(0,1) == 0:
        seed_posx += pixel_tam
    else:
        seed_posx -= pixel_tam

# Main loop
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw on screen
    screen.fill(color_background)

    # draw_seed()
    draw_ground()
    add_branch()
    draw_branch()
    grow()
    
    pygame.display.update()
    # sleep(0.1)

    clock.tick(30)