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

class My_Sprite():

    def __init__(self, bild, centerpos=(0, 0)):

        self.bild = bild
        self.rect = bild.get_rect()
        self.rect.center = centerpos

    def set_bild(self, bild):

        self.bild = bild
        centerpos = self.rect.center
        self.rect = self.bild.get_rect()
        self.rect.center = centerpos

    def pos_in_rect(self, pos, rect):

        if pos[0] > rect.left and pos[0] < rect.right:
            if pos[1] > rect.top and pos[1] < rect.bottom:
                return True

    def front_collision(self, sprite_object):
        """Gibt True zurueck, wenn eine der pos in self.collision_checkpos
        innerhalb von sprite_object.rect liegt"""

        for pos in self.collision_checkpos:
            if self.pos_in_rect(pos, sprite_object.rect):
                return True

    def rect_collision(self, sprite_object):

        x_dist = abs(self.rect.centerx - sprite_object.rect.centerx)
        y_dist = abs(self.rect.centery - sprite_object.rect.centery)

        x_dist -= (self.rect.width / 2.0 + sprite_object.rect.width / 2.0)
        y_dist -= (self.rect.height / 2.0 + sprite_object.rect.height / 2.0)

        if x_dist < 0 and y_dist < 0:
            return True
        else:
            return False

class Game_Object(My_Sprite):

    def __init__(self, image_or_imagelist):

        self.blit_me = True

        images = image_or_imagelist

        try:
            bild = images[0]
            self.images = images
            self.a_counter = 0
            self.i_index = 0
            self.i_index_max = len(images) - 1
        except:
            bild = images
            self.a_counter = None
            self.i_index = None
            self.i_index_max = None

        My_Sprite.__init__(self, bild)

    def x_movement(self):

        self.x += self.x_speed
        self.rect.centerx = self.x

    def jump(self):

        if abs(self.y_speed) < abs(self.y_speed_min):
            self.y_speed *= -1
            return
        if self.air > self.air_max:
            self.y_speed *= self.y_speed_factor

        self.y += self.y_speed
        self.air -= self.y_speed

        pos_new = (round(self.x), round(self.y))
        self.rect.center = pos_new

    def fall(self):

        if self.y_speed == 0:
            self.y_speed = self.y_speed_min

        else:
            if self.y_speed < self.fall_speed_max:
                self.y_speed /= self.y_speed_factor 
            if self.y_speed > self.fall_speed_max:
                self.y_speed = self.fall_speed_max

        self.y += self.y_speed

        pos_new = (round(self.x), round(self.y))
        self.rect.center = pos_new

    def bild_update(self):

        self.a_counter += 1
        if self.a_counter >= self.a_trigger:
            self.a_counter = 0
            self.i_index += 1
            if self.i_index > self.i_index_max:
                self.i_index = 0
            self.bild = self.images[self.i_index]
                
