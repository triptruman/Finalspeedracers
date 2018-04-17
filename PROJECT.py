####### 
##I am working on this project with Gabe Byder,
#  and initially, we were thinking of doing an arcade type game.
#  After toying around and thinking about this idea, we would rather have one
#  quality game rather than many games that are not up to par. 
# Gabe and I pivoted and will now be working on a 2d driving/racing simulator. 
# # # ####### 
# # # ##I am working on this project with Gabe Byder,
# # # #  and initially, we were thinking of doing an arcade type game.
# # # #  After toying around and thinking about this idea, we would rather have one
# # # #  quality game rather than many games that are not up to par. 
# # # # Gabe and I pivoted and will now be working on a 2d driving/racing simulator. 


# # # 1. ##What's your project?
# # # 2. ##What is your first major milestone?
# # # 3. ##What do you not know that you will need to learn?
# # # 4. ###In what ways is your project too ambitious?
# # # 5. ##In what ways is it possibly not ambitious enough?

# # 1. I am working on this project with gabe byder, our project is a 2d driving simulator/racing game
# # 2. our first major milestone is getting the car to move around on the screen
# # 3. what we need to learn is how to make the screen move behind the car, and create a low grade AI to make a computer
# # race agains the player
# # 4. our project is a bit too ambitious in that we will need to create a form of AI 
# # # 5. our projects is possibly not ambitious enough because our graphics may not be high grade 

#####CODE PROGRESS OVER BREAK

##THE following is taken from/derived from page 241 of the python crash course pdf

invasion.py
import pygame
def run_game():
 # creating the platform for the game, and making an object on the screen
    pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Speed Racers")
 # Starting the loop for the game 
while True:
 # Only using the keyuboard in the game, no mouse needed
 for event in pygame.event.get():
    if event.type == pygame.QUIT:
    sys.exit()

 ### Making screen visible
 pygame.display.flip()
run_game()


####the following is taken from/derived from page 242 in the python book

 def  run_game():
    
 pygame.display.set_caption("Speed Racers")
 # making the background color (subject to change)
 ###currently i have the color bisque4
u bg_color = (139,125,107)
 # Start the main loop for the game.
 while True:
 # Watch for keyboard events
 # Redraw the screen during each pass through the loop.
v screen.fill(bg_color)
 # Make the most recently drawn screen visible.
 pygame.display.flip()
run_game()




####now i will be creating a class
####the following is taken from/derived from page 243 in the python book
invasion.py import pygame
from settings import Settings
def run_game():
 # Initialize pygame, settings, and screen object.
 pygame.init()
 ai_settings = Settings()
vscreen = pygame.display.set_mode(
 (ai_settings.screen_width, ai_settings.screen_height))
 pygame.display.set_caption("Speed Racers")
 # Start the main loop for the game.
 while True:
 # Redraw the screen during each pass through the loop.
screen.fill(ai_settings.bg_color)

 # Make the most recently drawn screen visible.
 pygame.display.flip()


 ###the following is taken from page 245 in the python book 

 ### i will now CREATE the class for the RACE CAR (PALINDROME)


import pygame
class RACE CAR():
 def __init__(self, screen):
 """INitialize race car and get starting position."""
 self.screen = screen
 # Load the race car image and get its rect.
 self.image = pygame.image.load('images/race car.bmp')
self.rect = self.image.get_rect()
 self.screen_rect = screen.get_rect()

