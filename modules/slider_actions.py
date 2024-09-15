#IMPORTING EVERYTHING FROM CONFIG IN MODULES FOLDER
from modules.config import *

#SLIDER ACTIONS CLASS
class SliderActions():
    #INITIALIZE OF SLIDER ACTIONS
    def __init__(self, sliders, target, index, action) -> None:
        #SETTING SLIDERS FROM SLIDER
        self.sliders = sliders
        #SETTING TARGET
        self.target = target
        #SETTING INDEX
        self.index = index
        #SETTING ACTION
        self.action = action

    #DO ACTION PROCEDURE
    def do_action(self):
        #DO NOTHING
        pass