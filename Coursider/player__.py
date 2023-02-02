import pygame

import platform__

class Player(pygame.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        """Инициализирует игрока и его начальную позицию, хранит настройки игрока"""
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.Surface((30,50))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width/2, screen_height/2)

        self.change_right = 0 #Скорость вправо
        self.change_left = 0 #Скорость влево
        self.change_x = 0 #Рычаг скорости вправо/влево 
        self.change_y = 0 #Рычаг скорости вверх/вниз

        self.player_sreed_factor = 2 #Скорость игрока

        self.jumping = False #Проверка, находится ли игрок в прыжке
        self.jump_count = 8 #Коэффицент прыжка 

    def update(self):
        """Управление игроком"""
        self.gravity() #устанавливаем гравитацию
        self.rect.x += self.change_x #передвижение влево/вправо
        self.rect.y += self.change_y #передвижение вверх/вниз
        self.change_y = 0 #останавливаем вертикальное движение
    
    def gravity(self):
        """Гравитация игрока"""
        if self.change_y == 0:
            self.change_y = 10
        else:
            self.change_y += .95
        """Если уже на земле, ставим позицию y как 0"""
        if self.rect.y >= self.screen_height - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = self.screen_height - self.rect.height

    def jump_on(self):
        "Прыжок вверх"
        if self.jumping == True:
            if self.jump_count >= -8:
                if self.jump_count > 0:
                    self.change_y -= (self.jump_count ** 2) / 2 
                else:
                    self.change_y += (self.jump_count ** 2) / 2
                self.jump_count -= 0.3

            else:
                self.jumping = False
                self.jump_count = 8
    
    def go_left(self):
        """Ходьба влево"""
        self.change_left = -self.player_sreed_factor
        self.change_x = self.change_left

    def go_right(self):
        """Ходьба вправо"""
        self.change_right = self.player_sreed_factor
        self.change_x = self.change_right
        
    def stop(self):
        """Игрок стоит"""
        self.change_x = 0
    
    def stop_right(self):
        "Игрок стоит при коллизии справа"
        self.change_right = 0
        self.change_x = self.change_right

    def stop_left(self):
        "Игрок стоит при коллизии слева"
        self.change_left = 0
        self.change_x = self.change_left