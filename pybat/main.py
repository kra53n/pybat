import pygame as pg

from menu import Menu
from tools import resmngr, load_image
from config import Window, Paths


def load_all_bats():
    scale = 6
    names = 'default_bat', 'red_bat'
    for name in names:
        resmngr[name] = load_image(Paths.images / (name + '.png'), scale)


def load_all_blocks():
    pass


def load_all_resources():
    load_all_bats()
    load_all_blocks()


if __name__ == '__main__':
    pg.init()
    load_all_resources()
    screen = pg.display.set_mode(Window.size)
    pg.display.set_caption(Window.title)
    screen.fill(Window.bg)
    Menu(screen)
