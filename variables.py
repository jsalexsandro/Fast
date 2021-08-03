########################################
# Variables for "Fast" Language !      #
########################################
# Coding By José Alexsandro            #
# Github: https://github.com/eualexdev #
########################################

import os,sys

langName = "Fast"
langVersion = "0.0.1"

def GetFinalExtension(file:str):
    return file.split("\ "[0])[-1]

def GetPlatform():
    if sys.platform in {'linux', 'linux2'}:
        return "linux"
    elif os.name == "nt" or os.environ.get('OS', '') != 'Windows_NT' or sys.platform in {'win32', 'cygwin', 'msys'}:
        return "win"
    else:
        print("System not possible compilating")
    return None

def extForBuild():
    if GetPlatform() == "win":
        return ".exe"
    elif GetPlatform() == "linux":
        return ".out"