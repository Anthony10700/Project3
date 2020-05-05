# -*- coding: utf-8 -*-
# ! /usr/bin/env python
"""
Created on 27 avr 2020
@author: anthony thillerot
"""
from random import randint
from random import seed
from time import time
import constant as C


def show_interface(pygame_):
    """

    Parameters
    ----------
    pygame_ : pygame instance
        DESCRIPTION.

    Returns
    -------
    windows : TYPE
        DESCRIPTION : return pygame display set_mode (windows surface)

    """
    pygame_.init()  # initialisation de pygame
    pygame_.display.set_caption('P3')  # set title of windows
    clock = pygame_.time.Clock()  # instance of clock module pygame
    windows = pygame_.display.set_mode((C.NB_PIXEL_X, C.NB_PIXEL_Y))
    # set mumber pixel x and y for windows surface
    pygame_.mixer.music.load(C.PATH_OF_MUSIC)  # load music
    pygame_.mixer.music.play()  # play music
    pygame_.mixer.music.set_volume(0.1)  # set music in mixer at 0.1
    pygame_.mixer.music.play(-1)
    clock.tick(60)  # set 60 refresh per seconde in the loop game
    pygame_.display.flip()  # Update surface on the screen
    return windows


def create_lvl_randomly_easy():
    """
    EXEMPLE MAP
    "M","N","N","N","W","W","W","W","W","W","W","W","W","W","W",
    "W","N","W","N","W","W","W","W","W","W","W","W","W","W","W",
    "W","N","W","N","N","N","N","W","W","W","W","W","W","W","W",
    "W","N","W","N","W","W","N","W","W","W","W","W","W","W","W",
    "W","N","N","N","N","N","W","N","W","W","W","W","N","N","N",
    "W","N","W","W","W","W","W","N","N","N","N","N","N","W","N",
    "W","N","W","W","W","W","W","W","W","W","W","W","W","W","N",
    "N","N","N","N","N","N","N","N","N","N","W","W","W","W","N",
    "N","W","W","W","W","W","W","W","W","N","W","W","W","W","N",
    "N","W","W","W","W","N","N","N","N","N","N","N","N","N","N",
    "N","N","N","N","N","N","W","W","W","N","W","W","W","W","W",
    "W","N","N","W","W","W","W","W","W","N","N","N","N","N","W",
    "N","N","W","W","W","W","W","W","W","W","W","W","W","N","W",
    "W","W","W","W","W","W","W","W","W","W","W","W","W","N","W",
    "W","W","W","W","W","W","W","W","W","W","W","W","W","N","G"
    Returns
    -------
    map_create : TYPE
        DESCRIPTION.

    """
    map_create = [""]*C.NB_MAX_SPRITE
    map_create[0] = ('M')  # Macgyver on first sprite
    seed(time()+7)
    for i in range(1, 4):
        map_create[i] = ('N')

    past_v = 3
    v = 3
    while v <= C.NB_MAX_SPRITE - 2:  # create random path to Guardian
        nbr_rnd = randint(1, 4)
        past_v = v
        if map_create[v] != 'M' and map_create[v] != 'G':

            if nbr_rnd == 1 and v % C.NB_SPRITE_X < (C.NB_SPRITE_X-1):
                if v + 1 < C.NB_MAX_SPRITE:
                    map_create[v+1] = 'N'
                    v = v + 1
            elif nbr_rnd == 3 and v % C.NB_SPRITE_X > 0:
                if v - 1 > 1:
                    map_create[v-1] = 'N'
                    v = v - 1
            # elif v-C.NB_SPRITE_X > 1 and nbr_rnd == 40:
            #     map_create[v-C.NB_SPRITE_X] = 'N'
            #     v = v - C.NB_SPRITE_X
            elif v+C.NB_SPRITE_X < C.NB_MAX_SPRITE and nbr_rnd == 2:
                map_create[v+C.NB_SPRITE_X] = 'N'
                v = v + C.NB_SPRITE_X
            else:
                v = past_v
        else:
            v = v + 1

    for nb_branch in range(5, C.NB_SPRITE_X, 5):
        # create branch random in the path to guardian

        for n in range(nb_branch * C.NB_SPRITE_X, C.NB_MAX_SPRITE, 1):
            if map_create[n] == 'N':
                v = n
                for en in range(0, C.NB_RD_IN_BRANCH):
                    nbr_rnd = randint(1, 4)
                    past_v = v
                    if map_create[v] != 'M' and map_create[v] != 'G':
                        mod_var = v % C.NB_SPRITE_X
                        v_nb_s = v + C.NB_SPRITE_X
                        if nbr_rnd == 1 and mod_var < (C.NB_SPRITE_X-1):
                            if v + 1 < C.NB_MAX_SPRITE:
                                map_create[v+1] = 'N'
                                v = v + 1
                        elif nbr_rnd == 3 and mod_var > 0:
                            if v - 1 > 1:
                                map_create[v-1] = 'N'
                                v = v - 1
                        elif v-C.NB_SPRITE_X > 1 and nbr_rnd == 40:
                            map_create[v-C.NB_SPRITE_X] = 'N'
                            v = v - C.NB_SPRITE_X
                        elif v_nb_s < C.NB_MAX_SPRITE and nbr_rnd == 2:
                            map_create[v_nb_s] = 'N'
                            v = v_nb_s
                        else:
                            v = past_v
                    else:
                        v = v + 1
                break

    for a in range(0, C.NB_MAX_SPRITE-1):  # set all wall in the nothink value
        if map_create[a] == '':
            map_create[a] = ('W')

    map_create[C.NB_MAX_SPRITE-1] = ('G')  # Guardian on last sprite
    return map_create


