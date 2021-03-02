label check_questions_hack:
    python:
        from __future__ import unicode_literals
        #from hacks import hack_100_flyers does not work, gets error "no module named hacks even with __init__.py"
        from game.hacks.questions import hack_add_questions
        #Line 5 generates an error because "no module named hacks." To get hack_100_posters to be imported,
        #it looks like hack_100_posters still has to live in the game folder unfortunately!
        import sys
        #print(sys.path)
        #print(sys.version)
        #import mock
        #print(mock.__name__)
        import StringIO


        """
        Forever loop that waits until hack_add_questions.main() has a dictionary with length >= 5 
        """
        while True:
            reload(hack_add_questions)
            questions_dict = hack_add_questions.main()

            # Error checking
            while questions_dict is None:
                renpy.say("Clara", "Oh no! An error occurred. Check if the dictionary is still called 'questions' and the main() function is still returning it!")
                reload(hack_add_questions)
                questions_dict = hack_add_questions.main()
            
            questions_dict_len = len(questions_dict)
            if questions_dict_len < 5:
                renpy.say("Clara","Looks like I only have " + str(questions_dict_len) + " questions!")
                renpy.say("Clara","I should try to get at least 5")
            else:
                break


        del hack_add_questions
        del StringIO
        #$claras_computer_locked = False
        renpy.say("Clara", "Great. We have enough questions!!")
        renpy.say("Clara", "Welcome Back Clara")

    return
