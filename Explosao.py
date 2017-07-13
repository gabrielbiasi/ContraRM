import pygame
from Animacao import *

class Explosao(pygame.sprite.Sprite):

	def __init__(self, posicao, tempo, escala):
		pygame.sprite.Sprite.__init__(self)
		self.temp = 0
		self.sound = pygame.mixer.Sound("sons/tiro.wav")
		self.tocou = False
		self.Tempo = tempo
		self.Pos = [posicao[0], posicao[1]]
		self.Anim = Animacao("sprites/Explosao/*.gif", escala, 170)
		self.image = self.Anim.img
		self.rect = self.image.get_rect()
		self.rect.center = self.Pos

	def update(self, tempo):
		self.temp += tempo
		if self.tocou == False:
			#self.sound.play()
			self.tocou = True
		if self.temp < self.Tempo:
			self.image = self.Anim.img
			self.Anim.update(tempo)
			self.rect = self.image.get_rect()
			self.rect.center = self.Pos
		else:
			self.kill()

	def move(self, inc):
		self.Pos[0] -= inc
		self.rect.center = self.Pos


