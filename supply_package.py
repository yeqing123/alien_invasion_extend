import pygame

from random import randint
from pygame.sprite import Sprite

class SupplyPackage(Sprite):
    """创建并管理游戏中各种飞船补给包的类"""

    def __init__(self, ai_game, filepath, type):
        """初始化各类属性"""
        super().__init__()
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load(filepath)
        self.rect = self.image.get_rect()
        # 初始化补给包的位置
        self.rect.bottom = self.screen_rect.top
        # 初始化补给包的移动距离
        self.remove_distance = randint(0, self.settings.screen_width)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 设置补给包的类型
        self.type = type

    def update(self):
        """更新补给包的移动位置"""
        # 先检测是否到达屏幕两侧边缘
        self._check_edge()
        # 更新位置
        self.x += self.settings.sp_speed * self.settings.sp_direction
        self.y += self.settings.sp_speed
        self.rect.x = self.x
        self.rect.y = self.y
      
        # 更新需要移动的距离
        self.remove_distance -= self.settings.sp_speed
        #当距离缩小到小于或等于0时，重新获取一个新的值
        if self.remove_distance <= 0:
            # 随机变换移动方向
            self.settings.sp_direction *= -1
            self.remove_distance = randint(0, self.settings.screen_width)

    def _check_edge(self):
        """检查补给包是否移动到了屏幕的边缘"""
        # 当补给包触碰到屏幕两侧边缘时，改变其移动方向
        if self.rect.left <= 0 or self.rect.right >= self.screen_rect.right:
            self.settings.sp_direction *= -1

    def blitme(self):
        """在屏幕上绘制补给包图像"""
        self.screen.blit(self.image, self.rect)

        