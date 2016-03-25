import pygame, sys, random
sys.dont_write_bytecode = True

# Constants
WIDTH     = 800
HEIGHT    = 600
KEY_UP    = 38
KEY_RIGHT = 39
KEY_DOWN  = 40
KEY_LEFT  = 37
KEY_SPACE = 32
KEY_R     = 82
FPS       = 60

# Global variables
keys            = None
total_frames    = None
screen          = None
player          = None

clock = pygame.time.Clock()

def initGame():
        pygame.init()
        # load icon, set game title
        pygame.display.set_caption("Blah")

        global screen
        global keys

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        keys = pygame.key.get_pressed()

        splash()

def splash():

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

        initLevel()
        loop()

def initLevel():

        draw()

def loop():
        global total_frames
        global keys
        tick_done = False

        while True:
                total_frames += 1
                keys = pygame.key.get_pressed()
                checkExit()

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


def draw():
        screen.fill( (50, 0, 0) )

        pygame.display.flip()

initGame()
