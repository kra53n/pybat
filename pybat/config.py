from dataclasses import dataclass

from funcs import hex2rgb


@dataclass
class Window:
    size = (1280, 720)
    title = 'PyBat'
    bg = hex2rgb('#504945')


@dataclass
class Images:
    player = 'assets/bat.png'
