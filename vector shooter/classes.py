import sys, pygame, random
from constants import *
sys.dont_write_bytecode = True

# BaseClass - primary 'template' for all other classes
class BaseClass(pygame.sprite.Sprite):

	# add every object into the list 'allsprites'
	allsprites = pygame.sprite.Group()

	# initiate class
	def __init__(self, x, y, width, height, image_list):

		# inherit parameters from the pygame class 'Sprite'
		pygame.sprite.Sprite.__init__(self)
		BaseClass.allsprites.add(self)

		# pass image list from parameter into class
		for i in range(len(image_list)):
			self.imageList.append(pygame.image.load(image_list[i]))
		# assign first image
		self.image = self.imageList[0]

		# set the visible rectangle of the object
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.width = width
		self.height = height

	# method for destroying an object 
	def destroy(self, ClassName):
		ClassName.List.remove(self)
		BaseClass.allsprites.remove(self)
		del self

class Player(BaseClass):
	List = pygame.sprite.Group()

	# default parameters inherited from BaseClass
	def __init__(self, x, y, width, height, image_list):
		self.imageList = []
		BaseClass.__init__(self, x, y, width, height, image_list)
		Player.List.add(self)

		# custom parameters
		self.dir = 0
		self.velx = 0
		self.vely = 0
		self.accx = 0
		self.accy = 0
		self.cooldown = 0
		self.cooldown_limit = 20
		self.score = 0
		self.fuel = 0

	def update(self, total_frames):
		# update image based on direction
		self.image = self.imageList[self.dir]

		# keys for movement
		keys = pygame.key.get_pressed()
		if keys[pygame.K_d]:
			self.accx = 1
		if keys[pygame.K_a]:
			self.accx = -1
		if keys[pygame.K_w]:
			self.accy = -1
		if keys[pygame.K_s]:
			self.accy = 1

		# keys for direction
		if keys[pygame.K_UP]:
			self.dir = 0
		if keys[pygame.K_RIGHT]:
			self.dir = 1
		if keys[pygame.K_DOWN]:
			self.dir = 2
		if keys[pygame.K_LEFT]:
			self.dir = 3

		# slow player down
		if self.velx > 0:
			self.velx -= 0.5
		if self.velx < 0:
			self.velx += 0.5
		if self.vely > 0:
			self.vely -= 0.5
		if self.vely < 0:
			self.vely += 0.5

		# max speed limiters
		if self.velx > 5:
			self.velx = 5
		if self.velx < -5:
			self.velx = -5
		if self.vely > 5:
			self.vely = 5
		if self.vely < -5:
			self.vely = -5

		# increase speed based on acceleration
		self.velx += self.accx	
		self.vely += self.accy	

		# update player position
		self.rect.x += self.velx
		self.rect.y += self.vely
		
		# reset acceleration
		self.accx = 0
		self.accy = 0

		# generate bullet
		if keys[pygame.K_SPACE] and self.cooldown == 0:

			# adjust primary bullet position
			if self.dir == 0:
				bul_x = self.rect.x + 6
				bul_y = self.rect.y - 2
			if self.dir == 1:
				bul_x = self.rect.x + PLR_SIDE - BUL_SIDE + 2
				bul_y = self.rect.y + 6
			if self.dir == 2:
				bul_x = self.rect.x + 6
				bul_y = self.rect.y + PLR_SIDE - BUL_SIDE + 2
			if self.dir == 3:
				bul_x = self.rect.x - 2
				bul_y = self.rect.y + 6

			bullet = Bullet(bul_x, bul_y, 10, 10, ["images/bullet.png"], self.dir)
			self.cooldown = self.cooldown_limit

			# play bullet sound
			SHOT_WAV.play()

		# reset cooldown so that next bullet can be shot
		if self.cooldown > 0:
			self.cooldown -= 1

		# set screen boundaries
		if self.rect.x < 0:
			self.rect.x = 0
			self.velx *= -1
		if self.rect.x + self.width > WIDTH:
			self.rect.x = WIDTH - self.width
			self.velx *= -1
		if self.rect.y < 0:
			self.rect.y = 0
			self.vely *= -1
		if self.rect.y + self.height > HEIGHT:
			self.rect.y = HEIGHT - self.height
			self.vely *= -1

		# update powerup logic
		if self.fuel > 0:
			self.cooldown_limit = 5
		else:
			self.cooldown_limit = 20

