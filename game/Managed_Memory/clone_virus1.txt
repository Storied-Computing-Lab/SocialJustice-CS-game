import shutil
from time import sleep
import glob
import os

def main():
    counter = 0
    isAlive = True
    if isAlive: #stand-in I eventually want this to be just for the root virus to execute
        while counter != 10:
            #create clone_virus of myself
            virus_name = "clone_virus" + str(counter) +".txt"
            virus_path = "Users/princesssteffykins/Downloads/RENPY PROJECTS/SocialJustice-CS-game/game/Managed_Memory/" + virus_name
            shutil.copy2("Users/princesssteffykins/Downloads/RENPY PROJECTS/SocialJustice-CS-game/game/root_virus1.py", virus_path)
            counter += 1
            sleep(1)
    return
