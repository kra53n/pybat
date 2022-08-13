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
