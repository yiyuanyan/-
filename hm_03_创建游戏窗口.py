import pygame
# 引入类
from plane_sprites import *

pygame.init()
# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图片
# 1:加载图像数据
bg = pygame.image.load("./images/background.png")
# 2：blit方法绘制图像
screen.blit(bg, (0, 0))
# 3：update方法更新屏幕显示

# 绘制英雄飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))
# 创建时钟管理对象
clock = pygame.time.Clock()
# 1。定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)
# pygame框架创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)

pygame.display.update()
while True:
    clock.tick(60)
    # 捕获键盘事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        # 循环输入事件，如果有关闭按钮则退出游戏
        for event in event_list:
            if event.type == pygame.QUIT:
                print("退出游戏")
                pygame.quit()
                exit()
        print(event_list)

    # 2. 修改飞机的位置
    hero_rect.y -= 1

    # 判断飞机Y的值是否<=0
    if hero_rect.y + hero_rect.height <= 0:
        hero_rect.y = 700
    # 3. 调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    # 让精灵组调用方法

    # update方法,让组中的所有精灵更新位置
    enemy_group.update()
    # draw,将屏幕对象传递过去
    enemy_group.draw(screen)
    # 4.调用update方法更新显示
    pygame.display.update()
    pass

pygame.quit()
