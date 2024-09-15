#IMPORTING PYGAME LIBRARY
import pygame
#IMPORTING EVERYTHING FROM CONFIG, TEXT, BUTTON, IMAGE, SHAPE AND SLIDER IN MODULES FOLDER
from modules.config import *
from modules.text import *
from modules.button import *
from modules.image import *
from modules.shape import *
from modules.slider import *

#MENU CLASS
class Menu:
    #INITIALIZE OF MENU
    def __init__(self, game):
        #SETTING GAME
        self.game = game
        #SETTING SCREEN FROM GAME
        self.screen = self.game.screen
        #SETTING WINDOW WITH WIDTH AND HEIGHT FROM CONFIG
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        #SETTING TEXT CLASS FROM TEXT
        self.text = Text
        #SETTING BUTTON CLASS FROM BUTTON
        self.button = Button
        #SETTING IMAGE CLASS FROM IMAGE
        self.image = Image
        #SETTING SHAPE CLASS FROM SHAPE
        self.shape = Shape
        #SETTING SLIDER CLASS FROM SLIDER
        self.slider = Slider
        #SETTING BIG FONTSIZE FROM CONFIG
        self.bfontsize = BIG_FONTSIZE
        #SETTING CENTER WIDTH AND CENTER HEIGHT FROM CONFIG
        self.cw = CENTER_W
        self.ch = CENTER_H
        #SETTING BUTTON SIZE VARIABLES FROM CONFIG
        self.bw = BUTTON_WIDTH
        self.bh = BUTTON_HEIGHT
        #SETTING IMAGE SIZE VARIABLES FROM CONFIG
        self.iw = IMAGE_WIDTH
        self.ih = IMAGE_HEIGHT
        #SETTING SHAPE SIZE VARIABLES FROM CONFIG
        self.sw = SHAPE_WIDTH
        self.sh = SHAPE_HEIGHT
        #SETTING SLIDER SIZE VARIABLES FROM CONFIG
        self.slw = SLIDER_WIDTH
        self.slh = SLIDER_HEIGHT
        #SETTING VALUES OF SLIDER FROM CONFIG
        self.val = VAL
        self.min = MIN
        self.max = MAX
        #SETTING SHAPES FROM CONFIG
        self.r = RECT
        self.c = CIRCLE
        #SETTING COLORS FROM CONFIG
        self.black = BLACK
        self.white = WHITE
        self.green = GREEN
        self.dgreen = DARK_GREEN
        self.blue = BLUE
        self.red = RED
        self.ngray = NORMAL_GRAY
        #SETTING BACKGROUND COLOR
        self.bg_color = self.white
        #SETTING BUTTON BACKGROUND COLORS FROM CONFIG
        self.bg = BG, BG_HOV, BG_PRE
        #SETTING BUTTON FOREGROUND COLORS FROM CONFIG
        self.fg = FG, FG_HOV, FG_PRE
        #SETTING TEXT CONTENT FROM CONFIG
        self.text_str = TEXT
        #SETTING SLIDER TEXT FROM CONFIG
        self.slider_text = str(int(VAL))
        #CREATING TEXTS LIST
        self.texts = [
            #CREATING CHANGEABLE TEXT
            self.text([self.cw, self.ch-350], self.black, self.text_str, self.bfontsize),
            #CREATING TEXT FOR SLIDER
            self.text([self.cw, self.ch+300], self.black, self.slider_text, self.bfontsize)
        ]
        #SETTING BUTTON TEXTS FROM CONFIG
        self.txtButtons = MENU_BTNS
        #CREATING BUTTONS LIST
        self.buttons = [
            #CREATING BUTTON FOR CHANGING THE CHANGEABLE TEXT
            self.button([self.cw, self.ch-250], [self.bw, self.bh], self.bg, self.fg, self.txtButtons[0])
        ]
        #CREATING BUTTONS SPRITE GROUP
        self.buttonsGroup = pygame.sprite.Group()
        #ADDING ALL BUTTONS TO BUTTONS SPRITE GROUP
        self.buttonsGroup.add(self.buttons)
        #SETTING IMAGES PATH FROM CONFIG
        self.path = PATH
        #SETTING IMAGE NAME FROM CONFIG
        self.imagename = IMAGE1
        #SETTING FULL PATH OF IMAGE
        self.fullpath = self.path+self.imagename
        #CREATING IMAGES LIST
        self.images = [
            #CREATING IMAGE
            self.image([self.cw, self.ch-75], [self.iw, self.ih], self.fullpath)
        ]
        #CREATING SHAPES LIST
        self.shapes = [
            #CREATING SHAPE
            self.shape([self.cw, self.ch+100], [self.sw, self.sh], self.blue, self.r)
        ]
        #CREATING SLIDERS LIST
        self.sliders = [
            #CREATING SLIDER
            self.slider([self.cw, self.ch+200], [self.slw, self.slh], self.val, self.min, self.max)
        ]

    #UPDATE PROCEDURE
    def update(self):
        #ITERATING THROUGH ALL BUTTONS IN BUTTONS LIST
        for button in self.buttons:
            #CALLING MENU UPDATE PROCEDURE IN BUTTON CLASS
            button.menu_update(self.game, self.game.pressed)
        #SETTING MOUSE POSITION
        mouse_pos = pygame.mouse.get_pos()
        #SETTING MOUSE PRESSED
        mouse = pygame.mouse.get_pressed()
        #ITERATING THROUGH ALL SLIDERS
        for slider in self.sliders:
            #IF SLIDER COLLIDES WITH MOUSE POSITION AND LEFT MOUSE BUTTON IS PRESSED
            if slider.container_rect.collidepoint(mouse_pos) and mouse[0]:
                #CALLING MOVE SLIDER PROCEDURE IN SLIDER CLASS
                slider.move_slider(mouse_pos)
                #SETTING SLIDER TEXT TO CURRENT SLIDER VALUE
                self.slider_text = str(int(self.slider.get_value(slider)))
                #CALLING CONFIGURE PROCEDURE IN TEXT CLASS
                self.texts[1].configure(self.slider_text)
            #CALLING RENDER PROCEDURE IN SLIDER
            slider.render(self.screen)
        #FILLING WINDOW WITH BACKGROUND COLOR
        self.window.fill(self.bg_color)
        #CALLING DRAW PROCEDURE
        self.draw()
        #UPDATING PYGAME DISPLAY
        pygame.display.update()

    #DRAW PROCEDURE
    def draw(self):
        #ITERATING THROUGH ALL TEXTS IN TEXTS LIST
        for text in self.texts:
            #CALLING RENDER PROCEDURE IN TEXT CLASS
            text.render(self.window)
        #DRAWING ALL BUTTONS IN BUTTONS SPRITE GROUP TO WINDOW
        self.buttonsGroup.draw(self.window)
        #ITERATING THROUGH ALL IMAGES IN IMAGES LIST
        for image in self.images:
            #CALLING RENDER PROCEDURE IN IMAGE CLASS
            image.render(self.window)
        #ITERATING THROUGH ALL SHAPES IN SHAPES LIST
        for shape in self.shapes:
            #CALLING RENDER PROCEDURE IN SHAPE CLASS
            shape.render(self.window)
        #ITERATING THROUGH ALL SLIDERS IN SLIDERS LIST
        for slider in self.sliders:
            #CALLING RENDER PROCEDURE IN SLIDER CLASS
            slider.render(self.window)
        
    #DRAW WINDOW PROCEDURE
    def draw_window(self):
        #RENDERING WINDOW IN SCREEN
        self.screen.blit(self.window, (0, 0))