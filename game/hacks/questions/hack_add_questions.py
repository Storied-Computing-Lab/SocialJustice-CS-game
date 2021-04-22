from __future__ import unicode_literals

"""
This is an example of a dictionary that maps NFL teams to their cities.
Notice that each key is followed by a colon ( : ) and each mapping is followed
by a comma. Every key must be unique:

teams = {
    "Las Vegas" : "Raiders",
    "San Francisco" : "49ers",
    "Seattle" : "Seahawks",
    "Atlanta" : "Falcons",
}
--------------------------------
The dictionary above maps Strings (text) to other strings. 
However, we can map any type to any type. Here's an example
of a String to Integer mapping:

roman_numerals = {
    "I" : 1,
    "II" : 2,
    "III" : 3,
    "IV : 4,
    "V" : 5,
}

You don't have to do it here, but you can access these elements using square brackets:
>>> roman_numerals["IV"]

"""

def main():
    """
    Make a dictionary that maps at least 5 names to questions!
    ie: { "Clara": "Why does the military want to do this?" }
    """
    # Note: Do not change the name of this dictionary or the return statement!
    questions = {
        # Replace this line and add your own questions!
    }

    # Makes sure the questions variable exists
    if "questions" in locals():
        return questions
