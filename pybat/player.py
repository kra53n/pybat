from enum import IntEnum

from config import Paths
from tools import load_image


class Player:
    class Type(IntEnum):
        Red = 0
    
    def __init__(self, type=None):
        match type:
            case _:
                self.image = load_image(Paths.images / 'bat.png', colorkey=-1, scale=0.25)

    @property
    def image(self):
        return self.image
