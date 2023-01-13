import pygame as pg


class Unit:
    def __init__(self, surface: pg.Surface, texture: pg.Surface):
        self.surface = surface
        self.texture = texture
    
    def draw(self):
        self.surface.blit(self.texture, self.texture.get_rect())