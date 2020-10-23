# coding: utf-8
__author__ = 'CotherArt'

import pygame
import sys
from time import sleep
from random import randint
from branch import Branch

pygame.init()

# Colors ---------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (47,79,79)
GREEN = (0, 128, 0)
MAROON = (128,0,0)
BLUE = (30,144,255)
LIGTH_BLUE =(186, 212, 239)

color_background = LIGTH_BLUE
color_branch = BLACK
color_ground = GRAY
# /Colors---------------

# Constants
WIDTH, HEIGHT = 480, 480
ORIGEN_X, ORIGEN_Y = int(WIDTH/2), int(HEIGHT/2)

# Display properties
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('pixel garden by: CotherArt')
clock = pygame.time.Clock()

# Branch and Ground propertyes
pixel_tam = 1
ground_thick = 20
seed_posx = ORIGEN_X
seed_posy = HEIGHT - (ground_thick + pixel_tam)

# Objeto branch
br = Branch(seed_posx, seed_posy, color_branch)

# Dibuja el suelo
def draw_ground():
    pygame.draw.rect(screen, color_ground, pygame.Rect(0, HEIGHT-ground_thick, WIDTH, ground_thick))


# Main loop
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Draw on screen
    screen.fill(color_background)
    draw_ground()
    br.draw_branch(screen)
    

    pygame.display.update()
    clock.tick(30)