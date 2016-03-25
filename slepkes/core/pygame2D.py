import random
from Box2D import b2World, b2_dynamicBody, b2CircleShape
from colours import colour_x

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

######## SETTING THINGS UP #########

def init(resolution, pixels_per_meter, ):
    _set_PPM(pixels_per_meter)
    _set_RES(resolution)

def init_world(g=(0, -10), sleep=True):
    global world
    world = b2World(gravity=g, doSleep=sleep)
    return world
    
def _set_PPM(pixels_per_meter):
    global PPM
    PPM = pixels_per_meter

def _set_RES(resolution):
    global RES
    RES = resolution

def _set_b2world(world):
    global b2world
    b2world = world

####################################

def get_x(b2x):
    x = int(round(b2x * PPM, 3))
    return x

def get_y(b2y):
    y = RES[1] - b2y * PPM
    return int(round(y, 3))

def get_pos(b2pos):
    pos = (get_x(b2pos[0]), get_y(b2pos[1]))
    return pos

def get_b2x(x):
    return x / PPM

def get_b2y(y):
    return (RES[1] - y) / PPM

def get_b2pos(pos):
    return (get_b2x(pos[0]), get_b2y(pos[1]))

class Static_Box():

    def __init__(self, width, height, centerpos, colour=(0, 0, 0)):

        b2_centerpos = get_b2pos(centerpos)
        b2w, b2h = width / PPM / 2.0, height / PPM / 2.0
        
        self.body = world.CreateStaticBody(position=b2_centerpos)
        self.body.CreatePolygonFixture(box=(b2w, b2h))
        self.colour = colour

class Dynamic_Box():                                    

    def __init__(self, width, height, centerpos, colour=None,
                 dens=1, frict=0.5, rest=0.25):

        b2_centerpos = get_b2pos(centerpos)
        b2w, b2h = width / PPM / 2.0, height / PPM / 2.0
        
        self.body = world.CreateDynamicBody(position=b2_centerpos, angle=random.randint(1, 359))
        self.body.CreatePolygonFixture(box=(b2w, b2h), density=dens, friction=frict, restitution=rest)
        if not colour:
            self.colour = colour_x(gamma_min=150)
        else:
            self.colour = colour

class Dynamic_Ball():

    def __init__(self, radius, centerpos, colour=None,
                 dens=1, frict=0.5, rest=0.25):

        b2_centerpos = get_b2pos(centerpos)
        r = radius / PPM
        self.body = world.CreateDynamicBody(position=b2_centerpos)
        
        circle = b2CircleShape(pos=(0, 0), radius=r)
        ball = self.body.CreateFixture(shape=circle, density=dens, friction=frict, restitution=rest)
        if not colour:
            self.colour = colour_x(gamma_min=150)
        else:
            self.colour = colour
        
