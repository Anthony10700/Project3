# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 27 avr 2020
@author: anthony thillerot
"""
import json
from time import sleep
import pygame as py
import classes
import constant
import function


def main():
    """
    test
    """

    list_of_map = json.load(open("map.json"))
    lvl_select = list_of_map[0]["MAP"]
    show_is_ok = True
    continuer = 1

    needle = classes.ObjetInMap(9)
    needle.map = lvl_select
    needle.objet_caractere = constant.CHAR_OF_NEEDLE
    lvl_select = needle.SetPositionRandom(needle.map)

    ether = classes.ObjetInMap(1)
    ether.map = lvl_select
    ether.objet_caractere = constant.CHAR_OF_ETHER
    lvl_select = ether.SetPositionRandom(ether.map)

    plastic_tube = classes.ObjetInMap(4)
    plastic_tube.map = lvl_select
    plastic_tube.objet_caractere = constant.CHAR_OF_PLASTIC_TUBE
    lvl_select = plastic_tube.SetPositionRandom(plastic_tube.map)

    macgyver_obj = classes.MacGyverClass(1)
    macgyver_obj.map = lvl_select

    py.init()
    py.display.set_caption('P3')
    clock = py.time.Clock()

    windows = py.display.set_mode((constant.NB_PIXEL_X, constant.NB_PIXEL_Y))
    py.mixer.music.load(constant.PATH_OF_MUSIC)

    function.show_map(windows, lvl_select, py)  # select level and show map

    py.display.flip()

    py.mixer.music.play()
    py.mixer.music.set_volume(0.1)

    while continuer == 1:

        clock.tick(60)
        for event in py.event.get():
            if event.type == py.QUIT:

                continuer = 0
            if event.type == py.KEYDOWN:
                if event.key == py.constants.K_DOWN:
                    if macgyver_obj.PossibleMove("DOWN", lvl_select):
                        show_is_ok = True
                    else:
                        show_is_ok = False

                if event.key == py.constants.K_UP:
                    if macgyver_obj.PossibleMove("UP", lvl_select):
                        show_is_ok = True
                    else:
                        show_is_ok = False

                if event.key == py.constants.K_LEFT:
                    if macgyver_obj.PossibleMove("LEFT", lvl_select):
                        show_is_ok = True
                    else:
                        show_is_ok = False

                if event.key == py.constants.K_RIGHT:
                    if macgyver_obj.PossibleMove("RIGHT", lvl_select):
                        show_is_ok = True
                    else:
                        show_is_ok = False

                if event.key == py.constants.K_F7:
                    vol = py.mixer.music.get_volume() - 0.1
                    if vol < 0:
                        vol = 0
                    elif vol > 1:
                        vol = 1
                    py.mixer.music.set_volume(vol)

                if event.key == py.constants.K_F8:
                    vol = py.mixer.music.get_volume() + 0.1
                    if vol < 0:
                        vol = 0
                    elif vol > 1:
                        vol = 1
                    py.mixer.music.set_volume(vol)

                if show_is_ok:
                    lvl_select = macgyver_obj.GetMap
                    print(lvl_select)
                    windows.fill(constant.BLACK)
                    function.show_map(windows, lvl_select, py)
                    py.display.flip()

                    if function.endofgame(macgyver_obj.GetPositionInSprites
                                          - 1, lvl_select) == 1:
                        function.show_msg(windows, "YOU WIN", py)
                        py.display.flip()
                        sleep(2)
                        continuer = 0
                    elif function.endofgame(macgyver_obj.GetPositionInSprites
                                            - 1, lvl_select) == 2:
                        function.show_msg(windows, "YOU LOSE", py)
                        py.display.flip()
                        sleep(2)
                        continuer = 0

    py.mixer.music.stop()
    py.quit()


if __name__ == "__main__":
    main()
