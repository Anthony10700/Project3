# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 27 avr 2020
@author: anthony thillerot
"""
import json
import pygame as py
import classes
# import random
# import math


# from pygame.locals import *

# Constant
PATH_OF_MUSIC = "ressource/bensound-betterdays.wav"
PATH_OF_MACGYVER = "ressource/MacGyver.png"
PATH_OF_WALL = "ressource/wall_picture.png"
PATH_OF_PATH = "ressource/path.png"
PATH_OF_GUARDIAN = "ressource/Gardien.png"

# Variable


def show_map(iwindows, mymap):
    """
    Show map , map represent list of sprites with contain elements
    M = Macggyver , W = Wall , G = Guardian , N = Nothink or path
    """
    sprites = 0
    picture_guardian = py.image.load(PATH_OF_GUARDIAN).convert_alpha()
    picture_macgyver = py.image.load(PATH_OF_MACGYVER).convert_alpha()
    picture_wall = py.image.load(PATH_OF_WALL).convert_alpha()
    picture_path = py.image.load(PATH_OF_PATH).convert_alpha()

    for itm in mymap:
        if itm == "M":  # picture_MacGyver
            iwindows.blit(picture_macgyver, (sprites % 15*32, int(sprites/15)*32))
        elif itm == "W":  # picture_wall
            iwindows.blit(picture_wall, (sprites % 15*32, int(sprites/15)*32))
        elif itm == "G":  # picture_Guardian
            iwindows.blit(picture_guardian, (sprites % 15*32, int(sprites/15)*32))
        elif itm == "N":  # picture_path
            iwindows.blit(picture_path, (sprites % 15*32, int(sprites/15)*32))
        sprites += 1


def main():
    """
    test
    """
    list_of_map = json.load(open("map.json"))
    lvl_select = list_of_map[1]["MAP"]
    show_is_ok = True
    continuer = 1

    macgyver_obj = classes.MacGyverClass(1)
    macgyver_obj.map = lvl_select

    py.init()

    clock = py.time.Clock()

    windows = py.display.set_mode((480, 480))
    py.mixer.music.load(PATH_OF_MUSIC)

    show_map(windows, lvl_select)  # select level and show map

    py.display.flip()

    py.mixer.music.play()

    while continuer == 1:

        clock.tick(60)
        for event in py.event.get():
            if event.type == py.QUIT:

                continuer = 0
            if event.type == py.KEYDOWN:
                if event.key == py.constants.K_DOWN:
                    if macgyver_obj.PosibleMove("DOWN", lvl_select):
                        show_is_ok = True
                    else:
                        show_is_ok = False

                if event.key == py.constants.K_UP:
                    if macgyver_obj.PosibleMove("UP", lvl_select):
                        show_is_ok = True
                    else:
                        show_is_ok = False

                if event.key == py.constants.K_LEFT:
                    if macgyver_obj.PosibleMove("LEFT", lvl_select):
                        show_is_ok = True
                    else:
                        show_is_ok = False

                if event.key == py.constants.K_RIGHT:
                    if macgyver_obj.PosibleMove("RIGHT", lvl_select):
                        show_is_ok = True
                    else:
                        show_is_ok = False

                if show_is_ok:
                    lvl_select = macgyver_obj.GetMap
                    print(lvl_select)
                    windows.fill((0, 0, 0))
                    show_map(windows, lvl_select)
                    py.display.flip()

    py.mixer.music.stop()
    py.quit()


if __name__ == "__main__":
    main()
