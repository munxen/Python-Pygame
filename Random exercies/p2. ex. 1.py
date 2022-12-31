#Write a program that will write the names of the keys pressed to the console. 
# Implement support for enter, space, w, a, s, d, esc.

import sys
import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))

def keydowns():
    """Обработка клавиш"""
    if keys[pygame.K_RETURN]:
        print ("Нажата клавиша enter")
    if keys[pygame.K_SPACE]:
        print ("Нажата клавиша space")
    if keys[pygame.K_w]:
        print ("Нажата клавиша w")
    if keys[pygame.K_a]:
        print ("Нажата клавиша a")
    if keys[pygame.K_s]:
        print ("Нажата клавиша s")
    if keys[pygame.K_d]:
        print ("Нажата клавиша d")
    if keys[pygame.K_ESCAPE]:
        print ("Нажата клавиша esc")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        """Key Processing"""
        keys = pygame.key.get_pressed()
        keydowns()