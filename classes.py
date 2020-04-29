# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 27 avr 2020
@author: anthony thillerot
"""


class MacGyverClass:
    def __init__(self, position_in_sprites):
        self.position_x = 0
        self.position_y = 0
        self.number_of_sprite_x = 15
        self.number_of_sprite_y = 15
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

    def PosibleMove(self, mov, mapjson_select):
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
