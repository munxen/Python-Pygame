import sys

import pygame

from pygame.sprite import Group
from settings__ import Settings
from ship__ import Ship
from alien__ import Alien
import game_functions__ as gf

def run_game():

    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode ((ai_settings.screen_weight,
                                     ai_settings.screen_height))
    pygame.display.set_caption('Cosmosos')

    # Создание корабля, группы пуль и группы пришельцев
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Запуск основного цикла игры
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
