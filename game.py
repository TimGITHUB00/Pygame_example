#IMPORTING SYS LIBRARY
import sys
#IMPORTING PYGAME LIBRARY
import pygame
#IMPORTING EVERYTHING FROM CONFIG AND PYGAME_INIT IN MODULES FOLDER
from modules.config import *
from modules.pygame_init import *
#IMPORT EVERYTING FROM MENU
from menu import *

#GAME CLASS
class Game:
    #INITIALIZE OF GAME
    def __init__(self):
        #SETTING ROOT CLASS FROM PYGAME_INIT
        self.root = Root()
        #SETTING PYGAME SCREEN FROM PYGAME_INIT
        self.screen = self.root.screen
        #SETTING PYGAME EVENTS
        self.events = pygame.event.get()
        #SETTING RUNNING VARIABLE TO TRUE
        self.running = True
        #SETTING EXITGAME VARIABLE TO FALSE
        self.exitgame = False
        #SETTING MENU CLASS FROM MENU
        self.menu = Menu(self)
        #SETTING COLORS FROM CONFIG
        self.white = WHITE
        #SETTING SREEN BACKGROUND COLOR
        self.bg_color = self.white
        #SETTING MENU INDEX LEVEL
        self.level = 0
        #SETTING PRESSED TO FALSE
        self.pressed = False

    #MAINLOOP PROCEDURE
    def mainloop(self):
        #WHILE RUNNING IS TRUE
        while self.running:
            #CALLING UPDATE PROCEDURE
            self.update()
            #ITERATING THROUGH PYGAME EVENTS
            for event in pygame.event.get():
                #IF EVENT TYPE IS QUIT
                if event.type == pygame.QUIT:
                    #PYGAME QUIT
                    pygame.quit()
                    #TRY CATCH LOOP
                    try:
                        #SYS EXIT
                        sys.exit()
                    #FINALLY
                    finally:
                        #SETTING RUNNING TO FALSE
                        self.running = False
            #IF LEFT MOUSE BUTTON IS PRESSED
            if pygame.mouse.get_pressed()[0]:
                #SETTING PRESSED TO TRUE
                self.pressed = True

    #UPDATE PROCEDURE
    def update(self):
        #FILLING SCREEN WITH BACKGROUND COLOR
        self.screen.fill(self.bg_color)
        #CALLING DRAW PROCEDURE
        self.draw()
        #UPDATING PYGAME DISPLAY
        pygame.display.update()

    #RUN ONCE PROCEDURE
    #WHEN CALLED THE PROCEDURE BELOW IT RUNS ONLY ONCE
    def run_once(f):
        def wrapper(*args, **kwargs):
            if not wrapper.has_run:
                wrapper.has_run = True
                return f(*args, **kwargs)
        wrapper.has_run = False
        return wrapper

    #CALLING RUN ONCE PROCEDURE
    @run_once
    #DRAW MENU PROCEDURE
    def draw_menu(self):
        #CALLING DRAW WINDOW PROCEDURE IN MENU
        self.menu.draw_window()

    #DRAW PROCEDURE
    def draw(self):
        #IF MENU INDEX LEVEL IS 0
        if self.level == 0:
            #CALLING DRAW MENU PROCEDURE
            self.draw_menu()
            #CALLING UPDATE PROCEDURE IN MENU
            self.menu.update()