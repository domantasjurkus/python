from random import *

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


def fifty_fifty(dieses = None, jenes = None):
    """50 / 50 Funktion: Gibt eines der beiden Argumente resp. True oder False zurueck"""
    
    x = randint(0, 1)
    if x == 0:
        if dieses != None:
            return dieses
        else:
            return True
    elif x == 1:
        if dieses != None:
            return jenes
        else:
            return False

def index_x(objekt):
    """Gibt eine zufaellige Indexzahl (int !) des mitgegebenen Objektes zurueck"""
    
    index_x = randint(0, len(objekt) - 1)
    return index_x
