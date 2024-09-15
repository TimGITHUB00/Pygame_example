#IMPORTING PYGAME LIBRARY
import pygame
#IMPORTING EVERYTHING FROM CONFIG IN MODULES FOLDER
from modules.config import *

#TEXT CLASS
class Text():
    #INITIALIZE OF TEXT
    def __init__(self, pos, fg, content, fontsize):
        super().__init__()

        #SETTING FONT OF TEXT
        self.font = pygame.font.Font('freesansbold.ttf', fontsize)
        #CONTENT OF TEXT
        self.content = content
        #FOREGROUND COLOR OF TEXT
        self.fg = fg
        #POSITION OF TEXT
        self.pos = pos
    
    #RENDER PROCEDURE
    def render(self, screen):
        #SETTING RENDERED TEXT WITH FONT
        self.text = self.font.render(self.content, True, self.fg)
        #SETTING TEXT RECT
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.pos
        #RENDERING TEXT TO SCREEN
        screen.blit(self.text, self.text_rect)
    
    #CONFIGURE PROCEDURE
    def configure(self, new_text):
        #SETTING NEW CONTENT FOR TEXT
        self.content = new_text