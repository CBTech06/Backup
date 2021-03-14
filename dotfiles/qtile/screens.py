#!/usr/bin/python3

from libqtile.config import Screen
import platform 

hostname = platform.node()

#if num_screens[hostname] == 2:
from bars import main_bar # ,secondary_bar
    
main_screen = Screen(bottom=main_bar)
#secondary_screen = Screen(bottom=secondary_bar)
screens = [main_screen]
    
    



