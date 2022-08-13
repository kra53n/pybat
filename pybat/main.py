import pygame as pg

from config import Window


class Game:
    def __init__(self):
        pg.init()
        self._screen = pg.display.set_mode(Window.size, pg.SCALED)
        pg.display.set_caption(Window.title)

        self._run = True

        self._loop()

    def _update_keydown(self, key):
        pass

    def _update_keyup(self, key):
        pass

    def _update(self):
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    self._run = False
                case pg.KEYDOWN:
                    self._update_keydown(event.key)
                case pg.KEYUP:
                    self._update_keyup(event.key)

    def _loop(self):
        while self._run:
            self._update()


if __name__ == '__main__':
    Game()
