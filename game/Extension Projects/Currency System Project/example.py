"""
In this file we will be giving you an example approach. We will structure the points around how fast one completes the
hack.
"""

"First thing I am going to do is define a class that keeps track player's points.""
class points:

    def __init__(self):
        self.points = 0
        "Adds the appropriate points for the player depending on how fast they completed the hack."
    def addPoints(self, time):
        if time < 2:
            return self.points += 10
        elif time < 5:
            return self.points += 5
        else:
            return self.points += 2

"Creates an instance variable for Clara."
clara_Points = points()

"""
From here I would go into the hack files and the check hack files and import this file so I can use the class and clara_Points
to reward points depending on how fast the player completes the hack. I would also import the time library to time how fast the player completes the hack
and store that in a global variable. From here I would go into the script and see where Clara could benefit from more resources to help her community. For example
food for protesters in Hack 2. In these areas one could have a message pop asking the player if they want to use their points to buy these extra resources. If I wanted
to make it fancy I would download a store graphic and store it in the image folder and change the background to that when asking if players want to buy anything.

"""