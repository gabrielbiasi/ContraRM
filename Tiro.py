import pygame
from Animacao import *
from Explosao import *

class Tiro(pygame.sprite.Sprite):

	def __init__(self, jogador, nivel, velocidade):
		pygame.sprite.Sprite.__init__(self)
		self.Velocidade = velocidade
		self.Nivel = nivel
		self.image = pygame.image.load("sprites/Tiros/"+str(nivel)+".gif").convert_alpha()
		self.rect = self.image.get_rect()
		if jogador.estado == 0 or jogador.estado == 2 or jogador.estado == 4 or jogador.estado == 6:
			if jogador.estado != 6:
				inc = 5
			else:
				inc = 0
			self.rect.center = [jogador.rect.midright[0], jogador.rect.midright[1]-inc]
			self.Direcao = 1
		elif jogador.estado == 1 or jogador.estado == 3 or jogador.estado == 5 or jogador.estado == 7:
			if jogador.estado != 7:
				inc = 5
			else:
				inc = 0
			self.rect.center = [jogador.rect.midleft[0], jogador.rect.midleft[1]-inc]
			self.Direcao = 0
		elif jogador.estado == 10:
			self.rect.center = jogador.rect.topright
			self.Direcao = 2
		elif jogador.estado == 12:
			self.rect.center = [jogador.rect.bottomright[0], jogador.rect.bottomright[1]-20]
			self.Direcao = 3
		elif jogador.estado == 11:
			self.rect.center = jogador.rect.topleft
			self.Direcao = 4
		elif jogador.estado == 13:
			self.rect.center = [jogador.rect.bottomleft[0], jogador.rect.bottomleft[1]-20]
			self.Direcao = 5
		elif jogador.estado == 8:
			self.rect.center = [jogador.rect.midtop[0]+6, jogador.rect.midtop[1]]
			self.Direcao = 6
		elif jogador.estado == 9:
			self.rect.center = [jogador.rect.midtop[0]-2, jogador.rect.midtop[1]]
			self.Direcao = 6
		self.Pos = self.rect.center

	# Metodo para atualizar a posicao de cada tiro
	def update(self, inimigos, explosoes, tempo, resolucao):
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
		self.Pos = inc
		self.rect.center = self.Pos
		# Caso o tiro ultrapasse o limite da tela, ele eh removido do grupo de tiros.
		rect_resolucao = pygame.Rect([0,0],resolucao)
		if rect_resolucao.contains(self) == False:
			self.kill()
		else:
			sprite = pygame.sprite.spritecollideany(self, inimigos) # Colisao do tiro do Lance com algum inimigo.
			if sprite != None:
				sprite.Vidas -= self.Nivel
				self.kill()
				if sprite.Vidas <= 0:
					explosoes.add(Explosao(sprite.rect.center, 700, sprite.Escala_Explosao))
					inimigos.remove(sprite)



		