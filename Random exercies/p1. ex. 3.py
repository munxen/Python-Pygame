#Develop a program that splits the main game window into cells of a given size.

import pygame
import sys

from pygame.color import THECOLORS

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
screen = pygame.display.set_mode ((WINDOW_HEIGHT, WINDOW_WIDTH))
screen.fill (THECOLORS['gray'])
pygame.init()

def drawGrid():
    """draw rects"""
    blockSize = 20 #create size firs block
    for x in range (0, WINDOW_WIDTH, blockSize):
        for y in range (0, WINDOW_HEIGHT, blockSize):
            """Rect(left, top, width, height)"""
            rect = pygame.Rect (x, y, blockSize, blockSize)
            pygame.draw.rect(screen, (THECOLORS['orange']), rect, 1)

while True:
    drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
