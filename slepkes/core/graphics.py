import os
import sys
import pygame
import colours

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

def load_image(path, name, shadow_bool=False):
    """returns the image (pygame.Surface object) loaded from [path].
if [shadow_bool] is True, the Surface will be converted using perPixel Alpha"""
    
    full_filename = os.path.join(path, name)
    if not shadow_bool:
        image = pygame.image.load(full_filename).convert()
    else:
        image = pygame.image.load(full_filename).convert_alpha()
    return image

def rotate_image(image, angle):
    """returns the given [image], rotated counter-clockwise by [angle] degrees"""

    rotated = pygame.transform.rotate(image, angle)
    return rotated

def flip_image(image, x_bool, y_bool):
    """returns the given [image], flipped horizontally or vertically
depending on [x_bool] and [y_bool]"""
    
    flipped = pygame.transform.flip(image, x_bool, y_bool)
    return flipped
