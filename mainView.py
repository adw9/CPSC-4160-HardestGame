import pygame
import sys


class View():
   SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 700,500
   surface = pygame.display.set_mode(SCREEN_SIZE)

   screenColor = (50,50,50)


   def __init__(self):
      pygame.display.set_caption("Worlds easiest game?")
      surface = pygame.display.set_mode(self.SCREEN_SIZE)

   def viewUpdate(self, u1,obstacles):
      #background
      self.surface.fill(self.screenColor)
      #draw the ball
      for x in range(len(obstacles)):
         pygame.draw.circle(self.surface, obstacles[x].color, obstacles[x].ballPos, obstacles[x].diameter)
         
      #user paddles
      pygame.draw.rect(self.surface, u1.rectColor, u1.gameRect)
   
      pygame.display.update()


