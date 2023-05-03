import pygame
import sys
from mainView import View
from player import Player
from controller import mainController
from ball import Ball

lvlDict = {
1 : "L1.txt",
2 : "L2.txt",
3 : "L3.txt",
4 : "L4.txt",
5 : "L5.txt"
}



#Startup, create objects
pygame.init()
obj = View()
u1 = Player()
controller = mainController()


#this stores the red balls that kill the player
obstacles = []

#this stores the start/finish zones
startFinish = []

#this stores the one/multiple tokens to collect
tokens = []

#this stores powerup data
powerup = []


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

startFinish.append(pygame.Rect(startX, startY, 100, 200))
startFinish.append(pygame.Rect(finishX, finishY, 100, 200))

#set token, read from file
tokenX = 200
tokenY = 200

tokens.append(pygame.Rect(tokenX,tokenY,20,20))

#set powerup, read from file
powerupX = 200
powerupY = 400
powerupType = 1

powerup.append(pygame.Rect(powerupX,powerupY,20,20))

#type 1 is shield, type 2 is speed?
powerup.append(powerupType)






#game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
    
    controller.userInput(u1)
    controller.collisionDetection(u1,obstacles,startFinish,tokens,powerup)
    obj.viewUpdate(u1,obstacles,startFinish,tokens,powerup)   

    if(controller.winner == True):
        pygame.quit() 
        sys.exit()

