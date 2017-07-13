import pygame, glob

class Animacao():


	def __init__(self, caminho, escala, vel):
		self.time = 0
		self.Escala = escala
		self.ani_speed = vel
		self.ani = glob.glob(caminho)
		self.ani.sort()
		self.ani_pos = 0
		self.ani_max = len(self.ani) - 1
		self.img = pygame.image.load(self.ani[0]).convert()
		self.img = pygame.transform.scale(self.img, (int(self.img.get_width()*self.Escala),int(self.img.get_height()*self.Escala)))
		self.update(0)

	def update(self, tempo_atual):
		self.time += tempo_atual
		if self.time > self.ani_speed:
			self.time = 0
			self.img = pygame.image.load(self.ani[self.ani_pos]).convert()
			self.img  = pygame.transform.scale(self.img, (int(self.img.get_width()*self.Escala),int(self.img.get_height()*self.Escala)))
			if self.ani_pos == self.ani_max:
				self.ani_pos = 0
			else:
				self.ani_pos += 1

	def getSpriteAtual(self, tempo):
		self.update(tempo)
		return self.img

