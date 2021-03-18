#Tip: This type of coding is called object oriented programming. Your Notebook has more information about this.
#This class provides methods to customize the virus.
#__init__(self) defines what a new Virus itself comes with automatically, in this case, a pre-set message.
#change_message(self,message): changes the current message of the virus to the message passed in.
#invade(self): prints out the message.

class Virus:

    def __init__(self):
        self.message = "Niko wuz here"
    #Tip: Can you use this method in NIKO_WUZ_HERE_LOL.py to change the message
    def change_message(self, message):
        self.message = message
    #Tip: Is there a way you can change this function to eliminate the virus completely
    def invade(self):
        print(self.message)

#def main():
    #global niko_virus
    #niko_virus = Virus()