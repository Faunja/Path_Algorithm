import pygame

class define_Controls:
	def __init__(self):
		self.quitGame = pygame.K_ESCAPE
		
		self.changeCamera = [pygame.K_c]
		self.changeTime = [pygame.K_t]

		self.changedisplayStats = [pygame.K_F3, pygame.K_s]
		self.fullscreen = [pygame.K_F11, pygame.K_f]

Controls = define_Controls()
