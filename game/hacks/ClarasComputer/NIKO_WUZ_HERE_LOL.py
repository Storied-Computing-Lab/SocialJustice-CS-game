from __future__ import unicode_literals
from virus import Virus
#Tip: Check out the virus.py file to see what this type of virus can do.
niko_virus = Virus()

def main():
    """
    Welcome to your first Hack!
    Looks like this command, niko_virus.invade(), is outputting an ANNOYING message in the 'console'!
    Press shift + o inside the game to view this annoying mesage in the console!
        What does this virus currently print out?
        One way to unlock your computer is by changing this virus message to a less annoying one.

    All this text is a comment. Computers do not read between the """ """
    Press command + s to save changes here.
    Press shift + o inside the game to view the console in the game anytime.
    Once hack is completed, press space/click forward in the game as usual to proceed in the game.
    """

    niko_virus.invade() #What does this command do?

    #This is also a comment
    #BONUS: Can you make the virus say nothing at all?
    return

#Tip: Other commands like eliminate_virus() might be helpful.
#Tip: The in-game notebook has more examples of how to write a code command.
def eliminate_virus():
    global niko_virus
    niko_virus.change_message("Virus eliminated")
