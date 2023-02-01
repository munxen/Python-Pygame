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
    player = Player(ai_settings.screen_width, ai_settings.screen_height,)
    all_sprites_player.add(player)

    # Создание класса Platform и добавление в общую группу
    platform = Platform()
    all_sprites_platform.add(platform)

    #Функция по добавлению платформы
    def create_platform():
        platform = Platform()
        all_sprites_platform.add(platform)

    #Количество созданных платформ
    platforming = 1

    #Разрешение на создание платформ
    create = False

    #Рычаг столкновений
    collizions = True

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


        if platform.rect.y >= 300:
            create = True
            if platforming != 3 and create == True:
                create_platform()
                platforming += 1
                create == False


        # Прыжок
        player.jump_on()

        # Обновлене спрайтов
        all_sprites_player.update()
        all_sprites_platform.update()

        #Столкновение с платформой
        hits = pygame.sprite.spritecollide(player, all_sprites_platform, False)
        if hits:
            collizions = True
        else:
            collizions = False

        "Коллизии c платформами"
        if collizions == True:
            if player.change_right > 0:
                player.stop_right()
            if player.change_left < 0:
                player.stop_left()

        # Ограничение передвижения
        "Ограничение c экраном"
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