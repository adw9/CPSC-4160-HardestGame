import pygame
import sys
from mainView import View
from player import Player
from controller import mainController
from ball import Ball
from game import Game

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
game = Game()
levelKey = 1


game.fileReader(lvlDict[levelKey])

#game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
    
    controller.userInput(u1)
    controller.collisionDetection(u1,game.obstacles,game.startFinish,game.tokens,game.powerup)
    obj.viewUpdate(u1,game.obstacles,game.startFinish,game.tokens,game.powerup)   

    if(controller.winner == True):
        levelKey += 1
        game = Game()
        u1 = Player()
        game.fileReader(lvlDict[levelKey])
        controller.winner = False

        if(levelKey > 5):
            pygame.quit() 
            sys.exit()

