import pygame

class PlacarVida():
	def __init__(self, posicao):
		self.img = pygame.image.load("sprites/Vida.png").convert()
		self.img = pygame.transform.scale(self.img, (int(self.img.get_width()*1.5),int(self.img.get_height()*1.5)))
		self.Pos = posicao
		self.rect = self.img.get_rect()
		self.rect.topleft = self.Pos


	def update(self, tela, qtd):
		for i in range(0, qtd):
			rect = pygame.Rect([self.Pos[0] + (20*i), self.Pos[1]], self.rect.bottomleft)
			tela.blit(self.img, rect)
