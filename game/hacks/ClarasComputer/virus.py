
class Virus:
    """
    This class provides methods to customize the virus.
    There are many ways to solve this puzzle!
    """

    def __init__(self):
        """
        Set the default message for a Virus. 
        """
        self.message = "Niko wuz here"

    def change_message(self, message):
        """
        Change what the default message says.
        How to use: niko_virus.change_message("Your message here")
        """
        self.message = message

    def invade(self):
        """
        Print out a Virus' message.
        How to use: niko_virus.invade()
        """
        print(self.message)

#Tip: This type of coding is called object oriented programming. Your Notebook has more information about this.
