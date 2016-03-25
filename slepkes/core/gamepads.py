import pygame

VER = 1.01

###############################################################################
#                                                                             #
#              --- RECENT CHANGES ---                                         #
#                                                                             #
# 11.05.2013 - get_ready() Method can be called on Button instance            #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#              --- TO DOs ---                                                 #
#                                                                             #
#                                                                             #
#                                                                             #
###############################################################################

ordner = ("Icons")

buttons = {

    "left_stick" : {
        "nr" : 10,
        "blitpos" : (32, 60)},

    "right_stick" : {
        "nr" : 11,
        "blitpos" : (72, 60)},
    
    "digital_8" : {
        "nr" : None,
        "blitpos" : (22, 22)},
    
    "digital_6" : {
        "nr" : None,
        "blitpos" : (30, 32)},
    
    "digital_2" : {
        "nr" : None,
        "blitpos" : (22, 40)},
    
    "digital_4" : {
        "nr" : None,
        "blitpos" : (12, 32)},

    "L1" : {
        "blitpos" : (18, 8),
        "nr" : 4},
    
    "L2" : {
        "blitpos" : (18, 0),
        "nr" : 6},
    
    "R1" : {
        "blitpos" : (80, 8),
        "nr" : 5},
    
    "R2" : {
        "blitpos" : (80, 0),
        "nr" : 7},
    
    "button_8" : {
        "blitpos" : (88, 18),
        "nr" : 3},
    
    "button_6" : {
        "blitpos" : (100, 30),
        "nr" : 2},
    
    "button_2" : {
        "blitpos" : (88, 42),
        "nr" : 1},
    
    "button_4" : {
        "blitpos" : (76, 30),
        "nr" : 0},

    "start" : {
        "blitpos" : (64, 44),
        "nr" : 9},
    
    "select" : {

        "blitpos" : (46, 44),
        "nr" : 8}}

def get_gamepad_ids():
    """returns list with the IDs of all pads connected"""

    pad_ids = []

    nr_of_pads = pygame.joystick.get_count()

    for nr in range(0, nr_of_pads):
        pad_ids.append(nr)

    return pad_ids

def get_gamepads():
    """returns a list containing all connected gamepad objects"""

    gamepads_connected = []

    gamepad_ids = get_gamepad_ids()
    
    nr_of_pads = len(gamepad_ids)

    for nr in gamepad_ids:
        pad = Gamepad(nr)
        gamepads_connected.append(pad)

    return gamepads_connected

class Button():

    def __init__(self, button_type):

        self.type = button_type

        self.pressed = False
        self.ready = True

        self.blitpos = buttons[button_type]["blitpos"]
        self.nr = buttons[button_type]["nr"]

    def get_ready(self):

        if not self.pressed:
            self.ready = True

class Stick():

    def __init__(self, nr):

        self.nr = nr

        if self.nr == 1:
            self.type = "left_stick"
        elif self.nr == 2:
            self.type = "right_stick"

        self.button_nr = buttons[self.type]["nr"]

        self.x = 0
        self.y = 0
        self.pos = (self.x, self.y)
        self.null_blitpos = buttons[self.type]["blitpos"]
        self.blit_x = self.null_blitpos[0]
        self.blit_y = self.null_blitpos[1]
        self.blitpos = (self.blit_x, self.blit_y)

        self.pressed = False

class Gamepad():

    def __init__(self, id_nr):

        self.input = pygame.joystick.Joystick(id_nr)
        
        self.id = self.input.get_id()
        self.name = self.input.get_name()

        self.input.init()

        self.anzahl_sticks = self.input.get_numaxes() / 2
        self.anzahl_buttons = self.input.get_numbuttons()
        self.anzahl_numhats = self.input.get_numhats()

        self.buttons = {}
        for button_type in buttons.keys():
            if not button_type in ("left_stick", "right_stick"):
                self.buttons[button_type] = Button(button_type)

        self.sticks = {}
        for nr in range(1, self.anzahl_sticks + 1):
            if nr == 1:
                self.sticks["left_stick"] = Stick(nr)
            elif nr == 2:
                self.sticks["right_stick"] = Stick(nr)

        self.digital_pos = [0, 0]

    def get_ready(self, button_or_list):

        if type(button_or_list) == str:
            button_type = button_or_list
            button = self.buttons[button_type]

        elif str(type(button_or_list)) == "<type 'instance'>":
            button = button_or_list

        else:
            for button_type in button_or_list:
                button = self.buttons[button_type]
                if not button.pressed:
                    button.ready = True
            return

        if not button.pressed:
            button.ready = True
                
    def check_input(self):

        #---------------------------- Button Input -----------------------------------#

        for button_type in self.buttons.keys():
            button = self.buttons[button_type]
            if button.nr != None:
                if self.input.get_button(button.nr):
                    button.pressed = True
                else:
                    button.pressed = False

        #------------------------- Digital Pad Input ---------------------------------#

        self.digital_pos = self.input.get_hat(0)
        
        self.digital_x = self.digital_pos[0]
        self.digital_y = self.digital_pos[1]

        #---------------------------- Stick Input ------------------------------------#

        for stick_type in ("left_stick", "right_stick"):
            stick = self.sticks[stick_type]
 
            if self.input.get_button(stick.button_nr):
                stick.pressed = True
            else:
                stick.pressed = False
                
            if stick_type == "left_stick":
                stick.x = self.input.get_axis(0)
                stick.y = self.input.get_axis(1)
                stick.pos = (stick.x, stick.y)

            elif stick_type == "right_stick":
                stick.x = self.input.get_axis(2)
                stick.y = self.input.get_axis(3)
                stick.pos = (stick.x, stick.y)
