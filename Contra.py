#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Universidade Estadual de Mato Grosso do Sul
# Bacharelando em Ciência da Computação
# Tópicos em Computação I
# Trabalho Semestral, Remake do jogo Contra.

# Feito por:
# Gabriel de Biasi, 024785
# Guilherme Henrique Vieira Pereira, 024787

import pygame, random, sys
from pygame.locals import *
from Jogador import *
from TelaInicio import *
from Background import *
from Animacao import *
from Tiro import *
from Inimigo import *
from Melhoria import *
from PlacarVida import *

#Tamanho da Tela e FPS.
resolucao = (512,480)
FPS = 60
SONS = True


# Variáveis de controle do jogo.
loop = True
main = True
tempo = 0
inicio = False
fundo = None
fimdafase = False
Fases = []
FaseNum = 0
TrocaFase = False

# Possibilita iniciar o game em uma fase específica.
if len(sys.argv) == 2:
	FaseNum = int(sys.argv[1])-1

# Fases (O jogo segue a ordem que são colocadas na lista)
from mapas import Jungle, Hangar, SnowField

Fases.append(Jungle.Jungle())
Fases.append(SnowField.SnowField())
Fases.append(Hangar.Hangar())


pygame.init() # Inicializa o Pygame.
pygame.mixer.init() # Inicializa o mixer do pygame.
clock = pygame.time.Clock() # Criação do relógio do jogo.
pygame.display.set_caption("Contra RM 1.0") # Título da janela.
tela = pygame.display.set_mode(resolucao) # Resolução da tela.
pygame.key.set_repeat(50, 1000) # Permite repetição de teclas.
font = pygame.font.Font("fontes/font.ttf", 45) # Fonte utilizada no jogo.

chao = pygame.sprite.Group() # Conjunto de chãos do mapa.
paredes = pygame.sprite.Group() # Conjunto de paredes do mapa.
inimigos = pygame.sprite.Group() # Conjunto dos inimigos.
explosoes = pygame.sprite.Group() # Conjunto dos explosões.
melhorias = pygame.sprite.Group() # Conjunto de melhorias espalhadas.
tiros_lance = pygame.sprite.Group() # Conjunto de tiros do Lance.
tiros_inimigos = pygame.sprite.Group() # Conjunto de tiros dos Inimigos.

# Lance: Posição | Quant. de Vidas | Tempo Ivulnerável (ms) | Vel. de Mov. | Vel. do Tiro | Altura Max. Pulo | Gravidade | Vel. dos Frames | Resolucao da Tela
lance = Jogador([100,100], 3, 2500, 100, 200, 80, 600, 80, resolucao)

tela_inicio = TelaInicio(resolucao) # Carrega a tela de Inicio.
placar = PlacarVida([30,30]) # Cria o placar de Vidas


