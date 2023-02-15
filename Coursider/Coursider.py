import sys
import pygame

from settings__ import Settings
from player__ import Player
from platform__ import Platform
import game_func__ as gf

def run_game():

    # Инициализирует pygame, settings  и объект экрана, название игры и time
    gf.inital_game()
    ai_settings = Settings()
    screen = pygame.display.set_mode ((ai_settings.screen_width,ai_settings.screen_height))
    clock = pygame.time.Clock()

    edges = False # Края

    # Создание класса Player и добавление в общую группу
    player = Player(ai_settings.screen_width, ai_settings.screen_height)
    ai_settings.player_sprites.add(player)

    # Создание класса Platform, добавление в общую группу, создание списка коллизий
    platform = Platform(ai_settings.start_platform_hight, 
    ai_settings.start_platform_weight, ai_settings.speed_factor_platform,
    ai_settings.platform_wight, ai_settings.platform_hight, edges)

    ai_settings.platform_sprites.add(platform)
    ai_settings.platform_list.append(platform)

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
                if event.key == pygame.K_a and player.change_left < 0:
                    player.stop()
                    platform.platform_go_right = False
                if event.key == pygame.K_d and player.change_right > 0:
                    player.stop()
                    platform.platform_go_left = False

        # Установка условий для каждой платформы
        for p in ai_settings.platform_list:
            # Перемещение платформ при движении игрока
            gf.pull_platform(platform.platform_go_left, p, 
            platform.platform_go_right)
            # Коллизия игрока и платформы
            gf.collizions_platform(p, player, 
            ai_settings.platform_sprites)
            
        # Создание платформ
        if p.rect.bottom > 200 and platform.create_platform == True:
            gf.create_platform(ai_settings.platform_sprites,
            ai_settings.platform_list, ai_settings.speed_factor_platform, edges)
            if len(ai_settings.platform_list) > 2:
                platform.create_platform = False

        # Отслеживание игрока
        if player.rect.right >= 0 and player.rect.right <= 400 or\
            player.rect.right >= 801 and player.rect.right <= 1200:
            edges = True
        else:
            edges = False

        # Рендеринг
        gf.rendering(ai_settings.player_sprites,ai_settings.platform_sprites,screen,
        ai_settings.bg_color,clock,ai_settings.FPS, player, )

run_game()