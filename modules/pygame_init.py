#IMPORTING PYGAME LIBRARY
import pygame
#IMPORTING EVERYTHING FROM CONFIG IN MODULES FOLDER
from modules.config import *

#ROOT CLASS
class Root:
    #INITIALIZE OF PYGAME ROOT
    def __init__(self):
        #SETTING UP PYGAME CLOCK
        self.clock = pygame.time.Clock()
        #SETTING GAME FPS
        self.fps = FPS
        #SETTING DELTA TIME
        self.dt = self.clock.tick(self.fps)
        #PYGAME INIT
        pygame.init()
        #SETTING SCREEN WITH WIDTH AND HEIGHT FROM CONFIG
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))