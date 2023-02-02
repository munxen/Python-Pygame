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
                    #platform.platform_go_left = True
                if event.key == pygame.K_d:
                    player.go_right()
                    #platform.platform_go_right = True
                if not player.jumping:
                    if event.key == pygame.K_w:
                        player.jumping = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.change_left < 0:
                    player.stop()
                    #platform.platform_go_left = False
                if event.key == pygame.K_d and player.change_right > 0:
                    player.stop()
                    #platform.platform_go_right = False

        "Изменение платформы"
        #Прыжки
        if player.jump_count < 8 and player.jump_count > 0:
            platform.speed_factor_platform = 8 
        if player.jump_count < 0 or player.jump_count == 8:
            platform.speed_factor_platform = 2
        #Ходьба 
        if player.change_x < 0:
            platform.platform_go_left = True
        else:
            platform.platform_go_left = False

        if player.change_x > 0:
            platform.platform_go_right = True
        else:
            platform.platform_go_right = False
        
        # Прыжок
        player.jump_on()

        # Обновлене спрайтов
        all_sprites_player.update()
        all_sprites_platform.update()

        # Столкновение с платформой
        hits = pygame.sprite.spritecollide(player, all_sprites_platform, False)
        if hits:
            collizions = True
        else:
            collizions = False

        "Коллизии c платформами"
        if collizions == True:
            #Коллизия справа
            if player.rect.right >= platform.rect.left and\
                player.rect.right <= platform.rect.left + 30:
                player.rect.right = platform.rect.left
                platform.platform_go_right = False
            #Коллизия слева
            if player.rect.left <= platform.rect.right and\
                player.rect.left >= platform.rect.right - 30 :
                player.rect.left = platform.rect.right
                platform.platform_go_left = False
            #Коллизия игрока снизу
            if player.rect.bottom >= platform.rect.top and\
                player.rect.bottom <= platform.rect.top + 50 :
                player.rect.bottom = platform.rect.top

            #Коллизия игрока снизу    
            elif player.rect.top <= platform.rect.bottom and\
                player.rect.top >= platform.rect.bottom - 50 :
                player.rect.top = platform.rect.bottom

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