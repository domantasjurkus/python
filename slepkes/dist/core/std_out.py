from colours import *
import time
from font import get_font_names, get_font, Font_Sprite, Shadowed_Font_Sprite

VER = 1.0

###############################################################################
#                                                                             #
#              --- RECENT CHANGES ---                                         #
#                                                                             #
#                                                                             #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#              --- TO DOs ---                                                 #
#                                                                             #
#                                                                             #
#                                                                             #
###############################################################################

class Std_Out():

    def __init__(self, buf, font=None, colour=WEISS, shadow_colour=SCHWARZ, topleft=None):

        self.buffer = buf

        if not font:
            fontname = get_font_names()[0]
            self.font = get_font(fontname, 10)
        else:
            self.font = font

        self.font_colour = colour
        self.bg_colour = shadow_colour

        if not topleft:
            blit_x = 10
            blit_y = self.buffer.get_height() - 15
        else:
            blit_x, blit_y = topleft[0], topleft[1]

        self.message_blitpos = (blit_x, blit_y)

    def say(self, message):

        message_sprite = Shadowed_Font_Sprite(self.font, message, self.font_colour, self.bg_colour)
        self.buffer.blit(message_sprite.bild, self.message_blitpos)

    def tell_time(self):

        text = time.asctime( time.localtime(time.time()) )
        self.say(text)
