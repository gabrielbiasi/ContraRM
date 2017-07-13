#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from Chao import *

class Background:

	def __init__(self, mapa, resolucao, largura):
		self.Fimdomapa = False
		self.posicao = [0,0]
		self.TelaWidth = resolucao[0]
		self.TelaHeight = resolucao[1]
		self.Largura = largura
		self.ImagemCaminho = pygame.image.load(mapa).convert_alpha()
		self.RectImagem = self.ImagemCaminho.get_rect()
		self.RectImagem.topleft = self.posicao
		self.ImagemCaminho = pygame.transform.scale(self.ImagemCaminho, (self.Largura, self.TelaHeight))

	def move(self, inc):
		self.posicao[0] -= inc
		self.RectImagem.topleft = self.posicao


	def desenha(self, tela, lance, chao, paredes, inimigos, tiros_inimigos, explosoes, melhorias):
		inc = 0
		if (-self.posicao[0]) >= self.Largura-(1.5*self.TelaWidth): # Se chegar na uma tela e meia de distância do boss, aparece a barra de vida.
			self.Fimdomapa = True
		if self.Fimdomapa:
			if (-self.posicao[0]) < self.Largura-self.TelaWidth: # Empurra a tela para o final do mapa.
				inc = int(3)
				if(lance.Pos[0] < 0):
					lance.Pos[0] = 0
		elif lance.Pos[0] > (self.TelaWidth/2): # Se não chegou no final do mapa, apenas move para a direita.
			inc = int(lance.Pos[0]-(self.TelaWidth/2))

		if inc > 0: # Se precisar mover o cenário, move todos os elementos para a esquerda, junto com o lance.
			self.move(inc)
			chao.update(inc)
			paredes.update(inc)
			for i in inimigos.sprites():
				i.move(inc)
			for i in tiros_inimigos.sprites():
				i.move(inc)
			for i in explosoes.sprites():
				i.move(inc)
			for i in melhorias.sprites():
				i.move(inc)
			inc = [lance.Pos[0]-inc, lance.Pos[1]]
			lance.move(inc)
		self.RectImagem.topleft = self.posicao
		tela.blit(self.ImagemCaminho, self.RectImagem)
		chao.draw(tela)
		paredes.draw(tela)
