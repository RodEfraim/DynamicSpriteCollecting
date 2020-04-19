"""
Project: Dynamic Sprite Collector Game
Author: Rodrigo Efraim
Python Version: 3.6.3 :: Anaconda custom (64-bit)
Pygame Version: 1.9.6
"""
import pygame
import random
#import block_library
#import player_library
import game_library
 
# --- Global constants ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
 
def main():
    """ Main program function. """
    # Initialize Pygame and set up the window.
    pygame.init()
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("My Game")

    #Loading the sounds.
    good_sound = pygame.mixer.Sound("sonic-ring.ogg")
    bad_sound = pygame.mixer.Sound("error-beep.ogg")
    thud_sound = pygame.mixer.Sound("thud-sound.ogg")
 
    # Create our objects and set the data.
    done = False
    clock = pygame.time.Clock()
 
    # Create an instance of the Game class
    game = game_library.Game()
 
    # Main game loop
    while not done:
 
        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
 
        # Update object positions, check for collisions
        game.run_logic(good_sound, bad_sound, thud_sound)
 
        # Draw the current frame
        game.display_frame(screen)
 
        # Pause for the next frame
        #These value might need to be changed depending on the monitor.
        #clock.tick(60)
        clock.tick(30)
 
    # Close window and exit
    pygame.quit()
 
# Call the main function, start up the game
if __name__ == "__main__":
    main()
