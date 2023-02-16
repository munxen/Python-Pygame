import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, screen_width, screen_height, platform_x, platform_y):
        """Инициализирует игрока и его начальную позицию, хранит настройки игрока"""
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.platform_x = platform_x
        self.platform_y = platform_y
        self.image = pygame.Surface((30,50))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()

        #Начальная позиция игрока
        self.rect.x = platform_x + 80
        self.rect.y = platform_y - 100 

        self.change_right = 0 # Скорость вправо
        self.change_left = 0 # Скорость влево
        self.change_x = 0 # Рычаг скорости вправо/влево 
        self.change_y = 0 # Рычаг скорости вверх/вниз
        self.player_sreed_factor = 4 # Скорость игрока

        self.jumping = False # Проверка, находится ли игрок в прыжке
        self.jump_count = 6 # Коэффицент прыжка 

        self.pulling_right = False # Проверка, находится ли игрок в рывке справа
        self.pulling_left = False # Проверка, находится ли игрок в рывке справа
        self.pull_count = 0 # Коэффицент рывка

    def update(self):

        """Управление игроком"""
        self.gravity() #устанавливаем гравитацию
        self.rect.x += self.change_x #передвижение влево/вправо
        self.rect.y += self.change_y #передвижение вверх/вниз
        self.change_y = 0 #останавливаем вертикальное движение

        "Ограничение передвижения слева/справа/свехру"
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width 
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0

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
                    self.change_y -= (self.jump_count ** 2) / 2
                self.jump_count -= 0.14
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
        if self.pulling_right == True:
            self.rect.right += self.pull_count 
            self.pull_count += 0.8
            if self.pull_count > 18:
                self.pulling_right = False
                self.pull_count = 0

    def pull_left(self):
        """Рывок влево"""
        if self.pulling_left == True:
            self.rect.left -= self.pull_count 
            self.pull_count += 0.8
            if self.pull_count > 18:
                self.pulling_left = False
                self.pull_count = 0

    def stop(self):
        """Игрок стоит"""
        self.change_x = 0
        self.change_left = 0
        self.change_right = 0