import pygame

from sprite import My_Sprite
from graphics import load_image

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

WHEEL_UP = 4
WHEEL_DOWN = 5

LEFT_BUTTON = 1
RIGHT_BUTTON = 3
MID_BUTTON = 2

class Mouse(My_Sprite):

    def __init__(self, screen_res, buffersize=None, cursor_image=None):

        pos = pygame.mouse.get_pos()

        self.buffersize = buffersize
        self.res = screen_res

        if not self.buffersize:
            self.pos = pos
        else:
            x = pos[0] / round(self.res[0]) * self.buffersize[0]
            y = pos[1] / round(self.res[1]) * self.buffersize[1]
            self.pos = (x, y)
        
        self.pressed = []
        self.ready = True

        if cursor_image:
            My_Sprite.__init__(self, cursor_image)
            self.rect.topleft = self.pos
        else:
            self.rect = pygame.rect.Rect(10, 10, 10, 10)
            self.rect.topleft = self.pos

        self.all_buttons = (1, 2, 3, 4, 5)

    def get_ready(self):

        if not len(self.pressed):
            self.ready = True

    def pos_update(self):

        pos = pygame.mouse.get_pos()

        if not self.buffersize:
            self.pos = pos
        else:
            x = pos[0] / round(self.res[0]) * self.buffersize[0]
            y = pos[1] / round(self.res[1]) * self.buffersize[1]
            self.pos = (int(round(x)), int(round(y)))
            self.rect.topleft = self.pos

    def button_update(self, events):

        for wheel_button in (4, 5):
            if wheel_button in self.pressed:
                self.pressed.remove(wheel_button)

        for event in events:
            
            nr = event.button
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not nr in self.pressed:
                    self.pressed.append(nr)
                    
            elif event.type == pygame.MOUSEBUTTONUP and not event.button in (4, 5):
                if nr in self.pressed[:]:
                    self.pressed.remove(nr)

    def update(self, events):

        self.pos_update()
        self.get_ready()
        self.button_update(events)

        

        

        
