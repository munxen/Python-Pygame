import sys

import pygame

from pygame.sprite import Group
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
    ship = Ship(ai_settings, screen)

    # Создание группы для хранения пуль
    bullets = Group()

    # Запуск основного цикла игры
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

run_game()
