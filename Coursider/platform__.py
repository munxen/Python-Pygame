import pygame

import random

class Platform(pygame.sprite.Sprite):
    """Инициализация платформы"""
    def __init__(self, x_p, y_p):
        super().__init__()
        self.x_p = x_p #Координата x появления платформы
        self.y_p = y_p #Координата y появления платформы
        self.image = pygame.Surface((300, 70))
        self.image.fill((139, 69, 19))
        self.rect = self.image.get_rect()
        self.rect.center = (x_p, y_p)
        self.speed_factor_platform = 2
        self.platform_go_right = False #Рычаг ходьбы вправо
        self.platform_go_left = False #Рычаг ходьбы влево

    def update(self):
        "Движение платформы"
        self.rect.y += self.speed_factor_platform
        if self.rect.top > 640 :
            self.rect.center = (random.randrange(-100, 1200) , -100)
