#ЧЕРНОВИК\


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