#IMPORTING PYGAME LIBRARY
import pygame
#IMPORTING EVERYTHING FROM CONFIG IN MODULES FOLDER
from modules.config import *

#SHAPE CLASS
class Shape():
    #INITIALIZE OF SHAPE
    def __init__(self, pos: list, size: list, color, shape: str) -> None:

        #POSITION OF SHAPE
        self.pos = pos
        #COLOR OF SHAPE
        self.color = color
        #SIZE OF SHAPE
        self.size = size
        #SHAPE OF SHAPE
        self.shape = shape

        #IMAGE OF SHAPE
        self.image = pygame.Surface(self.size)
        #RECT OF SHAPE
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos)

    #RENDER PROCEDURE
    def render(self, screen):
        #IF SHAPE OF RECTANGLE
        if self.shape == RECT:
            #DRAWING RECTANGLE WITH PARAMETERS
            pygame.draw.rect(screen, self.color, pygame.Rect(self.rect))
        #IF SHAPE OF CIRCLE
        elif self.shape == CIRCLE:
            #DRAWING CIRCLE WITH PARAMETERS
            pygame.draw.circle(screen, self.color, self.pos, self.size[0]/2, 0)
    
    #CONFIGURE PROCEDURE
    def configure(self, new_color):
        #SETTING NEW COLOR FOR SHAPE
        self.color = new_color