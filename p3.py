# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 27 avr 2020
@author: anthony thillerot
"""
import json
from time import sleep
import pygame as py
import classes as cl
import constant as C
import function as F


def game(reload, mwindows, nb_win_game):
    """
    This is the game function,
    it call all other function and class for play
    Returns
    -------
    End of function = End of game
    """

    if not reload:
        if C.NB_SPRITE_X == 15:
            list_of_map = json.load(open("map.json"))  # Import structure game
            lvl_select = list_of_map[0]["MAP"]   # Select a special structure
        else:
            lvl_select = F.create_lvl_randomly_easy()
            # create random structure
    else:
        nb_win_game += 1
        lvl_select = F.create_lvl_randomly_easy()  # create random structure

    mwindows.fill(C.BLACK)  # color all windows in black
    gameloop = 1  # loop of game

    needle = cl.ObjetInMap(2)  # Creation of needle object in map
    needle.map = lvl_select  # set current map at needle object
    needle.objet_caractere = C.CHAR_OF_NEEDLE  # set special char for map list
    lvl_select = needle.set_position_random(needle.map)  # set random position

    ether = cl.ObjetInMap(46)  # Creation of ether object in map
    ether.map = lvl_select  # set current map at ether object
    ether.objet_caractere = C.CHAR_OF_ETHER  # set special char for map list
    lvl_select = ether.set_position_random(ether.map)  # set random position

    plastic_tube = cl.ObjetInMap(4)  # Creation of plastic_tube object in map
    plastic_tube.map = lvl_select  # set current map at plastic_tube object
    plastic_tube.objet_caractere = C.CHAR_OF_PLASTIC_TUBE  # set special char
    lvl_select = plastic_tube.set_position_random(plastic_tube.map)
    # set random position

    macgyver_obj = cl.MacGyverClass(1)  # macgyver object from class
    macgyver_obj.map = lvl_select  # set current map at macgyver_obj

    F.show_map(mwindows, lvl_select, py, nb_win_game)  # show map list in wind
    py.display.flip()  # Update surface on the screen
    show_is_ok = False  # boolean for update in the loop

    while gameloop == 1:  # loop on the game
        for event in py.event.get():  # loop for look event on keyboard
            if event.type == py.QUIT:   # if the mouse click on x screen
                gameloop = 0  # set gameloop to 0 for quit the loop

            if event.type == py.KEYDOWN:  # event keydown press
                if event.key == py.constants.K_DOWN:  # event kDOWN press
                    show_is_ok = (macgyver_obj.possible_move("DOWN",
                                                             lvl_select))
                    # look if move is possible

                if event.key == py.constants.K_UP:  # event kUP press
                    show_is_ok = (macgyver_obj.possible_move("UP",
                                                             lvl_select))
                    # look if move is possible

                if event.key == py.constants.K_LEFT:  # event kLEFT press
                    show_is_ok = (macgyver_obj.possible_move("LEFT",
                                                             lvl_select))
                    # look if move is possible

                if event.key == py.constants.K_RIGHT:  # event kRIGHT press
                    show_is_ok = (macgyver_obj.possible_move("RIGHT",
                                                             lvl_select))
                    # look if move is possible

                if event.key == py.constants.K_F7:  # event kF7 press
                    vol = py.mixer.music.get_volume() - 0.1  # set vol - 0.1
                    if vol < 0:
                        vol = 0
                    elif vol > 1:
                        vol = 1
                    py.mixer.music.set_volume(vol)  # set vol value to mixer

                if event.key == py.constants.K_F8:  # event kF8 press
                    vol = py.mixer.music.get_volume() + 0.1  # set vol + 0.1
                    if vol < 0:
                        vol = 0
                    elif vol > 1:
                        vol = 1
                    py.mixer.music.set_volume(vol)  # set vol value to mixer

                if show_is_ok:
                    lvl_select = macgyver_obj.get_map  # get map list to MG
                    # print(lvl_select)
                    mwindows.fill(C.BLACK)  # color all windows surface in Blk
                    F.show_map(mwindows, lvl_select, py, nb_win_game)
                    # show map list in window
                    py.display.flip()  # Update surface on the screen
                    tmp = F.endofgame(lvl_select)
                    # test if end of game (WIN , LOSE, CONTINUE)

                    if tmp == 1:  # if end of game is win
                        F.show_msg(mwindows, "YOU WIN", py)  # show message
                        py.display.flip()  # Update surface on the screen
                        sleep(3)  # wait 3 seconds for read message
                        reload = True  # boolean for restart game
                        game(reload, mwindows, nb_win_game)
                        # show window game for restart

                    elif tmp == 2:  # if end of game is lose
                        F.show_msg(mwindows, "YOU LOSE", py)  # show message
                        py.display.flip()  # Update surface on the screen
                        sleep(3)  # wait 3 seconds for read message
                        reload = False  # boolean for restart game
                        gameloop = 0  # set gameloop to 0 for quit the while

    py.mixer.music.stop()  # stop mixer pygame , stop music
    py.quit()  # quit pygame and the interface


if __name__ == "__main__":
    reload_ = False  # the boolean variable for the restart game if win
    nb_win_game = 0
    game(reload_, F.show_interface(py), nb_win_game)  # show window game
