from pygame import *
from random import *
import sys
font.init()

window = display.set_mode((700, 500), vsync = 1)
display.set_caption("Pingpong")

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()