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

obstacles = []


#loop this for the needed number of obstacles, read from file
for x in range(4):
    obstacles.append(Ball())


obstacleSize = 200
#loop this to set start pos for balls, read from file
for x in range(len(obstacles)):
    
    obstacles[x].setStartPos(obstacleSize,50)
    obstacleSize += 100





#game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
    
    controller.userInput(u1)
    controller.collisionDetection(u1,obstacles)
    obj.viewUpdate(u1,obstacles)   

