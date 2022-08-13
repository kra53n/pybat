from config import Images
from funcs import load_image


class Player:
    def __init__(self):
        self._image = load_image(Images.player, colorkey=-1, scale=0.25)

    @property
    def image(self):
        return self._image
