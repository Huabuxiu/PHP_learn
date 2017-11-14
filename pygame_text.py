import pygame

import sys


class Settings:
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        #屏幕的设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5

def check_events():
        #监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
           print(event.key)

def run_game(): #初始化
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    while True:
        check_events()

run_game()