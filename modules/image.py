#IMPORTING PYGAME LIBRARY
import pygame
#IMPORTING EVERYTHING FROM CONFIG IN MODULES FOLDER
from modules.config import *

#IMAGE CLASS
class Image():
    #INITIALIZE OF IMAGE
    def __init__(self, pos: list, size: list, image) -> None:

        #POSITION OF IMAGE
        self.pos = pos
        #SIZE OF IMAGE
        self.size = size

        #IMAGE OF IMAGE
        self.image = pygame.image.load(image)
        #TRANSFORMING IMAGE BY SIZE
        self.image = pygame.transform.scale(self.image, self.size)
        #RECT OF IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos)

    #RENDER PROCEDURE
    def render(self, screen):
        #RENDERING IMAGE TO SCREEN
        screen.blit(self.image, self.rect)