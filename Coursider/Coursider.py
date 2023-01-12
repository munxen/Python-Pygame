import sys
import pygame
import time

from settings__ import Settings
from player__ import Player
from platform__ import Platform

def run_game():

    # Инициализирует pygame, settings  и объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode ((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Coursider")
    clock = pygame.time.Clock()
    FPS = 60
    
    
    jump = False
    jumpCount = 0
    jumpMax = 15

    # Создание группы спрайтов
    all_sprites_platform = pygame.sprite.Group()
    all_sprites_player = pygame.sprite.Group()

    #Проверка, прыгнул ли Player
    jumping = False

    # Создание класса Player и добавление в общую группу
    platform = Platform()
    player = Player(ai_settings.screen_width,ai_settings.screen_height)
    all_sprites_platform.add(platform)
    all_sprites_player.add(player)

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        """Управление"""
        if event.type == pygame.KEYDOWN: #Если клавиши нажаты
            if event.key == pygame.K_LEFT:
                player.go_left()
            if event.key == pygame.K_RIGHT:
                player.go_right()
            if not jump and event.key == pygame.K_UP:
                jump = True
                jumpCount = jumpMax

        if jump:
            player.change_y += jumpCount
        if jumpCount > -jumpMax:
            jumpCount -= 1
        else:
            jump = False


        if event.type == pygame.KEYUP: #Если клавиши опущены
            if event.key == pygame.K_LEFT and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_RIGHT and player.change_x > 0:
                player.stop()

        # Проверка на столкновение с платформой
        #hits = pygame.sprite.spritecollide(player, all_sprites_platform, False)
        #for hit in hits:
            #if player.change_y > 0:
                #player.rect.bottom = platform.rect.top
            #elif player.change_y < 0:
                #player.rect.top = platform.rect.bottom
        
        # Обновлене спрайтов
        all_sprites_player.update()
        all_sprites_platform.update()

        #Ограничение передвижения
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

        #FPS
        clock.tick(FPS)

        # Отображение последнего прорисованного окна
        pygame.display.flip()

run_game()