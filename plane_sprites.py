import pygame
import random
# 屏幕大小的常亮
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常亮
CREATE_ENEMY_EVENT = pygame.USEREVENT


# 创建类，继承pygame.sprite.Sprite类
# 必须调用父类初始化方法__init__
class GameSprite(pygame.sprite.Sprite):
    """ 飞机大战游戏精灵 """

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()
        # 定义对象属性
        self.image = pygame.image.load(image_name)  # 图片
        self.rect = self.image.get_rect()  # 图片大小
        self.speed = speed  # 移动速度

    def update(self):
        """在屏幕垂直方向移动"""
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 1.调用父类方法实现精灵的创建
        super().__init__("./images/background.png")

        if is_alt:
            self.rect.y = -self.rect.height
        # 2.判断is_alt是否是交替图像，如果真，需要设置初始位置

    def update(self):
        """重写父类的update()方法"""
        # 1.调用父类的方法实现
        super().update()
        # 2.判断是否移出屏幕，如果移出，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
        pass


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1.调用父类方法，创建敌机精灵， 同时指定敌机图片
        super().__init__("./images/enemy1.png")
        # 2.指定敌机的初始随机速度
        self.speed = random.randint(1, 3)
        # 3.指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 1.调用父类方法，保持垂直方向的飞行
        super().update()
        # 2.判断是否飞出屏幕，如果是，则需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            # kill方法可以将精灵从精灵组中移除，精灵就会自动被销毁。
            self.kill()
            # print("飞出屏幕，需要从精灵组删除.....")

    def __del__(self):
        # print("敌机挂了 %s" % self.rect)
        pass


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 1.调用父类方法，设置image&speed
        super().__init__("./images/me1.png", 0)
        # 2.设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

    def update(self):
        # 英雄在水平方向移动
        self.rect.x += self.speed
        # 控制英雄不能离开屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right