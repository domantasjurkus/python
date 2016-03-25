import os
import sys
# import pickle
# import random

PLATFORM = sys.platform
if PLATFORM == "win32": # running on Windows
    pass
elif PLATFORM == "darwin": # running on Mac OS
    pass

GAME_PATH = os.getcwd()
# include Game Core (core Folder):
CORE_PATH = os.path.join(GAME_PATH, "core")
sys.path.append(CORE_PATH)

SPRITES_PATH = os.path.join(GAME_PATH, "sprites")

# from colours import *
from font import *
# from sounds import *
from graphics import *
from collision import *
from my_math import my_cos as cos
from my_math import my_sin as sin
from my_math import get_angle, reverse_angle

from mouse import Mouse, WHEEL_UP, WHEEL_DOWN, LEFT_BUTTON, RIGHT_BUTTON, MID_BUTTON
from keyboard import Keyboard
import gamepads

RES = (1200, 800)
WIDTH = 1200
HEIGHT = 800
RES_REAL = (WIDTH, HEIGHT)
SCREEN_CENTER = (RES[0] / 2, RES[1] / 2)

TICK = 10

ON = True
OFF = False
RANDOM = "random"
STD = "std"

RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"

CARDSIZE = (160, 230)

HEARTS = "h"
CLUBS = "c"
SPADES = "s"
DIAMONDS = "d"

SUITS = (CLUBS, HEARTS, SPADES, DIAMONDS)
VALUES = range(1, 14)

# VALUE CONSTANTS

ACE = 1
KING = 13
QUEEN = 12
JACK = 11

#####################################
#                                   #
#          Font Constants           #
#                                   #
#####################################

FONTNAME = "verdana"

'''
FONT_7 = get_font(FONTNAME, 7)
FONT_8 = get_font(FONTNAME, 8)
FONT_9 = get_font(FONTNAME, 9)
FONT_10 = get_font(FONTNAME, 10)
FONT_11 = get_font(FONTNAME, 11)
FONT_12 = get_font(FONTNAME, 12)
FONT_13 = get_font(FONTNAME, 13)
FONT_14 = get_font(FONTNAME, 14)
FONT_15 = get_font(FONTNAME, 15)
FONT_16 = get_font(FONTNAME, 16)
FONT_18 = get_font(FONTNAME, 18)
FONT_20 = get_font(FONTNAME, 20)
FONT_30 = get_font(FONTNAME, 30)
FONT_40 = get_font(FONTNAME, 40)
'''


# SLP part
SLP_CARD_PATH = os.path.join(GAME_PATH, "cards")
SLP_CARD_NUMBER = 103