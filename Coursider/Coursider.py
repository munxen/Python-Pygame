import sys
import pygame
import random

from settings__ import Settings
from player__ import Player
from platform__ import Platform

def run_game():

    # Инициализирует pygame, settings  и объект экрана, название игры и time
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode ((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Coursider")
    clock = pygame.time.Clock()

    # Создание групп спрайтов
    all_sprites_platform = pygame.sprite.Group()
    all_sprites_player = pygame.sprite.Group()

    # Создание класса Player и добавление в общую группу
    player = Player(ai_settings.screen_width, ai_settings.screen_height,)
    all_sprites_player.add(player)

    # Создание класса Platform, списка с коллизиями для каждой платформы и добавление в общую группу
    platform_list = []
    platform = Platform(random.randrange(-100, 1200) , -100)
    all_sprites_platform.add(platform)
    platform_list.append(platform)

    create = True #Рычаг создания новой платформы
    platforms = 1 #Количество созданных платформ

    # Запуск основного цикла игры
    while True:

        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.go_left()
                if event.key == pygame.K_d:
                    player.go_right()
                if not player.jumping:
                    if event.key == pygame.K_w:
                        player.jumping = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.change_left < 0:
                    player.stop()
                if event.key == pygame.K_d and player.change_right > 0:
                    player.stop()
        # Прыжок
        player.jump_on()

        for p in platform_list:
            """Коллизии"""
            if pygame.sprite.spritecollide(player, all_sprites_platform, False):
                #Коллизия справа
                if player.rect.right >= p.rect.left and\
                    player.rect.right <= p.rect.left + 10:
                    player.rect.right = p.rect.left

                #Коллизия слева
                if player.rect.left <= p.rect.right and\
                    player.rect.left >= p.rect.right - 10 :
                    player.rect.left = p.rect.right

                #Коллизия игрока снизу
                if player.rect.bottom >= platform.rect.top and\
                    player.rect.bottom <= platform.rect.top + 50 :
                    player.rect.bottom = p.rect.top

                #Коллизия игрока сверху   
                elif player.rect.top <= p.rect.bottom and\
                    player.rect.top >= p.rect.bottom - 50:
                    player.rect.top = p.rect.bottom

        #Создание второй платформы
        if p.rect.bottom > 200 and create == True:
            platform = Platform(random.randrange(-100, 1200) , -100)
            all_sprites_platform.add(platform)
            platform_list.append(platform)
            platforms += 1
            if platforms > 2:
                create = False


        # Обновлене спрайтов
        all_sprites_player.update()
        all_sprites_platform.update()

        # Ограничение передвижения
        "Ограничение c экраном"
        if player.rect.right > ai_settings.screen_width / 4 * 3:
            player.rect.right = ai_settings.screen_width / 4 * 3
        if player.rect.left < ai_settings.screen_width / 4:
            player.rect.left = ai_settings.screen_width / 4

        """Рендеринг"""
        # При каждом проходе цикла перерисовывается экран
        screen.fill(ai_settings.bg_color)

        # Отрисовка спрайтов
        all_sprites_platform.draw(screen)
        all_sprites_player.draw(screen)

        # FPS
        clock.tick(ai_settings.FPS)

        # Отображение последнего прорисованного окна
        pygame.display.flip()

run_game()