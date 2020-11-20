from __future__ import unicode_literals
from anti_virus import AntiVirus
from virus import Virus

niko_virus = Virus()

def main():
    """
    Welcome to your first hack!
    All you have to do is this:
    Change "Niko wuz here" to a new message & view your modification in the console

    All this text is a comment. Computers do not read between the """ """
    Press command + s to save changes here.
    Press shift + o inside the game to view the console in the game anytime.
    Once hack is completed, press space/click forward in the game as usual to proceed in the game
    """

    #print("Niko wuz here lol")

    #hint!! look in the anti_virus file!!
    niko_virus.invade()

    eliminate_virus()
    #rint(niko_virus.message)
    
    #This is also a comment
    #BONUS: Can you print another message below the first?
    return


def eliminate_virus():
    global virus
    virus.change_message("Virus eliminated")