while main:
	temp = 0 # temporária
	if TrocaFase: # Caso para modificar a fase.
		TrocaFase = False
		tela.fill([255,255,255])
		loop = True
		fimdafase = False
		lance.reset(1)
		tiros_lance.empty()
		tiros_inimigos.empty()
		if fundo != None:
			del(fundo) # Se houver, destroi a fase atual.
		fundo = Background(Fases[FaseNum].FaseCaminho, resolucao, Fases[FaseNum].FaseLargura) # Objeto que representa o fundo do jogo.
		pygame.mixer.music.load(Fases[FaseNum].FaseMusic) # Carrega música de fundo da fase.
		Fases[FaseNum].Coloca_Chao(chao) # Posiciona o chão no jogo.
		Fases[FaseNum].Coloca_Paredes(paredes) # Posiciona as paredes no jogo.
		Fases[FaseNum].Coloca_Melhorias(melhorias) # Posiciona todas as melhorias no mapa.
		Boss = Fases[FaseNum].Coloca_Inimigos(inimigos) # Posiciona todos os inimigos no mapa.
		if SONS:
			pygame.mixer.music.play(-1)

	while loop:
		tempo = clock.tick(FPS) # Obtem o tempo entre as iterações.
		for event in pygame.event.get():
			#Caso para encerrar o programa.
			if event.type == QUIT:
				loop = False
				main = False
		keys = pygame.key.get_pressed()
		if inicio:
			if lance.Vidas > 0: # Se ele estiver com vida restante, continua o jogo.
				if fimdafase == False:
					if lance.Vivo: # Se ele está vivo, os comandos são lidos.
						# Grande Tratador de Teclado
						if keys[K_ESCAPE]:
							loop = False
							main = False
						if keys[K_RIGHT] and keys[K_UP] and keys[K_z]:
							lance.atirar(tiros_lance, tempo)
							lance.andaDireita(1, tempo)
						elif keys[K_LEFT] and keys[K_UP] and keys[K_z]:
							lance.atirar(tiros_lance, tempo)
							lance.andaEsquerda(1, tempo)
						elif keys[K_RIGHT] and keys[K_UP] and keys[K_x]:
							lance.pular(tempo)
							lance.andaDireita(1, tempo)
						elif keys[K_LEFT] and keys[K_UP] and keys[K_x]:
							lance.pular(tempo)
							lance.andaEsquerda(1, tempo)
						elif keys[K_RIGHT] and keys[K_DOWN] and keys[K_z]:
							lance.atirar(tiros_lance, tempo)
							lance.andaDireita(2, tempo)
						elif keys[K_LEFT] and keys[K_DOWN] and keys[K_z]:
							lance.atirar(tiros_lance, tempo)
							lance.andaEsquerda(2, tempo)
						elif keys[K_RIGHT] and keys[K_z]:
							lance.atirar(tiros_lance, tempo)
							lance.andaDireita(0, tempo)
						elif keys[K_LEFT] and keys[K_z]:
							lance.atirar(tiros_lance, tempo)
							lance.andaEsquerda(0, tempo)
						elif keys[K_RIGHT] and keys[K_UP]:
							lance.andaDireita(1, tempo)
						elif keys[K_LEFT] and keys[K_UP]:
							lance.andaEsquerda(1, tempo)
						elif keys[K_RIGHT] and keys[K_DOWN]:
							lance.andaDireita(2, tempo)
						elif keys[K_LEFT] and keys[K_DOWN]:
							lance.andaEsquerda(2, tempo)
						elif keys[K_UP] and keys[K_z]:
							lance.cima(tempo)
							lance.atirar(tiros_lance, tempo)
						elif keys[K_DOWN] and keys[K_z]:
							lance.deitar(tempo)
							lance.atirar(tiros_lance, tempo)
						elif keys[K_DOWN] and keys[K_x]:
							lance.cair(tempo)
						elif keys[K_RIGHT] and keys[K_x]:
							lance.pular(tempo)
							lance.andaDireita(0, tempo)
						elif keys[K_LEFT] and keys[K_x]:
							lance.pular(tempo)
							lance.andaEsquerda(0, tempo)
						elif keys[K_UP] and keys[K_x]:
							lance.pular(tempo)
						elif keys[K_x] and keys[K_z]:
							lance.pular(tempo)
							lance.atirar(tiros_lance, tempo)
						elif keys[K_UP]:
							lance.cima(tempo)
						elif keys[K_DOWN]:
							lance.deitar(tempo)
						elif keys[K_RIGHT]:
							lance.andaDireita(0, tempo)
						elif keys[K_LEFT]:
							lance.andaEsquerda(0, tempo)
						elif keys[K_x]:
							lance.pular(tempo)
						elif keys[K_z]:
							lance.parar(tempo)
							lance.atirar(tiros_lance, tempo)
						elif keys[K_r]:
							lance.Vidas = 1
							lance.morre(tempo)
						elif keys[K_d]:
							lance.morre(tempo)
						elif keys[K_1]:
							lance.NivelTiro = 2
						elif keys[K_2]:
							lance.TempoTiro = 150
						elif keys[K_3]:
							lance.Vidas = 23
						elif keys[K_f]:
							fimdafase = True
						elif keys[K_m]:
							lance.Vidas = 23
							lance.Ivulneravel = True
							lance.TempoIvulneravel = 600000
							lance.NivelTiro = 100
							lance.TempoTiro = 150
							lance.Velocidade = 250/1000.0
						else:
							lance.parar(tempo)

					# ATUALIZAÇÕES DE POSIÇÕES/TEMPO
					lance.atualiza(chao, paredes, inimigos, tiros_inimigos, melhorias, tempo) # Aplica a gravidade, trata a colisão com o chão, com inimigos, com as melhorias e faz o movimento do pulo.
					tiros_lance.update(inimigos, explosoes, tempo, resolucao) # Atualiza a posição de cara tiro do Lance.
					inimigos.update(lance, tiros_inimigos, resolucao, tempo) # Atualiza os inimigos.
					tiros_inimigos.update(tempo, resolucao) # Atualiza os tiros inimigos.
					explosoes.update(tempo) # Atualiza as explosões.

					# DESENHOS NA TELA
					fundo.desenha(tela, lance, chao, paredes, inimigos, tiros_inimigos, explosoes, melhorias) # Desenha o cenário e o mantém na posição correta de acordo com o Lance.
					tela.blit(lance.image, lance.rect) # Desenha o Lance.
					inimigos.draw(tela) # Desenha todos os inimigos.
					tiros_lance.draw(tela) # Desenha todos os tiros do Lance.
					tiros_inimigos.draw(tela) # Desenha todos os tiros do Lance.
					explosoes.draw(tela) # Desenha as explosões ativas.
					melhorias.draw(tela) # Desenha as melhorias.
					placar.update(tela, lance.Vidas) # Desenha o placar.

					# BARRA DE VIDA DO BOSS E ENCERRAMENTO DA FASE
					if fundo.Fimdomapa == True and Boss.Vidas > 0: # Matando o boss
						pygame.draw.rect(tela, [35,205,35], [97, 70, 308, 8])
						pygame.draw.rect(tela, [255,0,0], [100, 73, (300/Boss.VidasInit)*Boss.Vidas, 2])
					elif Boss.Vidas <= 0: # Se matou o boss..
						inimigos.empty()
						tiros_inimigos.empty()
						if temp > 2000:
							fimdafase = True
						else:
							temp += tempo
				else:
					# Matou o Boss!
					pygame.mixer.music.stop()
					pygame.draw.rect(tela, [0,0,0], (100,100,300,300))
					if(FaseNum+1 == len(Fases)):
						text = "GAME"
						main = False
					else:
						text = "LEVEL"
					text1 = font.render(text, True, (255,255,255))
					text2 = font.render("COMPLETE", True, (255,255,255))
					text3 = font.render("[ENTER]", True, (255,255,255))
					tela.blit (text1, [190,130])
					tela.blit (text2, [140,180])
					tela.blit (text3, [170,340])
					if keys[K_RETURN]:
						loop = False
						FaseNum += 1
						TrocaFase = True
					elif keys[K_ESCAPE]:
						loop = False
						main = False
			else:
				# GAME OVER! Imprime o menu na tela e dá a possibilidade de começar de novo.
				pygame.mixer.music.stop()
				pygame.draw.rect(tela, [0,0,0], (100,100,300,300))
				text1 = font.render("GAME OVER", True, (255,0,0))
				text2 = font.render("CONTINUE?", True, (255,255,255))
				text3 = font.render("Y/N", True, (255,255,255))
				tela.blit (text1, [130,130])
				tela.blit (text2, [140,240])
				tela.blit (text3, [210,290])
				if keys[K_y]: # Caso positivo, refaz o jogo.
					TrocaFase = True
					loop = False
					if SONS:
						pygame.mixer.music.rewind()
						pygame.mixer.music.play(-1)
				elif keys[K_n] or keys[K_ESCAPE]:
					loop = False
					main = False
			#pos = pygame.mouse.get_pos()
			#print('pos? ['+str(pos)+'] pos real? ['+str(pos[0]-fundo.posicao[0])+','+str(pos[1])+']')
		else:
			# Inicio do Jogo, desenha a Tela Inicial.
			tela_inicio.update(tempo)
			tela.blit(tela_inicio.image, tela_inicio.rect)
			if keys[K_RETURN]:
				TrocaFase = True
				inicio = True
				loop = False
			elif keys[K_ESCAPE]:
				loop = False
				main = False
		pygame.display.flip()
pygame.quit()
sys.exit()