from constants import *

class Card(My_Sprite):

    def __init__(self, name):
        self.name = name

        self.image = load_image(SLP_CARD_PATH, str(name) + ".png", True)
        self.cover_image = load_image(SPRITES_PATH, "cover1.png", True)
        My_Sprite.__init__(self, self.cover_image)

        self.covered = True
        self.x_speed = 0.0
        self.y_speed = 0.0
        self.x = self.y = 0.0
        self.jump_speed_max = 0.0

    def cover(self):
        self.covered = True
        self.bild = self.cover_image

    def uncover(self):
        self.covered = False
        self.bild = self.image

    def gravity_update(self):
        self.y_speed += 0.03

    def move(self):
        self.gravity_update()
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.center = (self.x, self.y)
