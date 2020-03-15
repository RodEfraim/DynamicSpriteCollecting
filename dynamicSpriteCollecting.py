"""
Dynamic Sprite Collector Game
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

class Game(object):
    """ This class represents an instance of the game. If we need to
        reset the game we'd just need to create a new instance of this
        class. """
 
    def __init__(self):
        """ Constructor. Create all our attributes and initialize
        the game. """
 
        self.score = 0
        self.game_over = False
 
        # Create sprite lists.
        self.good_block_list = pygame.sprite.Group()#<-- Everything but the player.
        self.bad_block_list = pygame.sprite.Group() #<-- Everything but the player.
        self.all_sprites_list = pygame.sprite.Group()
 
        # Create the good block sprites.
        for i in range(50):
            block = Block(GREEN)
 
            #TODO: Change the x range starting from (SCREEN_WIDTH - 20) to maybe 900?
            block.rect.x = random.randrange(SCREEN_WIDTH - 20, 1200)
            block.rect.y = random.randrange(SCREEN_HEIGHT - 20)
 
            self.good_block_list.add(block)
            self.all_sprites_list.add(block)

        #Create the bad block sprites.
        for i in range(50):
            bad_block = Block(RED)
           
            #TODO: Change the x range starting from (SCREEN_WIDTH - 20) to maybe 900?
            bad_block.rect.x = random.randrange(SCREEN_WIDTH - 20, 1200)
            bad_block.rect.y = random.randrange(SCREEN_HEIGHT - 20)

            self.bad_block_list.add(bad_block)
            self.all_sprites_list.add(bad_block)
 
        # Create the player
        self.player = Player(20, 250 - 20)
        self.all_sprites_list.add(self.player)
 
    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """

        speed = 8
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            # Set the speed based on the key pressed.
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(-speed, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(speed, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, -speed)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, speed)
            # Reset speed when key goes up.
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(speed, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(-speed, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, speed)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, -speed)
            #Restarts the game.
            elif  event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
 
        return False
 
    def run_logic(self, good_sound, bad_sound, thud_sound):
        """
        This method is run each time through the frame. It
        updates positions and checks for collisions.
        """
        if not self.game_over:
            
            self.player.update_player(thud_sound)
   
            #Makes the good and bad blocks move at a constant velocity to the left.
            for good_block in self.good_block_list:
                good_block.update()
            for bad_block in self.bad_block_list:
                bad_block.update()
 
            # See if the player block has collided with anything.
            good_hit_list = pygame.sprite.spritecollide(self.player, self.good_block_list, True)
            bad_hit_list = pygame.sprite.spritecollide(self.player, self.bad_block_list,True)
 
            # Check the list of collisions.
            for block in good_hit_list:
                self.score += 1
                good_sound.play()
                print(self.score)

            #Loose points for colliding with bad blocks.
            for block in bad_hit_list:
                self.score -= 1
                bad_sound.play()
                print(self.score)
 
            if len(self.good_block_list) == 0:
                self.game_over = True
 
    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill(WHITE)
 
        if self.game_over:
            font = pygame.font.SysFont("serif", 25)
            text1 = font.render("Game Over", True, BLACK)
            text2 = font.render("Your Score: " + str(self.score) + "/50", True, BLACK)
            text3 = font.render("Click to restart" , True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text1.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text1.get_height() // 2)
            screen.blit(text1, [center_x, center_y])
            screen.blit(text2, [center_x, center_y + 30])
            screen.blit(text3, [center_x, center_y + (30 * 2)])
 
        if not self.game_over:
            self.all_sprites_list.draw(screen)
            
            # Select the font to use, size, bold, italics
            font = pygame.font.SysFont('Calibri', 25, True, False)
             
            # Render the text. "True" means anti-aliased text.
            # Black is the color. The variable BLACK was defined
            # above as a list of [0, 0, 0]
            # Note: This line creates an image of the letters,
            # but does not put it on the screen yet.
            text = font.render("Score: " + str(self.score),True,BLUE)
             
            # Put the image of the text on the screen at 250x250
            screen.blit(text, [10, 10])
 
        pygame.display.flip()
 
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
    game = Game()
 
    # Main game loop
    while not done:
 
        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
 
        # Update object positions, check for collisions
        game.run_logic(good_sound, bad_sound, thud_sound)
 
        # Draw the current frame
        game.display_frame(screen)
 
        # Pause for the next frame
        clock.tick(60)
 
    # Close window and exit
    pygame.quit()
 
# Call the main function, start up the game
if __name__ == "__main__":
    main()
