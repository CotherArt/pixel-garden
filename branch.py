# coding: utf-8
__author__ = 'CotherArt'

import pygame
from random import randint

class Branch:

	def __init__(self, posx=200, posy=200, color=(255,255,255)):
		self.posx = posx
		self.posy = posy
		self.tam = 13 
		self.tamint = self.tam
		self.ofset = 2
		self.color = color
		self.branchlist = []

	# Add pixels to the branchlist
	def grow(self):
		if self.tamint == 0:
			return

		self.color_change()
		self.tam = self.tam - .2
		self.tamint = int(self.tam)
		self.posy -= self.tamint 

		rando = randint(0, 3)
		if rando == 0:
			self.posx += self.ofset
		elif rando == 3:
			self.posx -= self.ofset
		self.branchlist.append((pygame.Rect(self.posx, self.posy, self.tamint, self.tamint), self.color))
		
	# Increse the green value in the color
	def color_change(self):
		r = self.color[0]
		g = self.color[1]
		b = self.color[2]
		g += 5
		if g > 200:
			return
		self.color = (r,g,b)		

	# Draws the branchlist on the screen
	def draw_branch(self, screen):
		for i in self.branchlist:
			pygame.draw.rect(screen, i[1], i[0])
		self.grow()
	
	def set_tam(self, tam):
		self.tam = tam
	def get_tam(self):
		return int(self.tam)
	
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

		# Draw on screen
		bra.draw_branch(screen)

		pygame.display.update()
