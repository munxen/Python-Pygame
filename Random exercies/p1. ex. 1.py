#Using the functions for working with the graphics of the pygame library, draw a house with a square base and 
# triangular roof.

import pygame
import sys
from pygame.color import THECOLORS
pygame.init()
screen = pygame.display.set_mode((800,640))
screen.fill(THECOLORS['gray'])

"""Rect(left, top, width, height)
rect(Surface, color, Rect, width=0)"""
r = pygame.Rect (350,400,100,100)
pygame.draw.rect (screen, (THECOLORS['brown']), r, 0)
r = pygame.Rect (390,460,20,40)
pygame.draw.rect (screen, (THECOLORS['black']), r , 0)
"""pygame.draw.line(Surface, color, start_pos, end_pos, width=1)"""
pygame.draw.line (screen, (THECOLORS['brown']), [340,400], [400,300], 20)
pygame.draw.line (screen, (THECOLORS['brown']), [400,300], [459,400], 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()