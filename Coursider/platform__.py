import pygame

import random

class Platform(pygame.sprite.Sprite):
    """Инициализация платформы"""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((400, 150))
        self.image.fill((139, 69, 19))
        self.rect = self.image.get_rect()
        self.rect.center = (620, 450)
        self.speed_factor_platform = 3

    def update(self):
        self.rect.y += self.speed_factor_platform
        if self.rect.top > 640 :
            self.rect.center = (random.randrange(-100, 1200) , -100)