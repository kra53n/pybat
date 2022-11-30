import pygame as pg

from config import Window, font, button_settings
from player import Player
from ui.button import Button
from menu import menu


class Game:
    def __init__(self):
        pg.init()
        self._screen = pg.display.set_mode(Window.size)
        pg.display.set_caption(Window.title)

        self._run = True
        self._clock = pg.time.Clock()
        self._player = Player()

        self._objs = Button(font, text='hello', action = lambda: print('hey'), **button_settings),

        self._draw()
        self._loop()

    def _draw(self):
        self._screen.fill(Window.bg)
        self._screen.blit(self._player.image, (20, 20))

        for obj in self._objs:
            obj.draw(self._screen)

    def _update_keydown(self, key):
        pass

    def _update_keyup(self, key):
        pass

    def _update(self):
        for event in pg.event.get():
            self._draw()

            match event.type:
                case pg.QUIT:
                    self._run = False
                case pg.KEYDOWN:
                    self._update_keydown(event.key)
                case pg.KEYUP:
                    self._update_keyup(event.key)

        for obj in self._objs:
            obj.update()

        pg.display.flip()

    def _loop(self):
        menu(self._screen)
        while self._run:
            self._clock.tick(60)
            self._update()
            #pg.display()


if __name__ == '__main__':
    Game()
