from __future__ import unicode_literals
from anti_virus import AntiVirus
from virus import Virus

niko_virus = Virus()

def main():
    """
    Welcome to your first hack!
    You are presented with a niko_virus!!! Be sure to check out the virus.py file to see what a virus can do.
    In order to defeat the virus you will have to change what the virus currently says!
    If you are stuck/unsure on what to do be sure to read the names of the methods given and
    read the notebook to find out what a method is and what to do with them!!!

    All this text is a comment. Computers do not read between the """ """
    Press command + s to save changes here.
    Press shift + o inside the game to view the console in the game anytime.
    Once hack is completed, press space/click forward in the game as usual to proceed in the game
    """

    niko_virus.invade()

    
    
    #This is also a comment
    #BONUS: Can you make the virus say nothing at all?
    return


def eliminate_virus():
    global niko_virus
    niko_virus.change_message("Virus eliminated")