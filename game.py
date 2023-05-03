import pygame
from ball import Ball

class Game():
    #this stores the red balls that kill the player
    obstacles = []

#this stores the start/finish zones
    startFinish = []

#this stores the one/multiple tokens to collect
    tokens = []

#this stores powerup data
    powerup = []



#all of these should read from file
    numObstacles = 4
    obstacleOffset = 200
    obstacleY = 50

    startX = 0
    startY = 300
    finishX = 600
    finishY = 0

    tokenX = 200
    tokenY = 200

    powerupX = 200
    powerupY = 400
    powerupType = 1

    testv = 5
#FILE READING TIME







    for x in range(numObstacles):
        obstacles.append(Ball())

    for x in range(len(obstacles)):
    
        obstacles[x].setStartPos(obstacleOffset,obstacleY)
        obstacleOffset += 100

    startFinish.append(pygame.Rect(startX, startY, 100, 200))
    startFinish.append(pygame.Rect(finishX, finishY, 100, 200))

    tokens.append(pygame.Rect(tokenX,tokenY,20,20))

    powerup.append(pygame.Rect(powerupX,powerupY,20,20))

#type 1 is shield, type 2 is speed?
    powerup.append(powerupType)








