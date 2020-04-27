# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 27 avr 2020
@author: anthony thillerot
"""
import pygame
# from pygame.locals import *


def main():
    """
    test
    """
    continuer = 1

    pygame.init()

    clock = pygame.time.Clock()

    fenetre = pygame.display.set_mode((640, 480))

    fond = pygame.image.load("ressource/MacGyver.png").convert_alpha()

    position_perso = fond.get_rect()

    fenetre.blit(fond, (0, 10))

    pygame.display.flip()

    # Boucle infinie
    while continuer == 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(event)
                continuer = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.constants.K_SPACE:
                    print("test")
                if event.key == pygame.constants.K_DOWN:
                    position_perso = position_perso.move(0, 3)
                if event.key == pygame.constants.K_UP:
                    position_perso = position_perso.move(0, -3)
                if event.key == pygame.constants.K_LEFT:
                    position_perso = position_perso.move(-3, 0)
                if event.key == pygame.constants.K_RIGHT:
                    position_perso = position_perso.move(3, 0)
            fenetre.fill((0, 0, 0))
            fenetre.blit(fond, position_perso)
            pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
