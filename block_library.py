"""
Project: Dynamic Sprite Collector Game
Class: Block
Author: Rodrigo Efraim
Python Version: 3.6.3 :: Anaconda custom (64-bit)
Pygame Version: 1.9.6
"""
import pygame
import random
 
# --- Global constants ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
 
class Block(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """
 
    def __init__(self, color):
        """ Constructor, create the image of the block. """
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(color)
        self.rect = self.image.get_rect()
 
    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        
        #The x respawn range starts from the end of the screen to 1000. Note this is just
        #200 pixels of respawn range from the initial respawn.
        self.rect.x = random.randrange(SCREEN_WIDTH - 20, 1000)
        self.rect.y = random.randrange(SCREEN_HEIGHT - 20)
 
    def update(self):
        """ Automatically called when we need to move the block. """
        self.rect.x -= 5
 
        #if self.rect.y > SCREEN_HEIGHT + self.rect.height:
        #    self.reset_pos()
        if self.rect.x < 0 - self.rect.width:#SCREEN_WIDTH + self.rect.width:
            self.reset_pos()
