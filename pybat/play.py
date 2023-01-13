import pygame as pg

from commands import cmds
from config import Window
from player import Player
from tools import get_blured_surf, get_colorize_surf


class Play:
    def __init__(self, screen: pg.Surface):
        self.screen = screen
        
        self.clock = pg.time.Clock()
        self.captured_screen = self.screen.copy()
        self.player = Player(surface=screen, type=Player.Type.Red)
        
        self.run()
        
    def go_to_menu(self):
        cmds.quit()
        cmds.quit_from_play()
    
    def update(self):
        for ev in pg.event.get():
            if ev.type == pg.QUIT or (ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE):
                from menu import Menu
                blured = get_blured_surf(self.captured_screen, 45)
                bg = get_colorize_surf(blured, pg.Color(0, 0, 0), 50)
                self.screen.blit(bg, (0, 0))
                Menu(
                    self.screen,
                    (
                        ('continue', lambda: cmds.quit()),
                        ('settings', lambda: print('settings?')),
                        ('exit', lambda: self.go_to_menu()),
                    ),
                )
    
    def draw(self):
        self.screen.fill(pg.Color(255, 255, 255))
        self.player.draw()
        pg.display.flip()
    
    def run(self):
        while 'quit_from_play' not in cmds:
            self.update()
            self.draw()
            self.clock.tick(60)
        cmds.remove('quit_from_play')
        self.screen.fill(Window.bg)