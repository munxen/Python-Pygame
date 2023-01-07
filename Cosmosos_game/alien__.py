import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс, представляющий одного пришельца"""
    def __init__(self, ai_setttings, screen):
        """Инициализирует пришельца и его начальную позицию"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_setttings

        #Загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('C:/Users/proro/Desktop/programm/git_projects/git repositories/Python Pygame/Cosmosos/alien_ship.bmp')
        self.rect = self.image.get_rect()

        #Каждый новый пришелец появляется в верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Сохранение точной позиции пришельца
        self.x = float(self.rect.x)

    def blitme(self):
        """Выводит пришельца в текущем положении"""
        self.screen.blit(self.image, self.rect)