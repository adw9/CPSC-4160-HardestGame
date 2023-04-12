import pygame
import sys


class View():
   SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 700,500
   surface = pygame.display.set_mode(SCREEN_SIZE)

   screenColor = (50,50,50)


   def __init__(self):
      pygame.display.set_caption("Worlds easiest game?")
      surface = pygame.display.set_mode(self.SCREEN_SIZE)

   def viewUpdate(self, u1,obstacles,startFinish, tokens):
      #background
      self.surface.fill(self.screenColor)
      #draw the ball
      for x in range(len(obstacles)):
         pygame.draw.circle(self.surface, obstacles[x].color, obstacles[x].ballPos, obstacles[x].diameter)
         

      #start/finish squares
      startRect = pygame.Rect(startFinish[0], startFinish[1], 100, 200)
      pygame.draw.rect(self.surface, (0,255,0), startRect)

      startRect = pygame.Rect(startFinish[2], startFinish[3], 100, 200)
      pygame.draw.rect(self.surface, (0,255,0), startRect)

      #tokens
      tokenRect = pygame.Rect(tokens[0],tokens[1],20,20)
      pygame.draw.rect(self.surface,(255,255,0),tokenRect)


      #user square
      pygame.draw.rect(self.surface, u1.rectColor, u1.gameRect)
   
      pygame.display.update()


