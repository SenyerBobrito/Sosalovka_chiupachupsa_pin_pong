from pygame import *
from random import randint
from time import time as tm

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()


        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
wight = 500
height = 500 

window = display.set_mode((wight, height))
window.fill((90, 423, 13))
FPS = 120 


start = True
while start == True:
    for e in event.get():
        if e.type == QUIT:
            start = False
    display.update()
    clock.tick(FPS)

