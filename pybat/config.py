from dataclasses import dataclass

import pygame as pg

from tools import hex2rgb


@dataclass
class Window:
    size = (1280, 720)
    title = 'PyBat'
    bg = hex2rgb('#504945')


@dataclass
class Images:
    player = 'assets/images/bat.png'


pg.font.init()


font = pg.font.Font("assets/fonts/MainFont.ttf", 50)
button_settings = {'rect': pg.Rect(120, 120, 240, 60),
                   'border_radius': 12,
                   'active_col': pg.Color('0xbb9af7'),
                   'non_active_col': pg.Color('0x1a1b26')}
