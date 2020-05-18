# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 27 avr 2020
@author: anthony thillerot
"""
from random import randint, seed
from time import time
import constant as CON


class ObjetInMap:
    """
    This class make an object in the list of element (map_select) and this
    characteristic
    """

    def __init__(self, position_in_sprites):
        """

        Parameters
        ----------
        position_in_sprites : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.number_of_sprite_x = CON.NB_SPRITE_X
        self.number_of_sprite_y = CON.NB_SPRITE_Y
        self.max_sprites = self.number_of_sprite_x * self.number_of_sprite_y
        assert 1 <= position_in_sprites <= self.max_sprites
        self.position_in_sprites = position_in_sprites
        self.map = []
        self.object_description = ""
        self.objet_caractere = ""

    @property
    def get_position_in_sprites(self):
        """
        Get Position In Sprites
        """
        return self.position_in_sprites

    @property
    def get_map(self):
        """
        Returns
        -------
        TYPE : list of element map len(max_sprites)
            DESCRIPTION. : return the list map of current game
        """
        return self.map

    def set_map(self, map_select):
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

    def set_position_random(self, map_select):
        """
        This function set a random position for the object created
        in the map where the element egal N (nothing)
        Parameters
        ----------
        map_select : TYPE = list of element in map
            DESCRIPTION.

        Returns
        -------
        map_select : TYPE = = list of element in map
            DESCRIPTION.

        """
        seed(time()+self.position_in_sprites)  # initialize the random number generator.
        number_rnd = randint(4, int(map_select.count('N')))
        # Return a random integer in range 4 to map_select.count('N')

        assert 1 <= number_rnd <= self.max_sprites
        # return error if the random number is not in the range
        nb_n_in_map = 0

        for i in range(0, len(map_select) - 1):
            if map_select[i] == "N":
                nb_n_in_map += 1
            if nb_n_in_map == number_rnd:
                map_select[i] = self.objet_caractere
                break
        return map_select
