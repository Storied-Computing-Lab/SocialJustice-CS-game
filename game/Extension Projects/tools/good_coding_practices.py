 """
 Good coding practices are important so other people looking at your code can understand what your code is doing. This
 includes naming your variables and functions something readable so people can understand what their purpose is by reading the name. In
 addition you should add comments before defining a function explaining the inputs of the function, how the function works and what it
 outputs. Furthermore add comments anytime you think it isn't clear what your code is doing.We have demonstrated a couple
 examples for you below.
 """

 """
 The function printingR takes an input count which is an integer and prints R count times.
 """
 def printingR(count):
    while count != 0:
        print ("R")
        count -= 1

player_points = {"Clara": 0, "Niko": 0} #Creatng a dictionary to keep track of the points of the players