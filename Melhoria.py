import pygame

class Melhoria(pygame.sprite.Sprite):

	def __init__(self, posicao, tipo):
		pygame.sprite.Sprite.__init__(self)
		self.Pos = posicao
		self.image = pygame.image.load("sprites/Melhorias/"+str(tipo)+".gif").convert()
		self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*1.5),int(self.image.get_height()*1.5)))
		self.rect = self.image.get_rect()
		self.rect.bottomleft = self.Pos
		self.Tipo = tipo

	def move(self, inc):
		self.Pos[0] -= inc
		self.rect.bottomleft = self.Pos