def endofgame(map_select):
    """
    Parameters
    ----------
    map_select : LIST
        Map is the list of element in the windows pygame,
        M = Macggyver , W = Wall , G = Guardian , N = Nothink or path
        X = CHAR_OF_NEEDLE , E= CHAR_OF_ETHER , P= PATH_OF_SYRINGE ,
        one items = one sprites

    Returns
    -------
    int
        return if the game is over (2), is win (1) or not (0)

    """

    nb_obj = (map_select.count(C.CHAR_OF_NEEDLE) +
              map_select.count(C.CHAR_OF_ETHER) +
              map_select.count(C.CHAR_OF_PLASTIC_TUBE))
    # addition number of object in list map

    if 'G' not in map_select and nb_obj == 0:
        return 1
    elif 'G' not in map_select and nb_obj > 0:
        return 2
    return 0


def show_msg(iwindows, msg, ipygame):
    """
    Parameters
    ----------
    iwindows : TYPE = pygame.display.set_mode
        DESCRIPTION.
    msg : TYPE = string
        replace with the message you want to display.
    ipygame : TYPE = pygame
        the pygame import.

    Returns
    -------
    perform the actions but return nothing.
    """
    iwindows.fill(C.WHITE)  # color all windows surface in WHITE
    font = ipygame.font.SysFont('arial', 40)  # set special font
    text = font.render((msg), True, C.WHITE, C.BLACK)  # set msg
    iwindows.blit(text, (C.NB_PIXEL_X/3, C.NB_PIXEL_Y/3))
    # show msg on specific coordinate


