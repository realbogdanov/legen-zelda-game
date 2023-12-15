import pygame, sys
from settings import *

class Game:
	def __init__(self):
		# general setup
		# основные настройки, инициализация игры
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption("Zelda")
		self.clock = pygame.time.Clock()

	def run(self):
		#Operation of the game and its closing conditions
		#Работа игры и условия её закрытия
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			self.screen.fill("black")
			pygame.display.update()
			self.clock.tick(FPS)
		pass


if __name__ == '__main__':
	game = Game()
	game.run()
 