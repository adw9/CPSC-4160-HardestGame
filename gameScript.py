import pygame
import sys
from mainView import View
from player import Player
from controller import mainController
from ball import Ball


#Startup, create objects
pygame.init()
obj = View()
u1 = Player()
controller = mainController()
ball = Ball()


#this stores the red balls that kill the player
obstacles = []

#this stores the start/finish zones
startFinish = []

#this stores the one/multiple tokens to collect
tokens = []

#loop this for the needed number of obstacles, read from file
for x in range(4):
    obstacles.append(Ball())


obstacleOffset = 200
#loop this to set start pos for balls, read from file
for x in range(len(obstacles)):
    
    obstacles[x].setStartPos(obstacleOffset,50)
    obstacleOffset += 100

#set start/finish zones, read from file
startX = 0
startY = 300
finishX = 600
finishY = 0

startFinish.append(startX)
startFinish.append(startY)
startFinish.append(finishX)
startFinish.append(finishY)

#set token, read from file
tokenX = 200
tokenY = 200
tokens.append(tokenX)
tokens.append(tokenY)





#game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
    
    controller.userInput(u1)
    controller.collisionDetection(u1,obstacles)
    obj.viewUpdate(u1,obstacles,startFinish,tokens)   

