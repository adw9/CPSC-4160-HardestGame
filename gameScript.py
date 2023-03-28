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


#game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
    
    controller.userInput(u1)
    controller.collisionDetection(u1,ball)
    obj.viewUpdate(u1,ball)   

