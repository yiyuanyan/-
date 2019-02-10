import pygame
from plane_sprites import *


class PlaneGame(object):
    """飞机大战游戏"""

    def __init__(self):

        print("游戏初始化")
        # 1.创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.创建私有方法，精灵和精灵组的创建
        self.__create_sprites()

    def __create_sprites(self):
        """私有方法，创建游戏窗口"""
        pass

    def start_game(self):
        print("游戏开始")
        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵组
            self.__update_sprites()
            # 5.更新显示
            pygame.display.update()

    def __event_handler(self):
        """事件监听"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
        pass
    def __check_collide(self):
        """碰撞检测"""
        pass
    def __update_sprites(self):
        """更新/绘制精灵组"""
        pass

    @staticmethod
    def __game_over():
        """静态方法，退出游戏"""
        print("游戏结束")
        pygame.quit()
        exit()

if __name__ == '__main__':
    pygame.init()
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()