import sys

import pygame

from pygame.sprite import Group

from settings__ import Settings
from ship__ import Ship
from alien__ import Alien
from game_stats__ import GameStats
from button__ import Button
from scoreboard__ import Scoreboard

import game_functions__ as gf

def run_game():

    # Инициализирует pygame, settings и объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode ((ai_settings.screen_weight,
                                     ai_settings.screen_height))
    pygame.display.set_caption('Cosmosos')

    # Создание кнопки Play
    play_button = Button(ai_settings, screen, "Play")

    # Создание корабля, группы пуль и группы пришельцев
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Создание экземпляра для хранения игровой статистики для GameStats и ScoreBoard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Запуск основного цикла игры
    while True:

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
