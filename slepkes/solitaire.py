import pygame
from random import randint
pygame.mixer.pre_init(22050, 8, 2, 4096 / 12)
pygame.init()

from constants import *

display = pygame.display.set_mode(RES_REAL)

from game_clock import Game_Clock
from std_out    import Std_Out
from card       import *
from stacks     import Stack, Suit_Stack, Stock

VER = 1.01

class Game:

    def __init__(self):
        # lots of primary settings we may not care about right now
        self.mode         = 0
        self.buffer       = pygame.Surface(RES)
        self.screen_rect  = Rect(0, 0, RES[0], RES[1])
        self.display      = display
        self.alpha        = 0
        self.blende       = pygame.Surface(RES, SRCALPHA)
        self.blende.fill(TRANSPARENT)

        self.gamepads = gamepads.get_gamepads()
        self.mouse    = Mouse(RES_REAL, RES)
        self.keyboard = Keyboard()

        self.clock    = Game_Clock(self.display, self.buffer, self.blende, self.keyboard)
        self.scene    = None

        self.std_out        = Std_Out(self.buffer)
        self.std_font_name  = get_font_names()[0]
        self.std_font       = get_font(self.std_font_name, 20)

        self.black_screen = pygame.Surface(RES)
        self.white_screen = pygame.Surface(RES)
        self.white_screen.fill(WHITE)

        self.board = pygame.Surface(RES)
        self.board.fill(DUNKELBLAU)

        self._init_cards_()
        self._init_stacks_()
    def _init_cards_(self):

        # Generate a random list of 52 elements ranging [1, 103]
        self.cards = []
        card_id_list = []

        while len(card_id_list) < 103:
            id = randint(1, 103)
            if id not in card_id_list:
                card_id_list.append(id)
    
        for id in card_id_list:
            cardname = id
            card = Card(cardname)       # create card instance
            self.cards.append(card)     # save card instance   


        '''
        for s in SUITS:                     # loop through [c, h, s, d]
            for v in VALUES:                # loop through [1, 13]
                cardname = s + str(v)       # "c13", "h7", "s11" etc.
                card = Card(cardname)       # create card instance
                self.cards.append(card)     # save card instance
        '''

    def _init_stacks_(self):

        # Main card stock (upside down cards)
        stock_pos = (15, 350)                 # position the stock
        self.stock = Stock(stock_pos)         # create Stock instance
        self.stock.append_cards(self.cards)   # add generated cards to stock
        self.stock.shuffle()

        # Reversed card slot (face-up)
        face_up_stock_pos = (200, 350)
        self.face_up_stock = Stack(face_up_stock_pos)     # create Stack instance

        # player_stacks:
        x_offset = 300                        # position for middle stacks
        y_offset = 70

        self.player_stacks = []               # list of 7 lists of cards at the middle

        for n in range(0, 7):                         # create 7 stack instances
            topleft = (x_offset, y_offset)            # set top-left corner
            self.player_stacks.append(Stack(topleft)) # create an empty Stack instance
            x_offset += 130                           # move next stack to the right

        self.cursor_stack = Stack((0, 0))             # cursor_stack ?

        # suit_stacks:
        x_offset = 400
        y_offset = 400

        self.suit_stacks = {}
        
        for suit in SUITS:                            # loop through [c, h, s, d]
            topleft = (x_offset, y_offset)            # set top-left corner
            suit_stack = Suit_Stack(topleft, suit)    # create a Suit_Stack instance
            self.suit_stacks[suit] = suit_stack       # save to game.suit_stack
            x_offset += 170                           # move right
    def blit_board(self):

        self.buffer.blit(self.board, (0, 0))



    # ----- Card drawing functions -----
    def blit_stacks(self):
        self.blit_stock()           # face-down cards
        self.blit_face_up_stock()   # face-up cards
        # self.blit_player_stacks()   # 7 main columns
        self.blit_suit_stacks()     # 4 columns for suits
        self.blit_cursor_stack()    # card in cursor
    def blit_stock(self):
        s = self.stock
        def blit_stock_boardmark():
            if not len(self.face_up_stock.cards):
                img = s.empty_boardmark
            else:
                img = s.boardmark
            self.buffer.blit(img, s.topleft)

        if not len(s.cards):
            blit_stock_boardmark()
            return
        
        if len(s.cards) > 3:
            nr_of_cards = 3
        else:
            nr_of_cards = len(s.cards)

        x_offset = 0

        for card in s.cards[nr_of_cards * -1:]:
            card.rect.topleft = (s.left + x_offset,
                                 s.top)
            self.blit_sprite(card)
            x_offset += 2
    def blit_face_up_stock(self):
        
        s = self.face_up_stock        
        if len(s.cards) > 3:
            nr_of_cards = 3
        else:
            nr_of_cards = len(s.cards)

        x_offset = 0

        for c in s.cards[nr_of_cards * -1:]:
            c.rect.topleft = (s.left + x_offset,
                              s.top)
            c.uncover()
            self.blit_sprite(c)
            x_offset += 10
    def blit_player_stacks(self):
        for s in self.player_stacks:
            self.blit_player_stack(s)
    def blit_suit_stacks(self):
        for s in self.suit_stacks.values():
            self.blit_suit_stack(s)
    def blit_cursor_stack(self):
        s = self.cursor_stack
        mpos = self.mouse.pos

        x_offset = CARDSIZE[0] / 2 * -1
        y_offset = -10
        n = 0

        for c in s.cards:
            c.rect.topleft = (mpos[0] + x_offset,
                              mpos[1] + y_offset)
            self.blit_sprite(c)
            if n == 0:
                y_offset += 10
            else:
                y_offset += 5
            n += 1
    def blit_suit_stack(self, suit_stack):
        
        s = suit_stack

        def blit_boardmark():
            self.buffer.blit(s.boardmark, s.topleft)

        if not len(s.cards):
            blit_boardmark()
            return
        
        upper_card = s.cards[-1]
        upper_card.rect.topleft = s.topleft
        self.blit_sprite(upper_card)
    def blit_player_stack(self, stack):

        y_offset = 0

        for c in stack.cards:
            c.rect.topleft = (stack.left,
                              stack.top + y_offset)
            self.blit_sprite(c)
            if c.covered:
                y_offset += 2
            else:
                y_offset += 7
    # -----------------------------------



    def new_game(self):
        self.stock.empty()                    # remove all cards from stock.cards
        self.face_up_stock.empty()                  # remove all cards from stock.r_cards
        for s in self.player_stacks:          # remove all cards from 7 stacks
            s.empty()
        for s in self.suit_stacks.values():   # remove all cards from suit stacks
            s.empty()

        self.stock.append_cards(self.cards)   # add the generated Card objects to self.stock
        self.stock.shuffle()                  # shuffle the stock list
        self.stock.cover_all()                # hide the cards
        self.deal_cards()                     # next function
    def deal_cards(self):
        nr_of_cards = 1
        for s in self.player_stacks:                      # loop through each main playing stack (7)
            cards = self.stock.cards[nr_of_cards * -1:]   # grab the last n cards from main stock
            s.append_cards(cards)                         # put those cards in one of the 7 stacks
            s.uncover()                                   # uncover the stack
            del self.stock.cards[nr_of_cards * -1:]       # remove the cards from the main stock
            nr_of_cards = 1                               # goes from 1 to 7



    # ----- Technical functions -----
    def input_update(self):
        # library functions
        mouse_events = []
        keyboard_events = []

        for event in pygame.event.get():

            if event.type in (KEYDOWN, KEYUP):
                keyboard_events.append(event)
                
            elif event.type in (MOUSEBUTTONDOWN, MOUSEBUTTONUP):
                mouse_events.append(event)

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()                

        self.mouse.update(mouse_events)
        self.keyboard.update(keyboard_events)

        shutdown = (K_RALT in self.keyboard.pressed or K_LALT in self.keyboard.pressed and
                    K_F4 in self.keyboard.pressed)

        if shutdown:
            pygame.quit()
            sys.exit()
    def set_alpha(self, value):

        self.alpha = value
        colour = (0, 0, 0, self.alpha)
        self.blende.fill(colour)
    def increase_alpha(self, value):

        self.alpha += value

        if self.alpha > 255:
            self.alpha = 255

        colour = (0, 0, 0, self.alpha)
        self.blende.fill(colour)
    def decrease_alpha(self, value):

        self.alpha -= value

        if self.alpha < 0:
            self.alpha = 0

        colour = (0, 0, 0, self.alpha)
        self.blende.fill(colour)
    def blit_sprite(self, sprite):

        self.buffer.blit(sprite.bild, sprite.rect)        
    def clear_buffer(self):

        self.buffer.fill(SCHWARZ)
    def get_standbild(self):

        standbild = self.buffer.copy()
        return standbild
    def blit_standbild(self, standbild):

        self.buffer.blit(standbild, (0, 0))
    def get_blitpos(self, topleft):

        x = topleft[0] - self.screen_rect.left
        y = topleft[1] - self.screen_rect.top
        return (x, y)
    def blit_wait_time(self, wait_time):
        
        self.std_out.say(str(wait_time))
    def blit_cursor(self):
        # draw the cursor
        self.buffer.blit(self.mouse.bild, self.mouse.rect)
    def check_skip(self):

        self.input_update()

        skip_scene = ((self.keyboard.ready and K_ESCAPE in self.keyboard.pressed)
                          or self.mouse.ready and 1 in self.mouse.pressed)
        if skip_scene:
            self.keyboard.ready = self.mouse.ready = False
            return True
        else:
            return False
    def check_ESC_pressed(self):

        ESC_pressed = self.keyboard.ready and K_ESCAPE in self.keyboard.pressed

        if ESC_pressed:
            self.keyboard.ready = False
            return True
        else:
            return False
    # ---------------------------------



    # ----- Card pickup detection -----
    def check_pick_up_from_face_up_stock(self):
        # check if cards are being picked up from the face-up stock
        # function called on mouse click
        # self.mouse.ready is True here !

        mpos = self.mouse.pos         # mouse position

        s = self.face_up_stock        # reference to face-up stock
        cs = self.cursor_stack        # reference to the mouse stack

        if len(s.cards):              # if there are cards in the face-up stock
            c = s.cards[-1]           # grab the top card

            # if the mouse is within the card rectangle AND left button is pressed
            if pos_in_rect(self.mouse.pos, c.rect) and LEFT_BUTTON in self.mouse.pressed:
                cs.cards.append(c)    # put the top card in the cursor stack
                cs.origin = s         
                del s.cards[-1]       # remove the card from face-up stock
                return True

        return False
    def check_pick_up_from_player_stacks(self):
        # check if a card is being picked from the 7 stacks
        mouse_x = self.mouse.pos[0]
        mouse_y = self.mouse.pos[1]

        # if the Y mouse value is above the 7 stacks - quit function
        if mouse_y < self.player_stacks[0].top:           
            return

        p_stack = None

        for s in self.player_stacks:                      # loop through 7 stacks
            if mouse_x > s.left and mouse_x < s.right:    # if the X mouse value is on the card
                p_stack = s                               # set our stack of interaction as p_stack
                break

        if not p_stack:                                   # if no stack has been assigned
            return                                        # return

        self.pick_up_cards_from_player_stack(p_stack)
    def pick_up_cards_from_player_stack(self, stack):
        # pick up a card from the 7 stacks
        mpos = self.mouse.pos
        s = stack                         # copy a reference to the stack
        i = -1                            # get upper card:

        for c in reversed(s.cards):       # loop through all cards in the playing stack
            if c.covered:                 # if the card is covered
                if i == -1:               # and if it's the top card
                    c.uncover()           # uncover it
                return
            if pos_in_rect(mpos, c.rect):               # if the mouse is on the card
                cards = s.cards[i:]                     # select the cards from -i to the end
                self.cursor_stack.append_cards(cards)   # copy the card(s) to the cursor stack
                self.cursor_stack.origin = s            # set the origin of the cursor stack
                del s.cards[i:]                         # remove cards from the playing stack
                return
            else:
                i -= 1                                  # move down one card
    def check_pick_up_from_suit_stacks(self):
        # pick up from the 4 suit stacks
        mpos = self.mouse.pos

        for s in self.suit_stacks.values():       # loop through all suits
            if pos_in_rect(mpos, s):              # if the mouse is on the stack
                if not len(s.cards):              # if the stack is empty - return
                    return
                upper_card = s.cards[-1]          # grab top card from stack
                self.cursor_stack.cards.append(upper_card)  # put the card in the cursor stack
                self.cursor_stack.origin = s      # set the cursor stack_origin
                s.cards.pop()                     # remove the card from the suit stack
                return
    def check_pick_up_cards(self):
        if self.check_pick_up_from_face_up_stock():
            return
        if self.check_pick_up_from_player_stacks():    # this includes uncovering player_stack_cards
            return
        self.check_pick_up_from_suit_stacks()
    def check_deal_from_stock(self):
        # A boolean that tells if the mouse was clicked on the face-down stock
        deal_cards = pos_in_rect(self.mouse.pos, self.stock)

        if deal_cards:
            self.deal_from_stock()
    def deal_from_stock(self, nr_of_cards = 1):

        stock = self.stock
        face_up_stock = self.face_up_stock

        if not len(stock.cards): # Stock empty -> refill
            self.refill_stock()
            return

        if len(stock.cards) >= nr_of_cards:
            cards = stock.cards[nr_of_cards * -1:]
            del stock.cards[nr_of_cards * -1:]
        else:
            cards = stock.cards[:]
            del stock.cards[:]

        face_up_stock.append_cards(reversed(cards))  
    # ---------------------------------

    def check_suit_stack_drop(self):

        mpos = self.mouse.pos

        for s in self.suit_stacks.values():
            if pos_in_rect(mpos, s):
                # self.check_suit_drop(s)
                self.drop_cards(s)
                return

    def check_suit_drop(self, suit_stack):

        cards = self.cursor_stack.cards
        
        if len(cards) > 1: # only 1 card can be dropped in suit stack !
            return

        c = cards[0]

        if c.suit != suit_stack.suit: # suit must match !
            return

        if not len(suit_stack.cards): # if suit stack is empty -> Ace needed!
            value_needed = ACE
        else:
            upper_card = suit_stack.cards[-1]
            value_needed = upper_card.value + 1

        if c.value == value_needed:
            self.drop_cards(suit_stack)         

    def check_player_stack_drop(self):

        mpos = self.mouse.pos
        p_stack = None

        # if mouse y is above the stacks - quit funtion
        if mpos[1] < self.player_stacks[0].top:
            return
        if mpos[1] > self.player_stacks[0].top + CARDSIZE[1]:
            return   

        for s in self.player_stacks:
            if (mpos[0] >= s.left and mpos[0] <= s.right):
                self.drop_cards(s)
                # p_stack = s
                break

        # if p_stack:
        #     self.check_drop(p_stack)

    def check_drop(self, destination_stack):

        s = destination_stack

        cards_to_drop = self.cursor_stack.cards
        upper_card = cards_to_drop[0]

        if not len(s.cards): # if destination stake is empty -> must be King !
            if upper_card.value != KING:
                return
            else:
                self.drop_cards(s)

        dest_card = s.cards[-1]

        if dest_card.covered: # if card not uncovered yet -> nothing can be dropped !
            return
        
        if dest_card.value == ACE: # if dest card is ACE -> nothing can be dropped !
            return

        value_needed = dest_card.value - 1
        if dest_card.colour == BLACK:
            colour_needed = RED
        else:
            colour_needed = BLACK

        drop_ok = (upper_card.colour == colour_needed and
                   upper_card.value == value_needed)

        if drop_ok:
            self.drop_cards(s)

    def check_drop_cards(self):

        # this method is only called if cursor_stake contains cards and Left Mouse Button was released !

        self.check_player_stack_drop()
        self.check_suit_stack_drop()

        # if still cards in cursor_stack -> put back:
        if len(self.cursor_stack.cards):
            self.put_cards_back()

    def check_direct_drop(self):

        mpos = self.mouse.pos

        stacks_to_check = self.player_stacks[:]
        stacks_to_check.append(self.face_up_stock)

        for s in stacks_to_check:
            if len(s.cards):
                upper_card = s.cards[-1]
                if pos_in_rect(mpos, upper_card.rect) and not upper_card.covered:
                    suit_stack = self.suit_stacks[upper_card.suit]
                    if not len(suit_stack.cards):
                        value_needed = ACE
                    else:
                        value_needed = suit_stack.cards[-1].value + 1
                    if upper_card.value == value_needed:
                        suit_stack.cards.append(upper_card)
                        del s.cards[-1]
                        return

    def drop_cards(self, destination_stack):

        cards_to_drop = self.cursor_stack.cards
        destination_stack.append_cards(cards_to_drop)
        self.cursor_stack.empty()

    def put_cards_back(self):
      
        cs = self.cursor_stack
        os = cs.origin

        os.append_cards(cs.cards)
        cs.empty()

    def refill_stock(self):

        r = self.face_up_stock
        s = self.stock

        s.append_cards(r.cards)
        s.reverse()
        s.cover_all()

        r.empty()

    def check_game_won(self):

        for s in self.suit_stacks.values():
            if len(s.cards) != 13:
                return False
        return True

    def game_won_scene(self):

        stacks = self.suit_stacks.values()
        all_cards = []
        for s in stacks:
            for c in s.cards:
                all_cards.append(c)
        jumping_cards = []

        while 1:

            def append_cards():
                if not len(jumping_cards):
                    if len(all_cards):
                        card = all_cards.pop()
                        card.x = card.rect.centerx
                        card.y = card.rect.centery
                        card.y_speed = random.randint(30, 80) / 100.0 * -1
                        card.jump_speed_max = random.randint(100, 400) / 100.0 * -1
                        card.x_speed = random.randint(50, 200) / 100.0
                        if random.randint(0, 1):
                            card.x_speed *= -1
                        jumping_cards.append(card)
                    else:
                        self.new_game()
                        self.scene = self.game_scene()
                        return

            def update_cards():
                for c in jumping_cards[:]:
                    c.move()
                    if c.rect.right < 0 or c.rect.left > RES[0]:
                        jumping_cards.remove(c)
                        continue
                    if c.rect.bottom > RES[1] and c.y_speed > 0:
                        c.rect.bottom = RES[1]
                        c.x, c.y = c.rect.centerx, c.rect.centery
                        c.jump_speed_max *= 0.95
                        c.y_speed = c.jump_speed_max

            def blit_cards():

                for c in jumping_cards:
                    self.blit_sprite(c)

            self.input_update()

            if self.check_ESC_pressed():
                self.new_game()
                self.scene = self.game_scene
                return

            append_cards()
            update_cards()
            blit_cards()

            self.clock.tick()        

    def game_scene(self):

        while 1:

            self.input_update()

            if self.check_ESC_pressed():
                self.new_game()
                continue

            if self.check_game_won():
                self.scene = self.game_won_scene
                return

            self.blit_board()

            if self.mouse.ready and LEFT_BUTTON in self.mouse.pressed and not len(self.cursor_stack.cards):
                self.mouse.ready = False
                self.check_pick_up_cards()
                self.check_deal_from_stock()
            elif len(self.cursor_stack.cards) and not LEFT_BUTTON in self.mouse.pressed:
                self.check_drop_cards()
            elif self.mouse.ready and RIGHT_BUTTON in self.mouse.pressed:
                self.check_direct_drop()
                self.mouse.ready = False

            self.blit_stacks()

            self.clock.tick()

    def run_scene(self):
        """Ruft die aktuelle Szene [self.scene] (= Methode!) auf"""

        self.scene()
      
    def run(self):

        self.new_game()
        self.blit_board()
        self.clock.tick(50)
        self.scene = self.game_scene
        while self.scene:
            self.run_scene()
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    ni = Game()
    ni.run()
