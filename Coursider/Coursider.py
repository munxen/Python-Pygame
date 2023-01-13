import sys
import pygame

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
    player = Player(ai_settings.screen_width, ai_settings.screen_height)
    all_sprites_player.add(player)

    # Создание класса Platform и добавление в общую группу
    platform = Platform()
    all_sprites_platform.add(platform)

    #Рычаг столкновений
    collizions = True
    print ("Координата верх платформы " + str(platform.rect.top))
    print ("Координата низ платформы " + str(platform.rect.bottom))
    print ("Координата слева платформы " + str(platform.rect.left))
    print ("Координата справа платформы " + str(platform.rect.right))

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
                if event.key == pygame.K_a and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_d and player.change_x > 0:
                    player.stop()

        # Прыжок
        player.jump_on()
        #print("Координата right Игрока: " + str(player.rect.right))
        #print("Координата left Платформы: " + str(platform.rect.left))

        # Проверка на столкновение с платформой
        hits = pygame.sprite.spritecollide(player, all_sprites_platform, False)
        if hits:
            print("Обнаружена коллизия")
            if player.rect.right == platform.rect.left:
                print("Обнаружено столкновение right игрока и left платформы ")
                #player.rect.right = platform.rect.left


        # Обновлене спрайтов
        all_sprites_player.update()
        all_sprites_platform.update()

        # Ограничение передвижения
        if player.rect.right > ai_settings.screen_width:
            player.rect.right = ai_settings.screen_width
        if player.rect.left < 0:
            player.rect.left = 0

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