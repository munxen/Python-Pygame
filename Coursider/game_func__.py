import pygame
import random

from platform__ import Platform


def inital_game():
    "Инициализация игры"
    pygame.init()
    pygame.display.set_caption("Coursider")

def pull_platform(platform_go_left, p, platform_go_right, jump_count):
        """Изменение расположения платформ при движении игрока"""
            # Платформа летит влево/вправо
        if platform_go_left == True:
            p.rect.left -= 1
            p.rect.right -= 1
        if platform_go_right == True:
            p.rect.left += 1
            p.rect.right += 1
            # Платформа падает/замедляется
        if jump_count < 6 and jump_count > 0:
            p.rect.y += 2
        if jump_count < 0:
            p.rect.y -= 1

def collizions_platform(p, player, platform_sprites):
    """Коллизии игрока и платформы"""
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

def create_platform(p, platform_sprites, 
platform_list, speed_factor_platform, create_platform):

    """Создание платформ"""
    if p.rect.bottom > 200 and create_platform == True:
        platform = Platform(random.randrange(-100, 1200) , -100, speed_factor_platform)
        platform_sprites.add(platform)
        platform_list.append(platform)

        if len(platform_list) > 2:
            create_platform = False
        return create_platform

    print (create_platform)