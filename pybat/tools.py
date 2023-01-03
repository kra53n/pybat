from pathlib import Path

import pygame as pg


def hex2rgb(hx: str) -> tuple:
    hx = hx.lstrip('#')
    if not any(map(lambda value: value == len(hx), (3, 6))):
        raise Exception('len of hx must be 3 or 6')
    return eval(f'0x{hx}')


def file_exist(path: str):
    fullpath = Path(path)
    if not fullpath.is_file():
        fullpath = str(fullpath.absolute())
        raise Exception(f'Couldn`t load image from {fullpath}')


def load_image(path: str, colorkey=None, scale: float = 1):
    file_exist(path)

    image = pg.image.load(path)

    if scale != 1:
        size = tuple(side * scale for side in image.get_size())
        image = pg.transform.scale(image, size)

    image = image.convert()

    if colorkey:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)

    return image


def get_blured_surf(surf: pg.Surface, amt: float):
    """
    Blur the given surface by the given 'amount'.  Only values 1 and greater
    are valid.  Value 1 = no blur.
    """
    assert amt >= 1, f'Arg `amt` must be greater than 1, passed in value is {amt}'
    scale = 1. / amt
    surf_size = surf.get_size()
    scale_size = int(surf_size[0]*scale), int(surf_size[1]*scale)
    surf = pg.transform.smoothscale(surf, scale_size)
    surf = pg.transform.smoothscale(surf, surf_size)
    return surf


def get_colorize_surf(surf: pg.Surface, color: pg.Color, percents: int):
    color.a = int(percents * 255 / 100)
    colorizer = pg.Surface(surf.get_size()).convert_alpha()
    colorizer.fill(color)
    surf.blit(colorizer, (0, 0))
    return surf