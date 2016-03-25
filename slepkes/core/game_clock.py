from constants import *

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

class Game_Clock():

    def __init__(self, display, buf, blende, keyboard):

        self.t_before = None

        self.display = display

        self.buffer = buf
        self.blende = blende
        self.keyboard = keyboard

        self.wait_ts = []
        self.passed_ts = []

    def input_update(self):

        keyboard_events = []

        for event in pygame.event.get():

            if event.type in (KEYDOWN, KEYUP):
                keyboard_events.append(event)

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        self.keyboard.update(keyboard_events)

        shutdown = ((K_RALT in self.keyboard.pressed or K_LALT in self.keyboard.pressed) and
                    K_F4 in self.keyboard.pressed)

        if shutdown:
            pygame.quit()
            sys.exit()

    def blit_display(self):
        """blittet blende und buffer"""

        self.buffer.blit(self.blende, (0, 0))

        pygame.transform.scale(self.buffer, RES_REAL, self.display)

    def flip_display(self):

        pygame.display.flip()

    def wait(self, mil_secs=TICK):

        pygame.time.wait(mil_secs)

    def tick(self, frames=1):

        frame_counter = 0

        if frames == 1:
            check_quit = False
        else:
            check_quit = True

        while frame_counter < frames:

            if check_quit:
                self.input_update()

            if not self.t_before:
                self.t_before = pygame.time.get_ticks()

            self.blit_display()
            self.flip_display()

            t_after = pygame.time.get_ticks()
            t_passed = t_after - self.t_before
            self.passed_ts.append(t_passed)
            wait_time = TICK - t_passed
            #print wait_time
            if wait_time < 0:
                wait_time = 0
            
            self.wait(wait_time)

            self.t_before = pygame.time.get_ticks()

            frame_counter += 1

        return wait_time
