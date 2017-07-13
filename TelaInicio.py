import pygame
from Animacao import *
class TelaInicio(pygame.sprite.Sprite):

	def __init__(self, resolucao):
		pygame.sprite.Sprite.__init__(self)
		self.Resolucao = resolucao
		self.Anim = Animacao("mapas/inicio/*.png", 1, 500)
		self.image = self.Anim.img
		self.rect = self.image.get_rect()
		self.rect.topleft = [0,0]

	def update(self, tempo):
		self.image = self.Anim.getSpriteAtual(tempo)
		self.image = pygame.transform.scale(self.image, self.Resolucao)