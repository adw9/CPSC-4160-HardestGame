import pygame


class mainController():
    #need a better solution for a var to pass than a bool
    #true = up, false = down
    input = False
    #top/left/right/bottom screen bounds
    topWall = pygame.Rect(0, -5, 700, 5)
    botWall = pygame.Rect(0, 500, 700, 5)
    leftWall = pygame.Rect(0,0,5,700)
    rightWall = pygame.Rect(700,0,5,700)
    

    def userInput(self, u1):
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_UP] and not u1.gameRect.colliderect(self.topWall)):
            input = True
            u1.move_rect(input)
        elif(keys[pygame.K_DOWN] and not u1.gameRect.colliderect(self.botWall)):
            input = False
            u1.move_rect(input)
        elif(keys[pygame.K_LEFT] and not u1.gameRect.colliderect(self.leftWall)):
            input = True
            u1.move_rect(input)
        elif(keys[pygame.K_RIGHT] and not u1.gameRect.colliderect(self.rightWall)):
            input = False
            u1.move_rect(input)

    def collisionDetection(self, u1, ball):

        if(u1.gameRect.colliderect(ball.gameRect)):
            ball.moveLeft = False

        #collision detection between ball and outside walls
        if(ball.gameRect.colliderect(self.topWall)):
            ball.moveDown = True
        elif(ball.gameRect.colliderect(self.botWall)):
            ball.moveDown = False
        elif(ball.gameRect.colliderect(self.leftWall)):
            
            ball.moveLeft = False
            ball.ball_reset()

        elif(ball.gameRect.colliderect(self.rightWall)):
            
            ball.moveLeft = True
            ball.ball_reset()


        ball.move_ball()
