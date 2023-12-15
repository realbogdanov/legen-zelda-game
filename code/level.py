import pygame


class Level:
    def __init__(self) -> None:

        # sprite group setup
        # настройка группы спрайтов
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
    
    def run(self):

        # update and draw the game
        # обновить и нарисовать игру
        pass
