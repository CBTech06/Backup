#!/usr/bin/python

# i3openit.sh  
# E.g.
# i3openit.sh 5 firefox

import sys
import subprocess

if len(sys.argv) != 3:
    print("Usage: i3openit.sh <workspace-number> <program-name> ")
    sys.exit(0);

workspace = sys.argv[1];
program = sys.argv[2];

# Custom workspace names
if workspace == "1":
    workspace = "1:web";
if workspace == "2":
    workspace = "2:browse";
if workspace == "3":
    workspace = "3:reading";
if workspace == "4":
    workspace = "4:music";
if workspace == "5":
    workspace = "5:video";
if workspace == "6":
    workspace = "6:misc";
if workspace == "7":
    workspace = "7:files";

workspacefull = workspace + ';';

print ("Workspace: " + workspace, ", Program: ", program);
subprocess.call(["i3-msg", "workspace", workspacefull, "exec", program]);
