import pygame

import random

class Platform(pygame.sprite.Sprite):
    """Инициализация платформы"""
    def __init__(self, start_platform_hight, start_platform_weight, speed_platform):
        super().__init__()
        self.start_platform_hight = start_platform_hight # Координата x появления платформы
        self.start_platform_weight = start_platform_weight # Координата y появления платформы
        self.speed_platform = speed_platform
        self.image = pygame.Surface((350, 120))
        self.image.fill((139, 69, 19))
        self.rect = self.image.get_rect()
        self.rect.center = (start_platform_hight, start_platform_weight)

        self.platform_go_right = False # Рычаг передвижения платформ вправо
        self.platform_go_left = False # Рычаг передвижения платформ влево
        self.platform_down = False # Рычаг ускорения падения платформы
        self.create_platform = True # Рычаг создания платформы

    def update(self):
        "Движение платформы"
            #Влево/вправо
        self.rect.y += self.speed_platform
        if self.rect.top > 640 :
            self.rect.center = (random.randrange(-100, 1200) , -100)

