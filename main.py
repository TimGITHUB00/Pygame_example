#IMPORTING EVERYTHING FROM GAME
from game import *

#CALLING GAME CLASS
g = Game()

#TESTING
print("TEST COMMAND")

#GAME LOOP
while g.running:
    #RUNNING GAME MAINLOOP
    g.mainloop()