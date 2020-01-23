label check_100_posters:
    python:
        from __future__ import unicode_literals
        #from hacks import hack_100_flyers does not work, gets error "no module named hacks even with __init__.py"
        from game.chapters.hacks import hack_100_posters
        #Line 5 generates an error because "no module named hacks." To get hack_100_posters to be imported,
        #it looks like hack_100_posters still has to live in the game folder unfortunately!
        import sys
        #print(sys.path)
        #print(sys.version)
        import mock
        #print(mock.__name__)
        import StringIO
        from functools import wraps

        #nikos_hack.main() #no problems here. It has to do with mock , new_callable = StringIO.StringIO
        #I need a data structure that stores the number of posters printed each time the student changes the code in
        #hack_100_posters

        def call_counter(func):
            @wraps(func)
            def helper(*args, **kwargs):
                helper.calls += 1
                return func(*args, **kwargs)
            helper.calls = 0
            return helper

        @call_counter
        def print_poster_once(my_string): #eventually_string_that_is_actually_filepath_to_an_image
            print(my_string)


        def reload_hack_100_posters():
            reloaded_hack = reload(hack_100_posters)
            reloaded_hack.print_poster_once = print_poster_once
            print_poster_once.calls = 0

        while True:
            try:
                reload_hack_100_posters()
                hack_100_posters.main()
                if print_poster_once.calls != 100:
                    renpy.say("Clara","Looks like I only printed " + str(print_poster_once.calls) + " posters!")
                else:
                    break
            except Exception as e:
                renpy.say("Clara","Error with check_100_posters.py")
                renpy.say("Clara",str(e))
                #renpy.say("Clara","Press enter to restart")
                continue

        #$claras_computer_locked = False
        renpy.say("Clara", "Great. We have enough posters!!")
        renpy.say("Clara", "Welcome Back Clara")

    return
