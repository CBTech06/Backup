#!/usr/bin/python3

from libqtile import bar, widget

widget_defaults = dict(
    font="CodeNewRoman Nerd Font",
    fontsize=12,
    #padding=0,
    highlight_method="line",
    highlight_color=(["090909","090909"]),
    disable_drag=False,
    this_screen_border = "#003153"
)


main_bar = bar.Bar(
    [
        widget.GroupBox(**widget_defaults),
        widget.Spacer( length = 600 ),
        widget.WindowName(
            font="CodeNewRoman Nerd Font",
            fontsize=14,
        ),
        widget.Chord(
            chords_colors={
                'launch': ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),

        widget.Spacer( length = 30 ),
        
        widget.CapsNumLockIndicator(
            font="CodeNewRoman Nerd Font",
            fontsize=14,
        ),

        widget.Spacer( length = 30 ),

        widget.Pomodoro(
            foreground="#003153",
            length_pomodori=25
        ),
        
        widget.Spacer( length = 30 ),
        
        widget.Clock(
            font="CodeNewRoman Nerd Font",
            fontsize=14,
            format='%a %d-%m-%Y [%H:%M:%S]' ),
        widget.Spacer( length = 30 ),
        widget.Systray(),
        widget.Spacer( length = 30 ),
        widget.CurrentLayoutIcon(
            custom_icon_paths = "~/.config/qtile/icons",
            foreground = "#292D3E",
            background = "#003153",
            padding = 0,
            scale = 0.7
        ),
        widget.CurrentLayout(
            font="CodeNewRoman Nerd Font",
            fontsize=14,
            foreground = "#FFFFFF",
            background = "#003153",
            padding = 5
        ),
    ], 24, background="#181C24", foreground="#999999")

"""
secondary_bar = bar.Bar(
    [
        widget.Prompt(),
        widget.WindowName(),
        widget.Chord(
            chords_colors={
                'launch': ("#ff0000", "#ffffff"),
            },
           name_transform=lambda name: name.upper(),
        ),
        widget.CurrentLayout(),
    ], 24, background="#181C24",foreground="#999999")
"""
