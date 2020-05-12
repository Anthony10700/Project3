# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 11 mai 2020
@author: anthony thillerot

"""
import pygame
import constant as C


class Display:
    """:argument this class is for all display pygame windows"""
    def __init__(self, map_list, id_map=0, lvl_map=0, nbrr_win_game=0):
        self.my_pygame = pygame
        self.my_pygame.init()  # initialisation de pygame
        self.my_pygame.display.set_caption('P3')  # set title of windows
        self.clock = self.my_pygame.time.Clock()
        # instance of clock module pygame
        self.windows = self.my_pygame.display.set_mode((C.NB_PIXEL_X, C.NB_PIXEL_Y))
        # set mumber pixel x and y for windows surface
        self.windows.fill(C.BLACK)  # color all windows in black
        self.my_pygame.mixer.music.load(C.PATH_OF_MUSIC)  # load music
        self.my_pygame.mixer.music.play()  # play music
        self.my_pygame.mixer.music.set_volume(0.1)  # set music in mixer at 0.1
        self.my_pygame.mixer.music.play(-1)
        self.clock.tick(60)  # set 60 refresh per seconde in the loop game
        self.map_list = map_list
        self.id_map = id_map
        self.lvl_map = lvl_map
        self.nb_win_game = nbrr_win_game

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
        return self.nb_win_game

    def set_nbr_win_game(self, nbr_win_gamee):
        """:argument set a number of win game"""
        self.nb_win_game = nbr_win_gamee

    def set_lvl_map(self, lvl_mapp):
        """:argument set a lvl map of game"""
        self.lvl_map = lvl_mapp

    def set_id_map(self, id_mapp):
        """:argument set a ID for current game"""
        self.id_map = id_mapp

    def set_map_list(self, mapp):
        """

        Parameters
        ----------
        mapp : TYPE : list of element map len(max_sprites)
            DESCRIPTION. : set specify map list of map game

        Returns
        -------
        None.

        """
        self.map_list = mapp

    def quit(self):
        """:return end of game close window"""
        self.my_pygame.mixer.quit()
        self.my_pygame.quit()

    def get_constant(self):
        """:returns all of constants in pygame.constants"""
        return self.my_pygame.constants

    def update_surface(self):
        """:argument Update surface on the screen"""
        self.my_pygame.display.flip()

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

    def show_msg(self, msg):
        """
        Parameters
        ----------
        msg : TYPE = string
            DESCRIPTION. : show message in window ex : you win !!
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
        self.windows.fill(C.BLACK)

        nb_obj = (self.map_list.count(C.CHAR_OF_NEEDLE) + self.map_list.count(
            C.CHAR_OF_ETHER) + self.map_list.count(C.CHAR_OF_PLASTIC_TUBE))
        # addition number of object in list self.map_list

        sprites = 0
        picture_guardian = self.my_pygame.image.load(C.PATH_OF_GUARDIAN).convert_alpha()
        # set picture to guardian obj

        picture_macgyver = self.my_pygame.image.load(C.PATH_OF_MACGYVER).convert_alpha()

        picture_wall = self.my_pygame.image.load(C.PATH_OF_WALL).convert_alpha()
        # set picture to wall obj

        picture_path = self.my_pygame.image.load(C.PATH_OF_PATH).convert_alpha()
        # set picture to path obj

        picture_needle = self.my_pygame.image.load(C.PATH_OF_NEEDLE).convert_alpha()
        # set picture to needle obj

        picture_ether = self.my_pygame.image.load(C.PATH_OF_ETHER).convert_alpha()
        # set picture to ether obj

        picture_plastic_tube = self.my_pygame.image.load(C.PATH_OF_PLASTIC_TUBE).convert_alpha()
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
                                       + str(self.nb_win_game)),
                                      True, C.WHITE, C.BLACK)
        self.windows.blit(text_number_lvl, (0, 16))
        # show on specific coordinate

        if nb_obj == 0:
            picture_syringe = self.my_pygame.image.load(
                C.PATH_OF_SYRINGE).convert_alpha()
            self.windows.blit(picture_syringe, ((C.NB_SPRITE_X-1)*C.NB_PIX_SPRITE, 0))
            # show syringe if all the objects are pick up
        else:
            if self.map_list.count(C.CHAR_OF_NEEDLE) == 0:
                picture_needle = self.my_pygame.image.load(
                    C.PATH_OF_NEEDLE).convert_alpha()
                self.windows.blit(picture_needle, ((C.NB_SPRITE_X-1) * C.NB_PIX_SPRITE, 0))
                # display if the object has been picked up
            if self.map_list.count(C.CHAR_OF_ETHER) == 0:
                picture_ether = self.my_pygame.image.load(C.PATH_OF_ETHER).convert_alpha()
                self.windows.blit(picture_ether, ((C.NB_SPRITE_X-2) * C.NB_PIX_SPRITE, 0))
                # display if the object has been picked up
            if self.map_list.count(C.CHAR_OF_PLASTIC_TUBE) == 0:
                picture_plastic_tube = self.my_pygame.image.load(C.PATH_OF_PLASTIC_TUBE
                                                                ).convert_alpha()
                self.windows.blit(picture_plastic_tube, ((C.NB_SPRITE_X-3) * C.NB_PIX_SPRITE, 0))
                # display if the object has been picked up

        for itm in self.map_list:
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
