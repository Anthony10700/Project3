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
import display as D


def main(game_inst, display):
    """
    This is the game function,
    it's call all other function and class for playing
    Returns
    -------
    End of function = End of game
    """

    if not game_inst.get_reload:  # get reload bool for look if game is restart
        if C.NB_SPRITE_X == 15:  # if number of sprite in X is 15 read in file a map lvl
            game_inst.read_map_in_file()  # read map list in file .json
        else:
            game_inst.create_random_map_list()  # create map list randomly


    else:
        game_inst.create_random_map_list()  # create random structure
        game_inst.increase_nbr_win_game()  # increase +1 the number of win game

    display.set_nbr_win_game(game_inst.get_nbr_win_game)  # set number of win game to display
    display.set_id_map(game_inst.get_id_map)  # set id of map game to display
    display.set_lvl_map(game_inst.get_lvl_map)  # set lvl map of game to display

    gameloop = 1  # loop of game

    needle = OIM.ObjetInMap(2)  # Creation of needle object in map
    needle.set_map(game_inst.get_map_game)  # set current map at needle object
    needle.objet_caractere = C.CHAR_OF_NEEDLE  # set special char for map list
    game_inst.set_map_game(needle.set_position_random(needle.map))
    #  set random position

    ether = OIM.ObjetInMap(46)  # Creation of ether object in map
    ether.set_map(game_inst.get_map_game)  # set current map at ether object
    ether.objet_caractere = C.CHAR_OF_ETHER  # set special char for map list
    game_inst.set_map_game(ether.set_position_random(ether.map))
    # set random position

    plastic_tube = OIM.ObjetInMap(4)  # Creation of plastic_tube object in map
    plastic_tube.set_map(game_inst.get_map_game)  # set current map at plastic_tube object
    plastic_tube.objet_caractere = C.CHAR_OF_PLASTIC_TUBE  # set special char
    game_inst.set_map_game(plastic_tube.set_position_random(plastic_tube.map))
    # set random position

    macgyver_obj = MG.MacGyver(1)  # macgyver object from class
    macgyver_obj.set_map(game_inst.get_map_game)  # set current map at macgyver_obj
    game_inst.set_map_game(macgyver_obj.map)  # set map game to game instance

    display.set_map_list(game_inst.get_map_game)  # set map game to display
    display.show_map_on_screen()  # show map list in wind
    display.update_surface() # Update surface on the screen

    show_is_ok = False  # boolean for update in the loop
    constant = display.get_constant()  # list of constant pygame

    while gameloop == 1:  # loop on the game
        for event in display.my_pygame.event.get():  # loop for look event on keyboard
            if event.type == display.my_pygame.QUIT:   # if the mouse click on x screen
                gameloop = 0  # set gameloop to 0 for quit the loop

            if event.type == display.my_pygame.KEYDOWN:  # event keydown press
                if event.key == constant.K_DOWN:  # event kDOWN press
                    show_is_ok = (macgyver_obj.possible_move("DOWN", game_inst.get_map_game))
                    # look if move is possible

                if event.key == constant.K_UP:  # event kUP press
                    show_is_ok = (macgyver_obj.possible_move("UP", game_inst.get_map_game))
                    # look if move is possible

                if event.key == constant.K_LEFT:  # event kLEFT press
                    show_is_ok = (macgyver_obj.possible_move("LEFT", game_inst.get_map_game))
                    # look if move is possible

                if event.key == constant.K_RIGHT:  # event kRIGHT press
                    show_is_ok = (macgyver_obj.possible_move("RIGHT", game_inst.get_map_game))
                    # look if move is possible

                if event.key == constant.K_F7:  # event kF7 press
                    display.decrease_vol()  # decrease the volume music

                if event.key == constant.K_F8:  # event kF8 press
                    display.increase_vol()  # increse the volume music

                if event.key == constant.K_F9:  # event kF9 press
                    display.pause_music()  # pause the music

                if event.key == constant.K_F10:  # event kF10 press
                    display.unpause_music()  # unpause the music

                if show_is_ok:
                    game_inst.set_map_game(macgyver_obj.get_map)  # get map list to MG
                    display.set_map_list(game_inst.get_map_game)  # set map game to display
                    display.show_map_on_screen()  # show map list in window
                    display.update_surface()  # Update surface on the screen

                    tmp = game_inst.look_end_of_game()
                    # test if end of game (WIN , LOSE, CONTINUE)

                    if tmp == 1:  # if end of game is win
                        display.show_msg("YOU WIN")  # show message
                        sleep(3)  # wait 3 seconds for read message
                        game_inst.set_reload(True)  # boolean for restart game
                        main(game_inst, display)  # show window game for restart

                    elif tmp == 2:  # if end of game is lose
                        display.show_msg("YOU LOSE")  # show message
                        sleep(3)  # wait 3 seconds for read message
                        game_inst.set_reload(False)  # boolean for restart game
                        gameloop = 0  # set gameloop to 0 for quit the while

    display.quit()  # quit pygame and the interface


if __name__ == "__main__":
    Mygame = GP.GamePy()  # create instance gamepy

    Mydisplay = D.Display(Mygame.read_map_in_file(),
                          Mygame.get_id_map,
                          Mygame.get_lvl_map,
                          Mygame.get_nbr_win_game)
    # create instance for pygame display usage
    Mydisplay.show_map_on_screen()
    # display the map list map on windows surface

    main(Mygame, Mydisplay)  # run main def for lunch game
