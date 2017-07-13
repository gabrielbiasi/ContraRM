#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from Inimigo import *
from Melhoria import *
from Parede import *
from Chao import *

class Hangar:
	FaseCaminho = "mapas/Hangar.png"
	FaseLargura = 2444
	FaseMusic = "sons/Hangar.mp3"

	#Chãos do Mapa
	def Coloca_Chao(self, chao):
		# Posição | Comprimento
		chao.empty()
		chao.add(Chao([0,310], 512))
		chao.add(Chao([550,247], 410))
		chao.add(Chao([520,440], 475))
		chao.add(Chao([1000,375], 215))
		chao.add(Chao([1258,310], 160))
		chao.add(Chao([1227,440], 420))
		chao.add(Chao([1450,247], 160))
		chao.add(Chao([1643,376], 245))
		chao.add(Chao([1900,310], 540))

	# Paredes do Mapa
	def Coloca_Paredes(self, paredes):
		paredes.empty()
		paredes.add(Parede([514,437], 120))
		paredes.add(Parede([999,437], 60))
		paredes.add(Parede([1218,437], 60))

	# Lista de Melhorias
	# L - Vida Extra
	# R - Atirar 2x mais rápido
	# M - Tiro 2x mais forte
	
	def Coloca_Melhorias(self, melhorias):
		#Posição | Tipo
		melhorias.empty()
		melhorias.add(Melhoria([1043,170], "R"))
		melhorias.add(Melhoria([1529,170], "L"))

	# Lista de Inimigos

	# Explicando o Ativo:
	# Este valor significa a porcentagem da tela de distância entre o jogador e o inimigo.
	# Se o inimigo estiver em uma distância menor que a porcentagem, o inimigo entra no estado ativo (usa a Matriz de IA).
	# Exemplo: valor = 60  -> Se o jogador estiver em uma distância menor que 60% do tamanho da tela, o inimigo começa a atirar.

	# Explicando a Matriz de IA dos inimigos:
	# 0 - Direção que irá atirar. (0-midleft, 1-midright, 2-topright, 3-bottomright, 4-topleft, 5-bottomleft, 6-midtop)
	# 1 - Tempo de espera para iniciar a rajada, em milisegundos.
	# 2 - Quantidade de tiros da rajada
	# 3 - Tempo entre cada tiro da rajada, em milisegundos.
	# 4 - Correção em pixels da criação do tiro à partir da direção escolhida.
	# É seguida a ordem da esquerda para a direita. Volta ao início quando chegar ao fim.
	# Forma da matriz: matriz = [[0,1,2,3,4], [0,1,2,3,4], [0,1,2,3,4]]
	#

	# Forma do cálculo da correção de Pixels (4):
	#	  + 4 -/- 6 +/- 2 +

	#	  -   * * * * *   -
	#	  0       J       1
	#	  +   * * * * *   +

	#	  + 5 -/- 7 +/- 3 +       

	def Coloca_Inimigos(self, inimigos):
		# Posição | Sprite | Quantidade de Vidas | Escala | Escala da Explosão | Ativo (? = 0) | Matriz IA (? = None)
		inimigos.empty()

		inimigos.add(Inimigo([552,436], "sprites/Atirador/AtiradorEsquerdaCima.gif", 2, 1.5, 1.5, 60, [[4,1000,2,500, 0], [4,1000,3,500, 0]]))

		inimigos.add(Inimigo([655,240], "sprites/Atirador/AtiradorDeitadoEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,2,500, 0], [0,1000,1,500, 0]]))

		inimigos.add(Inimigo([797,436], "sprites/Atirador/AtiradorEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,3,500, -18], [0,1000,3,1000, -18]]))

		inimigos.add(Inimigo([855,70], "sprites/Torres/TorreBaixoEsquerda.gif", 5, 1.3, 1.3, 90, [[5,700,3,500, 0]]))

		inimigos.add(Inimigo([915,240], "sprites/Atirador/AtiradorEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,3,500, -18], [0,1000,3,1000, -18]]))

		inimigos.add(Inimigo([1014,450], "sprites/Torres/TorreEsquerda.gif", 5, 1.3, 1.3, 90, [[0,700,3,500, 0]]))

		inimigos.add(Inimigo([1145,374], "sprites/Atirador/BigGunMan.png", 4, 1.5, 1.5, 60, [[0,500,2,500, -13], [0,1000,3,500, -13]]))
		inimigos.add(Inimigo([1317,307], "sprites/Atirador/AtiradorEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,3,500, -18], [0,1000,3,1000, -18]]))
		inimigos.add(Inimigo([1432,436], "sprites/Atirador/AtiradorEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,3,500, -18], [0,1000,3,1000, -18]]))
		inimigos.add(Inimigo([1449,290], "sprites/Torres/TorreEsquerda.gif", 5, 1.5, 1.5, 60, [[0,1000,2,500, 0], [0,1000,3,500, 0]]))
		inimigos.add(Inimigo([1522,240], "sprites/Atirador/AtiradorDeitadoEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,2,500, 0], [0,1000,1,500, 0]]))
		inimigos.add(Inimigo([1740,462], "sprites/Torres/TorreCimaEsquerda.gif", 5, 1.3, 1.3, 90, [[4,700,3,500, 0]]))
		inimigos.add(Inimigo([1781,374], "sprites/Atirador/BigGunMan.png", 4, 1.5, 1.5, 60, [[0,500,2,500, -13], [0,1000,3,500, -13]]))
		inimigos.add(Inimigo([1992,306], "sprites/Paredes/Parede1.gif", 5, 1.5, 2))

		inimigos.add(Inimigo([2024,170], "sprites/Bosses/boss2.gif", 6, 0.5, 3.5, 90, [[7, 500, 4, 500, 0], [7, 500, 5, 500, 0]]))
		inimigos.add(Inimigo([2124,170], "sprites/Bosses/boss2.gif", 6, 0.5, 3.5, 90, [[7, 500, 4, 500, 0], [7, 500, 5, 500, 0]]))
		inimigos.add(Inimigo([2224,170], "sprites/Bosses/boss2.gif", 6, 0.5, 3.5, 90, [[7, 500, 4, 500, 0], [7, 500, 5, 500, 0]]))

		inimigos.add(Inimigo([2165,306], "sprites/Atirador/AtiradorDeitadoEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,2,500, 0], [0,1000,1,500, 0]]))
		inimigos.add(Inimigo([2124,462], "sprites/Torres/TorreCimaEsquerda.gif", 5, 1.3, 1.3, 90, [[4,700,3,500, 0]]))

		boss1 = Inimigo([2300,306], "sprites/Bosses/boss3.gif", 35, 1.5, 3.5, 90, [[0, 1000, 3, 500, -15], [5, 1000, 3, 500, 0]])
		inimigos.add(boss1)
		return boss1
