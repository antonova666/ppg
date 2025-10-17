#крипер сдох

from pygame import *
from time import sleep
init()
window = display.set_mode((500, 500))
window.fill((255,255,255))



class GameSprite(sprite.Sprite):
    def __init__(self, name, speed, x, y, w = 65, h = 65):
        super().__init__()
        self.image = transform.scale(image.load(name), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        if keys_pressed[K_KP8] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_KP2] and self.rect.y < 450:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, name, speed, x, y, w = 65, h = 65):
        super().__init__(name, speed, x, y, w, h)
        self.end1xy = 450 #низ, правый бок
        self.end2xy = 5 #верх, левый бок
        self.speedx = self.speed
        self.speedy = self.speed
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x >= self.end1xy:
            self.speedx *= -1
        if self.rect.y >= self.end1xy:
            self.speedy *= -1
        if self.rect.x <= self.end2xy:
            self.speedx *= -1
        if self.rect.y <= self.end2xy:
            self.speedy *= -1
        


    #должен отскакивать от мечей и взрываться
    #collide_rect использовать
    #считаем тики, после использования обнуляем
    

p1 = Player1('меч1.png', 3, 30, 225)
p2 = Player2('меч1.png', 3, 400, 225)
c = Enemy('крипер.png', 5, 225, 225)
game = True
clock = time.Clock()
while game:
    display.update()
    clock.tick(60)
    window.fill((255,255,255))

    keys_pressed = key.get_pressed()
    

    p1.reset()
    p2.reset()
    p1.update()
    p2.update()
    c.reset()
    c.update()
    
    if sprite.collide_rect(c, p1):
       c.speedx *= -1 
    if sprite.collide_rect(c, p2):
       c.speedx *= -1 
    
    for e in event.get():
        if e.type == QUIT:
            game = False


