# # #week 1 Decided on idea
# # #week 2 
# # #week 3 Had moving car
# # #week 4 Replaced moving car with scrolling background

# # #based off of https://youtu.be/AX8YU2hLBUg
# # import math, random, sys, os, time
# # import pygame
# # from pygame.locals import *

# # # exit the program
# # def events():
# # 	for event in pygame.event.get():
# # 		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
# # 			pygame.quit()
# # 			sys.exit()

# # # define display surface			
# # W, H = 1280, 720
# # HW, HH = W / 2, H / 2
# # AREA = W * H

# # # initialise display
# # pygame.init()
# # CLOCK = pygame.time.Clock()
# # DS = pygame.display.set_mode((W, H))
# # pygame.display.set_caption("code.Pylet - Scrolling Background with Player")
# # FPS = 500

# # # define some colors
# # BLACK = (0, 0, 0, 255)
# # WHITE = (255, 255, 255, 255)

# # bg = pygame.image.load("mario.png").convert()
# # bgWidth, bgHeight = bg.get_rect().size

# # #creating stage
# # stageWidth = bgWidth * 2
# # stagePosX = 0

# # stageHeight = bgHeight * 2
# # stagePosY = 0

# # #set cords
# # startScrollingPosX = HW
# # startScrollingPosY = HH

# # #circle stats
# # circleRadius = 25
# # circlePosX = circleRadius

# # #starting place
# # playerPosX = circleRadius
# # playerPosY = 600
# # playerVelocityX = 0
# # playerVelocityY = 0
# # ###################

# # # main loop
# # time = 0

# # while True:
# # 	#check if close game
# # 	events()
# # 	#short hand to call key presses
# # 	k = pygame.key.get_pressed()
	
# # 	if k[K_RIGHT]:
# # 		playerVelocityX = 2.5
# # 	elif k[K_LEFT]:
# # 		playerVelocityX = -2.5
# # 	elif k[K_SPACE]:
# # 		if playerPosY <= 610:
# # 			playerVelocityY = -2.5
# # 	else:
# # 		playerVelocityX = 0

# # 	#max cords to limit and control jumping
# # 	if playerPosY <= 500:
# # 		playerVelocityY = 2.5
# # 	if playerPosY > 610:
# # 		playerVelocityY = 0
# # 		playerPosY = 610

	
# # 	#moving player on x axis
# # 	playerPosX += playerVelocityX

# # 	circlePosX = startScrollingPosX
# # 	stagePosX += -playerVelocityX

# # 	#moves player on Y axis and influences jumping
# # 	playerPosY += playerVelocityY
# # 	circlePosY = startScrollingPosY

# # 	#moves x cord of screen
# # 	rel_x = stagePosX % bgWidth
# # 	DS.blit(bg, (rel_x - bgWidth, 0))
# # 	if rel_x < W:
# # 		DS.blit(bg, (rel_x, 0))
	
# # 	#draw circle
# # 	pygame.draw.circle(DS, WHITE, (int(circlePosX), int(playerPosY - 25)), int(circleRadius), 0)

# # 	#update screen
# # 	pygame.display.update()
# # 	CLOCK.tick(FPS)
# # 	DS.fill(BLACK)

# # ############



# ####this week i began to work with OPEN CV. 
# # ##MY objective was to attempt to have "mario" sense colors
# # becuase the python program itself cannot sense colors, i was going to use open CV
# # open cv is a low grade artificial intelligence that can detect objects
# # after experimenting with this and working with Mr. Cozort, i realized that there would be an easier way to do this 
# # ###open cv was far too dificult, to work with as artificial inteliigence

# # gabe and i then pivtoed to using a ball for "mario" and have the objects be rectangles
# # the following code is derived from a stack overflow, and adjusted accordingly 

# import math

# def collision(rleft, rtop, width, height,   # rectangle definition
#               center_x, center_y, radius):  # circle definition
#     """ Detect collision between a rectangle and circle. """

#     # setting peramters for the rectangle
#     rright, rbottom = rleft + width/2, rtop + height/2

#     # setting boundaries for the circle
#     cleft, ctop     = center_x-radius, center_y-radius
#     cright, cbottom = center_x+radius, center_y+radius

#     # stating what happens if they do not collide
#     if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
#         return False  # no collision possible

#     # stating what happens if they collide
#     for x in (rleft, rleft+width):
#         for y in (rtop, rtop+height):
#             # compare distance between circle's center point and each point of
#             # the rectangle with the circle's radius
#             if math.hypot(x-center_x, y-center_y) <= radius:
#                 return True  # collision detected

#     # check if center of circle is inside rectangle
#     if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
#         return True  # overlaid

# import math

# def dist(p1, p2, c): 
#     x1,y1 = p1
#     x2,y2 = p2
#     x3,y3 = c
#     px = x2-x1
#     py = y2-y1

#     something = px*px + py*py

#     u =  ((x3 - x1) * px + (y3 - y1) * py) / float(something)

#     if u > 1:
#         u = 1
#     elif u < 0:
#         u = 0

#     x = x1 + u * px
#     y = y1 + u * py

#     dx = x - x3
#     dy = y - y3

#     dist = math.sqrt(dx*dx + dy*dy)

#     return dist


#     rect = [[0. ,  0. ],
#        [ 0.2,  1. ],
#        [ 2.2,  0.6],
#        [ 2. , -0.4]]

# c = 0.5, 2.0
# r = 1.0

# distances = [dist(rect[i], rect[j], c) for i, j in zip([0, 1, 2, 3], [1, 2, 3, 0])]
# print distances
# print any(d < r for d in distances)




######code was not working, trying it again




