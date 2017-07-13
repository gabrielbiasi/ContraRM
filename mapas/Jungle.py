#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from Inimigo import *
from Melhoria import *
from Parede import *
from Chao import *

class Jungle:
	FaseCaminho = "mapas/Jungle.png"
	FaseLargura = 2742
	FaseMusic = "sons/Jungle.mp3"

	#Chãos do Mapa
	def Coloca_Chao(self, chao):
		# Posição | Comprimento
		chao.empty()
		chao.add(Chao([0,237], 2742))
		chao.add(Chao([323,300], 192))
		chao.add(Chao([515,363], 256))
		chao.add(Chao([836,300], 128))
		chao.add(Chao([1222,427], 128))
		chao.add(Chao([1286,349], 128))
		chao.add(Chao([1417,326], 128))
		chao.add(Chao([1928,320], 64))

	# Paredes do Mapa
	def Coloca_Paredes(self, paredes):
		paredes.empty()
		#paredes.add(Parede([150,237], 50))

	# Lista de Melhorias
	# L - Vida Extra
	# R - Atirar 2x mais rápido
	# M - Tiro 2x mais forte
	def Coloca_Melhorias(self, melhorias):
		# Posição | Tipo
		melhorias.empty()
		melhorias.add(Melhoria([2230,237], "L"))
		melhorias.add(Melhoria([1230,425], "R"))
		melhorias.add(Melhoria([1940,320], "M"))

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

		inimigos.add(Inimigo([400,300], "sprites/Atirador/AtiradorEsquerdaCima.gif", 2, 1.5, 1.5, 60, [[4,1000,3,300, 0], [4, 1000, 2, 500, 0]]))

		inimigos.add(Inimigo([700,360], "sprites/Atirador/AtiradorEsquerdaCima.gif", 2, 1.5, 1.5, 60, [[4,1000,3,300, 0], [4, 1000, 2, 500, 0]]))

		inimigos.add(Inimigo([929,237], "sprites/Atirador/AtiradorEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,3,500, -18], [0,1000,3,1000, -18]]))
		inimigos.add(Inimigo([1050,350], "sprites/Torres/TorreCima.gif", 3, 1.3, 1.3, 60, [[6,1000,3,500, 0]]))

		inimigos.add(Inimigo([1160,237], "sprites/Atirador/AtiradorDeitadoEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,2,500, 0], [0,1000,1,500, 0]]))
		inimigos.add(Inimigo([1308,347], "sprites/Fogo/1.gif", 2, 1, 1))
		inimigos.add(Inimigo([1374,347], "sprites/Fogo/1.gif", 2, 1, 1))
		inimigos.add(Inimigo([1310,428], "sprites/Atirador/AtiradorEsquerdaCima.gif", 2, 1.5, 1.5, 60, [[4,700,3,500, 0], [4,700,2,500, 0]]))

		inimigos.add(Inimigo([1490,323], "sprites/Atirador/AtiradorEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,3,500, -18], [0,1000,3,1000, -18]]))
		inimigos.add(Inimigo([1650,428], "sprites/Atirador/NadadorCima.gif", 5, 1.5, 2, 80, [[6,600,2,500, -5]]))

		inimigos.add(Inimigo([1870,350], "sprites/Torres/TorreCimaEsquerda.gif", 5, 1.3, 1.3, 60, [[4,1500,5,400, -10]]))
		inimigos.add(Inimigo([2010,350], "sprites/Torres/TorreCimaEsquerda.gif", 3, 1.3, 1.3, 60, [[4,700,3,500, -10]]))
		inimigos.add(Inimigo([2080,237], "sprites/Atirador/AtiradorEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,3,500, -18], [0,1000,3,1000, -18]]))

		inimigos.add(Inimigo([2170,428], "sprites/Atirador/NadadorCima.gif", 5, 1.5, 2, 80, [[6,600,2,500, -5]]))
		inimigos.add(Inimigo([2320,428], "sprites/Atirador/NadadorCima.gif", 5, 1.5, 2, 80, [[6,600,2,500, -5]]))

		inimigos.add(Inimigo([2400,237], "sprites/Paredes/Parede1.gif", 10, 1.5, 2))
		boss1 = Inimigo([2595,237], "sprites/Bosses/boss3.gif", 30, 1.5, 3.5, 90, [[0, 1000, 3, 500, -30], [5, 1000, 3, 500, 80]])
		inimigos.add(boss1)
		return boss1