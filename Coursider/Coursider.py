import sys
import pygame
import time

from settings__ import Settings
from player__ import Player

def run_game():
    # Инициализирует pygame, settings  и объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode ((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Coursider")

    # Фреймрейт
    clock = pygame.time.Clock()

    # Создание группы спрайтов
    all_sprites = pygame.sprite.Group()
    
    # Создание класса Player и добавление в общую группу
    player = Player()
    all_sprites.add(player)

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
         # Обновлене спрайтов
        all_sprites.update()

        # При каждом проходе цикла перерисовывается экран
        screen.fill(ai_settings.bg_color)

        # Отрисовка спрайтов
        all_sprites.draw(screen)

        # Отображение последнего прорисованного окна
        pygame.display.flip()

run_game()