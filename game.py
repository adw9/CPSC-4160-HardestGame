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
    obstacleX = 200
    obstacleY = 50
    ballSpeed = .05

    startX = 0
    startY = 300
    finishX = 600
    finishY = 0

    tokenX = 200
    tokenY = 200

    powerupX = 200
    powerupY = 400
    powerupType = 1
    
    def fileReader(self,fileName):
       
        with open(fileName, 'r') as f:
            for line in f:
                data = line.split(".")

                match data[0]:
                    case "L0":
                        self.numObstacles = int(data[1])
                        self.obstacleOffset = int(data[2])
                        self.obstacleY = int(data[3])
                        self.ballSpeed = float("."+data[4])
                    case "L1":
                        self.startX = int(data[1])
                        self.startY = int(data[2])
                        self.finishX = int(data[3])
                        self.finishY = int(data[4])
                    case "L2":
                        self.tokenX = int(data[1])
                        self.tokenY = int(data[2])
                    case "L3":
                        self.powerupX = int(data[1])
                        self.powerupY = int(data[2])
                        self.powerupType = int(data[3])
        for x in range(self.numObstacles):
            self.obstacles.append(Ball())
            self.obstacles[x].setSpeed(self.ballSpeed)

        for x in range(len(self.obstacles)):
    
            self.obstacles[x].setStartPos(self.obstacleX,self.obstacleY)
            self.obstacleX += self.obstacleOffset

        self.startFinish.append(pygame.Rect(self.startX, self.startY, 100, 200))
        self.startFinish.append(pygame.Rect(self.finishX, self.finishY, 100, 200))

        self.tokens.append(pygame.Rect(self.tokenX,self.tokenY,20,20))

        self.powerup.append(pygame.Rect(self.powerupX,self.powerupY,20,20))

#type 1 is shield, type 2 is speed?
        self.powerup.append(self.powerupType)

    def resetGame(self):
        for x in range(len(self.obstacles)):
            self.obstacles.pop()
        for x in range(len(self.startFinish)):
            self.startFinish.pop()
        for x in range(len(self.tokens)):
            self.tokens.pop()
        for x in range(len(self.powerup)):
            self.powerup.pop()
        
