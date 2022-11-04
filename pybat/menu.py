import pygame as pg

from config import Window
from ui_comps import Button
from config import button_settings


def menu(screen):
    options = 'play', 'settings', 'exit'
    actions = (lambda: print('play'), lambda: print('settings'), lambda: print('exit'))

    run = True
    clock = pg.time.Clock()
    objs = []

    x = Window.size[0] // 2
    y = 0
    pad = 120
    for i, (opt, act) in enumerate(zip(options, actions)):
        btn = Button(text=opt, action=act, **button_settings)
        btn._rect.center = x, y
        y += pad
        objs.append(btn)

    pressed = True
    while run:
        for event in pg.event.get():
            pressed = True
            match event.type:
                case pg.QUIT:
                    run = False

        if pressed:
            for obj in objs:
                print(obj)
                obj.update()

        if pressed:
            screen.fill(Window.bg)
            for obj in objs:
                obj.draw(screen)

        pg.display.flip()
        clock.tick(60)

        pressed = False
