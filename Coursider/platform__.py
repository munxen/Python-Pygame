import pygame

class Platform(pygame.sprite.Sprite):
    """Инициализация платформы"""
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((400,150))
        self.image.fill((139, 69, 19))
        self.rect = self.image.get_rect()
        self.rect.center = (900, 600)