# coding: utf-8
__author__ = 'CotherArt'

import pygame
from random import randint

class Branch:
	UP, LEFT, RIGHT = 0, 1, 2

	def __init__(self, posx=200, posy=200, color=(255,255,255), tam=13):
		self.grow_direction = self.UP

		self.posx = posx
		self.posy = posy
		self.tam = tam # Grosor de la rama
		self.tamint = self.tam # Grosor de la rama sin decimales
		self.ofset = 2
		self.color = color
		self.branchlist = []
		
		self.randomend = False
		self.maxlen = 15


	# Add pixels to the branchlist
	def grow(self):
		if self.randomend:
			self.maxlen = randint(5, self.maxlen)
			if len(self.branchlist) > self.maxlen:
				return

		if self.tamint == 0:
			return

		self.color_change()
		self.tam = self.tam - .2
		self.tamint = int(self.tam)
		rando = randint(0, 3)

		# Set direction of growing
		if self.grow_direction == self.UP:
			self.posy -= self.tamint 
			if rando == 0:
				self.posx += self.ofset
			elif rando == 3:
				self.posx -= self.ofset

		if self.grow_direction == self.RIGHT:
			self.posx += self.tamint 
			if rando == 0:
				self.posy += self.ofset
			elif rando == 3:
				self.posy -= self.ofset

		if self.grow_direction == self.LEFT:
			self.posx -= self.tamint 
			if rando == 0:
				self.posy += self.ofset
			elif rando == 3:
				self.posy -= self.ofset


		self.branchlist.append((pygame.Rect(self.posx, self.posy, self.tamint, self.tamint), self.color))
	
	# Returns true when the branch ends
	def is_branch_ends():
		return len(self.branchlist) == self.maxlen

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
	def set_maxlen(self, maxlen):
		self.maxlen = maxlen

	def get_len(self):
		return len(self.branchlist)
	def get_rect(self, listpos):
		return self.branchlist[listpos][0]
	def set_direction(self, direction):
		self.grow_direction = direction	

			
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
