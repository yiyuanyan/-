import pygame


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
