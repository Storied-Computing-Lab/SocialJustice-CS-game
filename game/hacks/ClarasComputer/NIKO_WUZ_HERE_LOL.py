from __future__ import unicode_literals
from virus import Virus
#Tip: Check out the virus.py file to see what this type of virus can do.
niko_virus = Virus() #this code creates a new Virus

def main():
    """
    Welcome to your first Hack!
    Looks like this command, niko_virus.invade(), is outputting an ANNOYING message in the 'console'!
    Press shift + o inside the game to view this annoying mesage in the console!
        What does this virus currently print out?
        One way to unlock Clara's computer is by changing this virus message to a less annoying one.

    All this text is a comment. Computers do not read between the """ """
    Press command + s to save changes here.
    Press shift + o inside the game to view the console in the game anytime.
    Once hack is completed, press space/click forward in the game as usual to proceed in the game.
    """

    niko_virus.invade() #What does this command do?
    #Hint: try putting eliminate_virus() right after this line. What happens?
    return

def eliminate_virus():
    """
    Changes the message of  nico_virus to "Virus eliminated".
    How to use: write eliminate_virus() immediately after niko_virus.invade()
    """
    global niko_virus
    niko_virus.change_message("Virus eliminated")
