import pygame

import random

class Platform(pygame.sprite.Sprite):
    """Инициализация платформы"""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((500, 150))
        self.image.fill((139, 69, 19))
        self.rect = self.image.get_rect()
        self.rect.center = (620, 600)
        self.speed_factor_platform = 4
        self.platform_go_right = False #Рычаг ходьбы вправо
        self.platform_go_left = False #Рычаг ходьбы влево
    def update(self):
        self.rect.y += self.speed_factor_platform
        if self.rect.top > 640 :
            self.rect.center = (random.randrange(-100, 1200) , -100)
        if self.platform_go_right == True:
            self.rect.right -= 2
            self.rect.left -= 2
        if self.platform_go_left == True:
            self.rect.right += 2
            self.rect.left += 2