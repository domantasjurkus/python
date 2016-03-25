import pygame
import sys, os

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


def load_sound(path, filename):

    full_filename = os.path.join(path, filename)
    sound = pygame.mixer.Sound(full_filename)
    return sound

def play_music(path, filename, loops=0):

    full_filename = os.path.join(path, filename)
    pygame.mixer.music.stop()
    pygame.mixer.music.load(full_filename)
    pygame.mixer.music.play(loops)

def pause_music():

    pygame.mixer.music.pause()

def resume_music():

    pygame.mixer.music.unpause()

def stop_music():

    pygame.mixer.music.stop()

    

    
