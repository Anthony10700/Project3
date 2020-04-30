# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 27 avr 2020
@author: anthony thillerot
"""
import constant


def endofgame(position_macgyver, map_select):
    nb_obj = (map_select.count(constant.CHAR_OF_NEEDLE) +
              map_select.count(constant.CHAR_OF_ETHER) +
              map_select.count(constant.CHAR_OF_PLASTIC_TUBE))

    if 'G' not in map_select and nb_obj == 0:
        return 1
    elif 'G' not in map_select and nb_obj > 0:
        return 2
    else:
        return 0


def show_msg(iwindows, msg, ipygame):
    iwindows.fill(constant.WHITE)
    font = ipygame.font.SysFont('arial', 40)
    text = font.render((msg), True, constant.WHITE, constant.BLACK)
    iwindows.blit(text, (constant.NB_PIXEL_X/3, constant.NB_PIXEL_Y/2))


def show_map(iwindows, mymap, ipygame):
    """
    Show map , map represent list of sprites with contain elements
    M = Macggyver , W = Wall , G = Guardian , N = Nothink or path
    """
    nb_obj = (mymap.count(constant.CHAR_OF_NEEDLE) + mymap.count(
        constant.CHAR_OF_ETHER) +
              mymap.count(constant.CHAR_OF_PLASTIC_TUBE))
    sprites = 0
    picture_guardian = ipygame.image.load(constant.PATH_OF_GUARDIAN
                                          ).convert_alpha()
    picture_macgyver = ipygame.image.load(constant.PATH_OF_MACGYVER
                                          ).convert_alpha()
    picture_wall = ipygame.image.load(constant.PATH_OF_WALL).convert_alpha()
    picture_path = ipygame.image.load(constant.PATH_OF_PATH).convert_alpha()
    picture_needle = ipygame.image.load(constant.PATH_OF_NEEDLE
                                        ).convert_alpha()
    picture_ether = ipygame.image.load(constant.PATH_OF_ETHER).convert_alpha()
    picture_plastic_tube = ipygame.image.load(
        constant.PATH_OF_PLASTIC_TUBE).convert_alpha()

    font = ipygame.font.SysFont('arial', 12)
    text = font.render((' Number of objects taken: ' + str(3 - nb_obj) + ' / 3'
                        + '            Press : F7 Sound -   OR   F8 Sound + '),
                       True, constant.WHITE, constant.BLACK)
    iwindows.blit(text, (0, 5))

    if nb_obj == 0:
        picture_syringe = ipygame.image.load(
            constant.PATH_OF_SYRINGE).convert_alpha()
        iwindows.blit(picture_syringe, (14*32, 0))

    for itm in mymap:
        if itm == "M":  # picture_MacGyver
            iwindows.blit(picture_macgyver, (sprites % 15*32,
                                             int(sprites/15+1)*32))
        elif itm == "W":  # picture_wall
            iwindows.blit(picture_wall, (sprites % 15*32,
                                         int(sprites/15+1)*32))
        elif itm == "G":  # picture_Guardian
            iwindows.blit(picture_guardian, (sprites % 15*32,
                                             int(sprites/15+1)*32))
        elif itm == "N":  # picture_path
            iwindows.blit(picture_path, (sprites % 15*32,
                                         int(sprites/15+1)*32))
        elif itm == constant.CHAR_OF_NEEDLE:  # picture_needle
            iwindows.blit(picture_needle, (sprites % 15*32,
                                           int(sprites/15+1)*32))
        elif itm == constant.CHAR_OF_ETHER:  # picture_ether
            iwindows.blit(picture_ether, (sprites % 15*32,
                                          int(sprites/15+1)*32))
        elif itm == constant.CHAR_OF_PLASTIC_TUBE:  # picture_plastic_tube
            iwindows.blit(picture_plastic_tube, (sprites % 15*32,
                                                 int(sprites/15+1)*32))
        sprites += 1
