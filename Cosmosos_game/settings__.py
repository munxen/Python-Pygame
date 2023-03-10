class Settings():
    """Класс для хранения настроек игры"""
    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана

        self.screen_weight = 1000
        self.screen_height = 600
        self.bg_color = (169, 169, 169)

        # Настройки корабля
        self.ship_limit = 3

        # Параметры пули
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #Настройки пришельцев
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 5

        #Темп ускорения игры
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5 #1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)