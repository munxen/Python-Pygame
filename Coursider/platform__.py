import pygame

class Platform():
    """Инициализация платформы"""
    def __init__(self,screen_width):
        self.screen_width = screen_width
        self.surf = pygame.Surface((screen_width,20))
        self.surf.fill((255,0,0))