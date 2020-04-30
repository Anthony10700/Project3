# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 27 avr 2020
@author: anthony thillerot
"""
from random import randint
from random import seed
from time import time

# CONSTANT
NUMBER_OF_SPRITEX = 15
NUMBER_OF_SPRITEY = 15


class MacGyverClass:
    def __init__(self, position_in_sprites):
        self.position_x = 0
        self.position_y = 0
        self.number_of_sprite_x = NUMBER_OF_SPRITEX
        self.number_of_sprite_y = NUMBER_OF_SPRITEY
        self.max_sprites = self.number_of_sprite_x * self.number_of_sprite_y
        assert 1 <= position_in_sprites <= self.max_sprites
        self.position_in_sprites = position_in_sprites
        self.map = []

    @property
    def GetPositionInSprites(self):
        """ Get Position In Sprites"""
        return self.position_in_sprites

    @property
    def GetMap(self):
        """ Get map"""
        return self.map

    def PossibleMove(self, mov, mapjson_select):
        """ test if the movemennt is possible and return true or false"""
        self.map = mapjson_select
        pos = self.position_in_sprites
        nb_sprites_x = self.number_of_sprite_x
        nb_sprites_y = self.number_of_sprite_x

        if mov == "RIGHT":
            if pos % nb_sprites_x == 0 or mapjson_select[pos] == "W":
                return False
            else:
                self.map[self.position_in_sprites-1] = "N"
                self.map[self.position_in_sprites] = "M"
                self.position_in_sprites = self.position_in_sprites + 1
        elif mov == "LEFT":
            if pos % nb_sprites_x == 1 or mapjson_select[pos-2] == "W":
                return False
            else:
                self.map[self.position_in_sprites-1] = "N"
                self.map[self.position_in_sprites - 2] = "M"
                self.position_in_sprites = self.position_in_sprites - 1
        elif mov == "UP":
            if pos / 15 - 1 <= 0 or mapjson_select[pos - 16] == "W":
                return False
            else:
                self.map[self.position_in_sprites-1] = "N"
                self.map[self.position_in_sprites - 16] = "M"
                self.position_in_sprites = self.position_in_sprites - 15
        elif mov == "DOWN":
            if pos / 15 + 1 > nb_sprites_y or mapjson_select[pos + 14] == "W":
                return False
            else:
                self.map[self.position_in_sprites-1] = "N"
                self.map[self.position_in_sprites + 14] = "M"
                self.position_in_sprites = self.position_in_sprites + 15
        return True


class ObjetInMap:
    def __init__(self, position_in_sprites):
        self.number_of_sprite_x = NUMBER_OF_SPRITEX
        self.number_of_sprite_y = NUMBER_OF_SPRITEY
        self.max_sprites = self.number_of_sprite_x * self.number_of_sprite_y
        assert 1 <= position_in_sprites <= self.max_sprites
        self.position_in_sprites = position_in_sprites
        self.map = []
        self.position_x = 0
        self.position_y = 0
        self.object_description = ""
        self.objet_caractere = ""

    @property
    def GetPositionInSprites(self):
        """ Get Position In Sprites"""
        return self.position_in_sprites

    def SetPositionRandom(self, map_select):
        Nb_N_In_Mapcount = int(map_select.count('N'))
        seed(time()+self.position_in_sprites)
        number_rnd = randint(4, Nb_N_In_Mapcount)
        print(number_rnd)
        assert 1 <= number_rnd <= self.max_sprites
        nb_n_in_map = 0

        for i in range(0, len(map_select) - 1):
            if map_select[i] == "N":
                nb_n_in_map += 1
            if nb_n_in_map == number_rnd:
                map_select[i] = self.objet_caractere
                break
        return map_select
