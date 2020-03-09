#!/usr/local/bin/python3.7
import sys,os
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # __file__获取执行文件相对路径，整行为取上一级的上一级目录
#sys.path.append(BASE_DIR)

import pygame
from pygame.sprite import Group


from settings import Settings
from ship import Ship
from alien import Alien

import game_functions as gf 
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # set the bg_color
    bg_color = (230, 230, 230)
    #创建一艘飞船,一个子弹编组，一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 创建一个外星人 alien = Alien(ai_settings, screen)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens,bullets)
        #todo:
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings, screen, ship,aliens,bullets)
        # 创建外星人群
        #gf.create_fleet(ai_settings, screen, ship,aliens)

run_game()
