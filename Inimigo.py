#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, math
from TiroInimigo import *

class Inimigo(pygame.sprite.Sprite):

	def __init__(self, posicao, imagem, vidas, escala, escala_explosao, ativo = 0, matriz = None):
		pygame.sprite.Sprite.__init__(self)
		self.Pos = posicao
		self.Escala = escala
		self.Escala_Explosao = escala_explosao
		self.Vidas = vidas
		self.VidasInit = vidas
		self.image = pygame.image.load(imagem).convert()
		self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*self.Escala),int(self.image.get_height()*self.Escala)))
		self.rect = self.image.get_rect()
		self.rect.bottomleft = self.Pos

		self.MatrizIA = matriz
		if matriz != None and len(matriz) > 0:
			self.ValorAtivo = ativo/100.0
			self.MatrizPos = 0
			self.MatrizIA = matriz
			self.LenMatrixIA = len(self.MatrizIA)-1
			self.Rajada = False
			self.tempTiros = 0 # Tiros dados até o momento.
			self.tempI = 0 # Tempo passado de cada tiro da rajada.
			self.tempA = 0 # Tempo passado de atraso.
			self.tempoTiro = 0 #Tempo fixo entre cada tiro.
		else:
			self.MatrizIA = None


	def move(self, inc):
		self.Pos[0] -= inc
		self.rect.bottomleft = self.Pos

	def update(self, jogador, tiros, resolucao, tempo):
		if self.MatrizIA != None: # Ele atira?
			dist = math.sqrt((math.pow(jogador.Pos[0]-self.Pos[0], 2)+math.pow(jogador.Pos[1]-self.Pos[1], 2))) # Teorema de Pitágoras \o/
			if dist <= (resolucao[0]*self.ValorAtivo): # Ele está perto o suficiente?
				if self.tempA > self.MatrizIA[self.MatrizPos][1]: # Pode iniciar uma rajada?
					self.Rajada = True
					self.tempoTiro = self.MatrizIA[self.MatrizPos][3] # Atraso entre os tiros da rajada.
					self.Direcao = self.MatrizIA[self.MatrizPos][0] # Seta a direção da rajada.
					cor1 = 0 # Corretores de pixels.
					cor2 = 0
					correcao = 0
					correcao = self.MatrizIA[self.MatrizPos][4]
				if self.Rajada: # Se pode iniciar a rajada, ela começa.
					if self.tempI > self.tempoTiro: # Pode atirar?
						self.tempI = 0 # Reseta o contador.
						if self.Direcao == 0:
							cor2 = correcao
							pos = [self.rect.midleft[0]+cor1, self.rect.midleft[1]+cor2]
						elif self.Direcao == 1:
							cor2 = correcao
							pos = [self.rect.midright[0]+cor1, self.rect.midright[1]+cor2]
						elif self.Direcao == 2:
							if(correcao >= 0):
								cor1 = correcao
							else:
								cor2 = correcao
							pos = [self.rect.topright[0]+cor1, self.rect.topright[1]+cor2]
						elif self.Direcao == 3:
							if(correcao >= 0):
								cor2 = (-correcao)
							else:
								cor1 = correcao
							pos = [self.rect.bottomright[0]+cor1, self.rect.bottomright[1]+cor2]
						elif self.Direcao == 4:
							if(correcao >= 0):
								cor2 = correcao
							else:
								cor1 = (-correcao)
							pos = [self.rect.topleft[0]+cor1, self.rect.topleft[1]+cor2]
						elif self.Direcao == 5:
							if(correcao >= 0):
								cor2 = (-correcao)
							else:
								cor1 = (-correcao)
							pos = [self.rect.bottomleft[0]+cor1, self.rect.bottomleft[1]+cor2]
						elif self.Direcao == 6:
							cor1 = correcao
							pos = [self.rect.midtop[0]+cor1, self.rect.midtop[1]+cor2]
						elif self.Direcao == 7:
							cor1 = correcao
							pos = [self.rect.midbottom[0]+cor1, self.rect.midbottom[1]+cor2]
						tiros.add(TiroInimigo(pos, self.Direcao, 0.2)) # Cria o tiro na direção da rajada.

						self.tempTiros += 1
						if self.tempTiros == self.MatrizIA[self.MatrizPos][2]: # É o ultimo tiro da rajada?
							# Reseta as variáveis para iniciar uma nova rajada.
							self.Rajada = False
							self.tempA = 0
							self.tempTiros = 0
							if self.MatrizPos == self.LenMatrixIA: # Chegou no fim das rajadas?
								self.MatrizPos = 0 # Volta pro inicio.
							else:
								self.MatrizPos += 1 # Seleciona a próxima rajada.
					else:
						#Se não pode atirar agora, incrementa o tempo.
						self.tempI += tempo
				else:
					# Se não pode começar uma rajada, incrementa o tempo.
					self.tempA += tempo
