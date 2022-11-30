import pygame as pg

from ui.frame import Frame
from ui.button import Button
from config import Window, font, button_settings
from commands import Commands


class Menu:
    def __init__(self, screen: pg.Surface):
        self._screen = screen

        self._run = True
        self._clock = pg.time.Clock()
        self._cmds = Commands()
        self._frame = None
        self._pressed = True

        self._init_buttons()

    def _init_buttons(self):
        self._frame = Frame(rect=pg.Rect(0, 0, 300, 0), padding=40)
        options = 'play', 'settings', 'exit'
        actions = lambda: self._cmds.quit(), lambda: print('settings'), lambda: print('exit')
        for opt, act in zip(options, actions):
            self._frame.append(Button(font, text=opt, action=act, **button_settings))
        self._frame.centerize(pg.Rect(0, 0, *Window.size))

    def update(self):
        for event in pg.event.get():
            self._pressed = True
            match event.type:
                case pg.QUIT:
                    self._run = False

            if 'quit' in self._cmds:
                self._cmds.remove('quit')
                self._run = False

        if self._pressed:
            self._frame.update()

    def draw(self):
        if self._pressed:
            self._screen.fill(Window.bg)
            self._frame.draw(self._screen)
            pg.display.flip()

    def run(self):
        while self._run:
            self.update()
            self.draw()
            self._clock.tick(60)
            self._pressed = False
