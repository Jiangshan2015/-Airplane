# __author song
# creat Time 2019-04-22

import random
import pygame
# from plane_main import*

SCREEN_RECT = pygame.Rect(0,0,480,700)
FRAME_PER_SEC = 60
#创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT

HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprites(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        super().__init__()

        #定义对象的属性

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        #在屏幕垂直方向移动
        self.rect.y += self.speed

class Background(GameSprites):

    def __init__(self,is_alt = False):

        super().__init__("./imgae/background.png")

        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        super().update()


        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprites):
    """敌机精灵"""
    def __init__(self):
        super().__init__("./imgae/enemy0.png")
        self.speed = random.randint(1,3)
        # self.rect.size = ()
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)



    def update(self):
        super().update()

        if self.rect.y >=SCREEN_RECT.height:
            # print("飞出屏幕")
            self.kill()

    def __del__(self):
        # print("敌机。。%s"%(self.rect))
        pass

class Hero(GameSprites):
    """英雄精灵"""
    def __init__(self):
        super().__init__("./imgae/hero1.png",0)

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom-120

        self.bullets = pygame.sprite.Group()


    def update(self):
        # super().update()
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x + self.rect.width > SCREEN_RECT.right:
            self.rect.x = SCREEN_RECT.right - self.rect.width



    def fire(self):
        # print("发射子弹")
        for i in (0,1,2):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y -i * 20

            bullet.rect.centerx = self.rect.centerx

            self.bullets.add(bullet)




class Bullet(GameSprites):
    def __init__(self):
        super().__init__("./imgae/bullet1.png",-2)
        pass

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
        pass

    def __del__(self):
        pass