class Bullet(BaseClass):
	List = pygame.sprite.Group()

	# list for bullet deletion
	normalList = []

	# default parameters inherited from BaseClass
	def __init__(self, x, y, width, height, image_list, direction):
		self.imageList = []
		BaseClass.__init__(self, float(x), float(y), width, height, image_list)
		Bullet.List.add(self)
		Bullet.normalList.append(self)

		# custom parameters
		self.dir = direction
		self.velx = 0
		self.vely = 0

		# set bullet speed based on direction
		if self.dir == 0:
			self.vely -= BUL_SPEED
		elif self.dir == 1:
			self.velx += BUL_SPEED
		elif self.dir == 2:
			self.vely += BUL_SPEED
		elif self.dir == 3:
			self.velx -= BUL_SPEED

	def update(self):

		# update bullet coordinate based on direction
		self.rect.x += self.velx
		self.rect.y += self.vely

		# set screen boundaries
		if self.rect.x < 0:
			self.rect.x = 0
			self.velx *= -1
		if self.rect.x + self.width > WIDTH:
			self.rect.x = WIDTH - self.width
			self.velx *= -1
		if self.rect.y < 0:
			self.rect.y = 0
			self.vely *= -1
		if self.rect.y + self.height > HEIGHT:
			self.rect.y = HEIGHT - self.height
			self.vely *= -1

		# delete bullet if it goes off-screen
		if self.rect.x + BUL_SIDE < 0 or self.rect.x > WIDTH or self.rect.y + BUL_SIDE < 0 or self.rect.y > HEIGHT:
			self.destroy(Bullet)

	# method for the entire class
	@staticmethod
	def update_all():
		for bullet in Bullet.List:
			bullet.update()

class Square(BaseClass):
	List = pygame.sprite.Group()
	spawn_rate = 50

	def __init__(self, x, y, width, height, image_list, direction):
		self.imageList = []
		BaseClass.__init__(self, x, y, width, height, image_list)
		Square.List.add(self)

		self.dir = direction
		self.speed = 2
		self.appeared = True
		self.currentFrame = 0
		self.currentHitFrame = 0
		self.isHit = False
		self.hitAdjusted = False

	def update_movement(self, total_frames):

		# update movement based on primary direction
		if self.isHit == False:
			if self.dir == 0:
				self.rect.y -= self.speed
			if self.dir == 1:
				self.rect.x += self.speed
			if self.dir == 2:
				self.rect.y += self.speed
			if self.dir == 3:
				self.rect.x -= self.speed

		# check for wall collision
		if self.appeared == True:
			if self.rect.y < 0:
				self.dir = 2
			if self.rect.x + self.width > WIDTH:
				self.dir = 3
			if self.rect.y + self.height > HEIGHT:
				self.dir = 0
			if self.rect.x < 0:
				self.dir = 1

	def animate(self, total_frames):

		# animate square
		if self.isHit == False:
			if total_frames % 2 == 0:
				self.currentFrame += 1
			if self.currentFrame == 20:
				self.currentFrame = 0
			self.image = self.imageList[self.currentFrame]

		# once square is hit
		if self.isHit == True:
			if self.hitAdjusted == False:
				self.rect.x -= 14
				self.rect.y -= 14
				self.hitAdjusted = True

			self.image = SQR_ANIM_HIT[self.currentHitFrame]
			if total_frames % 1 == 0:
				self.currentHitFrame += 1
			if self.currentHitFrame == 7:
				self.destroy(Square)

			# play square hit sound
			HIT_WAV.play()

	# method for the entire class
	@staticmethod
	def update_all(total_frames):
		for square in Square.List:
			square.update_movement(total_frames)
			square.animate(total_frames)

class Powerup(BaseClass):
	List = pygame.sprite.Group()

	def __init__(self, x, y, width, height, image_list):
		self.imageList = []
		BaseClass.__init__(self, x, y, width, height, image_list)
		Powerup.List.add(self)

		self.currentFrame = 0
		self.currentTouchFrame = 15
		self.hasAppeared = False
		self.isTouched = False

	def animate(self, total_frames):
		if self.hasAppeared == False and self.isTouched == False:
			self.image = PWR_ANIM_APR[self.currentFrame]
			self.currentFrame += 1
			if self.currentFrame == 16:
				self.hasAppeared = True
				self.currentFrame = 0

		if self.hasAppeared == True and self.isTouched == False:
			self.currentFrame += 1
			if self.currentFrame == 44:
				self.currentFrame = 0
			self.image = self.imageList[self.currentFrame]

		if self.hasAppeared == True and self.isTouched == True:
			self.image = PWR_ANIM_APR[self.currentTouchFrame]
			self.currentTouchFrame -= 1
			if self.currentTouchFrame == -1:
				self.destroy(Powerup)

	@staticmethod
	def update_all(total_frames):
		for pup in Powerup.List:
			pup.animate(total_frames)