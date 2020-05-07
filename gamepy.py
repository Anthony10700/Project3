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
import pygame
import constant as C


class GamePy:
    """
    game class, need pygame instance
    """

    def __init__(self):
        """
         init pygame and display the windows
         declaration varriable for game

        Returns
        -------
        None.

        """
        self.my_pygame = pygame  # instance de pygame
        self.my_pygame.init()  # initialisation de pygame
        self.my_pygame.display.set_caption('P3')  # set title of windows
        self.clock = self.my_pygame.time.Clock()
        # instance of clock module pygame
        self.windows = self.my_pygame.display.set_mode((C.NB_PIXEL_X,
                                                        C.NB_PIXEL_Y))
        # set mumber pixel x and y for windows surface
        self.my_pygame.mixer.music.load(C.PATH_OF_MUSIC)  # load music
        self.my_pygame.mixer.music.play()  # play music
        self.my_pygame.mixer.music.set_volume(0.1)  # set music in mixer at 0.1
        self.my_pygame.mixer.music.play(-1)
        self.clock.tick(60)  # set 60 refresh per seconde in the loop game
        self.my_pygame.display.flip()  # Update surface on the screen
        self.map = []  # the representation of the list map
        self.nbr_win_game = 0  # number of game win
        self.reload = False  # it use for test if regame
        self.id_map = 0  # id map in json file
        self.lvl_map = 0  # lvl for map in json file

    def set_windows_name(self, name):  # define a windows name
        """

        Parameters
        ----------
        name : TYPE : string
            DESCRIPTION. : set windows name

        Returns
        -------
        None.

        """

        self.my_pygame.display.set_caption(name)

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

    @property
    def get_map_game(self):
        """

        Returns
        -------
        TYPE : list of element map len(max_sprites)
            DESCRIPTION. : return the list map of current game

        """
        return self.map

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

    def create_random_map_list(self):
        """
        This function create a ramdom map list for next game if win
        Returns
        -------
        None.

        """
        self.id_map = self.id_map + 1
        self.lvl_map = 1 + int((C.NB_SPRITE_X - 15) / 5)
        map_create = [""]*C.NB_MAX_SPRITE
        map_create[0] = ('M')  # Macgyver on first sprite
        seed(time()+7)
        for i in range(1, 4):
            map_create[i] = ('N')

        past_v = 3
        var_v = 3
        while var_v <= C.NB_MAX_SPRITE - 2:  # create random path to Guardian
            nbr_rnd = randint(1, 4)
            past_v = var_v
            if map_create[var_v] != 'M' and map_create[var_v] != 'G':

                if nbr_rnd == 1 and var_v % C.NB_SPRITE_X < (C.NB_SPRITE_X-1):
                    if var_v + 1 < C.NB_MAX_SPRITE:
                        map_create[var_v+1] = 'N'
                        var_v = var_v + 1
                elif nbr_rnd == 3 and var_v % C.NB_SPRITE_X > 0:
                    if var_v - 1 > 1:
                        map_create[var_v-1] = 'N'
                        var_v = var_v - 1
                # elif var_v-C.NB_SPRITE_X > 1 and nbr_rnd == 40:
                #     map_create[var_v-C.NB_SPRITE_X] = 'N'
                #     var_v = var_v - C.NB_SPRITE_X
                elif var_v+C.NB_SPRITE_X < C.NB_MAX_SPRITE and nbr_rnd == 2:
                    map_create[var_v+C.NB_SPRITE_X] = 'N'
                    var_v = var_v + C.NB_SPRITE_X
                else:
                    var_v = past_v
            else:
                var_v = var_v + 1

        for nb_branch in range(5, C.NB_SPRITE_X, 5):
            # create branch random in the path to guardian

            for var_n in range(nb_branch * C.NB_SPRITE_X, C.NB_MAX_SPRITE, 1):
                if map_create[var_n] == 'N':
                    var_v = var_n
                    whi_var = 0
                    while whi_var < C.NB_RD_IN_BRANCH:
                        whi_var += 1
                        nbr_rnd = randint(1, 4)
                        past_v = var_v
                        if map_create[var_v] != 'M' and map_create[var_v] != 'G':
                            mod_var = var_v % C.NB_SPRITE_X
                            v_nb_s = var_v + C.NB_SPRITE_X
                            if nbr_rnd == 1 and mod_var < (C.NB_SPRITE_X-1):
                                if var_v + 1 < C.NB_MAX_SPRITE:
                                    map_create[var_v+1] = 'N'
                                    var_v = var_v + 1
                            elif nbr_rnd == 3 and mod_var > 0:
                                if var_v - 1 > 1:
                                    map_create[var_v-1] = 'N'
                                    var_v = var_v - 1
                            elif var_v-C.NB_SPRITE_X > 1 and nbr_rnd == 40:
                                map_create[var_v-C.NB_SPRITE_X] = 'N'
                                var_v = var_v - C.NB_SPRITE_X
                            elif v_nb_s < C.NB_MAX_SPRITE and nbr_rnd == 2:
                                map_create[v_nb_s] = 'N'
                                var_v = v_nb_s
                            else:
                                var_v = past_v
                        else:
                            var_v = var_v + 1
                    break

        for var_a in range(0, C.NB_MAX_SPRITE-1):
            # set all wall in the nothink value
            if map_create[var_a] == '':
                map_create[var_a] = ('W')

        map_create[C.NB_MAX_SPRITE-1] = ('G')  # Guardian on last sprite
        self.map = map_create

    def decrease_vol(self):
        """
        decrease the volume to -0.1
        Returns
        -------
        None.

        """
        vol = self.my_pygame.mixer.music.get_volume() - 0.1  # set vol + 0.1
        if vol < 0:
            vol = 0
        elif vol > 1:
            vol = 1
        self.my_pygame.mixer.music.set_volume(vol)  # set vol value to mixer

    def increase_vol(self):
        """
        increase the volume to +0.1

        Returns
        -------
        None.

        """
        vol = self.my_pygame.mixer.music.get_volume() + 0.1  # set vol - 0.1
        if vol < 0:
            vol = 0
        elif vol > 1:
            vol = 1
        self.my_pygame.mixer.music.set_volume(vol)  # set vol value to mixer

    def pause_music(self):
        """
        pause the music

        Returns
        -------
        None.

        """

        self.my_pygame.mixer.music.pause()  # pause the music

    def unpause_music(self):
        """
        unpause the music

        Returns
        -------
        None.

        """

        self.my_pygame.mixer.music.unpause()  # unpause the music after pause

    def look_end_of_game(self):
        """
        look if the game is win "1" or loose "2" or nothink "0"

        Returns game is win "1" or loose "2" or nothink "0"


        """
        nb_obj = (self.map.count(C.CHAR_OF_NEEDLE) +
                  self.map.count(C.CHAR_OF_ETHER) +
                  self.map.count(C.CHAR_OF_PLASTIC_TUBE))
    # addition number of object in list map

        if 'G' not in self.map:
            if nb_obj > 0:
                return 2
            self.nbr_win_game += 1
            return 1
        return 0

    def show_msg(self, msg):
        """

        Parameters
        ----------
        msg : TYPE = string
            DESCRIPTION. : show message in windows ex : you win !!

        Returns
        -------
        None.

        """
        self.windows.fill(C.WHITE)  # color all windows surface in WHITE
        font = self.my_pygame.font.SysFont('arial', 40)  # set special font
        text = font.render((msg), True, C.WHITE, C.BLACK)  # set msg
        self.windows.blit(text, (C.NB_PIXEL_X/3, C.NB_PIXEL_Y/3))
        self.my_pygame.display.flip()  # Update surface on the screen

    def show_map_on_screen(self):
        """
        display the map list self.map on windows surface
        and display a specify text

        Returns
        -------
        None.

        """
        nb_obj = (self.map.count(C.CHAR_OF_NEEDLE) + self.map.count(
            C.CHAR_OF_ETHER) + self.map.count(C.CHAR_OF_PLASTIC_TUBE))
    # addition number of object in list map

        sprites = 0
        picture_guardian = self.my_pygame.image.load(
                                            C.PATH_OF_GUARDIAN).convert_alpha()
        # set picture to guardian obj
        picture_macgyver = self.my_pygame.image.load(
                                            C.PATH_OF_MACGYVER).convert_alpha()

        picture_wall = self.my_pygame.image.load(
                                                C.PATH_OF_WALL).convert_alpha()
        # set picture to wall obj
        picture_path = self.my_pygame.image.load(
                                                C.PATH_OF_PATH).convert_alpha()
        # set picture to path obj

        picture_needle = self.my_pygame.image.load(
                                            C.PATH_OF_NEEDLE).convert_alpha()
        # set picture to needle obj

        picture_ether = self.my_pygame.image.load(
                                            C.PATH_OF_ETHER).convert_alpha()
        # set picture to ether obj

        picture_plastic_tube = self.my_pygame.image.load(
                                        C.PATH_OF_PLASTIC_TUBE).convert_alpha()
        # set picture to plastic_tube obj

        font = self.my_pygame.font.SysFont('arial', 11)  # set special font
        text = font.render((' Number of objects taken: ' + str(3 - nb_obj) +
                            ' / 3' + '    Press : F7 Sound : -' +
                            '  |  F8 : + or F9 for pause F10 for play'),
                           True, C.WHITE, C.BLACK)
        self.windows.blit(text, (0, 3))
        # show on specific coordinate

        text_number_lvl = font.render((' ID = ' + str(self.id_map) +
                                       ' LVL = ' + str(self.lvl_map) +
                                       ' | Number of level win : '
                                       + str(self.nbr_win_game)),
                                      True, C.WHITE, C.BLACK)
        self.windows.blit(text_number_lvl, (0, 16))
        # show on specific coordinate

        if nb_obj == 0:
            picture_syringe = self.my_pygame.image.load(
                C.PATH_OF_SYRINGE).convert_alpha()
            self.windows.blit(picture_syringe, (
                                        (C.NB_SPRITE_X-1)*C.NB_PIX_SPRITE, 0))
            # show syringe if all the objects are pick up
        else:
            if self.map.count(C.CHAR_OF_NEEDLE) == 0:
                picture_needle = self.my_pygame.image.load(
                    C.PATH_OF_NEEDLE).convert_alpha()
                self.windows.blit(picture_needle, (
                                    (C.NB_SPRITE_X-1) * C.NB_PIX_SPRITE, 0))
                # display if the object has been picked up
            if self.map.count(C.CHAR_OF_ETHER) == 0:
                picture_ether = self.my_pygame.image.load(
                    C.PATH_OF_ETHER).convert_alpha()
                self.windows.blit(picture_ether, (
                                    (C.NB_SPRITE_X-2) * C.NB_PIX_SPRITE, 0))
                # display if the object has been picked up
            if self.map.count(C.CHAR_OF_PLASTIC_TUBE) == 0:
                picture_plastic_tube = self.my_pygame.image.load(
                    C.PATH_OF_PLASTIC_TUBE).convert_alpha()
                self.windows.blit(picture_plastic_tube, (
                                    (C.NB_SPRITE_X-3) * C.NB_PIX_SPRITE, 0))
                # display if the object has been picked up

        for itm in self.map:
            if itm == "M":  # picture_MacGyver
                self.windows.blit(picture_macgyver, (sprites % (C.NB_SPRITE_X)
                                                     * C.NB_PIX_SPRITE,
                                                     int(sprites /
                                                         C.NB_SPRITE_Y+1) *
                                                     C.NB_PIX_SPRITE))
                # show picture_macgyver on specific coordinate

            elif itm == "W":  # picture_wall
                self.windows.blit(picture_wall, (sprites % C.NB_SPRITE_X *
                                                 C.NB_PIX_SPRITE,
                                                 int(sprites/C.NB_SPRITE_Y+1) *
                                                 C.NB_PIX_SPRITE))
                # show picture_wall on specific coordinate

            elif itm == "G":  # picture_Guardian
                self.windows.blit(picture_guardian, (sprites % C.NB_SPRITE_X *
                                                     C.NB_PIX_SPRITE,
                                                     int(sprites /
                                                         C.NB_SPRITE_Y+1) *
                                                     C.NB_PIX_SPRITE))
                # show picture_guardian on specific coordinate
            elif itm == "N":  # picture_path
                self.windows.blit(picture_path, (sprites % C.NB_SPRITE_X *
                                                 C.NB_PIX_SPRITE,
                                                 int(sprites/C.NB_SPRITE_Y+1) *
                                                 C.NB_PIX_SPRITE))
                # show picture_path on specific coordinate
            elif itm == C.CHAR_OF_NEEDLE:  # picture_needle
                self.windows.blit(picture_needle, (sprites % C.NB_SPRITE_X *
                                                   C.NB_PIX_SPRITE,
                                                   int(sprites /
                                                       C.NB_SPRITE_Y+1) *
                                                   C.NB_PIX_SPRITE))
                # show picture_needle on specific coordinate
            elif itm == C.CHAR_OF_ETHER:  # picture_ether
                self.windows.blit(picture_ether, (sprites % C.NB_SPRITE_X *
                                                  C.NB_PIX_SPRITE,
                                                  int(sprites /
                                                      C.NB_SPRITE_Y+1) *
                                                  C.NB_PIX_SPRITE))
                # show picture_ether on specific coordinate
            elif itm == C.CHAR_OF_PLASTIC_TUBE:  # picture_plastic_tube
                self.windows.blit(picture_plastic_tube, (sprites %
                                                         C.NB_SPRITE_X *
                                                         C.NB_PIX_SPRITE,
                                                         int(sprites /
                                                             C.NB_SPRITE_Y+1) *
                                                         C.NB_PIX_SPRITE))
                # show picture_plastic_tube on specific coordinate
            sprites += 1
