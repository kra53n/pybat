import pygame as pg
from pygame import Vector2 as V2


class Frame(list):
    def __init__(self, **kw):
        super().__init__()

        self._rect = pg.Rect(0, 0, 0, 0)
        if 'rect' in kw:
            self._rect = kw['rect']

        self._padding = 0
        if 'padding' in kw:
            self._padding = kw['padding']

        self._to_centerize = False

    @property
    def x(self):
        return self._rect.x

    @property
    def y(self):
        return self._rect.y

    @property
    def w(self):
        return self._rect.w

    @w.setter
    def w(self, val):
        self._rect.w = val
        for obj in self:
            obj._rect.w = val

    def append(self, obj):
        super().append(obj)
        obj._rect.y = self._rect.h
        obj._rect.x = 0
        obj._rect.w = self._rect.w
        self._rect.h += self._padding + obj._rect.h

    def centerize(self, rect: pg.Rect):
        diff = V2(rect.center) - V2(self._rect.center)
        self._rect.x += diff.x
        self._rect.y += diff.y
        for obj in self:
            obj._rect.x += diff.x
            obj._rect.y += diff.y

    def update(self):
        for obj in self:
            obj.update()

    def draw(self, screen: pg.Surface):
        for obj in self:
            obj.draw(screen)
