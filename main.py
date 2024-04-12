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
    def __init__(self, img, x, y, speed_x, speed_y):
        super().__init__(img, x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y

    
    def control_ball(self):
        global finish
        if finish == 1:
            self.pos_x += self.speed_x
            self.pos_y += self.speed_y
            self.rect.x = self.pos_x
            self.rect.y = self.pos_y
            if self.pos_x >= window.get_width() - 60:
                finish = 3

            elif self.pos_x <= 0:
                finish = 2

            elif self.pos_y >= window.get_height() - 60 or self.pos_y <= 0:
                self.speed_y *= -1

            elif sprite.collide_rect(racket_left, ball):
                self.speed_x *= -1

            elif sprite.collide_rect(racket_right, ball):
                self.speed_x *= -1
            
            else:
                pass




def new_game():
    global finish
    finish = 1
    ball.pos_x = 310
    ball.pos_y = 75
    racket_left.pos_x = 65
    racket_left.pos_y = 200
    racket_right.pos_x = 625
    racket_right.pos_y = 200




racket_left = Player(img_racket, 65, 200, 0.6, K_w, K_s)
racket_right = Player(img_racket, 625, 200, 0.6, K_UP, K_DOWN)
ball = Ball(img_ball, 310, 75, 0.3, 0.3)


font1 = font.SysFont("Arial", 25)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish == 1:
        racket_left.control()
        racket_right.control()
        ball.control_ball()

        window.blit(background, (0, 0))
        racket_left.draw()
        racket_right.draw()
        ball.draw()



    elif finish == 2:
        window.blit(background, (0, 0))
        label1 = font1.render(f"Победа правого участника. Поздравляем!", True, "#0300b8")
        window.blit(label1, (20, 100))
        label2 = font1.render(f"Для перезапуска игры нажмите пробел.", True, "#0300b8")
        window.blit(label2, (25, 250))
        keys = key.get_pressed()
        if keys[K_SPACE]:
            new_game()

    elif finish == 3:
        window.blit(background, (0, 0))
        label1 = font1.render(f"Победа левого участника. Поздравляем!", True, "#0300b8")
        window.blit(label1, (20, 100))
        label2 = font1.render(f"Для перезапуска игры нажмите пробел.", True, "#0300b8")
        window.blit(label2, (25, 250))
        keys = key.get_pressed()
        if keys[K_SPACE]:
            new_game()
    else:
        pass

    display.update()

