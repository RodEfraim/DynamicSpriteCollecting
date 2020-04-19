"""
Project: Dynamic Sprite Collector Game
Class: Player
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
 

class Player(pygame.sprite.Sprite):
    """ This class represents the player. """
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLUE)

        #Make the top left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        #Speed Vector
        self.change_x = 0
        self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    def update_player(self, thud_sound):
        """ Update the player location."""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if(self.rect.x < 0):
            self.rect.x = 0
            thud_sound.play()
        elif(self.rect.x > (SCREEN_WIDTH - 20)):
            self.rect.x = SCREEN_WIDTH - 20
            thud_sound.play()
        elif(self.rect.y < 0):
            self.rect.y = 0
            thud_sound.play()
        elif(self.rect.y > (SCREEN_HEIGHT - 20)):
            self.rect.y = SCREEN_HEIGHT - 20
            thud_sound.play()

