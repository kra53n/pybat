import pygame as pg

from ui.frame import Frame
from ui.button import Button
from config import Window, font, button_settings


def menu(screen):
    run = True
    clock = pg.time.Clock()

    frame = Frame(rect=pg.Rect(0, 0, 300, 0), padding=40)
    frame.w = 300
    options = 'play', 'settings', 'exit'
    actions = (lambda: print('play'), lambda: print('settings'), lambda: print('exit'))
    for opt, act in zip(options, actions):
        frame.append(Button(font, text=opt, action=act, **button_settings))
    frame.centerize(pg.Rect(0, 0, *Window.size))

    pressed = True

    while run:
        for event in pg.event.get():
            pressed = True
            match event.type:
                case pg.QUIT:
                    run = False

        if pressed:
            frame.update()
            # frame.centerize(pg.Rect(0, 0, *Window.size))
            # for obj in objs:
            #     print(obj)
            #     obj.update()

        if pressed:
            screen.fill(Window.bg)
            frame.draw(screen)
            # for obj in objs:
            #     obj.draw(screen)

        pg.display.flip()
        clock.tick(60)

        pressed = False
