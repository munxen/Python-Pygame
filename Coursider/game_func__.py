import pygame
import random

from platform__ import Platform


def inital_game():
    "Инициализация игры"
    pygame.init()
    pygame.display.set_caption("Coursider")

def pull_platform(platform_go_left, p, platform_go_right):
        """Изменение расположения платформ при движении игрока"""
            # Платформа летит влево/вправо
        if platform_go_left == True:
            p.rect.left -= 1
            p.rect.right -= 1
        if platform_go_right == True:
            p.rect.left += 1
            p.rect.right += 1

def collizions_platform(p, player, platform_sprites,):
    """Коллизии игрока и платформ"""
    if pygame.sprite.spritecollide(player, platform_sprites, False):

        #Коллизия справа
        if player.rect.right >= p.rect.left and\
            player.rect.right <= p.rect.left + 10:
            player.rect.right = p.rect.left

        #Коллизия слева
        if player.rect.left <= p.rect.right and\
            player.rect.left >= p.rect.right - 10 :
            player.rect.left = p.rect.right

        #Коллизия игрока снизу
        if player.rect.bottom >= p.rect.top and\
            player.rect.bottom <= p.rect.top + 10:
            player.rect.bottom = p.rect.top

        #Коллизия игрока сверху   
        elif player.rect.top <= p.rect.bottom and\
            player.rect.top >= p.rect.bottom - 20:
            player.rect.top = p.rect.bottom

def create_platform(platform_sprites, platform_list, 
speed_factor_platform):
    """Создание платформ"""
    platform = Platform(random.randrange(400, 800) , -100, speed_factor_platform, 
    random.randrange(150, 400), 80)
    platform_sprites.add(platform)
    platform_list.append(platform)

def rendering(player_sprites,platform_sprites,screen,
        bg_color,clock,FPS, player ):

    # Рычаги рывков
    player.pull_right()
    player.pull_left()

    # Рычаг прыжка
    player.jump_on()

    # Обновлене спрайтов
    player_sprites.update()
    platform_sprites.update()

    # При каждом проходе цикла перерисовывается экран
    screen.fill(bg_color)

    # Отрисовка спрайтов
    platform_sprites.draw(screen)
    player_sprites.draw(screen)

    # Установка ограничения кадров
    clock.tick(FPS)

    # Отображение последнего прорисованного окна
    pygame.display.flip()

 # Установка условий для каждой платформы

def platforming(platform_list, platform_go_left, 
    platform_go_right, player, platform_sprites,
    creating_platform, speed_factor_platform,):

    """Установка условий для каждой платформы, генерация"""
    for p in platform_list:
        # Перемещение платформ при движении игрока
        pull_platform(platform_go_left, p, platform_go_right)
        # Коллизия игрока и платформы
        collizions_platform(p, player, platform_sprites)

        # Создание платформ
    if p.rect.bottom > 200 and creating_platform == True:
        create_platform(platform_sprites, platform_list, speed_factor_platform)

        # Ограничение создания платформ 
    if len(platform_list) > 2:
        creating_platform = False

