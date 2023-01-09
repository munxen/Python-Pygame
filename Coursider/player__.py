import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        """Инициализирует игрока и его начальную позицию"""
        super().__init__()
        self.image = pygame.Surface((50,50)) #Размеры поверхности
        self.image.fill((0,0,255))
        self.player_color = (255, 100, 0) #Цвет игрока
        pygame.draw.rect(self.image, self.player_color, pygame.Rect(0, 0, 300, 200))
        self.rect = self.image.get_rect()