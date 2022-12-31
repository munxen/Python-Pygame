#Using loops, using a 10x10 pixel square and its footprint, draw a 100x100 pixel frame.

import pygame
import sys
from pygame.color import THECOLORS
pygame.init()

"""Introducing a clock to limit fps"""
clock = pygame.time.Clock()

"""create rect"""
rect = pygame.Rect(10, 10, 20, 20)

screen = pygame.display.set_mode((600, 600))
screen.fill(THECOLORS['gray'])

def player():
    """object management rect"""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            rect.move_ip(-10, 0)
        elif event.key == pygame.K_RIGHT:
            rect.move_ip(10, 0)
        elif event.key == pygame.K_UP:
            rect.move_ip(0, -10)
        elif event.key == pygame.K_DOWN:
            rect.move_ip(0, 10)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    player()

    pygame.draw.rect (screen, (THECOLORS['brown']), rect, 0)
    pygame.display.flip()
    
    """We limit fps for the convenience of object management"""
    clock.tick(5)