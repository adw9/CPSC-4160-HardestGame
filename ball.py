import pygame


class Ball():
    #storage vars
    diameter = 0
    color = (0,0,0)
    ballPos = ballX, ballY = 0, 0
    speedX = 0
    speedY = 0

    moveLeft = True
    moveDown = True


    #collision detection vars
    rectWidth = 0
    rectHeight = 0
    gameRect = pygame.Rect(ballX, ballY, rectWidth, rectHeight)

    def __init__(self):
        self.ballPos = self.ballX, self.ballY = 350, 250
        self.diameter = 10
        self.color = (255,0,0)
        self.speedX = .05
        self.speedY = .05


        self.rectWidth = 10
        self.rectHeight = 10

    def move_ball(self):            
        #
        #if(self.moveLeft):
            #self.ballX -= self.speedX
        #else:
            #self.ballX += self.speedX
        
        if(self.moveDown):
            self.ballY += self.speedY
        else:
            self.ballY -= self.speedY

        #update gameRect with new var
        self.ballPos = self.ballX, self.ballY
        self.gameRect = pygame.Rect(self.ballX, self.ballY, self.rectWidth, self.rectHeight)
    
    #this funct may be unnecesary after pong, keeping just incase
    def ball_reset(self):
        self.ballPos = self.ballX, self.ballY = 350, 250
        self.gameRect = pygame.Rect(self.ballX, self.ballY, self.rectWidth, self.rectHeight)
    
    
    def setStartPos(self, x, y):
        self.ballX = x
        self.ballY = y

        #update gameRect, not sure if I have to actually do this
        self.gameRect = pygame.Rect(self.ballX, self.ballY, self.rectWidth, self.rectHeight)
        