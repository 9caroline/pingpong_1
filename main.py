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

class Player(GameSprite):
    def __init__(self, img, x, y, speed, k_up, k_down):
        super().__init__(img, x, y, speed)
        self.k_up = k_up
        self.k_down = k_down

    def control(self):
        keys = key.get_pressed()
        if keys[self.k_up] and self.pos_y > 0: self.pos_y -= self.speed
        if keys[self.k_down] and self.pos_y < window.get_height() - 100: self.pos_y += self.speed
        self.rect.topleft = (self.pos_x, self.pos_y)


class Ball(GameSprite):
    def __init__(self, img, x, y, speed):
        super().__init__(img, x, y, speed)
        self.k_up = k_up
        self.k_down = k_down

racket_right = Player(img_racket, 20, 200, 0.6, K_w, K_s)
racket_left = Player(img_racket, 590, 200, 0.6, K_UP, K_DOWN)
ball = GameSprite(img_ball, 350, 200, 0.6)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        racket_right.control()
        racket_left.control()

        window.blit(background, (0, 0))
        racket_right.draw()
        racket_left.draw()
        ball.draw()

    display.update()

