from zufall import index_x

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

def get_xy_distance(pos_a, pos_b):
    """returns the x- and y distance between pos_a and pos_b as tuple"""

    x_dist, y_dist = pos_a[0] - pos_b[0], pos_a[1] - pos_b[1]

    return (abs(x_dist), abs(y_dist))

def get_distance(pos_a, pos_b):
    """returns the distance (float) between pos_a and pos_b"""

    x_dist, y_dist = get_xy_distance(pos_a, pos_b)

    distance = (x_dist ** 2 + y_dist ** 2) ** 0.5

    return distance

def approach(pos_a, pos_b, speed):
    """laesst pos_a sich mit der Geschw. speed pos_b annaehern und gibt die neue Position von pos_a zurueck"""

    dist = get_distance(pos_a, pos_b)

    if int(round(dist - speed)) <= 0:
        return pos_b

    # (else:)

    ### abfangen, ob das Ziel unter- / oberhalb resp. links / rechts vom Startpunkt ist ###

    if pos_b[0] - pos_a[0] < 0:
        x_richtung = "negativ" # pos_b ist links von pos_a aus gesehen
    else:
        x_richtung = "positiv" # pos_b ist rechts von pos_a aus gesehen (ODER es gibt keine x-Differenz!)

    if pos_b[1] - pos_a[1] < 0:
        y_richtung = "negativ" # pos_b ist oberhalb von pos_a
    else:
        y_richtung = "positiv" # pos_b ist unterhalb von pos_a (ODER es gibt keine x-Differenz!)

    ### die neue Position von pos_a wird ausgerechnet ###

    if pos_a[0] == pos_b[0]: # wenn genau uebereinander:
        if y_richtung == "negativ":
            pos_a_neu = (pos_a[0], pos_a[1] - speed)
        else:
            pos_a_neu = (pos_a[0], pos_a[1] + speed)
            
        return pos_a_neu

    if pos_a[1] == pos_b[1]: # wenn genau nebeneinander:
        if x_richtung == "negativ":
            pos_a_neu = (pos_a[0] - speed, pos_a[1])
        else:
            pos_a_neu = (pos_a[0] + speed, pos_a[1])
            
        return pos_a_neu

    # wenn nicht genau ueber- / unter- oder nebeneinander
    # wird zuerst das Verhaeltnis von der x- zur y-Distanz ausgerechnet:

    x_dist, y_dist = get_xy_distance(pos_a, pos_b)
    
    dist_hoch2, x_dist_hoch2, y_dist_hoch2 = dist * dist, x_dist * x_dist, y_dist * y_dist

    x_anteil = 1.0 / dist_hoch2 * x_dist_hoch2
    y_anteil = 1.0 / dist_hoch2 * y_dist_hoch2

    dist_neu = dist - speed
    dist_hoch2_neu = dist_neu * dist_neu

    x_dist_hoch2_neu = dist_hoch2_neu * x_anteil
    y_dist_hoch2_neu = dist_hoch2_neu * y_anteil

    x_dist_neu = x_dist_hoch2_neu ** 0.5
    y_dist_neu = y_dist_hoch2_neu ** 0.5

    x_abweichung = x_dist - x_dist_neu
    y_abweichung = y_dist - y_dist_neu

    if x_richtung == "negativ":
        x_abweichung *= -1
    if y_richtung == "negativ":
        y_abweichung *= -1

    pos_a_neu = (pos_a[0] + x_abweichung, pos_a[1] + y_abweichung)

    return pos_a_neu

def get_direction(pos_a, pos_b):
    """gibt die Richtung (2, 4, 6, 8) zurueck, in welcher pos_b liegt von pos_a aus gesehen"""

    x_diff, y_diff = pos_b[0] - pos_a[0], pos_b[1] - pos_a[1]
    if x_diff < 0:
        x_diff *= -1
    if y_diff < 0:
        y_diff *= -1

    #----------------------------------------------------------------------------------------------------#

    if round(pos_a[0]) == round(pos_b[0]) and round(pos_a[1]) == round(pos_b[1]): # wenn beide Pos gleich:
        return (2, 4, 6, 8)[index_x((2, 4, 6, 8))]

    #----------------------------------------------------------------------------------------------------#

    if round(pos_b[0]) == round(pos_a[0]): # wenn genau uebereinander:
        if pos_b[1] > pos_a[1]:
            direction = 2
        else:
            direction = 8
            
        return direction
    
    elif round(pos_b[1]) == round(pos_a[1]): # wenn genau nebeneinander:
        if pos_b[0] > pos_a[0]:
            direction = 6
        else:
            direction = 4

        return direction

    #----------------------------------------------------------------------------------------------------#
        
    if pos_b[0] > pos_a[0] and pos_b[1] > pos_a[1]: # SEKTOR 3
        if x_diff >= y_diff:
            direction = 6
        else:
            direction = 2
            
    elif pos_b[0] < pos_a[0] and pos_b[1] > pos_a[1]: # SEKTOR 1
        if x_diff >= y_diff:
            direction = 4
        else:
            direction = 2
        
    elif pos_b[0] < pos_a[0] and pos_b[1] < pos_a[1]: # SEKTOR 7
        if x_diff >= y_diff:
            direction = 4
        else:
            direction = 8
            
    elif pos_b[0] > pos_a[0] and pos_b[1] < pos_a[1]: # SEKTOR 9
        if x_diff >= y_diff:
            direction = 6
        else:
            direction = 8

    return direction

def in_range(pos_a, pos_b, radius):
    """Gibt True zurueck, wenn sich pos_b innerhalb des radius von pos_a befindet"""

    dist = get_distance(pos_a, pos_b)

    if dist <= radius:
        return True
    else:
        return False

def pos_in_rect(pos, rect):
    """Gibt True zurueck, wenn sich pos innerhalb rect befindet"""

    is_inside = (pos[0] >= rect.left and
                 pos[0] < rect.right and
                 pos[1] >= rect.top and
                 pos[1] < rect.bottom)

    return is_inside

def rect_collision(game_obj_a, game_obj_b):

    """gibt True zurueck, wenn game_obj_a und game_obj_b sich irgendwo ueberschneiden"""

    objects = (game_obj_a, game_obj_b)

    for obj in objects:

        if obj == game_obj_a:
            obj_1 = game_obj_a
            obj_2 = game_obj_b
        else:
            obj_1 = game_obj_b
            obj_2 = game_obj_a

        ####### midpos - Kollisionsabfrage ##########

        for midpos in obj_1.midpos:
            if pos_in_rect(midpos, obj_2.blitpos, obj_2.width, obj_2.height):
                return True

        #############################################

        x_range = range(round(obj_2.blit_x + 1), round(obj_2.blit_x + obj_2.width))
        y_range = range(round(obj_2.blit_y + 1), round(obj_2.blit_y + obj_2.height))

        for pos in obj_1.cornerpos[:]:
            pos = (round(pos[0]), round(pos[1]))

            if pos[0] in x_range and pos[1] in y_range:
                return True
    
