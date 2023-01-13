from enum import IntEnum

import pygame as pg

from config import Paths
from tools import load_image


class Player:
    class Type(IntEnum):
        Red = 0
    
    def __init__(self, surface: pg.Surface, type=None):
        self.surface = surface
        scale = 6
        
        match type:
            case Player.Type.Red:
                self.image = load_image(Paths.images / 'red_bat.png', scale=scale)
            case _:
                self.image = load_image(Paths.images / 'default_bat.png', scale=scale)

    def draw(self):
        self.surface.blit(self.image, self.image.get_rect())