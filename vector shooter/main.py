import sys, pygame, random
sys.dont_write_bytecode = True
from constants import *
from classes import *
from process import *
pygame.init()

# game objects
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player(WIDTH/2, HEIGHT/2, PLR_SIDE, PLR_SIDE, PLR_ANIM)
total_frames  = 0
scoreForPowerup = [50]

# main loop, clean screen after every iteration
while True:
	screen.fill( (0, 0, 0) )
	checkExit()

	# general gameplay processes
	spawnSquares(total_frames)
	spawnPowerups(player, scoreForPowerup)
	sqr_bul_collisions(player)
	plr_pup_collisions(player)

	# class-related updates
	player.update(total_frames)
	Square.update_all(total_frames)
	Bullet.update_all()
	Powerup.update_all(total_frames)

	# other processes
	updateFuel(screen, player)
	scoreLabel(screen, player)
	# draw
	BaseClass.allsprites.draw(screen)

	font = pygame.font.Font(None, 20)
	text = font.render(str(Square.spawn_rate), 1, (255, 255, 255))
	screen.blit(text, (WIDTH-100, HEIGHT-50) )

	pygame.display.flip()
	plr_sqr_collisions(player, screen, clock)

	clock.tick(FPS)
	total_frames += 1
