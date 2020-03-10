import pygame
import sys
from pygame.locals import *

pygame.init()

maSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Space invaders')

fond = pygame.image.load('assets/bg.jpg')
fond = pygame.transform.scale(fond, (640, 480))

vaisseau = pygame.image.load('assets/fusee.png')
vaisseau = pygame.transform.scale(vaisseau, (120, 80))

maSurface.blit(fond, (0, 0))
maSurface.blit(vaisseau, (320, 400))

inProgress = True
x = 250
y = 400

while inProgress:
    for event in pygame.event.get():
        if event.type == QUIT:
            inProgress = False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                x += 50
            if event.key == K_LEFT:
                x -= 50

    maSurface.blit(fond, (0, 0))
    maSurface.blit(vaisseau, (x, y))
    pygame.display.update()

pygame.quit()
