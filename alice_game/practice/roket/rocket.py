import pygame

class Rocket():

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始化的位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞车图像并获取其外接矩形
        self.image = pygame.image.load('alice_game/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每收新飞船放在屏幕底部中央
        self.rect.center = self.screen_rect.center

        # 在飞船的属性center中存储小数值
        self.center = self.rect.center

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center