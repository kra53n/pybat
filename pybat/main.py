import pyxel as px

from config import Window


class App:
    def __init__(self):
        px.init(Window.w, Window.h, title=Window.title)
        px.run(self._update, self._draw)

    def _update(self):
        pass

    def _draw(self):
        pass


if __name__ == '__main__':
    App()
