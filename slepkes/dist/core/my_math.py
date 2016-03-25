from math import cos, sin, acos, asin, degrees, radians

VER = 1.11

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


def my_cos(winkel):

    bogenmass = radians(winkel)
    return round(cos(bogenmass), 3)

def my_sin(winkel):

    bogenmass = radians(winkel)
    return round(sin(bogenmass), 3)

def my_acos(x):

    return round(degrees(acos(x)), 3)

def my_asin(y):

    return round(degrees(asin(y)), 3)

def get_angle(a):
    """Berechnet den Winkel a (Einheitskreis), wenn [n] >= 360 oder < 0 ist
und gibt diesen zurueck. Sonst wird n zurueckgegeben"""

    while a >= 360:
        a -= 360
    while a < 0:
        a += 360
    return a

def reverse_angle(a):
    """Gibt den um 180 Grad gedrehten Winkel u von [a] zurueck"""

    a -= 180
    return get_angle(a)

def get_180_winkel(a):
    """Gibt den Umkehrwinkel von a zurueck, wenn a groesser 180 ist.
Wenn nicht wird a selbst zurueckgegeben"""

    if a > 180:
        return get_umkehrwinkel(a)
    else:
        return a

def get_spiegelwinkel(a):
    """gibt den an der x-Achse gespiegelten winkel von a zurueck, wenn a > 180"""

    if a > 180:
        return abs(a - 360)
    return a

def get_winkeldiff(w1, w2):
    """Gibt die Differenz in Grad aus zwischen Winkel1 und Winkel2"""

    x = get_winkel(w1 - w2)
    if x > 180:
        x = 360 - x
    return x

