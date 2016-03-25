import sys
import pygame
import random
sys.dont_write_bytecode = True
from globals import *
from classes import *

clock = pygame.time.Clock()

def initGame():
	pygame.init()
	# load icon, set game title
	pygame.display.set_caption("Zombocalypso")
	icon = pygame.image.load("images/icon.png")
	print icon
	pygame.display.set_icon(icon)

	global screen
	global keys
	global player
	global highscore

	screen = pygame.display.set_mode((WIDTH, HEIGHT+HEIGHT2))
	keys = pygame.key.get_pressed()
	player = Player(START_POS_X, START_POS_Y, SQR, SQR, player_img_list)

	# try loading an existing highscore from file
	try:
		game_file = open("game.dat", "r")
		highscore = int(game_file.read())
		game_file.close()
		print 'exists'
	# if no such file exists - create one
	except:
		game_file = open("game.dat", "w")
		game_file.write("0")
		game_file.close()
		highscore = 0
		print "didn't exist"

	#initFirstLevel()
	splash()

def splash():
	screen.blit(splash_img, (0, 0))

	# splash text
	font = pygame.font.SysFont("lucidaconsole", 32)
	red = (255, 0, 0)
	text = font.render("Zombocalypso", 1, red)
	x_pos = (WIDTH-text.get_width())/2
	y_pos = (HEIGHT-text.get_height())/2 - 50
	screen.blit(text, (x_pos, y_pos) )

	font = pygame.font.SysFont("lucidaconsole", 20)
	white = (255, 255, 255)
	text = font.render("move with arrow keys", 1, white)
	x_pos = (WIDTH-text.get_width())/2
	y_pos = (HEIGHT-text.get_height())/2 + 30
	screen.blit(text, (x_pos, y_pos) )

	text = font.render("teleport with spacebar", 1, white)
	x_pos = (WIDTH-text.get_width())/2
	y_pos = (HEIGHT-text.get_height())/2 + 60
	screen.blit(text, (x_pos, y_pos) )

	text = font.render("press space to play", 1, white)
	x_pos = (WIDTH-text.get_width())/2
	y_pos = (HEIGHT-text.get_height())/2 + 130
	screen.blit(text, (x_pos, y_pos) )

	pygame.display.flip()
	global keys

	while True:
		keys = pygame.key.get_pressed()
		checkExit()

		if keys[pygame.K_SPACE]:
			initFirstLevel()
			return

		clock.tick(FPS)

def initFirstLevel():
	# assign values to global variables
	global total_frames			# for obstacle animation
	global obst_frame			# for obstacle animation
	global zombie_count			# for zombie spawning
	global obstacle_count		# for obstacle spawning
	global isGameOver			# for triggering gameOver()
	global isTeleportDone		# for preventing multiple teleports

	total_frames 	= 0
	obst_frame 		= 0
	zombie_count 	= 7
	obstacle_count  = 15
	isGameOver 		= False
	isTeleportDone 	= False

	# delete existing zombies and obstacles
	Zombie.List.empty()
	Obstacle.List.empty()

	death_sound.stop()
	pygame.mixer.music.play()

	player.resetPlayer(START_POS_X, START_POS_Y)
	generateObstacles(obstacle_count)
	initLevel(zombie_count)
	loop()

def initLevel(zombie_count):
	generateZombies(zombie_count)
	#player.updateTeleport()
	draw()

def generateObstacles(count):
	for i in range(count):
		x_pos = random.randint(0, COLS-1)
		y_pos = random.randint(0, ROWS-1)
		# distance between player and zombie
		dist_x = abs(player.x_pos - x_pos);
		dist_y = abs(player.y_pos - y_pos);
		# regenerate coordinates if too close to player
		while dist_x < 3 or dist_y < 3:
			x_pos = random.randint(0, COLS-1)
			y_pos = random.randint(0, ROWS-1)
			dist_x = abs(player.x_pos - x_pos);
			dist_y = abs(player.x_pos - x_pos);

		obst = Obstacle(x_pos, y_pos, SQR, SQR, obst_img_list);
		# zomb_array.push(zombie);

