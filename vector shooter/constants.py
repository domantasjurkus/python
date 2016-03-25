import sys, pygame
sys.dont_write_bytecode = True

pygame.mixer.init(frequency=48000, size=-16, channels=4, buffer=512)

# constants
WIDTH = 1000
HEIGHT = 600
FPS = 60
PLR_SIDE = 22
BUL_SIDE = 10
PWR_SIDE = 31
BUL_SPEED = 12

# player animation frames
PLR_ANIM = [
	"images/player/player_up.png",
	"images/player/player_right.png",
	"images/player/player_down.png",
	"images/player/player_left.png"
]

# square animation frames
SQR_ANIM = []
for i in range(1, 21):
	if i < 10:
		file_name = 'images/square/square_' + '0' + str(i) + '.png'
	else:
		file_name = 'images/square/square_' + str(i) + '.png'
	SQR_ANIM += [file_name]

# square hit animation frames
SQR_ANIM_HIT = []
for i in range(1, 8):
	file_name = 'images/square hit/hit_' + '0' + str(i) + '.png'
	SQR_ANIM_HIT.append(pygame.image.load(file_name))

PWR_ANIM = []
for i in range(1, 45):
	if i < 10:
		file_name = 'images/powerup/powerup_' + '0' + str(i) + '.png'
	else:
		file_name = 'images/powerup/powerup_' + str(i) + '.png'
	PWR_ANIM += [file_name]

# square hit animation frames
PWR_ANIM_APR = []
for i in range(1, 17):
	if i < 10:
		file_name = 'images/powerup appear/appear_' + '0' + str(i) + '.png'
	else:
		file_name = 'images/powerup appear/appear_' + str(i) + '.png'
	PWR_ANIM_APR.append(pygame.image.load(file_name))

# sounds
SHOT_WAV = pygame.mixer.Sound('sounds/shot.wav')
HIT_WAV = pygame.mixer.Sound('sounds/hit.wav')
POWER_WAV = pygame.mixer.Sound('sounds/powerup.wav')

# To do list:
# * prevent .pyc files from being created
# * add armour
# * add score label for squares