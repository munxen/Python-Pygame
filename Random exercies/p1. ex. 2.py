#2. Using the functions for working with the graphics of the pygame library, draw a white flag with Olympic rings.

import pygame
import sys

from pygame.color import THECOLORS

pygame.init()

screen = pygame.display.set_mode ((800,640))
screen.fill (THECOLORS ['gray'])
#white flag
r = pygame.Rect (200, 200, 400, 200)
pygame.draw.rect (screen, (THECOLORS['white']), r, 0)

#circles
pygame.draw.circle(screen, (THECOLORS['blue']), (300,275), 40, 5)
pygame.draw.circle(screen, (THECOLORS['black']), (400,275), 40, 5)
pygame.draw.circle(screen, (THECOLORS['red']), (500,275), 40, 5)
pygame.draw.circle(screen, (THECOLORS['yellow']), (350,315), 40, 5)
pygame.draw.circle(screen, (THECOLORS['green']), (450,315), 40, 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
