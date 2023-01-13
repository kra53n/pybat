import pygame as pg


class ResourceManager(dict):
    def __getitem__(self, k: str) -> pg.Surface:
        v = super().__getitem__(k)
        assert isinstance(v, pg.Surface), f'Key must give pg.Surface value, given {type(v)}'
        return v


resmngr = ResourceManager()
