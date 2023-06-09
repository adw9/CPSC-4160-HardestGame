import pygame


class Player():
    rectColor = (155,0,255)
    rectSize = rectWidth, rectHeight = 50, 50
    rectPos = rectX, rectY = 0, 0
    rectSpeed = 0

    spawnX = 0
    spawnY = 0

    gotToken = False
    shield = 0

    SCREEN_HEIGHT = 0

    gameRect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)
    
    
    def __init__(self):
        self.rectY = 400
        self.rectSpeed = .5
        self.SCREEN_HEIGHT = 400
        self.gameRect = pygame.Rect(self.rectX, self.rectY, self.rectWidth, self.rectHeight)


    def move_rect(self,input):
        if(input == "UP"):
            self.rectY -= self.rectSpeed
        elif(input == "DOWN"):
            self.rectY += self.rectSpeed
        elif(input == "LEFT"):
            self.rectX -= self.rectSpeed
        elif(input == "RIGHT"):
            self.rectX += self.rectSpeed
            

        #update gameRect with new var
        self.gameRect = pygame.Rect(self.rectX, self.rectY, self.rectWidth, self.rectHeight)

    def reset_player(self):
        self.rectY = self.spawnY
        self.rectX = self.spawnX
        self.gameRect = pygame.Rect(self.rectX, self.rectY, self.rectWidth, self.rectHeight)
        self.rectSpeed = .5
        self.shield = 0

    def setSpawn(self,spX,spY):
        self.spawnX = spX
        self.spawnY = spY

    def speedPowerup(self):
        self.rectSpeed = .75


