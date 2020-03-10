import pygame
import sys
from pygame.locals import *
import threading
import time
import os
import playsound


class bullet:
    posX = 0
    posY = 0
    radius = 5

    def __init__(self, vaisseauX, vaisseauY):
        self.posX = vaisseauX + 58
        self.posY = vaisseauY
        launche = threading.Thread(target=self.__launch)
        launche.start()

    def __launch(self):
        while self.posY > 0:
            time.sleep(0.05)
            self.posY = self.posY - 10

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0),
                           (self.posX, self.posY), self.radius)


pygame.init()
bullets = []
listeAlien = []
block = []

maSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Space invaders')

fond = pygame.image.load('assets/bg.jpg')
fond = pygame.transform.scale(fond, (640, 480))

vaisseau = pygame.image.load('assets/fusee.png')
vaisseau = pygame.transform.scale(vaisseau, (120, 80))

alien = pygame.image.load('assets/alien.png')
alien = pygame.transform.scale(alien, (40, 30))

inProgress = True
vaisseauX = 250
vaisseauY = 400

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

score: int = 0


def setScore():
    global score
    global textsurface
    score += 1
    textsurface = myfont.render(
        ' Score : ' + str(score), False, (255, 255, 255))
    maSurface.blit(textsurface, (0, 0))


myfont = pygame.font.SysFont('', 30)
textsurface = myfont.render(' Score : '+str(score), False, (255, 255, 255))


def afficheAlien(alien, listeAlien):
    for x in range(len(listeAlien)):
        if listeAlien[x][2] == True:
            maSurface.blit(
                alien, (listeAlien[x][0], listeAlien[x][1]))


def creationAlien(listeAlien):
    x = 20
    y = 50
    etat = True
    for y in range(50, 150, 30):
        for x in range(40, 600, 40):
            listeAlien.append([x, y, etat])


def redrawGameWindow():
    maSurface.blit(fond, (0, 0))
    maSurface.blit(vaisseau, (vaisseauX, vaisseauY))
    # alien
    afficheAlien(alien, listeAlien)
    # block
    block.append(pygame.draw.rect(maSurface, WHITE, [50, 340, 80, 40]))
    block.append(pygame.draw.rect(maSurface, WHITE, [200, 340, 80, 40]))
    block.append(pygame.draw.rect(maSurface, WHITE, [350, 340, 80, 40]))
    block.append(pygame.draw.rect(maSurface, WHITE, [500, 340, 80, 40]))
    maSurface.blit(textsurface, (0, 0))
    # handle bullets
    for bullet in bullets:
        if(bullet.posY <= 5):
            bullets.remove(bullet)
        for b in block:
            if(bullet.posX >= b[0] and bullet.posX <= b[0] + 80):
                bullets.remove(bullet)
                break
        for x in range(len(listeAlien)):
            if bullet.posX >= listeAlien[x][0] and bullet.posX <= listeAlien[x][0] + 40 and listeAlien[x][2] == True:
                if bullet.posY >= listeAlien[x][1] and bullet.posY <= listeAlien[x][1] + 30 and listeAlien[x][2] == True:
                    bullets.remove(bullet)
                    setScore()
                    listeAlien[x][2] = False
                    alienDead = threading.Thread(target=playExplosion)
                    alienDead.start()
                    break
        bullet.draw(maSurface)
    pygame.display.update()


def playLazer():
    playsound.playsound('assets/lazer.mp3')


def playExplosion():
    playsound.playsound('assets/explo.mp3')


clock = pygame.time.Clock()
creationAlien(listeAlien)
while inProgress:
    for event in pygame.event.get():
        if event.type == QUIT:
            inProgress = False
        if event.type == KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                if(vaisseauX + 20 + 100 <= 640):
                    vaisseauX += 20
            if keys[pygame.K_LEFT]:
                if(vaisseauX + 20 >= 0):
                    vaisseauX -= 20
            if keys[pygame.K_SPACE]:
                lazerT = threading.Thread(target=playLazer)
                lazerT.start()
                bullets.append(bullet(vaisseauX, vaisseauY))
    redrawGameWindow()
    clock.tick(100)

pygame.quit()
