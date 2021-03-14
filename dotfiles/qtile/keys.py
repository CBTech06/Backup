#!/usr/bin/python3

import os
import subprocess
import xcffib

from libqtile.config import Key, Drag, Click, ScratchPad, DropDown
from libqtile.command import lazy


mod="mod4"
TERM="urxvt -e tmux"

from libqtile import qtile

_show_cursor = qtile.conn.conn(xcffib.xfixes.key).ShowCursor
_hide_cursor = qtile.conn.conn(xcffib.xfixes.key).HideCursor

def show_cursor():
        _show_cursor(qtile.root.wid)
        qtile.conn.flush()

def hide_cursor():
        _hide_cursor(qtile.root.wid)
        qtile.conn.flush()
        
# ---- [ KEYBINDINGS ] ---- #
keys = [
# [SWITCH BETWEEN WINDOW] 
    Key([mod], "h", 
        lazy.layout.left(), 
        desc="Move focus to left"),
    Key([mod], "l", 
        lazy.layout.right(), 
        desc="Move focus to right"),
    Key([mod], "j", 
        lazy.layout.down(), 
        desc="Move focus down"),
    Key([mod], "k",
        lazy.layout.up(), 
        desc="Move focus up"),

# [MODE + SHIFT]
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

# [RESTART /CLOSE]
    Key([mod, "shift"], "r",
        lazy.restart(), 
        desc="Restart Qtile"),

    Key([mod, "control"], "q", 
        lazy.shutdown(), 
        desc="Shutdown Qtile"),
    
# [SWICTH GROUPS]
    Key([mod, "control"], "h", 
        lazy.screen.prev_group(),
        desc="Move to prev Group"),
    Key([mod, "control"], "l", 
        lazy.screen.next_group(),
        desc="Move to next group"),

# [ SWITCH SCREEN ]
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"),

    #Key([mod],"space",
    #    lazy.next_screen(),
    #    desc = "Move focus to next Screen ",
    #    ),
    Key([mod],"space",
        lazy.spawn("~/.config/i3/Scripts/mouse"),
        desc = "Hide Mouse",
        ),

# [ LAUNCHER /TERM /ROFI]
    Key([mod], "Return", 
        lazy.spawn(TERM), 
        desc="Launch terminal"),
   
    Key([mod],"d", 
        lazy.spawn("rofi -modi window,run -show run -sidebar-mode"),
        desc="Run ROFI"),

    Key([mod], "r", 
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

# [WINDOW FULLSCREEN / KILL]
    Key([mod], "c", 
        lazy.window.kill(), 
        desc="Kill focused window"),
    Key([mod], "f", 
        lazy.window.toggle_fullscreen(),
        desc="Maximize Fullscreen"),

    Key([mod], "m",
        lazy.window.toggle_minimize(),				
        desc="Toogle minimize"),

    Key([mod], "Tab",
	lazy.window.toggle_floating(),
        desc= "Toggle floating"),

# [TAKE SCREENSHOT]  
    Key([], "Print", 
        lazy.spawn("scrot -e 'mv $f ~/Work/Screenshots/'"),
        desc="Print screenshot"),
]

