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

    winner = False
    

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

    def collisionDetection(self, u1, obstacles,startFinish,tokens,powerup):
        

        #manage obstacles
        for x in range(len(obstacles)):


            if(u1.gameRect.colliderect(obstacles[x].gameRect)):
                obstacles[x].moveLeft = False

            #collision detection between obstacles[x] and outside walls
            if(obstacles[x].gameRect.colliderect(self.topWall)):
                obstacles[x].moveDown = True
            elif(obstacles[x].gameRect.colliderect(self.botWall)):
                obstacles[x].moveDown = False

            if(obstacles[x].gameRect.colliderect(u1.gameRect)):
                u1.reset_player()

            obstacles[x].move_ball()

        #manage tokens
        for x in range(len(tokens)):
            if(u1.gameRect.colliderect(tokens[x])):
                tokens.pop(x)
                u1.gotToken = True
        
        #hardcoded to 1 since this will always be the finish zone
        if(u1.gameRect.colliderect(startFinish[1])):
            if(u1.gotToken == True):
                print("You win!")
                self.winner = True

        #hardcoded to 0 since there will always be a single powerup
        if(u1.gameRect.colliderrect(powerup[0])):
            match powerup[1]:
                case 1:
                    u1.gotShield = True
                    
                case 2:
                    u1.gotSpeed = True



        