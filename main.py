from pygame import *
from random import *
import sys
font.init()

window = display.set_mode((700, 500), vsync = 1)
display.set_caption("Pingpong")

game = True
finish = False

background = transform.scale(image.load("background.jpg"), (window.get_width(), window.get_height()))
img_racket = transform.scale(image.load("racket.png"), (100, 100))
img_ball = transform.scale(image.load("ball.png"), (60, 60))

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, speed = 0):
        super().__init__()
        self.image = img
        self.speed = speed
        self.rect = self.image.get_rect()
        self.pos_x = x
        self.pos_y = y
        self.rect.topleft = (x, y)

    def draw(self):
        window.blit(self.image, self.rect.topleft)


racket_right = GameSprite(img_racket, 30, 200, 0.6)
racket_left = GameSprite(img_racket, 590, 200, 0.6)
ball = GameSprite(img_ball, 350, 200, 0.6)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        racket_right.draw()
        racket_left.draw()
        ball.draw()

    display.update()