def generateZombies(count):
	for i in range(count):
		x_pos = random.randint(0, COLS-1)
		y_pos = random.randint(0, ROWS-1)
		# distance between player and zombie
		dist_x = abs(player.x_pos - x_pos);
		dist_y = abs(player.y_pos - y_pos);
		# regenerate coordinates if too close to player
		while dist_x < 6 or dist_y < 6:
			x_pos = random.randint(0, COLS-1)
			y_pos = random.randint(0, ROWS-1)
			dist_x = abs(player.x_pos - x_pos);
			dist_y = abs(player.x_pos - x_pos);
		# regenerate coordinates if on top of an obstacle
		for obst in Obstacle.List:
			while x_pos == obst.x_pos and y_pos == obst.y_pos:
				x_pos = random.randint(0, COLS-1)
				y_pos = random.randint(0, ROWS-1)

		zombie = Zombie(x_pos, y_pos, SQR, SQR, zombie_img_list);
		# zomb_array.push(zombie);

def loop():
	global total_frames
	global keys
	tick_done = False

	while True:
		total_frames += 1
		keys = pygame.key.get_pressed()
		checkExit()

		# animate obstacles
		if total_frames % OBST_ANIM_SPEED == 0:
			global obst_frame
			obst_frame = (obst_frame+1)%4
			for obst in Obstacle.List:
				obst.animate(obst_frame)
				# 1 - draw grid tile
				screen.blit(grid_img, (obst.rect.x, obst.rect.y))
				# 2 - draw new obstacle frame
				Obstacle.List.draw(screen)
				pygame.display.flip()

		# tick only if a gameplay key is being pressed
		keys = pygame.key.get_pressed()
		arrowKeyPressed = keys[pygame.K_UP] or \
							keys[pygame.K_RIGHT] or \
							keys[pygame.K_DOWN] or \
							keys[pygame.K_LEFT]

		if arrowKeyPressed and tick_done != True:
			# deterime which direction the player should go
			if keys[pygame.K_UP]:
				dir = 0;
			elif (keys[pygame.K_RIGHT]):
				dir = 1;
			elif (keys[pygame.K_DOWN]):
				dir = 2;
			elif (keys[pygame.K_LEFT]):
				dir = 3;
			#elif (keys[pygame.K_SPACE])and(player.tele_count > 0):
			#	dir = -1;

			tick(dir);
			tick_done = True;

		# reset tick_done boolean
		if arrowKeyPressed == False:
			tick_done = False

		# teleport without doing a tick()
		global isTeleportDone
		if keys[pygame.K_SPACE] and player.tele_count>0 and isTeleportDone==False:
			player.teleport()
			tele_sound.play()
			isTeleportDone = True
			# draw screen after teleporting
			draw()

		# reset isTeleportDone boolean
		if keys[pygame.K_SPACE] != True:
			isTeleportDone = False

		clock.tick(FPS)

def checkExit():
	global keys
	# exit with Esc button
	if keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()
	# exit with top-right Close button
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

def tick(dir):
	# 1 - update player and zombies
	player.update(dir)
	for zomb in Zombie.List:
		zomb.update(player)

	# 2 - check for collisions
	checkPlayerZombieCol()
	checkPlayerObstacleCol()
	checkZombieCols()
	checkZombieObstacleCol()

	# 3 - if all zombies are dead - new level
	if len(Zombie.List) == 0:
		global zombie_count
		zombie_count += 2
		# if there are more than 3 obstacles - delete one
		if len(Obstacle.List) > 3:
			# let's count how many obstacles there are
			obst_counted = 0
			for obst in Obstacle.List:
				obst_counted += 1
				# if we've counted the last obstacle...
				if obst_counted == len(Obstacle.List):
					# destroy one obstacle
					obst.destroy(Obstacle)
		player.score += zombie_count
		global stp_done
		step_done = True
		initLevel(zombie_count)

	# 4 - after checking collisions, update teleport
	player.updateTeleport()

	# 5 - draw after doing all the logic
	draw()

	# 6 - check wheter gameOver is triggered
	if isGameOver == True:
		# gameOver is a loop - play sounds only once
		#music.pause();
		#death_sound.play();

		gameOverSplash()
		gameOver()
		# terminate the current execution instance
		return

def checkPlayerZombieCol():
	# if zombie reaches player
	for zomb in Zombie.List:
		if zomb.x_pos==player.x_pos and zomb.y_pos==player.y_pos:
			global isGameOver
			isGameOver = True

def checkZombieCols():
	for z1 in Zombie.List:
		for z2 in Zombie.List:
			if z1.x_pos == z2.x_pos and z1.y_pos == z2.y_pos and z1!=z2:
				z1.destroy(Zombie)
				player.score += 2

