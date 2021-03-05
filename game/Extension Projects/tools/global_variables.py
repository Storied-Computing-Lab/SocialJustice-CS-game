#This file is meant to give a quick background about global variables and why they are useful
"""
Global Variables are vary useful when one wants to keep track of a variable throughout the whole game
and to use that variable in multiple files. For example in this game if we wanted to keep track of a player's points throughout
the game we would have a global variable that keeps track of the points of the player. Anytime the player gains points
we would add to this global variable. And the same logic would follow if the player loses points. Below we will show you
how to create and use global variables.

"""
#this is how you create a global variable
global claraPoints
# Imagine this is the start of the game so Clara has no points so we set claraPoints to 0
claraPoints = 0
#After Clara finishes her first hack we want to add 2 points to her overall points variable.
claraPoints += 2
#If we wanted to we could create a function that we could call anytime Clara completed a hack to add the points for us.
def hackPoints():
    claraPoints += 2 # notice how we did not have to pass in claraPoints as a parameter to the function since it is a global variable

#Note to Zaynab add about use of diff files and import statements