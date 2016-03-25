import sys, pygame, random
sys.dont_write_bytecode = True

# constants
KEY_UP    = 38
KEY_RIGHT = 39
KEY_DOWN  = 40
KEY_LEFT  = 37
KEY_SPACE = 32
KEY_R     = 82

ROWS    = 19
COLS    = 29
SQR     = 30
WIDTH   = COLS*SQR
HEIGHT  = ROWS*SQR
HEIGHT2 = 100
FPS     = 60
START_POS_X     = 15
START_POS_Y     = 10
OBST_ANIM_SPEED = 12

# global variables
keys = None
total_frames     = None
obst_frame       = None
zombie_count     = None
obstacle_count   = None
highscore        = None
isGameOver       = None
isGameKeyPressed = None
isTeleportDone   = None

# game objects
screen = None
player = None

# splash
splash_img = pygame.image.load("images/splash.jpg")
# grid graphics
grid_img = pygame.image.load("images/background.png")
# player graphics
player_img_list = []
player_img_filename = [
	"images/player/player_01.png",
	"images/player/player_02.png",
	"images/player/player_03.png",
	"images/player/player_04.png"
]
for filename in player_img_filename:
	player_img_list.append(pygame.image.load(filename))
# zombie graphics
zombie_img_list = []
zombie_img_filename = [
	"images/zombie/zombie_01.png",
	"images/zombie/zombie_02.png",
	"images/zombie/zombie_03.png",
	"images/zombie/zombie_04.png"
]
for filename in zombie_img_filename:
	zombie_img_list.append(pygame.image.load(filename))
# obstacle graphics
obst_img_list = []
obst_img_filename = [
	"images/obstacle/obst_01.png",
	"images/obstacle/obst_02.png",
	"images/obstacle/obst_03.png",
	"images/obstacle/obst_04.png"
]
for filename in obst_img_filename:
	obst_img_list.append(pygame.image.load(filename))

# init mixer in order to load sounds
#pygame.mixer.quit()
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

# load sounds
pygame.mixer.music.load('sound/music.ogg')
radar_sound = pygame.mixer.Sound('sound/radar.ogg')
tele_sound  = pygame.mixer.Sound('sound/teleport.ogg')
death_sound = pygame.mixer.Sound('sound/death.ogg')