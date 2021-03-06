import pygame
from pygame.locals import *


class Wall:
    # set all class variables in the constructor
    def __init__(self, newX, newY):
        self.x = -50
        self.y = 550
        self.img = pygame.image.load("Anvil(1).gif")


    # draw your image
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    # This method will be completed in the Running Man lab
    # set x and y to newX and newY
    def setPos(self, newX, newY):
        self.x = newX
        self.y = newY
        pass

    # DO NOT CHANGE THIS
    # This method returns a rectangle - (x, y, width, height) - that represents
    # the object
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
