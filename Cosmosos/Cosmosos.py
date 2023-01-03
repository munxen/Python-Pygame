import sys

import pygame

from settings__ import Settings
from ship__ import Ship
import game_functions__ as gf

def run_game():

    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode ((ai_settings.screen_weight,
                                     ai_settings.screen_height))
    pygame.display.set_caption('Cosmosos')

    # Создание корабля
    ship = Ship(screen)

    # Запуск основного цикла игры
    while True:

        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ship)
        ship.update()
        
        # При каждом проходе цикла перерисовывается экран
        gf.update_screen(ai_settings, screen, ship)

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

run_game()
