import sys, pygame, random
from classes import *
sys.dont_write_bytecode = True

def checkExit():
	# exit with Esc button
	keys = pygame.key.get_pressed()
	if keys[pygame.K_ESCAPE]:
			pygame.quit()
			sys.exit()
	# exit with top-right Close button
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

def spawnSquares(total_frames):
	if total_frames % Square.spawn_rate == 0:
		direction = random.randint(0, 3)
		if direction == 0:
			x = random.randint(0, WIDTH-22)
			y = HEIGHT+22
		if direction == 1:
			x = -22
			y = random.randint(0, HEIGHT-22)
		if direction == 2:
			x = random.randint(0, WIDTH-22)
			y = -22
		if direction == 3:
			x = WIDTH+22
			y = random.randint(0, HEIGHT-22)
		square = Square(x, y, 31, 31, SQR_ANIM, direction)

	# speed up spawn rate
	if total_frames % 50 == 0 and Square.spawn_rate > 1:
		Square.spawn_rate -= 1

def spawnPowerups(player, scoreForPowerup):
	if player.score == scoreForPowerup[0]:
		x = random.randint(0, WIDTH-31)
		y = random.randint(0, HEIGHT-33)
		powerup = Powerup(x, y, 33, 33, PWR_ANIM)
		scoreForPowerup[0] += 50

def sqr_bul_collisions(player):

	# loop through all the squares
	for square in Square.List:

		# make a list of all bullets that overlap squares
		# AND remove bullet from Bullet.list
		sqr_bul = pygame.sprite.spritecollide(square, Bullet.List, True)
		
		if len(sqr_bul) > 0:
			square.isHit = True
			player.score += 10

def plr_pup_collisions(player):
	for pup in Powerup.List:
		col = pygame.sprite.collide_rect(player, pup)
		if col == True and pup.hasAppeared == True:
			# the if ensures one-time events
			if pup.isTouched == False:
				player.fuel += 100
				POWER_WAV.play()
			pup.isTouched = True

def plr_sqr_collisions(player, screen, clock):
	for sqr in Square.List:
		col = pygame.sprite.collide_rect(player, sqr)
		if col == True:
			gameOver(screen, clock)

def updateFuel(screen, player):
	if player.fuel > 0:
		pygame.draw.rect(screen,(200,200,0),(30,HEIGHT-30,player.fuel,20))
		player.fuel -= 1

def scoreLabel(screen, player):
	font = pygame.font.Font(None, 20)
	text = font.render("score: " + str(player.score), 1, (255, 255, 255))
	screen.blit(text, (WIDTH-100, HEIGHT-30) )

def gameOver(screen, clock):
	font1 = pygame.font.Font(None, 26)
	font2 = pygame.font.Font(None, 20)
	text1 = font1.render("Ship crashed - Game Over", 1, (255, 255, 255))
	text2 = font2.render("Press Esc to Exit", 1, (255, 255, 255))
	#screen.blit(text, (0, 0))
	screen.blit(text1, (WIDTH/2 - text1.get_width()/2, HEIGHT/2 - text1.get_height()/2))
	screen.blit(text2, (WIDTH/2 - text2.get_width()/2, HEIGHT/2 - text2.get_height()/2 + 30))
	pygame.display.flip()
	while True:
		clock.tick(FPS)
		checkExit()