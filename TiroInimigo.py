#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, math
from Animacao import *
from Explosao import *

class TiroInimigo(pygame.sprite.Sprite):

	def __init__(self, posicao, direcao, velocidade):
		pygame.sprite.Sprite.__init__(self)
		self.Velocidade = velocidade
		self.Pos = posicao
		self.image = pygame.image.load("sprites/Tiros/1.gif").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.center = self.Pos
		self.Direcao = direcao

	def move(self, inc):
		self.Pos[0] -= inc
		self.rect.bottomleft = self.Pos

	def update(self, tempo, resolucao):
		rect_resolucao = pygame.Rect([0,0], resolucao)
		# Caso o tiro ultrapasse o limite da tela, ele eh removido do grupo de tiros.
		if rect_resolucao.contains(self) == False:
			self.kill()
		else:
			if self.Direcao == 0:
				inc = [round(self.Pos[0]-(self.Velocidade*tempo)), self.Pos[1]]
			elif self.Direcao == 1:
				inc = [round(self.Pos[0]+(self.Velocidade*tempo)), self.Pos[1]]
			elif self.Direcao == 2:
				inc = [round(self.Pos[0]+(self.Velocidade*tempo)), round(self.Pos[1]-(self.Velocidade*tempo))]
			elif self.Direcao == 3:
				inc = [round(self.Pos[0]+(self.Velocidade*tempo)), round(self.Pos[1]+(self.Velocidade*tempo))]
			elif self.Direcao == 4:
				inc = [round(self.Pos[0]-(self.Velocidade*tempo)), round(self.Pos[1]-(self.Velocidade*tempo))]
			elif self.Direcao == 5:
				inc = [round(self.Pos[0]-(self.Velocidade*tempo)), round(self.Pos[1]+(self.Velocidade*tempo))]
			elif self.Direcao == 6:
				inc = [self.Pos[0], round(self.Pos[1]-(self.Velocidade*tempo))]
			elif self.Direcao == 7:
				inc = [self.Pos[0], round(self.Pos[1]+(self.Velocidade*tempo))]
			self.Pos = inc
			self.rect.center = self.Pos
