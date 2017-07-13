import pygame


class Parede(pygame.sprite.Sprite):
	def __init__(self, posicao, tamanho):
		pygame.sprite.Sprite.__init__(self)
		self.Pos = posicao
		#self.image = pygame.image.load("sprites/chao.png")
		self.image = pygame.image.load("sprites/null.gif")
		self.image = pygame.transform.scale(self.image, (2, tamanho))
		self.rect = self.image.get_rect()
		self.rect.bottomleft = self.Pos

	def update(self, inc):
		self.Pos[0] -= inc
		self.rect.bottomleft = self.Pos