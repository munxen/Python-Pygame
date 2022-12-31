#Write a program in which a 20x20 pixel square will move by pressing the keys. 
# Take into account that the square should not go beyond the boundaries of the screen.
#Modify the program so that the square changes its color to random with each movement.

import pygame
import sys
pygame.init()
from pygame.color import THECOLORS
clock = pygame.time.Clock()
from random import randint

"""Параметры экрана"""
S_WEIGHT = 600
S_HEIGHT = 600
screen = pygame.display.set_mode((S_WEIGHT, S_HEIGHT))
def window():
    "настройки полей и игрового поля"
    screen.fill(THECOLORS['grey'])
    pygame.draw.line (screen, (THECOLORS['brown']), [0,0], [S_WEIGHT,0], 10)
    pygame.draw.line (screen, (THECOLORS['brown']), [S_WEIGHT,0], [S_WEIGHT,S_HEIGHT], 10)
    pygame.draw.line (screen, (THECOLORS['brown']), [S_WEIGHT,S_HEIGHT], [0,S_HEIGHT], 10)
    pygame.draw.line (screen, (THECOLORS['brown']), [0,S_HEIGHT], [0,0], 10)

"""Создаём квадрат и параметры управления"""
#Координаты появления объекта
x = 100
y = 100
#Размеры объекта
w = 20
h = 20
#Координаты передвижения объекта
speed = 5
#Изначальный цвет объекта
one_color=randint(0,255)
two_color=randint(0,255)
three_color=randint(0,255)

def object():
    """Параметры объекта"""
    color = (one_color,two_color,three_color)
    pygame.draw.rect (screen, (color), (x,y,w,h))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
    """Управление объектом"""
    keys = pygame.key.get_pressed()
    if keys [pygame.K_LEFT] and x > 9:
        x -= speed
        one_color=randint(0,255)
        two_color=randint(0,255)
        three_color=randint(0,255)
    if keys [pygame.K_RIGHT] and x < 576:
        x += speed
        one_color=randint(0,255)
        two_color=randint(0,255)
        three_color=randint(0,255)
    if keys [pygame.K_UP] and y > 9:
        y -= speed
        one_color=randint(0,255)
        two_color=randint(0,255)
        three_color=randint(0,255)
    if keys [pygame.K_DOWN] and y < 576:
        y += speed
        one_color=randint(0,255)
        two_color=randint(0,255)
        three_color=randint(0,255)
    window()
    object()
    pygame.display.update()
    """FPS"""
    clock.tick(60)