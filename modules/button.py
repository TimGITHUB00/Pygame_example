#IMPORTING PYGAME LIBRARY
import pygame
#IMPORTING EVERYTHING FROM CONFIG IN MODULES FOLDER
from modules.config import *

#BUTTON CLASS
class Button(pygame.sprite.Sprite):
    #INITIALIZE OF BUTTON
    def __init__(self, pos: list, size: list, bg: list, fg: list, text: str) -> None:
        super().__init__()

        #FONTSIZE AND FONT OF BUTTON
        self.fontsize = FONTSIZE
        self.font = pygame.font.Font('freesansbold.ttf', self.fontsize)
        #TEXT ON BUTTON
        self.text = text
        #POSITION OF BUTTON
        self.pos = pos
        #SIZE OF BUTTON
        self.size = size
        #BACKGROUND COLORS OF BUTTON
        self.bg = bg[0]
        self.bg_hover = bg[1]
        self.bg_pre = bg[2]
        #FOREGROUND COLORS OF BUTTON
        self.fg = fg[0]
        self.fg_hover = fg[1]
        self.fg_pre = fg[2]

        #RECT OF BUTTON
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.rect.center = (self.pos)

        #TEMPORARY RECT OF BUTTON
        self.tmp_rect = pygame.Rect(0, 0, *self.rect.size)

        #CREATING DIFFERENT COLORS TO BUTTON WHEN DOING ACTIONS
        self.org = self._create_image(self.bg, self.fg, text, self.tmp_rect)
        self.hov = self._create_image(self.bg_hover, self.fg_hover, text, self.tmp_rect)
        self.pre = self._create_image(self.bg_pre, self.fg_pre, text, self.tmp_rect)

        #IMAGE OF BUTTON
        self.image = self.org

    #CREATING IMAGES PROCEDURE
    def _create_image(self, bg, fg, text, rect):
        #GETTING IMAGE AND FILLING IT
        img = pygame.Surface(rect.size)
        img.fill(bg)
        #TESTING IF TEXT IS NOT EMPTY
        if text != '':
            #CREATING TEXT SURFACE FOR TEXT
            text_surf = self.font.render(text, 1, fg)
            #GETTING RECT FROM TEXT SURFACE
            text_rect = text_surf.get_rect()
            #SETTING RECT CENTER POSITION
            text_rect.center = (self.size[0]/2, self.size[1]/2)
            #COMBINING TEXT SURFACE AND TEXT RECT
            img.blit(text_surf, text_rect)
        #RETURNING IMAGE
        return img

    #UPDATING MENU PROCEDURE
    def menu_update(self, menu, pressed):
        #SETTING GAME VARIABLE
        self.menu = menu
        #SETTINGS MENU STUFF FROM CONFIG
        self.txtBtns = MENU_BTNS
        self.debugs = MENU_DEBUGS
        self.change = CHANGE
        #SETTING MOUSE POSITION TO VARIABLE
        pos = pygame.mouse.get_pos()
        #SETTING COLLIDE TEST TO VARIABLE
        hit = self.rect.collidepoint(pos)
        #SETTING BUTTON IMAGE DEPENDING ON THE ACTION 
        self.image = self.hov if hit else self.org
        #IF BUTTON IS PRESSED AND SELECTED
        if pressed and hit:
            #SETTING BUTTON IMAGE TO PRESSED FORM
            self.image = self.pre
            #ITERATING THROUGH ALL BUTTONS
            for i in range(len(self.txtBtns)):
                #IF TEXT IS ONE OF THE BUTTONS TEXT
                if self.text == self.txtBtns[i]:
                    #DEBUG PRINT BUTTON VALUE
                    print(self.debugs[i])
                    #IF BUTTON INDEX IS 0
                    if i == 0:
                        #TEXT CHANGE
                        self.menu.menu.texts[0].configure(self.change)
                    #BUTTON IS PRESSED IS FALSE
                    self.menu.pressed = False
                    pressed = False