import sys
import pygame
import random

from settings__ import Settings
from player__ import Player
from platform__ import Platform
import game_func__ as gf

def run_game():

    # Инициализирует pygame, settings, объект экрана и time
    gf.inital_game()
    ai_settings = Settings()
    screen = pygame.display.set_mode ((ai_settings.screen_width,ai_settings.screen_height))
    clock = pygame.time.Clock()

    # Создание класса Platform, добавление в общую группу, создание списка коллизий
    platform = Platform(ai_settings.start_platform_hight, ai_settings.start_platform_weight,
    ai_settings.speed_factor_platform, ai_settings.platform_wight, ai_settings.platform_hight)
    ai_settings.platform_sprites.add(platform)
    ai_settings.platform_list.append(platform)

    # Создание класса Player и добавление в общую группу
    player = Player(ai_settings.screen_width, ai_settings.screen_height, platform.rect.x, platform.rect.y)
    ai_settings.player_sprites.add(player)

    # Запуск основного цикла игры
    while True:

        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.go_left()
                    platform.platform_go_right = True
                if event.key == pygame.K_d:
                    player.go_right()
                    platform.platform_go_left = True
                if not player.jumping:
                    if event.key == pygame.K_w:
                        player.jumping = True
                if event.key == pygame.K_SPACE and platform.platform_go_right == True:
                    player.pulling_left = True
                if event.key == pygame.K_SPACE and platform.platform_go_left == True:
                    player.pulling_right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player.stop()
                if event.key == pygame.K_d:
                    player.stop()

        # Генерация платформ
        gf.platforming(ai_settings.platform_list, platform.platform_go_left,platform.platform_go_right,
        player, ai_settings.platform_sprites, platform.create_platform, ai_settings.speed_factor_platform)

        # Ограничение создания платформ
        if len(ai_settings.platform_list) > 2:
            platform.create_platform = False
        
        # Рычаги перемещения платформ
        if player.change_left == 0:
            platform.platform_go_right = False
        if player.change_right == 0:
            platform.platform_go_left = False

        # Рендеринг
        gf.rendering(ai_settings.player_sprites, ai_settings.platform_sprites, screen,
        ai_settings.bg_color,clock, ai_settings.FPS, player)

run_game()