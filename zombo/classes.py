import sys, pygame, random
sys.dont_write_bytecode = True
from globals import *

class BaseClass(pygame.sprite.Sprite):

	def __init__(self, x_pos, y_pos, width, height, image_list):
		# inherit parameters from the pygame class 'Sprite'
		pygame.sprite.Sprite.__init__(self)

		# assign first image
		self.image = image_list[0]
		# position on grid
		self.x_pos = x_pos
		self.y_pos = y_pos
		# set the visible rectangle of the object
		self.rect = self.image.get_rect()
		self.rect.x = x_pos*SQR
		self.rect.y = y_pos*SQR
		self.width = width
		self.height = height

	# method for destroying an object 
	def destroy(self, ClassName):
		ClassName.List.remove(self)
		del self

class Player(BaseClass):
	List = pygame.sprite.Group()

	def __init__(self, x, y, width, height, image_list):
		BaseClass.__init__(self, x, y, width, height, image_list)
		Player.List.add(self)

		# custom parameters
		self.score = 0
		self.dir = 0
		self.image = image_list[0]
		self.tele_count = 0
		self.next_tele_at = 4

	def resetPlayer(self, x, y):
		self.x_pos = x
		self.y_pos = y
		self.rect.x = x*SQR
		self.rect.y = y*SQR
		self.score = 0
		self.dir = 0
		self.tele_count = 0
		self.next_tele_at = 4

	def update(self, dir):
		self.dir = dir
		self.movePlayer(dir)

		# update drawing coordinates
		self.rect.x = self.x_pos*SQR
		self.rect.y = self.y_pos*SQR

		# update image based on direction
		self.image = player_img_list[self.dir]

	def updateTeleport(self):
		# check whether player gets another teleport
		if self.score >= self.next_tele_at:
			self.tele_count += 1
			self.next_tele_at *= 2
			radar_sound.play()

	def movePlayer(self, dir):
		if dir == 0 and self.y_pos > 0 :
			self.y_pos -= 1
		elif dir == 1 and self.x_pos < COLS-1:
			self.x_pos += 1
		elif dir == 2 and self.y_pos < ROWS-1:
			self.y_pos += 1
		elif dir == 3 and self.x_pos > 0:	
			self.x_pos -= 1

	def teleport(self):
		self.tele_count -= 1
		# generate random position

		self.x_pos = random.randint(0, COLS-1)
		self.y_pos = random.randint(0, ROWS-1)

		# if a player spawns too close to a zombie
		# distance between player and zombie
		for z in Zombie.List:
			dist_x = abs(self.x_pos - z.x_pos)
			dist_y = abs(self.y_pos - z.y_pos)
			# regenerate coordinates if too close to zombie
			while dist_x < 3 or dist_y < 3:
				self.x_pos = random.randint(0, COLS-1)
				self.y_pos = random.randint(0, ROWS-1)
				dist_x = abs(self.x_pos - z.x_pos)
				dist_y = abs(self.y_pos - z.y_pos)

		# if a player spawns on top ob an obstacle
		for o in Obstacle.List:
			while self.x_pos==o.x_pos and self.y_pos==o.y_pos:
				self.x_pos = random.randint(0, COLS-1)
				self.y_pos = random.randint(0, ROWS-1)

		# update drawing coordinates
		self.rect.x = self.x_pos*SQR
		self.rect.y = self.y_pos*SQR

		#tele_sound.play()

class Zombie(BaseClass):
	List = pygame.sprite.Group()

	def __init__(self, x, y, width, height, image_list):
		BaseClass.__init__(self, x, y, width, height, image_list)
		Zombie.List.add(self)

		# custom parameters
		self.dir = random.randint(0, 3)
		self.image = zombie_img_list[self.dir]

	def update(self, player):
		self.findDirection(player)
		self.move()

		# set drawing coordinates based of grid coordinates
		self.rect.x = self.x_pos*SQR
		self.rect.y = self.y_pos*SQR

		# update image based on direction
		if self.dir == 0:
			self.image = zombie_img_list[0]
		elif self.dir == 1:
			self.image = zombie_img_list[1]
		elif self.dir == 2:
			self.image = zombie_img_list[2]
		elif self.dir == 3:
			self.image = zombie_img_list[3]
	
	def findDirection(self, player):
		# if player and zombie are on the same vertical line
		if self.x_pos == player.x_pos:
			# if player is top of zombie
			if player.y_pos < self.y_pos:
				self.dir = 0
			# if player is down from zombie
			elif self.y_pos < player.y_pos:
				self.dir = 2
			# if the zombie is on the player
			else:
				self.dir = -1

		# if player and zombie are on the same horizontal line
		if self.y_pos == player.y_pos:
			# if player is left from zombie
			if player.x_pos < self.x_pos:
				self.dir = 3
			# if player is right from zombie
			elif self.x_pos < player.x_pos:
				self.dir = 1
			# if the zombie is on the player
			else:
				self.dir = -1
			
		# if player is on the 1st quadrangle
		elif (self.x_pos < player.x_pos)and(self.y_pos > player.y_pos):
			self.dir = random.randint(0, 1)
		
		# if player is on the 2nd quadrangle
		elif (self.x_pos > player.x_pos)and(self.y_pos > player.y_pos):
			self.dir = random.randint(3, 4)%4
		
		# if player is on the 3rd quadrangle
		elif (self.x_pos > player.x_pos)and(self.y_pos < player.y_pos):
			self.dir = random.randint(2, 3)
		
		# if player is on the 4th quadrangle
		elif (self.x_pos < player.x_pos)and(self.y_pos < player.y_pos):
			self.dir = random.randint(1, 2)
		
	def move(self):
		if self.dir == 0:
			self.y_pos -= 1
		elif self.dir == 1:
			self.x_pos += 1
		elif self.dir == 2:
			self.y_pos += 1
		elif self.dir == 3:
			self.x_pos -= 1

class Obstacle(BaseClass):
	List = pygame.sprite.Group()

	def __init__(self, x, y, width, height, image_list):
		BaseClass.__init__(self, x, y, width, height, image_list)
		Obstacle.List.add(self)

	def animate(self, frame):
		self.image = obst_img_list[frame]