from pygame import *
from random import *
import sys
font.init()

window = display.set_mode((700, 500), vsync = 1)
display.set_caption("Pingpong")

game = True
finish = 1

background = transform.scale(image.load("background.jpg"), (window.get_width(), window.get_height()))
img_racket = transform.scale(image.load("racket.png"), (20, 100))
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

    
    def control_ball(self):
        self.pos_x += self.speed
        self.pos_y += self.speed



        #self.pos_y += self.speed
        #if self.pos_y > window.get_height():
            #self.pos_y = randint(-220, -80)
            #self.pos_x = randint(0, window.get_width() - 100)
        #self.rect.topleft = (self.pos_x, self.pos_y)
        pass
        

racket_right = Player(img_racket, 20, 200, 0.6, K_w, K_s)
racket_left = Player(img_racket, 660, 200, 0.6, K_UP, K_DOWN)
ball = Ball(img_ball, 310, 200, 0.3)


font1 = font.SysFont("Arial", 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish == 1:
        racket_right.control()
        racket_left.control()
        ball.control_ball()

        window.blit(background, (0, 0))
        racket_right.draw()
        racket_left.draw()
        ball.draw()



    elif finish == 2:
        label1 = font1.render(f"Победа правого участника. Поздравляем!", True, "#ea94ff")
        window.blit(label1, (125, 320))
        label2 = font1.render(f"Для перезапуска игры нажмите пробел.", True, "#ea94ff")
        window.blit(label2, (125, 400))

    elif finish == 3:
        label1 = font1.render(f"Победа левого участника. Поздравляем!", True, "#ea94ff")
        window.blit(label1, (125, 320))
        label2 = font1.render(f"Для перезапуска игры нажмите пробел.", True, "#ea94ff")
        window.blit(label2, (125, 400))

    display.update()

