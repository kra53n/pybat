import pygame as pg

from play import Play
from tools import cmds
from ui import Frame, Button
from config import Window, font, button_settings

class Menu:
    def __init__(self, screen: pg.Surface, btns = None):
        self._screen = screen

        self._run = True
        self._clock = pg.time.Clock()
        self._frame = Frame(rect=pg.Rect(0, 0, 300, 0), padding=40)
        self._pressed = True
        self.btns = btns

        if self.btns is None:
            self.btns = (
                ('play', lambda: cmds.start_playing()),
                ('settings', lambda: print('settings')),
                ('exit', lambda: cmds.quit()),
            )
        self._init_buttons()
        
        self.run()

    def _init_buttons(self):
        for opt, act in self.btns:
            self._frame.append(Button(font, text=opt, action=act, **button_settings))
        self._frame.centerize(pg.Rect(0, 0, *Window.size))

    def update(self):
        for event in pg.event.get():
            self._pressed = True
            match event.type:
                case pg.QUIT:
                    self._run = False

            if 'quit' in cmds:
                cmds.remove('quit')
                self._run = False
            if 'start_playing' in cmds:
                cmds.remove('start_playing')
                Play(self._screen)

        if self._pressed:
            self._frame.update()

    def draw(self):
        if self._pressed:
            self._frame.draw(self._screen)
            pg.display.flip()

    def run(self):
        while self._run:
            self.update()
            self.draw()
            self._clock.tick(60)
            self._pressed = False
