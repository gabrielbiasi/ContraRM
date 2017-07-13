#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from Animacao import *
from Tiro import *

class Jogador(pygame.sprite.Sprite):

	def __init__(self, posicao, vidas, temp_ivulneravel, vel, vel_tiro, altura, gravidade, vel_per_frame, resolucao):
		pygame.sprite.Sprite.__init__(self)
		self.A_PulandoEsquerda = Animacao("sprites/LancePulandoEsquerda/*.gif", 1.5, vel_per_frame)
		self.A_PulandoDireita = Animacao("sprites/LancePulandoDireita/*.gif", 1.5, vel_per_frame)
		self.A_PulandoEsquerda = Animacao("sprites/LancePulandoEsquerda/*.gif", 1.5, vel_per_frame/4)
		self.A_PulandoDireita = Animacao("sprites/LancePulandoDireita/*.gif", 1.5, vel_per_frame/4)
		self.A_ParadoCimaEsquerda = Animacao("sprites/LanceParadoCimaEsquerda/*.gif", 1.5, vel_per_frame)
		self.A_ParadoCimaDireita = Animacao("sprites/LanceParadoCimaDireita/*.gif", 1.5, vel_per_frame)
		self.A_DeitadoEsquerda = Animacao("sprites/LanceDeitadoEsquerda/*.png", 1.5, vel_per_frame)
		self.A_DeitadoDireita = Animacao("sprites/LanceDeitadoDireita/*.png", 1.5, vel_per_frame)
		self.A_ParadoEsquerda = Animacao("sprites/LanceParadoEsquerda/*.png", 1.5, vel_per_frame)
		self.A_ParadoDireita = Animacao("sprites/LanceParadoDireita/*.png", 1.5, vel_per_frame)
		self.A_AndandoEsquerda = Animacao("sprites/LanceAndandoEsquerda/*.gif", 1.5, vel_per_frame)
		self.A_AndandoDireita = Animacao("sprites/LanceAndandoDireita/*.gif", 1.5, vel_per_frame)
		self.A_AndandoCimaEsquerda = Animacao("sprites/LanceAndandoCimaEsquerda/*.gif", 1.5, vel_per_frame)
		self.A_AndandoCimaDireita = Animacao("sprites/LanceAndandoCimaDireita/*.gif", 1.5, vel_per_frame)
		self.A_AndandoBaixoEsquerda = Animacao("sprites/LanceAndandoBaixoEsquerda/*.gif", 1.5, vel_per_frame)
		self.A_AndandoBaixoDireita = Animacao("sprites/LanceAndandoBaixoDireita/*.gif", 1.5, vel_per_frame)
		self.A_MorrendoEsquerda = Animacao("sprites/LanceMorrendoEsquerda/3.gif", 1.5, vel_per_frame)
		self.A_MorrendoDireita = Animacao("sprites/LanceMorrendoDireita/3.gif", 1.5, vel_per_frame)
		self.A_AtirandoEsquerda = Animacao("sprites/LanceAtirandoEsquerda/*.png", 1.5, vel_per_frame)
		self.A_AtirandoDireita = Animacao("sprites/LanceAtirandoDireita/*.gif", 1.5, vel_per_frame)
		self.sound = pygame.mixer.Sound("sons/tiro.wav")
		self.image = self.A_AndandoDireita.img
		self.rect = self.image.get_rect()
		self.Pos = posicao
		self.rect.bottomleft = self.Pos

		self.Velocidade = vel/1000.0
		self.AlturaPulo = altura
		self.Alt = 0
		self.pulando = False
		self.nochao = False
		self.Gravidade = gravidade/1000.0
		self.time = 0
		self.estado = 2
		self.Vidas = vidas
		self.Vivo = True
		self.Resolucao = resolucao
		self.TempoTiro = 300
		self.temp = 0
		self.Tempo_Morto = 700
		self.temp_Morto = 0
		self.Velocidade_Tiro = vel_tiro/1000.0
		self.NivelTiro = 1

		self.Ivulneravel = False
		self.TempoIvulneravel = temp_ivulneravel
		self.tempI = 0
		self.TempInvisivel = 0

	def move(self, posicao):
		self.rect = self.image.get_rect()
		self.Pos = posicao
		self.rect.bottomleft = self.Pos

	def andaDireita(self, tipo, tempo):
		if self.nochao:
			if tipo  == 0:
				if self.temp >= self.TempoTiro:
					self.image = self.A_AndandoDireita.getSpriteAtual(tempo)
				else:
					self.image = self.A_AtirandoDireita.getSpriteAtual(tempo)
				self.estado = 2
			elif tipo == 1:
				self.image = self.A_AndandoCimaDireita.getSpriteAtual(tempo)
				self.estado = 10
			elif tipo == 2:
				self.image = self.A_AndandoBaixoDireita.getSpriteAtual(tempo)
				self.estado = 12
		inc = round(self.Pos[0] + (self.Velocidade*tempo))
		if(inc < self.Resolucao[0]-25): # Colisão com o fim do mapa.
			inc = [inc, self.Pos[1]]
			self.move(inc)

	def andaEsquerda(self, tipo, tempo):
		if self.nochao:
			if tipo == 0:
				if self.temp >= self.TempoTiro:
					self.image = self.A_AndandoEsquerda.getSpriteAtual(tempo)
				else:
					self.image = self.A_AtirandoEsquerda.getSpriteAtual(tempo)
				self.estado = 3
			elif tipo == 1:
				self.image = self.A_AndandoCimaEsquerda.getSpriteAtual(tempo)
				self.estado = 11
			elif tipo == 2:
				self.image = self.A_AndandoBaixoEsquerda.getSpriteAtual(tempo)
				self.estado = 13
		inc = round(self.Pos[0] - (self.Velocidade*tempo))
		if(inc >= 0): # Colisao com o fim esquerdo da tela
			inc = [inc, self.Pos[1]]
			self.move(inc)

	def cima(self, tempo):
		if self.nochao:
			if self.estado % 2 == 0:
				self.image = self.A_ParadoCimaDireita.getSpriteAtual(tempo)
				self.estado = 8
			else:
				self.image = self.A_ParadoCimaEsquerda.getSpriteAtual(tempo)
				self.estado = 9
			self.rect = self.image.get_rect()
			self.rect.bottomleft = self.Pos

	def deitar(self, tempo):
		if self.nochao:
			if self.estado % 2 == 0:
				self.image = self.A_DeitadoDireita.getSpriteAtual(tempo)
				self.estado = 6
			else:
				self.image = self.A_DeitadoEsquerda.getSpriteAtual(tempo)
				self.estado = 7
			self.rect = self.image.get_rect()
			self.rect.bottomleft = self.Pos

	def parar(self, tempo):
		if self.nochao and self.Vivo:
			if self.estado % 2 == 0:
				self.image = self.A_ParadoDireita.getSpriteAtual(tempo)
				self.estado = 0
			else:
				self.image = self.A_ParadoEsquerda.getSpriteAtual(tempo)
				self.estado = 1
			self.rect = self.image.get_rect()
			self.rect.bottomleft = self.Pos

	def pular(self, tempo):
		if self.nochao:
			self.nochao = False
			self.pulando = True
			if self.estado % 2 == 0:
				self.image = self.A_PulandoDireita.getSpriteAtual(tempo)
				self.estado = 4
			else:
				self.image = self.A_PulandoEsquerda.getSpriteAtual(tempo)
				self.estado = 5
			self.rect = self.image.get_rect()
			self.rect.bottomleft = self.Pos

	def cair(self, tempo):
		if self.estado == 6 or self.estado == 7:
			self.nochao = False
			if self.estado == 6:
				self.estado = 4
			else:
				self.estado = 5
			inc = int(self.Pos[1] + 35)
			inc = [self.Pos[0], inc]
			self.move(inc)

	def atualiza(self, tiles, paredes, inimigos, tiros_inimigos, melhorias, tempo):
		self.temp += tempo # Temporizador da arma

		# Sessão quando Lance morre
		if self.Vivo == False:
			self.temp_Morto += tempo
			if self.estado == 0:
				inc = round(self.Pos[0] - (0.06*tempo)) # Joga Lance para trás.
			else:
				inc = round(self.Pos[0] + (0.06*tempo)) # Joga Lance para trás.
			inc = [inc, self.Pos[1]]
			self.move(inc)
			if self.temp_Morto > self.Tempo_Morto: # Volta ao normal.
				self.Vidas -= 1
				self.NivelTiro = 1
				self.pulando = False
				self.Alt = 0
				self.TempoTiro = 300
				self.temp_Morto = 0
				if self.Vidas > 0:
					self.Vivo = True
					if self.estado % 2 == 0: # Recupera o estado anterior.
						self.image = self.A_AndandoDireita.getSpriteAtual(tempo)
						self.estado = 0
					else: # Recupera o estado anterior.
						self.image = self.A_AndandoEsquerda.getSpriteAtual(tempo)
						self.estado = 1
					self.move([100,100])
					self.Ivulneravel = True # Fica ivulnerável.
		else: # Se ele não está morto...
			if self.Ivulneravel: # Está ivulnerável?
				if self.TempInvisivel > 100: # Enquanto está ivulnerável, fica piscando.
					self.TempInvisivel = 0
					if self.image.get_alpha() == None:
						self.image.set_alpha(100)
					else:
						self.image.set_alpha(None)
				else:
					self.TempInvisivel += tempo
				if self.tempI > self.TempoIvulneravel: # Tratador do tempo de ivulnerabilidade.
					self.Ivulneravel = False
					self.tempI = 0
				else:
					self.tempI += tempo
			else: # Se não está ivulnerável, colidirá com paredes, inimigos e tiros.
				# Colidiu com alguma parede?
				sprite = pygame.sprite.spritecollideany(self, paredes)
				if sprite != None:
					dist = self.image.get_width()/2.0
					inc = sprite.rect.center[0]-self.rect.center[0]
					if inc > 0: # Colidiu com uma parede pela esquerda.
						inc = [self.Pos[0]-(dist-inc), self.Pos[1]]
					else: # Colidiu com uma parede pela direita.
						inc = [self.Pos[0]+(dist+inc), self.Pos[1]]
					self.move(inc)
				# Colidiu diretamente com os inimigos?
				sprite = pygame.sprite.spritecollideany(self, inimigos)
				if sprite != None:
					self.morre(tempo)
				# Colidiu com algum tiro inimigo?
				sprite = pygame.sprite.spritecollideany(self, tiros_inimigos)
				if sprite != None:
					tiros_inimigos.remove(sprite)
					self.morre(tempo)
			# Colidiu com alguma melhoria?
			sprite = pygame.sprite.spritecollideany(self, melhorias)
			if sprite != None:
				if sprite.Tipo == "R":
					self.TempoTiro = 150
				elif sprite.Tipo == "M":
					self.NivelTiro = 2
				elif sprite.Tipo == "L":
					self.Vidas += 1
				melhorias.remove(sprite)


			# Pulador!
			if self.time < 2:
				self.time += 1
			else:
				self.time = 0
				if self.estado == 4:
					self.image = self.A_PulandoDireita.getSpriteAtual(tempo)
				elif self.estado == 5:
					self.image = self.A_PulandoEsquerda.getSpriteAtual(tempo)
				if self.pulando: # Se ele está pulando, continua a subí-lo.
					if(self.Alt < self.AlturaPulo):
						self.Alt += 9
						inc = [self.Pos[0], self.Pos[1]-9]
						self.move(inc);
					else: # Ponto máximo do salto.
						self.pulando = False
						self.Alt = 0
				else: # Se Lance não está pulando, aplica a gravidade.
					self.aplicaGravidade(tiles, tempo)

	def atirar(self, grupo, tempo):
		if self.temp > self.TempoTiro: # Verifica o temporizador.
			self.temp = 0
			self.sound.play()
			grupo.add(Tiro(self, self.NivelTiro, self.Velocidade_Tiro))

	def morre(self, tempo):
		self.Vivo = False
		if self.estado % 2 == 0:
			self.image = self.A_MorrendoDireita.getSpriteAtual(tempo)
			self.estado = 0
		else:
			self.image = self.A_MorrendoEsquerda.getSpriteAtual(tempo)
			self.estado = 1
		self.rect = self.image.get_rect()
		self.rect.bottomleft = self.Pos

	def aplicaGravidade(self, tiles, tempo):
		sprite = pygame.sprite.spritecollideany(self, tiles)
		if sprite == None: # Se não está colidindo com nenhum chão, aplica a gravidade.
			self.nochao = False
			inc = [self.Pos[0], round(self.Pos[1]+(tempo*self.Gravidade))]
			self.move(inc)
			if self.Pos[1] >= self.Resolucao[1]: # Passou do limite da tela: Morre
				self.morre(tempo)
		elif self.nochao == False: # Se colidiu, ele esta em algum chão
			self.nochao = True
			self.parar(tempo)
			self.rect = self.image.get_rect() # Corrige sua posição de acordo com o nível do chão	
			self.Pos = [self.Pos[0], sprite.rect.topleft[1]+1]
			self.rect.bottomleft = self.Pos

	def reset(self, tempo):
		self.temp_Morto = 0
		self.Vivo = True
		self.Ivulneravel = False
		self.TempoIvulneravel = 2500
		self.pulando = False
		self.Alt = 0
		self.nochao = False
		self.Vidas = 3
		self.Pos = [100,100]
		self.image = self.A_AndandoDireita.getSpriteAtual(tempo)
		self.rect.bottomleft = self.Pos
		self.estado = 2
		self.TempoTiro = 300
		self.NivelTiro = 1

