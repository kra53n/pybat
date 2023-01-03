import pygame as pg

from commands import Commands
from tools import get_blured_surf, get_colorize_surf


class Play:
    def __init__(self, screen: pg.Surface):
        self.screen = screen
        
        self.cmds = Commands()
        self.clock = pg.time.Clock()
        
        # blured = get_blured_surf(self.screen, 45)
        # self.bg = get_colorize_surf(blured, pg.Color(0, 0, 0), 50)
        
        self.run()
    
    def update(self):
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    self.cmds.quit()
    
    def draw(self):
        self.screen.fill(pg.Color(12, 12, 12))
        pg.display.flip()
    
    def run(self):
        while 'quit' not in self.cmds:
            self.update()
            self.draw()
            self.clock.tick(60)
        self.cmds.remove('quit')