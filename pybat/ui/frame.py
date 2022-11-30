import pygame as pg


class Frame(list):
    def __init__(self):l
        super().__init__()

        self._rect = pg.Rect(0, 0, 0, 0)
        self._padding = 0

    @propety
    def set_padding(self, val: float):
        self._padding = val

    @property
    def x(self):
        return self._rect.x

    @x.setter
    def x(self):
        self._rect.x = x

    @property
    def y(self):
        return self._rect.y

    @x.setter
    def y(self):
        self._rect.y = y

    def draw(self, screen: pg.Surface):
        pass