def checkZombieObstacleCol():
	# collect a list of zombies that need to be deleted
	del_list = []
	for zomb in Zombie.List:
		for obst in Obstacle.List:
			if zomb.x_pos==obst.x_pos and zomb.y_pos==obst.y_pos:
				del_list.append(zomb)

	# delete zombies within the list
	for zomb in del_list:
		zomb.destroy(Zombie)
		player.score += 1

def checkPlayerObstacleCol():
	global isGameOver
	for obst in Obstacle.List:
		if obst.x_pos==player.x_pos and obst.y_pos==player.y_pos:
			isGameOver = True

def draw():
	screen.fill( (50, 0, 0) )

	# draw HUD
	# teleport info
	font = pygame.font.SysFont("lucidaconsole", 16)
	white = (255, 255, 255)
	text = font.render("Teleports Remaining: " + str(player.tele_count), 1, white)
	screen.blit(text, (30, HEIGHT+30))
	text = font.render("Score for Teleport:  " + str(player.next_tele_at), 1, white)
	screen.blit(text, (30, HEIGHT+60))

	# score, highscore
	font = pygame.font.SysFont("lucidaconsole", 20)
	text = font.render("Score: " + str(player.score), 1, white)
	x_pos = (WIDTH-text.get_width())/2
	y_pos = HEIGHT+(HEIGHT2-text.get_height())/2
	screen.blit(text, (x_pos, y_pos) )
	text = font.render("Highscore: " + str(highscore), 1, white)
	screen.blit(text, (WIDTH-250, y_pos))

	# draw grid
	for i in range(ROWS):
		for j in range(COLS):
			screen.blit(grid_img, (j*SQR, i*SQR))

	# draw all sprites
	Player.List.draw(screen)
	Zombie.List.draw(screen)
	Obstacle.List.draw(screen)

	# flip buffer
	pygame.display.flip()

def gameOverSplash():
	# splash rectangle
	foreground = (60, 0, 0)
	background = (30, 0, 0)
	pygame.draw.rect(screen, background, (WIDTH/2-195, HEIGHT/2-80, 400, 210))
	pygame.draw.rect(screen, foreground, (WIDTH/2-200, HEIGHT/2-85, 400, 210))

	# determine player rank
	rank = getRank(player.score)

	# splash text
	font = pygame.font.SysFont("lucidaconsole", 32)
	white = (255, 255, 255)
	text = font.render("Death Be Upon You", 1, white)
	x_pos = (WIDTH-text.get_width())/2
	y_pos = (HEIGHT-text.get_height())/2 - 30
	screen.blit(text, (x_pos, y_pos) )

	font = pygame.font.SysFont("lucidaconsole", 24)
	text = font.render("Final Score: " + str(player.score), 1, white)
	x_pos = (WIDTH-text.get_width())/2
	y_pos = (HEIGHT-text.get_height())/2 + 20
	screen.blit(text, (x_pos, y_pos) )

	text = font.render("Final Rank: " + rank, 1, white)
	x_pos = (WIDTH-text.get_width())/2
	y_pos = (HEIGHT-text.get_height())/2 + 50
	screen.blit(text, (x_pos, y_pos) )

	text = font.render("Try Agan? Press R", 1, white)
	x_pos = (WIDTH-text.get_width())/2
	y_pos = (HEIGHT-text.get_height())/2 + 100
	screen.blit(text, (x_pos, y_pos) )

	pygame.display.flip()

def getRank(score):
	if score < 1:
		return "Try Harder"
	if score < 5:
		return "Stew Cooker"
	if score < 10:
		return "Mud Skipper"
	if score < 25:
		return "Sewer Crawler"
	if score < 50:
		return "Leg Twister"
	if score < 100:
		return "Path Finder"
	if score < 250:
		return "Grass Runner"
	if score < 500:
		return "Flame Juggler"
	if score < 1000:
		return "Corpse Basher"
	else:
		return "Bug Finder"

def gameOver():
	pygame.mixer.music.stop()
	death_sound.play()

	# save highscore
	global highscore
	if player.score > highscore:
		# write to game.dat
		highscore = player.score
		game_file = open("game.dat", "w")
		game_file.write(str(highscore))
		game_file.close()

	while True:
		global keys
		keys = pygame.key.get_pressed()
		checkExit()

		if keys[pygame.K_r]:
			initFirstLevel()
			#return

		clock.tick(FPS)

initGame()
