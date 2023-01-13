from enum import IntEnum

import pygame as pg

from config import Paths
from tools import resmngr


class Player:
    class Type(IntEnum):
        Red = 0
    
    def __init__(self, surface: pg.Surface, type=None):
        self.surface = surface
        
        self.image = {
            Player.Type.Red: resmngr['red_bat'],
            None: resmngr['default_bat'],
        }[type]

    def draw(self):
        self.surface.blit(self.image, self.image.get_rect())