#IMPORTING PYGAME LIBRARY
import pygame
#IMPORTING EVERYTHING FROM CONFIG IN MODULES FOLDER
from modules.config import *

#SLIDER CLASS
class Slider():
    #INITIALIZE OF SLIDER
    def __init__(self, pos: list, size: list, initial_val: float, min: int, max: int) -> None:

        #POSITION OF SLIDER
        self.pos = pos
        #SIZE OF SLIDER
        self.size = size

        #SETTING SLIDER LEFT SIDE POSITION
        self.slider_left_pos = self.pos[0] - (self.size[0]/2)
        #SETTING SLIDER RIGHT SIDE POSITION
        self.slider_right_pos = self.pos[0] + (self.size[0]/2)
        #SETTING SLIDER TOP SIDE POSITION
        self.slider_top_pos = self.pos[1] - (self.size[1]/2)

        #SETTING MIN VALUE OF SLIDER
        self.min = min
        #SETTING MAX VALUE OF SLIDER
        self.max = max
        #SETTING CURRENT VALUE OF SLIDER
        self.initial_val = (self.slider_right_pos-self.slider_left_pos)*initial_val # <- percentage

        #SETTING SLIDER BASE RECT
        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        #SETTING SLIDER BUTTON/SLIDER THINGY RECT
        self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_val - 5, self.slider_top_pos - 10, 20, self.size[1]+20)
    
    #MOVE SLIDER PROCEDURE
    def move_slider(self, mouse_pos):
        #SETTING BLIDER BUTTON/SLIDER THINGY X VALUE BY MOUSE POSITION
        self.button_rect.centerx = mouse_pos[0]

    #RENDER PROCEDURE
    def render(self, screen):
        #DRAWING RECT OF SLIDER BASE TO SCREEN
        pygame.draw.rect(screen, "darkgray", self.container_rect)
        #DRAWING RECT OF SLIDER BUTTON/SLIDER THINGY TO SCREEN
        pygame.draw.rect(screen, "blue", self.button_rect)

    #GET VALUE PROCEDURE
    def get_value(self):
        #SETTING VALUE RANGE
        val_range = self.slider_right_pos - self.slider_left_pos - 1
        #SETTING BUTTON/SLIDER THINGY VALUE/LOCATION
        button_val = self.button_rect.centerx - self.slider_left_pos

        #RETURNING VALUE OF BUTTON/SLIDER THINGY
        return (button_val/val_range)*(self.max-self.min)+self.min
