import shutil
from time import sleep
import glob
import os

counter = 0
isParent = True
if isParent: #stand-in I eventually want this to be just for the root virus to execute
    while counter != 20:
        #create clone_virus of myself
        virus_name = "clone_virus" + str(counter) +".txt"
        virus_path = "/Users/princesssteffykins/Desktop/Managed_Memory/" + virus_name
        shutil.copy2("/Users/princesssteffykins/Desktop/Managed_Memory/root_virus.py", virus_path)
        counter += 1
        sleep(1)
