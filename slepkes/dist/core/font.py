import pygame
from pygame.locals import *

from colours import *
from sprite import My_Sprite

VER = 1.10

###############################################################################
#                                                                             #
#              --- RECENT CHANGES ---                                         #
#                                                                             #
# 24.02.2013 - farbe -> colour                                                #
# 25.03.2013 - included kw arg shadow_diffs for Shadowed Font Sprites         #
# 05.09.2013 - Message_Window class added                                     #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#              --- TO DOs ---                                                 #
#                                                                             #
# - Framed Font Sprite Class                                                  #
#                                                                             #
###############################################################################

def get_font_names():

    all_font_names = pygame.font.get_fonts()

    return all_font_names

def get_font(font_name, font_size, bold=False):
    """seeks for font_name and returns font object"""

    full_font_name = pygame.font.match_font(font_name)
    font = pygame.font.Font(full_font_name, font_size)

    if bold:
        font.set_bold(True)

    return font

def get_std_font(font_size=12):

    fontname = pygame.font.get_default_font()
    full_font_name = pygame.font.match_font(fontname)
    font = pygame.font.Font(full_font_name, font_size)

    return font

class Font_Sprite(My_Sprite):
    """Basic Font Sprite Class"""

    def __init__(self, font, text, a_alias=False, colour=WEISS, centerpos=(0, 0)):

        self.bild = font.render(text, a_alias, colour, TRANSPARENT)
        self.bild.set_colorkey((0, 0, 0))

        My_Sprite.__init__(self, self.bild, centerpos)

class Shadowed_Font_Sprite(My_Sprite):
    """Shadowed Font Sprite Class"""

    def __init__(self, font, text, colour=WEISS, shadow_colour=SCHWARZ, centerpos=(0, 0), a_alias=False,
                 bold=False, shadow_diffs=None):

        f = font

        if bold:
            if not f.get_bold():
                f.set_bold(True)
        else:
            if f.get_bold():
                f.set_bold(False)

        shadow_font_sprite = Font_Sprite(f, text, a_alias, shadow_colour)
        font_sprite = Font_Sprite(f, text, a_alias, colour)

        if not shadow_diffs:
            x_diff = y_diff = round(font.get_height() / 13.0)
            if x_diff < 1:
                x_diff = 0
            if y_diff < 1:
                y_diff = 1
        else:
            x_diff, y_diff = shadow_diffs[0], shadow_diffs[1]

        cut_y = font.get_height() / 12.0 # das Font_Sprite ist zu gross (height)

        w = font_sprite.rect.width + 2
        h = font_sprite.rect.height - cut_y

        surf = pygame.Surface((w, h))
        surf = surf.convert_alpha()
        surf.fill(TRANSPARENT)

        surf.blit(shadow_font_sprite.bild, (x_diff, y_diff))
        surf.blit(font_sprite.bild, (0, 0))

        My_Sprite.__init__(self, surf, centerpos)

class Message_Window(My_Sprite):

    def __init__(self, font, width, text,
                 text_colour=WHITE, bg_colour=BLACK, frame_colour=WHITE, frame_thickness=2):

        self.font = font
        self.width = width
        self.text = text

        self._init_words()

    def _init_words_(self):

        self.words = []
        word = ""

        for s in self.text:
            if s in (" ", "\n"):
                self.words.append(word)
                word = ""
            else:
                word += s

        print self.words

    def _count_lines_(self):

        pass
