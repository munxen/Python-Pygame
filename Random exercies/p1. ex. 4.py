#4. Modify the program so that its sequence number is recorded in each cell.

import pygame
import sys

from pygame.color import THECOLORS


WINDOW_WEIGHT = 600
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WEIGHT))
screen.fill(THECOLORS['grey'])
pygame.init()


def drawGrid():
    blockSize = 100
    """Setting parameters to the text"""
    font = pygame.font.SysFont('couriernew', 40)
    text = font.render(str('HELLO'), True, THECOLORS['green'])
    """Draw rects"""
    for x in range (0, WINDOW_WEIGHT, blockSize):
        for y in range (0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, (THECOLORS['orange']), rect, 1)
            ('text', rect.centerx, rect.centery, 20)
    

while True:
    drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()