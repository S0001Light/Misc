import pygame
from pygame.locals import *
from sys import exit

from random import randint

pygame.init()
screen = pygame.display.set_mode((400, 260), 0, 32)

while True:
        
        for event in pygame.event.get():
                if event.type == QUIT:
                        exit()
        
        rand_color3 = (randint(0, 4), randint(0, 4), randint(20,250))
        a = 1
        while a in range(-1, 400):
                a += 1
                pos_1 = a
                b = 1
                while b in range(-260, 260):
                        b += 1
                        c = (a, b)
                        screen.set_at(c,rand_color3)
        
        pygame.display.update()
                        
        
