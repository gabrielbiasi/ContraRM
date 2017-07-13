#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from Inimigo import *
from Melhoria import *
from Parede import *
from Chao import *

class SnowField:
	FaseCaminho = "mapas/SnowField.png"
	FaseLargura = 4877
	FaseMusic = "sons/SnowField.mp3"

	#Chãos do Mapa
	def Coloca_Chao(self, chao):
		# Posição | Comprimento
		chao.empty()
		chao.add(Chao([0,310], 650))
		chao.add(Chao([710,232], 220))
		chao.add(Chao([656,406], 310))
		chao.add(Chao([980,310], 240))
		chao.add(Chao([1170,407], 250))
		chao.add(Chao([1430,214], 240))
		chao.add(Chao([1366,311], 570))
		chao.add(Chao([1845,214], 270))
		chao.add(Chao([2073,312], 440))
		chao.add(Chao([2200,215], 310))
		chao.add(Chao([2520,440], 450))
		chao.add(Chao([2650,215], 250))
		chao.add(Chao([2970,345], 60))
		chao.add(Chao([3036,250], 120))
		chao.add(Chao([3228,310], 120))
		chao.add(Chao([3420,310], 60))
		chao.add(Chao([3550,248], 120))
		chao.add(Chao([3740,310], 310))
		chao.add(Chao([4060,356], 810))

	# Paredes do Mapa
	def Coloca_Paredes(self, paredes):
		paredes.empty()
		paredes.add(Parede([2510,435], 120))
		paredes.add(Parede([2970,438], 90))
		paredes.add(Parede([3035,340], 40))
		paredes.add(Parede([4055,356], 40))
		paredes.add(Parede([4682,356], 40))

	# Lista de Melhorias
	# L - Vida Extra
	# R - Atirar 2x mais rápido
	# M - Tiro 2x mais forte
	def Coloca_Melhorias(self, melhorias):
		# Posição | Tipo
		melhorias.empty()
		melhorias.add(Melhoria([3435,307], "L"))
		melhorias.add(Melhoria([1170,400], "R"))
		melhorias.add(Melhoria([1739,161], "M"))

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

		inimigos.add(Inimigo([543,309], "sprites/Atirador/AtiradorEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,3,500, -18], [0,1000,3,1000, -18]]))
		inimigos.add(Inimigo([788,228], "sprites/Atirador/AtiradorDeitadoEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,3,500, 0], [0,1000,3,1000, 0]]))

		inimigos.add(Inimigo([740,404], "sprites/Fogo/1.gif", 2, 1, 1))
		inimigos.add(Inimigo([770,404], "sprites/Fogo/1.gif", 2, 1, 1))
		inimigos.add(Inimigo([800,404], "sprites/Fogo/1.gif", 2, 1, 1))
		inimigos.add(Inimigo([830,404], "sprites/Fogo/1.gif", 2, 1, 1))
		inimigos.add(Inimigo([860,404], "sprites/Fogo/1.gif", 2, 1, 1))
		inimigos.add(Inimigo([890,404], "sprites/Fogo/1.gif", 2, 1, 1))

		inimigos.add(Inimigo([1120,309], "sprites/Atirador/BigGunMan.png", 4, 1.5, 1.5, 60, [[0,500,2,500, -13], [0,1000,3,500, -13]]))

		inimigos.add(Inimigo([1366,400], "sprites/Atirador/AtiradorDeitadoEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,2,500, 0], [0,1000,1,500, 0]]))

		inimigos.add(Inimigo([1508,309], "sprites/Atirador/BigGunMan.png", 4, 1.5, 1.5, 60, [[0,500,2,500, -13], [0,1000,3,500, -13]]))

		inimigos.add(Inimigo([1571,211], "sprites/Atirador/AtiradorEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,3,500, -18], [0,1000,3,1000, -18]]))

		inimigos.add(Inimigo([2151,309], "sprites/Atirador/AtiradorEsquerdaCima.gif", 2, 1.5, 1.5, 60, [[4,1000,3,500, 0], [4,1000,3,1000, 0]]))

		inimigos.add(Inimigo([2369,309], "sprites/Atirador/AtiradorEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,3,500, -18], [0,1000,3,1000, -18]]))

		inimigos.add(Inimigo([2405,211], "sprites/Atirador/BigGunMan.png", 5, 1.5, 1.5, 60, [[0,500,2,500, -13], [0,1000,3,500, -13]]))

		inimigos.add(Inimigo([2600,435], "sprites/Fogo/1.gif", 2, 1, 1))
		inimigos.add(Inimigo([2660,435], "sprites/Fogo/1.gif", 2, 1, 1))

		inimigos.add(Inimigo([2725,288], "sprites/Torres/TorreBaixoEsquerda.gif", 5, 1.3, 1.3, 90, [[5,700,3,500, 0], [5, 500, 5, 500, 0]]))

		inimigos.add(Inimigo([2791,211], "sprites/Atirador/AtiradorEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,3,500, -18], [0,1000,3,1000, -18]]))

		inimigos.add(Inimigo([2855,435], "sprites/Atirador/AtiradorEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,3,500, -18], [0,1000,3,1000, -18]]))

		inimigos.add(Inimigo([3170,430], "sprites/Atirador/NadadorCima.gif", 5, 1.5, 2, 80, [[6,600,2,500, -5]]))
		inimigos.add(Inimigo([3362,442], "sprites/Atirador/NadadorCima.gif", 5, 1.5, 2, 80, [[6,600,2,500, -5]]))
		inimigos.add(Inimigo([3494,430], "sprites/Atirador/NadadorCima.gif", 5, 1.5, 2, 80, [[6,600,2,500, -5]]))
		inimigos.add(Inimigo([3598,243], "sprites/Atirador/AtiradorDeitadoEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,2,500, 0], [0,1000,1,500, 0]]))
		inimigos.add(Inimigo([3685,442], "sprites/Atirador/NadadorCima.gif", 5, 1.5, 2, 80, [[6,600,2,500, -5]]))
		inimigos.add(Inimigo([3949,309], "sprites/Atirador/AtiradorEsquerda.gif", 2, 1.5, 1.5, 60, [[0,1000,3,500, -18], [0,1000,3,1000, -18]]))
		inimigos.add(Inimigo([4222,370], "sprites/Paredes/Parede1.gif", 5, 1.5, 2))
		inimigos.add(Inimigo([4346,355], "sprites/Atirador/BigGunMan.png", 4, 1.5, 1.5, 60, [[0,500,2,500, -13], [0,1000,3,500, -13]]))
		inimigos.add(Inimigo([4605,166], "sprites/null.gif", 5, 1.5, 2, 80, [[5,600,2,500, 0], [7, 500, 5, 500, 0], [5, 500, 4, 500, 0], [7, 500, 5, 500, 0]]))
		inimigos.add(Inimigo([4644,166], "sprites/null.gif", 5, 1.5, 2, 80, [[3,600,2,500, 0], [7, 500, 5, 500, 0], [3, 500, 4, 500, 0], [7, 500, 5, 500, 0]]))
		inimigos.add(Inimigo([4460,160], "sprites/Bosses/boss2.gif", 6, 0.5, 3.5, 90, [[7, 500, 4, 500, 0], [7, 500, 5, 500, 0]]))
		inimigos.add(Inimigo([4750,160], "sprites/Bosses/boss2.gif", 6, 0.5, 3.5, 90, [[5, 500, 4, 500, 0], [5, 500, 5, 500, 0]]))
		boss1 = Inimigo([4580,180], "sprites/Bosses/boss2.gif", 30, 1.5, 3.5, 90, [[7, 500, 4, 500, 0], [7, 500, 5, 500, 0]])
		inimigos.add(boss1)
		return boss1