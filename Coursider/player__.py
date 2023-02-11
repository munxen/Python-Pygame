import pygame

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
        self.player_sreed_factor = 4 #Скорость игрока

        self.jumping = False #Проверка, находится ли игрок в прыжке
        self.jump_count = 6 #Коэффицент прыжка 


    def update(self):

        """Управление игроком"""
        self.gravity() #устанавливаем гравитацию
        self.rect.x += self.change_x #передвижение влево/вправо
        self.rect.y += self.change_y #передвижение вверх/вниз
        self.change_y = 0 #останавливаем вертикальное движение

        "Ограничение передвижения слева/справа"
        if self.rect.right > self.screen_width / 4 * 3:
            self.rect.right = self.screen_width / 4 * 3 
        if self.rect.left < self.screen_width / 4:
            self.rect.left = self.screen_width / 4

    def gravity(self):
        """Гравитация игрока"""
        if self.change_y == 0:
            self.change_y = 6
        else:
            self.change_y += .95
        """Если уже на земле, ставим позицию y как 0"""
        if self.rect.y >= self.screen_height - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = self.screen_height - self.rect.height

    def jump_on(self):
        "Прыжок"
        if self.jumping == True:
            if self.jump_count >= -6:
                if self.jump_count > 0:
                    self.change_y -= (self.jump_count ** 2) / 2 + 3
                self.jump_count -= 0.2
                if self.jump_count < -6:
                    self.jump_count = 6
                    self.jumping = False

    def go_left(self):
        """Ходьба влево"""
        self.change_left = -self.player_sreed_factor
        self.change_x = self.change_left

    def go_right(self):
        """Ходьба вправо"""
        self.change_right = self.player_sreed_factor
        self.change_x = self.change_right
    
    def pull_right(self):
        """Рывок вправо"""
        self.rect.x += 120

    def pull_left(self):
        """Рывок влево"""
        self.rect.x -= 120

    def stop(self):
        """Игрок стоит"""
        self.change_x = 0
        self.change_left = 0
        self.change_right = 0