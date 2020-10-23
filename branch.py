# coding: utf-8
__author__ = 'CotherArt'

import pygame
from random import randint

class Branch:

    def __init__(self, posx=200, posy=200, color=(255,255,255)):
        self.posx = posx
        self.posy = posy
        self.tam = 1
        self.color = color
        self.branchlist = []
    
    # Add pixels to the branchlist
    def grow(self):
        self.posy -= self.tam
        if randint(0,1) == 0:
            self.posx += self.tam
        else:
            self.posx -= self.tam

        self.branchlist.append(pygame.Rect(self.posx, self.posy, self.tam, self.tam))
    
    # Draws the branchlist on the screen
    def draw_branch(self, screen):
        for i in self.branchlist:
            pygame.draw.rect(screen, self.color, i)
        self.grow()
    
    def set_tam(self, tam):
        self.tam = tam

if __name__ == '__main__':
    pygame.init()

    # Display properties
    screen = pygame.display.set_mode((400, 400))

    bra = Branch()

    # Main loop
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Draw on screen
        screen.fill((0,0,0))
        bra.draw_branch(screen)

        pygame.display.update()
