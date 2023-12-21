import pygame
from pygame.sprite import _Group
from settings import *


class Player(pygame.sprite.Sprite):
    """
    Based class player
    Базовый класс определяющий игрока
    """

    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
