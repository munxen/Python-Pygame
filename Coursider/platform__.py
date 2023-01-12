import pygame

class Platform(pygame.sprite.Sprite):
    """Инициализация платформы"""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((600,100))
        self.image.fill((139, 69, 19))
        self.rect = self.image.get_rect()
        self.rect.center = (600, 500)