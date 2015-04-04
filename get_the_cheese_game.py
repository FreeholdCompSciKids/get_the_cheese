import pygame
from pygame.locals import *

from globals import *

import random, math
import time

from sprites import *


#------------------------------------------------------------
# main part of the program
#



class GetTheCheeseGame(object):

    FPS=60  #determines how fast the games move - higher number, faster game

    MSG_BOX_HEIGHT=50

    #--------------------------------------------------------------------------------
    # game set-up functions
    #

    def __init__(self):
        self.setup_variables()
        self.setup_gameboard()
        self.setup_sprites()


    def setup_variables(self):
        self.score = 0
        self.level = 1

        self.num_starting_cats = 2
        self.num_cheese_per_level = 5

    def setup_gameboard(self):
        pygame.init()

        pygame.display.set_caption("Cat and Mouse")
        self.screen = pygame.display.set_mode([MAX_X, MAX_Y + self.MSG_BOX_HEIGHT])
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(1000/self.FPS); # pressed key, will repeat triggering

        self.print_level()
        self.print_score()
        

    def draw_first_gameboard(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.allSpritesGroup.draw(screen)
        pygame.display.flip()

    #--------------------------------------------------------------------------------
    # sprites set up functions
    #

    def add_cheese(self, num_cheese):
        for i in range(num_cheese):
            cheese = Cheese()
            self.eatMeGroup.add(cheese)
            self.allSpritesGroup.add(cheese)

    def add_cats(self, num_cats):
        for i in range(num_cats):
            cat = Cat()
            self.dontTouchGroup.add(cat)
            self.allSpritesGroup.add(cat)

    
    def add_goats(self, num_goats):
        for i in range(num_goats):
            goat = Goat()
            self.dontTouchGroup.add(goat)
            self.allSpritesGroup.add(goat)        
    

    def setup_sprites(self):
        #create sprite groups
        self.allSpritesGroup = pygame.sprite.Group()
        self.playerSpriteGroup = pygame.sprite.GroupSingle()
        self.eatMeGroup = pygame.sprite.Group()
        self.dontTouchGroup = pygame.sprite.Group()

        # create the player character - a single mouse
        self.mouse = Mouse()
        self.playerSpriteGroup.add(self.mouse)
        self.allSpritesGroup.add(self.mouse)

        # create cats
        self.add_cats(self.num_starting_cats)

        # create cheese
        self.add_cheese(self.num_cheese_per_level)


   #--------------------------------------------------------------------------------
   # printing functions
   #

    def print_level(self):
        self.print_in_msg_box("Level " + str(self.level), BLACK, 110, 20, 24)

    def print_score(self):
        self.print_in_msg_box("Score " + str(self.score), RED, 310, 20, 24)

    def print_in_msg_box(self, msg, fg_color, x_pos, y_pos, size):
        self.print_msg(msg, fg_color, x_pos, MAX_Y + y_pos, size)

    def print_msg(self, msg, fg_color, x_pos, y_pos, size):
        fontObj = pygame.font.Font("freesansbold.ttf",size)
        textSurface = fontObj.render(msg, True, fg_color, BACKGROUND_COLOR)
        textRect = textSurface.get_rect()
        textRect.center = (x_pos, y_pos)
        self.screen.blit(textSurface, textRect)
        return (textSurface,textRect)

    def print_flash_screen(self, msg, fg_color):
        self.screen.fill(BACKGROUND_COLOR)
        self.print_msg(msg, fg_color, MAX_X / 2, MAX_Y / 2, 48)
        pygame.display.flip()

        time.sleep(2)
        

    def next_level(self):
        #move to next level
        self.level += 1
        self.add_cats(self.num_starting_cats)
        self.add_goats(2)
        self.add_cheese(self.num_cheese_per_level)
        self.print_flash_screen("Level" + str(self.level) , BLACK)


   #--------------------------------------------------------------------------------
   # run function - this will run the game
   #

    def run(self):
        done = False
        while not done:
    
            for event in pygame.event.get():
                if (event.type == pygame.QUIT 
                            or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE) ) :
                    pygame.quit()
                elif event.type == pygame.KEYDOWN :
                    self.playerSpriteGroup.update(event.key)
    
            self.screen.fill(BACKGROUND_COLOR)
    
            #move cats
            self.dontTouchGroup.update()
    
            #check if we ate all the cheese
            if pygame.sprite.spritecollide( self.mouse,  self.eatMeGroup, True):
                self.score += 1
                if len(self.eatMeGroup) == 0:
                    self.next_level()
                    
            #check if we were eaten by the cats
            if pygame.sprite.spritecollide( self.mouse, self.dontTouchGroup, False) :
                self.print_flash_screen("YOU LOST", RED)
                done = True 
    
            #redraw all the sprites and update screen
            self.allSpritesGroup.draw(self.screen)

            self.print_score()
            self.print_level()
    
            #make chages to screen visible
            self.clock.tick(self.FPS)
            pygame.display.flip()
    
    
