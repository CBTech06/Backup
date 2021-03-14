#!/usr/bin/python3

from libqtile import bar, layout, widget, hook
from libqtile.config import Key,Group, ScratchPad, DropDown, Match
from libqtile.command import lazy

from keys import keys

mod = "mod4"
TERM = "urxvt -e tmux"

cls_group_dict = {
    "qutebrowser": "1",
    "firefox": "6",
    "URxvt":"2",
    "Zathura": "3",
    "TuxGuitar": "5",
    "Guitarix": "5",
    "QjackCtl": "5",
}
group_labels = [
    "[D1]", "[D2]", "[D3]",
    "[D4]", "[D5]", "[D6]",
]

group_names = [
    "a", "z", "e",
    "r", "t", "y",
]


group_layouts = [
    "MonadTall", "MonadTall", "MonadTall",
    "MonadTall", "Floating", "Max",
]

group_matches = [
    Match(wm_class='qutebrowser'), 
    Match(wm_class='URxvt'), 
    Match(wm_class='Zathura'), 
    Match(wm_class=['TuxGuitar','Guitarix','QjackCtl']), 
    Match(wm_class='Music'), 
    Match(wm_class='firefox'),
]
groups = []

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
            matches=group_matches[i],
        ))

for i in groups:

        keys.append(
            Key([mod], i.name , lazy.group[i.name].toscreen())
        )

        keys.append(    
            Key([mod, "shift"], i.name , lazy.window.togroup(i.name))
        )

@hook.subscribe.client_managed
def go_to_group(window):
    if(window.window.get_wm_class()[1] in cls_group_dict.keys()):
       window.group.cmd_toscreen()
        

    """
@hook.subscribe.client_new
def agroup(client):
        apps = { 
            # 1 Browser
            "Navigator": "1", "class_name": "qutebrowser",
            "Navigator": "6", "class_name": "firefox",
            
            # 2 Shell
            "urxvt": "2", "class_name": "urxvt",
            
            # 3 Graph 
            "gimp": "5", "class_name": "gimp",
            "inkscape": "5", "class_name": "inkscape",
            
            # 4 Music
            "QjackCtl": "4" , "class_name": "QjackCtl",
            "TuxGuitar": "4", "class_name": "TuxGuitar",
            "guitarix": "4", "class_name": "guitarix",

            # 5 
            "cmus": "5", "class_name": "Music",
        }

        wm_class = client.window.get_wm_class()[0]
        group = apps.get(wm_class, None)
        if group:
            client.togroup(group)
            client.group.cmd_toscreen()
"""
