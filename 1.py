#крипер сдох

from pygame import *
from time import sleep
from random import randint
import time as tm
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
        self.rc = randint(15, 20)
        self.startt = tm.time()
        self.plb = 20
    def update(self):
        if self.plb == 20:
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.y >= self.end1xy:
                self.speedy *= -1
            if self.rect.y <= self.end2xy:
                self.speedy *= -1
    def boom(self):
        self.rc = randint(15, 20)
        self.startt = tm.time()
    def check(self):
        if tm.time()-self.startt >= self.rc:
            self.plb = 1
            self.boom()
    def reset(self):
        if self.plb == 20:
            super().reset()
        else:
            window.blit(transform.scale(image.load('взрыв.png'), (self.plb*10, self.plb*10)), (self.rect.x-self.plb*5, self.rect.y-self.plb*5))
            self.plb += 1
            if self.plb == 20:
                self.nagibator()
    def nagibator(self):
        self.startt = tm.time()
        self.rect.x = 250
        self.rect.y = 250

    #должен отскакивать от мечей и взрываться
    #collide_rect использовать
    #считаем тики, после использования обнуляем
    #создать св-во с нач. временем, функция для проверки, превосходит ли время жизни self.rc, если превосходит, то запускается функция boom
count1 = 0
count2 = 0
p1 = Player1('меч1.png', 3, 30, 225)
p2 = Player2('меч1.png', 3, 400, 225)
c = Enemy('крипер.png', 3, 225, 225)

font = font.Font(None, 30)
c1text = font.render('Счёт слева: '+str(count1), True, (76,81,74))
c2text = font.render('Счёт справа: '+str(count2), True, (76,81,74))
game = True
clock = time.Clock()
while game:
    display.update()
    clock.tick(60)
    window.fill((255,255,255))
    window.blit(c1text, (10, 20))
    window.blit(c2text, (330, 20))
    keys_pressed = key.get_pressed()
    

    p1.reset()
    p2.reset()
    p1.update()
    p2.update()
    c.reset()
    c.update()
    c.check()
    
    if sprite.collide_rect(c, p1):
       c.speedx *= -1 
       c.rect.x += c.speed
    if sprite.collide_rect(c, p2):
       c.speedx *= -1 
       c.rect.x -= c.speed

    if c.rect.x >= 500:
        count1 += 1
        c1text = font.render('Счёт слева: '+str(count1), True, (76,81,74))
        c.nagibator()
    
    if c.rect.x <= 0:
        count2 +=1
        c2text = font.render('Счёт справа: '+str(count2), True, (76,81,74))
        c.nagibator()


    for e in event.get():
        if e.type == QUIT:
            game = False

