#ЧЕРНОВИК\
        #Создание второй платформы
        if p.rect.bottom > 200 and platform.create_platform == True:
            platform = Platform(random.randrange(-100, 1200) , -100, ai_settings.speed_factor_platform)
            ai_settings.platform_sprites.add(platform)
            ai_settings.platform_list.append(platform)
            ai_settings.num_platforms += 1
            if ai_settings.num_platforms > 2:
                platform.create_platform = False
