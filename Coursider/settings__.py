class Settings():
    """Класс для хранения настроек игры Coursider"""
    
    def __init__(self):
        """Инициализирует настройки игры"""
        #Параметры экрана
        self.screen_width = 1200
        self.screen_height = 640
        self.bg_color = (230,230,230)

        #Счётчик частоты кадров
        self.FPS = 30