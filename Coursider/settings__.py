import random

import pygame

class Settings():
    """Класс для хранения настроек игры Coursider"""
    
    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 640
        self.bg_color = (230,230,230)

        # Счётчик частоты кадров
        self.FPS = 60

        # Скорость движения платформ
        self.speed_factor_platform = 2

        # Координаты появления платформ
        self.start_platform_hight = random.randrange(-100, 1200)
        self.start_platform_weight = -100

        # Количество создаваемых платформ
        self.create_platform = True

        # Список с платформами
        self.platform_list = []

        # Группа спрайтов с платформами
        self.platform_sprites = pygame.sprite.Group()

        # Группа спрайтов с игроком
        self.player_sprites = pygame.sprite.Group()
