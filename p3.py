# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 27 avr 2020
@author: anthony thillerot
"""
from time import sleep
import gamepy as GP
import macgyver as MG
import objetinmap as OIM
import constant as C


def main(game_inst):
    """
    This is the game function,
    it call all other function and class for play
    Returns
    -------
    End of function = End of game
    """

    if not game_inst.reload:
        if C.NB_SPRITE_X == 15:
            game_inst.read_map_in_file()  # read map list in file .json
        else:
            game_inst.create_random_map_list()  # create map list randomly

    else:
        game_inst.create_random_map_list()  # create random structure

    ipy = game_inst.my_pygame
    game_inst.windows.fill(C.BLACK)  # color all windows in black
    gameloop = 1  # loop of game

    needle = OIM.ObjetInMap(2)  # Creation of needle object in map
    needle.map = game_inst.get_map_game  # set current map at needle object
    needle.objet_caractere = C.CHAR_OF_NEEDLE  # set special char for map list
    game_inst.set_map_game(needle.set_position_random(needle.map))
    # set random pos

    ether = OIM.ObjetInMap(46)  # Creation of ether object in map
    ether.map = game_inst.get_map_game  # set current map at ether object
    ether.objet_caractere = C.CHAR_OF_ETHER  # set special char for map list
    game_inst.set_map_game(ether.set_position_random(ether.map))
    # set random position

    plastic_tube = OIM.ObjetInMap(4)  # Creation of plastic_tube object in map
    plastic_tube.map = game_inst.get_map_game
    # set current map at plastic_tube object
    plastic_tube.objet_caractere = C.CHAR_OF_PLASTIC_TUBE  # set special char
    game_inst.set_map_game(plastic_tube.set_position_random(plastic_tube.map))
    # set random position

    macgyver_obj = MG.MacGyver(1)  # macgyver object from class
    macgyver_obj.map = game_inst.get_map_game
    # set current map at macgyver_obj

    game_inst.show_map_on_screen()  # show map list in wind
    ipy.display.flip()  # Update surface on the screen
    show_is_ok = False  # boolean for update in the loop

    while gameloop == 1:  # loop on the game
        for event in ipy.event.get():  # loop for look event on keyboard
            if event.type == ipy.QUIT:   # if the mouse click on x screen
                gameloop = 0  # set gameloop to 0 for quit the loop

            if event.type == ipy.KEYDOWN:  # event keydown press
                if event.key == ipy.constants.K_DOWN:  # event kDOWN press
                    show_is_ok = (macgyver_obj.possible_move("DOWN",
                                                             game_inst.
                                                             get_map_game))
                    # look if move is possible

                if event.key == ipy.constants.K_UP:  # event kUP press
                    show_is_ok = (macgyver_obj.possible_move("UP",
                                                             game_inst.
                                                             get_map_game))
                    # look if move is possible

                if event.key == ipy.constants.K_LEFT:  # event kLEFT press
                    show_is_ok = (macgyver_obj.possible_move("LEFT",
                                                             game_inst.
                                                             get_map_game))
                    # look if move is possible

                if event.key == ipy.constants.K_RIGHT:  # event kRIGHT press
                    show_is_ok = (macgyver_obj.possible_move("RIGHT",
                                                             game_inst.
                                                             get_map_game))
                    # look if move is possible

                if event.key == ipy.constants.K_F7:  # event kF7 press
                    game_inst.decrease_vol()  # decrease the volume music

                if event.key == ipy.constants.K_F8:  # event kF8 press
                    game_inst.increase_vol()  # increse the volume music

                if event.key == ipy.constants.K_F9:  # event kF9 press
                    game_inst.pause_music()  # pause the music

                if event.key == ipy.constants.K_F10:  # event kF10 press
                    game_inst.unpause_music()  # unpause the music

                if show_is_ok:
                    game_inst.set_map_game(macgyver_obj.get_map)
                    # get map list to MG
                    # print(lvl_select)
                    game_inst.windows.fill(C.BLACK)
                    # color all windows surface in Blk
                    game_inst.show_map_on_screen()
                    # show map list in window
                    ipy.display.flip()  # Update surface on the screen
                    tmp = game_inst.look_end_of_game()
                    # test if end of game (WIN , LOSE, CONTINUE)

                    if tmp == 1:  # if end of game is win
                        game_inst.show_msg("YOU WIN")  # show message
                        sleep(3)  # wait 3 seconds for read message
                        game_inst.reload = True  # boolean for restart game
                        main(game_inst)
                        # show window game for restart

                    elif tmp == 2:  # if end of game is lose
                        game_inst.show_msg("YOU LOSE")  # show message
                        sleep(3)  # wait 3 seconds for read message
                        game_inst.reload = False  # boolean for restart game
                        gameloop = 0  # set gameloop to 0 for quit the while

    ipy.mixer.music.stop()  # stop mixer pygame , stop music
    ipy.quit()  # quit pygame and the interface


if __name__ == "__main__":
    Mygame = GP.GamePy()  # create instance gamepy
    Mygame.read_map_in_file()  # read map list in file .json
    Mygame.show_map_on_screen()
    # display the map list map on windows surface
    Mygame.reload = False  # the boolean variable for the restart game if win
    Mygame.nbr_win_game = 0  # set number of win game at 0

    main(Mygame)  # show window game
