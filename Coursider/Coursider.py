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

    # Фреймрейт
    clock = pygame.time.Clock()

    # Создание группы спрайтов
    all_sprites = pygame.sprite.Group()
    
    # Создание класса Player и добавление в общую группу
    platform = Platform()
    player = Player(ai_settings.screen_width,ai_settings.screen_height)
    all_sprites.add(player)
    all_sprites.add(platform)

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
            if event.key == pygame.K_UP:
                player.jump()

        if event.type == pygame.KEYUP: #Если клавиши опущены
            if event.key == pygame.K_LEFT and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_RIGHT and player.change_x > 0:
                player.stop()


        #Проверка на столкновение с платформой
        hits = pygame.sprite.spritecollide(player, all_sprites, False)
        for hit in hits:
            if player.change_y > 0:
                player.rect.bottom = platform.rect.top
            elif player.change_y <0:
                player.rect.top = platform.rect.bottom
            #player.change_y = 0 #Останавливаем вертикальное движение

                
        # Обновлене спрайтов
        all_sprites.update()

        #Ограничение передвижения
        if player.rect.right > ai_settings.screen_width:
            player.rect.right = ai_settings.screen_width
        if player.rect.left < 0:
            player.rect.left = 0

        """Рендеринг"""
        # При каждом проходе цикла перерисовывается экран
        screen.fill(ai_settings.bg_color)

        # Отрисовка спрайтов
        all_sprites.draw(screen)

        # Отображение последнего прорисованного окна
        pygame.display.flip()

run_game()