import random

VER = 1.0

###############################################################################
#                                                                             #
#              --- RECENT CHANGES ---                                         #
#                                                                             #
# 24.02.2013 - changed colour_x() Logic: keywords = gamma_min, gamma_max      #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#              --- TO DOs ---                                                 #
#                                                                             #
#                                                                             #
#                                                                             #
###############################################################################

def colour_x(gamma_min=0, gamma_max=255):
    
    any_rgb_1 = random.randint(gamma_min, gamma_max)
    if random.randint(0, 1):
        any_rgb_2 = random.randint(gamma_min, gamma_max)
        any_rgb_3 = 0
    else:
        any_rgb_2 = any_rgb_3 = 0
    colour = [any_rgb_1, any_rgb_2, any_rgb_3]
    random.shuffle(colour)
        
    return colour

WEISS = WHITE = (255, 255, 255)
SCHWARZ = BLACK = (0, 0, 0)
ROT = RED = (255, 0, 0)
GRUEN = GREEN = (0, 255, 0)
GELB = YELLOW = (255, 255, 0)
BLAU = BLUE = (0, 0, 255)
PINK = (255, 0, 255)
GRAU = GREY = (127, 127, 127)
ORANGE = (255, 128, 0)

TRANSPARENT = (0, 0, 0, 0)
HALBTRANSPARENT = (0, 0, 0, 128)

DUNKELBLAU = DARK_BLUE = (0, 0, 128)
DUNKELGRUEN = DARK_GREEN = (0, 128, 0)
DUNKELGRAU = DARK_GREY = (70, 70, 70)
DUNKELROT = DARK_RED = (128, 0, 0)

HELLGRAU = BRIGHT_GREY = (200, 200, 200)
HELLBLAU = BRIGHT_BLUE = (0, 200, 255)

LEUCHTSTIFT_PINK = (255, 0, 255, 128)
LEUCHTSTIFT_GRUEN = (0, 255, 0, 128)
LEUCHTSTIFT_BLAU = (0, 255, 255, 128)
LEUCHTSTIFT_GELB = (255, 255, 0, 128)
LEUCHTSTIFT_ROT = (255, 0, 0, 128)
