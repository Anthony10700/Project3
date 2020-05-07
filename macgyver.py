# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 27 avr 2020
@author: anthony thillerot
"""
import constant as C


class MacGyver:
    """
    class of mac gyver object, the class contain function,
    Get position in sprite
    Test if the move is possible
    """

    def __init__(self, position_in_sprites):
        """

        Parameters
        ----------
        position_in_sprites : TYPE : int
            DESCRIPTION. : position of macgyver in sprites in map list

        Returns
        -------
        None.

        """
        self.number_of_sprite_x = C.NB_SPRITE_X
        self.number_of_sprite_y = C.NB_SPRITE_Y
        self.max_sprites = self.number_of_sprite_x * self.number_of_sprite_y
        assert 1 <= position_in_sprites <= self.max_sprites
        self.position_in_sprites = position_in_sprites
        self.map = []

    @property
    def setposition_in_sprites(self):
        """
        Get Position In Sprites
        """
        return self.position_in_sprites

    @property
    def get_map(self):
        """
        Get map list
        """
        return self.map

    def possible_move(self, mov, mapjson_select):
        """
        test if the movemennt is possible and return true or false

        Parameters
        ----------
        mov : TYPE : string = 'RIGHT'
            DESCRIPTION.
        mapjson_select : TYPE : maplist of game
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        self.map = mapjson_select
        pos = self.position_in_sprites
        # position_in_sprites in range 1 to NB_MAX_SPRITE
        # not 0 to NB_MAX_SPRITE - 1
        nb_sprites_x = self.number_of_sprite_x
        nb_sprites_y = self.number_of_sprite_y

        if mov == "RIGHT":
            if pos % nb_sprites_x == 0 or mapjson_select[pos] == "W":
                # return false if we are on a border
                # or the desired position is equal to W
                return False
            self.map[self.position_in_sprites-1] = "N"
            self.map[self.position_in_sprites] = "M"
            self.position_in_sprites = self.position_in_sprites + 1
        elif mov == "LEFT":
            if pos % nb_sprites_x == 1 or mapjson_select[pos-2] == "W":
                # return false if we are on a border
                # or the desired position is equal to W
                return False
            self.map[self.position_in_sprites-1] = "N"
            self.map[self.position_in_sprites - 2] = "M"
            self.position_in_sprites = self.position_in_sprites - 1
        elif mov == "UP":
            if (pos / C.NB_SPRITE_X) - 1 <= 0 or mapjson_select[pos - (C.NB_SPRITE_X + 1)] == "W":
                # return false if we are on a border
                # or the desired position is equal to W
                return False
            self.map[self.position_in_sprites - 1] = "N"
            self.map[self.position_in_sprites - (C.NB_SPRITE_X + 1)] = "M"
            self.position_in_sprites = self.position_in_sprites - C.NB_SPRITE_X
        elif mov == "DOWN":
            if (pos / C.NB_SPRITE_X) + 1 > nb_sprites_y or mapjson_select[pos + (C.NB_SPRITE_X - 1)] == "W":
                # return false if we are on a border
                # or the desired position is equal to W
                return False
            self.map[self.position_in_sprites-1] = "N"
            self.map[self.position_in_sprites + (C.NB_SPRITE_X - 1)] = "M"
            self.position_in_sprites = self.position_in_sprites + C.NB_SPRITE_X
        return True
