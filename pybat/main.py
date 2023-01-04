import pygame as pg

from menu import Menu
from config import Window


if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode(Window.size)
    pg.display.set_caption(Window.title)
    screen.fill(Window.bg)
    Menu(screen)
