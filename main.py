import sys, pygame
import math
from time import time, sleep

class Main():
    endgame = False
    
    def __init__(self):
        endgame = False
        pygame.init()
        size = width, height = 320, 240
        screen = pygame.display.set_mode(size)


    def run(self):
        while not self.endgame:
            start = time()
            #do something
            current = time()
            #If the frame is ahead of schedule time do this
            if current - start <= 1/60:
                sleep(1/60 - (current - start))
            #if the friend is behind of schedule do this
            else:
                ticks = math.floor((current-start)/(1/60))
                while ticks>0:
                    ticks -= 1

main = Main()
main.run()

"""
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("Mac-Man_sprite.png")
ballrect = ball.get_rect()

count = 0
""" 