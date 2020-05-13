# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 27 avr 2020
@author: anthony thillerot

This file contains all the game constant

"""

# Constant
NB_PIX_SPRITE = 32
NB_SPRITE_X = 15
NB_SPRITE_Y = NB_SPRITE_X
NB_MAX_SPRITE = NB_SPRITE_X * NB_SPRITE_Y
NB_PIXEL_X = NB_SPRITE_X * NB_PIX_SPRITE
NB_PIXEL_Y = NB_SPRITE_X * NB_PIX_SPRITE + NB_PIX_SPRITE

NB_RD_IN_BRANCH = int(NB_SPRITE_X / 15) * 50

PATH_OF_MUSIC = "ressource/bensound-betterdays.wav"
PATH_OF_MACGYVER = "ressource/MacGyver.png"
PATH_OF_WALL = "ressource/wall_picture.png"
PATH_OF_PATH = "ressource/path.png"
PATH_OF_GUARDIAN = "ressource/Gardien.png"
PATH_OF_NEEDLE = "ressource/aiguille.png"
PATH_OF_ETHER = "ressource/ether.png"
PATH_OF_PLASTIC_TUBE = "ressource/tube_plastique.png"
PATH_OF_SYRINGE = "ressource/seringue.png"

CHAR_OF_NEEDLE = 'X'
CHAR_OF_ETHER = 'E'
CHAR_OF_PLASTIC_TUBE = 'P'

CONSTANT_LOSE = 2
CONSTANT_WIN = 1
CONSTANT_CONTINUE = 0

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
BLACK = (0, 0, 0)