def show_map(iwindows, mymap, ipygame, nb_win_game):
    """
    Show map , map represent list of sprites with contain elements
    Parameters
    ----------
    iwindows : TYPE = pygame.display.set_mode
        DESCRIPTION.
    mymap : LIST
        Map is the list of element in the windows pygame,
        M = Macggyver , W = Wall , G = Guardian , N = Nothink or path
        X = CHAR_OF_NEEDLE , E= CHAR_OF_ETHER , P= CHAR_OF_SYRINGE ,
        one items = one sprites
    ipygame : TYPE = pygame
        the pygame import.

    Returns
    -------
    perform the actions but return nothing.
    """

    nb_obj = (mymap.count(C.CHAR_OF_NEEDLE) + mymap.count(
        C.CHAR_OF_ETHER) + mymap.count(C.CHAR_OF_PLASTIC_TUBE))
    # addition number of object in list map

    sprites = 0
    picture_guardian = ipygame.image.load(C.PATH_OF_GUARDIAN
                                          ).convert_alpha()
    # set picture to guardian obj
    picture_macgyver = ipygame.image.load(C.PATH_OF_MACGYVER
                                          ).convert_alpha()

    picture_wall = ipygame.image.load(C.PATH_OF_WALL).convert_alpha()
    # set picture to wall obj
    picture_path = ipygame.image.load(C.PATH_OF_PATH).convert_alpha()
    # set picture to path obj

    picture_needle = ipygame.image.load(C.PATH_OF_NEEDLE
                                        ).convert_alpha()
    # set picture to needle obj

    picture_ether = ipygame.image.load(C.PATH_OF_ETHER).convert_alpha()
    # set picture to ether obj

    picture_plastic_tube = ipygame.image.load(
        C.PATH_OF_PLASTIC_TUBE).convert_alpha()
    # set picture to plastic_tube obj

    font = ipygame.font.SysFont('arial', 11)  # set special font
    text = font.render((' Number of objects taken: ' + str(3 - nb_obj) + ' / 3'
                        + '            Press : F7 Sound -   OR   F8 Sound + '),
                       True, C.WHITE, C.BLACK)
    iwindows.blit(text, (0, 3))
    # show on specific coordinate

    text_number_lvl = font.render((' Number of level win : ' +
                                   str(nb_win_game)), True, C.WHITE, C.BLACK)
    iwindows.blit(text_number_lvl, (0, 16))
    # show on specific coordinate

    if nb_obj == 0:
        picture_syringe = ipygame.image.load(
            C.PATH_OF_SYRINGE).convert_alpha()
        iwindows.blit(picture_syringe, ((C.NB_SPRITE_X-1)*C.NB_PIX_SPRITE, 0))
        # show syringe if all the objects are pick up
    else:
        if mymap.count(C.CHAR_OF_NEEDLE) == 0:
            picture_needle = ipygame.image.load(
                C.PATH_OF_NEEDLE).convert_alpha()
            iwindows.blit(picture_needle, ((C.NB_SPRITE_X-1) *
                                           C.NB_PIX_SPRITE, 0))
            # display if the object has been picked up
        if mymap.count(C.CHAR_OF_ETHER) == 0:
            picture_ether = ipygame.image.load(
                C.PATH_OF_ETHER).convert_alpha()
            iwindows.blit(picture_ether, ((C.NB_SPRITE_X-2) *
                                          C.NB_PIX_SPRITE, 0))
            # display if the object has been picked up
        if mymap.count(C.CHAR_OF_PLASTIC_TUBE) == 0:
            picture_plastic_tube = ipygame.image.load(
                C.PATH_OF_PLASTIC_TUBE).convert_alpha()
            iwindows.blit(picture_plastic_tube, ((C.NB_SPRITE_X-3) *
                                                 C.NB_PIX_SPRITE, 0))
            # display if the object has been picked up

    for itm in mymap:
        if itm == "M":  # picture_MacGyver
            iwindows.blit(picture_macgyver, (sprites % (C.NB_SPRITE_X) *
                                             C.NB_PIX_SPRITE,
                                             int(sprites/C.NB_SPRITE_Y+1) *
                                             C.NB_PIX_SPRITE))
            # show picture_macgyver on specific coordinate

        elif itm == "W":  # picture_wall
            iwindows.blit(picture_wall, (sprites % C.NB_SPRITE_X *
                                         C.NB_PIX_SPRITE,
                                         int(sprites/C.NB_SPRITE_Y+1) *
                                         C.NB_PIX_SPRITE))
            # show picture_wall on specific coordinate

        elif itm == "G":  # picture_Guardian
            iwindows.blit(picture_guardian, (sprites % C.NB_SPRITE_X *
                                             C.NB_PIX_SPRITE,
                                             int(sprites/C.NB_SPRITE_Y+1) *
                                             C.NB_PIX_SPRITE))
            # show picture_guardian on specific coordinate
        elif itm == "N":  # picture_path
            iwindows.blit(picture_path, (sprites % C.NB_SPRITE_X *
                                         C.NB_PIX_SPRITE,
                                         int(sprites/C.NB_SPRITE_Y+1) *
                                         C.NB_PIX_SPRITE))
            # show picture_path on specific coordinate
        elif itm == C.CHAR_OF_NEEDLE:  # picture_needle
            iwindows.blit(picture_needle, (sprites % C.NB_SPRITE_X *
                                           C.NB_PIX_SPRITE,
                                           int(sprites/C.NB_SPRITE_Y+1) *
                                           C.NB_PIX_SPRITE))
            # show picture_needle on specific coordinate
        elif itm == C.CHAR_OF_ETHER:  # picture_ether
            iwindows.blit(picture_ether, (sprites % C.NB_SPRITE_X *
                                          C.NB_PIX_SPRITE,
                                          int(sprites/C.NB_SPRITE_Y+1) *
                                          C.NB_PIX_SPRITE))
            # show picture_ether on specific coordinate
        elif itm == C.CHAR_OF_PLASTIC_TUBE:  # picture_plastic_tube
            iwindows.blit(picture_plastic_tube, (sprites % C.NB_SPRITE_X *
                                                 C.NB_PIX_SPRITE,
                                                 int(sprites/C.NB_SPRITE_Y+1) *
                                                 C.NB_PIX_SPRITE))
            # show picture_plastic_tube on specific coordinate
        sprites += 1
