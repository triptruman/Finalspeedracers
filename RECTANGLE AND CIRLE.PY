import math, random, sys
import pygame
from pygame.locals import*

#exit the program

def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key==K _ESCAPE):
            pygame.quit()
            sys.exit()

            # define display surface			
W, H = 1280, 720
HW, HH = W / 2, H / 2
AREA = W * H


# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Scrolling Background with Player")
FPS = 500

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
BROWN = (139, 69, 19)


# main loop
time = 0
factor = 0
while True:
	#check if close game
	events()
	#short hand to call key presses
	k = pygame.key.get_pressed()
	
	if k[K_RIGHT]:
		playerVelocityX = 2.5
	elif k[K_LEFT]:
		playerVelocityX = -2.5
	elif k[K_SPACE]:
		if playerPosY <= 610:
			playerVelocityY = -2.5
	elif k[K_d]:
		print(str(playerPosX) + ", " + str(playerPosY))
	else:
		playerVelocityX = 0

	#max cords to limit and control jumping
	if playerPosY <= 500:
		playerVelocityY = 2.5
	if playerPosY > 610:
		playerVelocityY = 0
		playerPosY = 610



#####MUST PUT THE CLASS FOR THE RECTANGLE HERE!!!!!!!!!!!
####2:40  CODE.PYLET 
#### i used the same class that pylet used, need to adjust for our code

class rectangle:
    def_init_(self,x,y,w,h,id):
    global BROWN
    self.x1= x
    self.y1 = y
    self.x2 = x + w
    self.y2 = y + h

    self.w = w
    self.h = h 

    self.fillColor = Brown

    self.stained = False
    self.id = id


    def setXY(self,xy):
    self.x1, self.y1 = xy
    self.x2 = xy[0] + self.w
    self.y2 = xy[1] + self.h

def getXY(SELF):
    return(self.x1,self.y1)

def rect(self):
    return self.getXY() + (self.w, self.h)

def coords(self):
    return self.getXY() + (self.x2, self.y2)

def hasCOLLIDED(self,target):
    tx1,ty1,tx2,ty2=target.coords()
    if tx>1 self.x2 or tx2 <self.x1 or ty1 > self.y2 or ty2 < self.y1:return False
    return True

def draw(self, surface = None):
    if not surface: surface = pygame.display.get_surface()
    pygame.draw.rect(surface,self.fillColor, SELF.RECT(),0)


rectangles=list(rectangle(random.r)



    #####THE FOUR TESTS WE NEED TO PERFORM TO RETURN FALSE
# # # #   IS THE target's x1 greater than source's x2?

# # # # is the target's x2 less than the source's x1?
# # # # is the target's y1 greater than source's y2?
# # # # and 
# # # # is the target's y2 less than the source's y1??


    #######4.38 PYLET 
      



      ######9.14 













