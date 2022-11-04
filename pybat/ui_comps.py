import pygame as pg

from config import font


class Button:
    def __init__(self,
                 text: str,
                 rect: pg.Rect,

                 #functions
                 action,

                 border_radius: int,
                 active_col: int,
                 non_active_col:int):
        self._text = text
        self._rect = rect.copy()

        self._action = action

        self._border_radius = border_radius
        self._active_col = active_col
        self._non_active_col = non_active_col

        self._cols = self._active_col, self._non_active_col

    def __str__(self):
        return f'<Button> - text: {self._text}, x: {self._rect.x}, y: {self._rect.y}'

    def _cover(self):
        return self._rect.collidepoint(pg.mouse.get_pos())

    def update(self):
        if self._cover() and pg.mouse.get_pressed()[0]:
            self._action()

    def draw(self, screen: pg.Surface):
        covering = self._cover()
        ren = font.render(self._text, True, self._cols[covering])

        pg.draw.rect(screen, self._cols[not covering], self._rect,
                     border_radius=self._border_radius)

        rect = ren.get_rect()
        rect.center = self._rect.center
        screen.blit(ren, rect)
