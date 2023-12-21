import pygame

from settings import *


class Level:

    def __init__(self) -> None:
        # get the display surface
        # получение отображения дисплея
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        # настройка группы спрайтов
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        # sprite setup
        # настройки спрайтов
        self.create_map

    def create_map(self):
        # method for create world map
        #метод для создания карты миры
        for row_index, row in enumerate(WORLD_MAP):
            print(row_index)
            print(row)
    
    def run(self):
        # update and draw the game
        # обновить и нарисовать игру
        pass
