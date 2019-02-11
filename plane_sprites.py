import pygame
# 屏幕大小的常亮
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
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
    def __init__(self, is_alt = False):
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
