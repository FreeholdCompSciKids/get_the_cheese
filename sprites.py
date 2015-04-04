import pygame
from pygame.locals import *

from globals import *

import random, math

#--------------------------------------------------------------------------------
# Basic Creature
#

class Creature(pygame.sprite.Sprite):

    def __init__(self, imageName, speed=0, startX=None , startY=None):
        super(Creature,self).__init__()

        imagePath = "./images/" + imageName

        self.image = pygame.image.load(imagePath).convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = speed

        if startX is None:
            self.rect.centerx = random.randint(0,MAX_X)

        if startX is None:
            self.rect.centery = random.randint(0,MAX_Y)

        # self.direction of 0  means that it is not being used - 
        #  Creatures that want to use it to control motion need to update the value
        self.x_direction = 0
        self.y_direction = 0


    def keep_on_screen(self):
        if self.rect.right > MAX_X:
            self.rect.right = MAX_X
            self.x_direction *= -1
        elif self.rect.left < 0:
            self.rect.left = 0
            self.x_direction *= -1

        if self.rect.bottom > MAX_Y:
            self.rect.bottom = MAX_Y
            self.y_direction *= -1
        elif self.rect.top < 0:
            self.rect.top = 0
            self.y_direction *= -1


#--------------------------------------------------------------------------------
# Cat
#

class Cat(Creature):

    def __init__(self):
        super(Cat,self).__init__("cat.png", speed=3)

        self.speed = random.randint(1,3)
        self.x_direction = 1 
        self.y_direction = 0 # no up-down movement


    def update(self):
        self.rect.x += (self.speed * self.x_direction) 
        self.rect.y += (self.speed * self.y_direction) 
        self.keep_on_screen()

#--------------------------------------------------------------------------------
# Goat
#


class Mouse(Creature):

    def __init__(self):
        super(Mouse,self).__init__("mouse.png", speed=6)

        #set starting point to middle of the bottom part of the screen
        self.rect.centerx = MAX_X // 2
        self.rect.bottom = MAX_Y


    def update(self, key):

        if key == pygame.K_UP:
            self.rect.y -= self.speed
        elif key == pygame.K_DOWN:
            self.rect.y += self.speed
        elif key == pygame.K_LEFT:
            self.rect.x -= self.speed
        elif key == pygame.K_RIGHT:
            self.rect.x += self.speed

        self.keep_on_screen()


#--------------------------------------------------------------------------------
# Goat
#

class Goat(Creature):

    def __init__(self):
        super(Goat,self).__init__("goat.png", speed=3)

        self.speed = random.randint(1,2)
        self.x_direction = 0 
        self.y_direction = 2 # no up-down movement


    def update(self):
        self.rect.x += (self.speed * self.x_direction) 
        self.rect.y += (self.speed * self.y_direction) 
        self.keep_on_screen()




#--------------------------------------------------------------------------------
# Other
#


class Cheese(Creature):
    def __init__(self):
        super(Cheese,self).__init__("cheese.png")





