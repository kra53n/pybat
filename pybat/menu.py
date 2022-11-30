import pygame as pg

from ui.frame import Frame
from ui.button import Button
from config import Window, font, button_settings
from commands import Commands


def menu(screen):
    run = True
    clock = pg.time.Clock()
    cmds = Commands()

    frame = Frame(rect=pg.Rect(0, 0, 300, 0), padding=40)
    frame.w = 300
    options = 'play', 'settings', 'exit'
    actions = (lambda: cmds.quit(), lambda: print('settings'), lambda: print('exit'))
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

            if 'quit' in cmds:
                cmds.remove('quit')
                run = False

        if pressed:
            frame.update()

            screen.fill(Window.bg)
            frame.draw(screen)

        pg.display.flip()
        clock.tick(60)

        pressed = False
