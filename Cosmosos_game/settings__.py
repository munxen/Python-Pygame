class Settings():
    """Класс для хранения настроек игры"""
    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_weight = 1000
        self.screen_height = 600
        self.bg_color = (255, 192, 203)

        # Настройки корабля
        self.ship_speed_factor = 1.5

        # Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3