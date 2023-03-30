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
            input = "UP"
            u1.move_rect(input)
        elif(keys[pygame.K_DOWN] and not u1.gameRect.colliderect(self.botWall)):
            input = "DOWN"
            u1.move_rect(input)
        elif(keys[pygame.K_LEFT] and not u1.gameRect.colliderect(self.leftWall)):
            input = "LEFT"
            u1.move_rect(input)
        elif(keys[pygame.K_RIGHT] and not u1.gameRect.colliderect(self.rightWall)):
            input = "RIGHT"
            u1.move_rect(input)

    def collisionDetection(self, u1, obstacles):
        
        for x in range(len(obstacles)):


            if(u1.gameRect.colliderect(obstacles[x].gameRect)):
                obstacles[x].moveLeft = False

            #collision detection between obstacles[x] and outside walls
            if(obstacles[x].gameRect.colliderect(self.topWall)):
                obstacles[x].moveDown = True
            elif(obstacles[x].gameRect.colliderect(self.botWall)):
                obstacles[x].moveDown = False
            elif(obstacles[x].gameRect.colliderect(self.leftWall)):
                
                obstacles[x].moveLeft = False
                obstacles[x].ball_reset()

            elif(obstacles[x].gameRect.colliderect(self.rightWall)):
                
                obstacles[x].moveLeft = True
                obstacles[x].ball_reset()


            obstacles[x].move_ball()
