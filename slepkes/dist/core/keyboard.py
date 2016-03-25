import pygame
from pygame.constants import *

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

COMBO_KEYS = (K_RSHIFT, K_LSHIFT, K_RCTRL, K_LCTRL, K_RALT, K_LALT)

class Keyboard():

    def __init__(self):

        self.ready = True
        self.pressed = []

    def get_ready(self):

        if not len(self.pressed):
            self.ready = True
            return

        """else:
            for key in self.pressed:
                if not key in COMBO_KEYS:
                    return"""

    def key_update(self, events):

        for event in events:
            key = event.key
            if event.type == KEYDOWN:
                if not key in self.pressed:
                    self.pressed.append(key)
            elif event.type == KEYUP:
                if key in self.pressed:
                    self.pressed.remove(key)

    def update(self, events):

        self.key_update(events)
        self.get_ready()
