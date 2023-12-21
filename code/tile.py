import pygame
from pygame.sprite import _Group
from settings import *


class Tile(pygame.sprite.Sprite):
    """
    Based class tile, tile == 64
    Базовый класс определяющий плитку, плитка == 64
    """

    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
