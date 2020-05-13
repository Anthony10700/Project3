# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 27 avr 2020
@author: anthony thillerot
"""
from random import randint
from random import seed
from time import time
import json
import constant as CON

class GamePy:
    """
    game class all methode for the content of game
    """

    def __init__(self):
        """
         init pygame and display the window
         declaration varriable for game
        Returns
        -------
        None.
        """
        self.map = []  # the representation of the list map
        self.nbr_win_game = 0  # number of game win
        self.reload = False  # it use for test if regame
        self.id_map = 0  # id map in json file
        self.lvl_map = 0  # lvl for map in json file

    @property
    def get_reload(self):
        """:returns bool reload for look game is restart"""
        return self.reload

    @property
    def get_id_map(self):
        """:returns id of current level"""
        return self.id_map

    @property
    def get_lvl_map(self):
        """:returns level of current map"""
        return self.lvl_map

    @property
    def get_nbr_win_game(self):
        """:returns number of win game"""
        return self.nbr_win_game

    @property
    def get_map_game(self):
        """
        Returns
        -------
        TYPE : list of element map len(max_sprites)
            DESCRIPTION. : return the list map of current game
        """
        return self.map

    def set_nbr_win_game(self, nbr_win_gamee):
        """:argument set a number of win game"""
        self.nbr_win_game = nbr_win_gamee

    def set_lvl_map(self, lvl_mapp):
        """:argument set a lvl map of game"""
        self.lvl_map = lvl_mapp

    def set_id_map(self, id_mapp):
        """:argument set a ID for current game"""
        self.id_map = id_mapp

    def increase_nbr_win_game(self):
        """:returns increase +1 of number of win game"""
        self.nbr_win_game += 1

    def set_reload(self, reloadd):
        """:argument set a bool reload for look the game is restart"""
        self.reload = reloadd

    def set_map_game(self, map_select):
        """
        Parameters
        ----------
        map_select : TYPE : list of element map len(max_sprites)
            DESCRIPTION. : set specify map list of map game

        Returns
        -------
        None.
        """
        self.map = map_select

    def read_map_in_file(self, index_in_list_of_map=0):
        """
        Parameters
        ----------
        index_in_list_of_map : TYPE, optional
            DESCRIPTION. The default is 0.

        Returns
        -------
        None

        """
        list_of_map = json.load(open("map.json"))  # Import structure game
        # Select a special structure
        self.id_map = list_of_map[index_in_list_of_map]["ID"]
        # set id map from the json file
        self.lvl_map = list_of_map[index_in_list_of_map]["LVL"]
        # set lvl map from the json file
        self.map = list_of_map[index_in_list_of_map]["MAP"]
        return self.map

    def create_random_map_list(self):
        """
        This function create a ramdom map list for next game if win
        Returns
        -------
        None.

        """
        self.id_map = self.id_map + 1
        self.lvl_map = 1 + int((CON.NB_SPRITE_X - 15) / 5)
        map_create = [""]*CON.NB_MAX_SPRITE
        map_create[0] = ('M')  # Macgyver on first sprite
        seed(time()+7)
        for i in range(1, 4):
            map_create[i] = ('N')

        past_v = 3
        var_v = 3
        while var_v <= CON.NB_MAX_SPRITE - 2:  # create random path to Guardian
            nbr_rnd = randint(1, 4)
            past_v = var_v
            if map_create[var_v] != 'M' and map_create[var_v] != 'G':

                if nbr_rnd == 1 and var_v % CON.NB_SPRITE_X < (CON.NB_SPRITE_X-1):
                    if var_v + 1 < CON.NB_MAX_SPRITE:
                        map_create[var_v+1] = 'N'
                        var_v = var_v + 1
                elif nbr_rnd == 3 and var_v % CON.NB_SPRITE_X > 0:
                    if var_v - 1 > 1:
                        map_create[var_v-1] = 'N'
                        var_v = var_v - 1
                # elif var_v-CON.NB_SPRITE_X > 1 and nbr_rnd == 40:
                #     map_create[var_v-CON.NB_SPRITE_X] = 'N'
                #     var_v = var_v - CON.NB_SPRITE_X
                elif var_v+CON.NB_SPRITE_X < CON.NB_MAX_SPRITE and nbr_rnd == 2:
                    map_create[var_v+CON.NB_SPRITE_X] = 'N'
                    var_v = var_v + CON.NB_SPRITE_X
                else:
                    var_v = past_v
            else:
                var_v = var_v + 1

        for nb_branch in range(5, CON.NB_SPRITE_X, 5):
            # create branch random in the path to guardian

            for var_n in range(nb_branch * CON.NB_SPRITE_X, CON.NB_MAX_SPRITE, 1):
                if map_create[var_n] == 'N':
                    var_v = var_n
                    whi_var = 0
                    while whi_var < CON.NB_RD_IN_BRANCH:
                        whi_var += 1
                        nbr_rnd = randint(1, 4)
                        past_v = var_v
                        if map_create[var_v] != 'M' and map_create[var_v] != 'G':
                            mod_var = var_v % CON.NB_SPRITE_X
                            v_nb_s = var_v + CON.NB_SPRITE_X
                            if nbr_rnd == 1 and mod_var < (CON.NB_SPRITE_X-1):
                                if var_v + 1 < CON.NB_MAX_SPRITE:
                                    map_create[var_v+1] = 'N'
                                    var_v = var_v + 1
                            elif nbr_rnd == 3 and mod_var > 0:
                                if var_v - 1 > 1:
                                    map_create[var_v-1] = 'N'
                                    var_v = var_v - 1
                            elif var_v-CON.NB_SPRITE_X > 1 and nbr_rnd == 40:
                                map_create[var_v-CON.NB_SPRITE_X] = 'N'
                                var_v = var_v - CON.NB_SPRITE_X
                            elif v_nb_s < CON.NB_MAX_SPRITE and nbr_rnd == 2:
                                map_create[v_nb_s] = 'N'
                                var_v = v_nb_s
                            else:
                                var_v = past_v
                        else:
                            var_v = var_v + 1
                    break

        for var_a in range(0, CON.NB_MAX_SPRITE-1):
            # set all wall in the nothink value
            if map_create[var_a] == '':
                map_create[var_a] = ('W')

        map_create[CON.NB_MAX_SPRITE-1] = ('G')  # Guardian on last sprite
        self.map = map_create

    def look_end_of_game(self):
        """
        look if the game is win "1" or loose "2" or nothing "0"

        Returns game is win "1" or loose "2" or nothing "0"


        """
        nb_obj = (self.map.count(CON.CHAR_OF_NEEDLE) +
                  self.map.count(CON.CHAR_OF_ETHER) +
                  self.map.count(CON.CHAR_OF_PLASTIC_TUBE))
    # addition number of object in list map

        if 'G' not in self.map:
            if nb_obj > 0:
                return CON.CONSTANT_LOSE
            return CON.CONSTANT_WIN
        return CON.CONSTANT_CONTINUE
