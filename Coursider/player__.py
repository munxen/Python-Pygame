import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        """Инициализирует игрока и его начальную позицию"""
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.Surface((30,50))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.change_x = 0 #скорость влево/вправо
        self.change_y = 0 #скорость вверх/вниз
        self.rect.center = (screen_width/2, screen_height/2)

    def update(self):
        """Управление игроком"""
        self.gravity()
        self.rect.x += self.change_x #передвижение влево/вправо
        self.rect.y += self.change_y #передвижение вверх/вниз
    
    def gravity(self):
        """Гравитация игрока"""
        if self.change_y == 0:
            self.change_y = 0.1
        else:
            self.change_y += .95
    
    def go_left(self):
        """Ходьба влево"""
        self.change_x = -1
    
    def go_right(self):
        """Ходьба вправо"""
        self.change_x = 1

    def jump(self):
        "Прыжок"
        self.change_y += -5

    def stop(self):
        """Чел стоит"""
        self.change_x = 0
    
