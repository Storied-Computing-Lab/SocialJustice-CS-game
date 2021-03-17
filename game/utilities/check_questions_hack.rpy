label check_questions_hack:
    python:
        from __future__ import unicode_literals
        from game.hacks.questions import hack_add_questions
        import sys
        import StringIO

        global questions_dict


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
                renpy.say("Clara", "I need at least 5 questions, I currently have " + str(questions_dict_len))
                renpy.say("Clara","I need to ask more people!")
            else:
                break


        del hack_add_questions
        del StringIO
        renpy.say("Clara", "Great. We have enough questions!!")

    return
