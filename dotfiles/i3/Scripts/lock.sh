#!/bin/bash
IMAGE=/tmp/screen_locked.png

xset b off
scrot $IMAGE

#convert -scale 25% -scale 400% $IMAGE $IMAGE
convert -blur 3x3 $IMAGE $IMAGE

i3lock -i $IMAGE