label check_100_posters:
    python:
        from __future__ import unicode_literals
        #from hacks import hack_100_flyers does not work, gets error "no module named hacks even with __init__.py"
        from hacks import hack_100_posters
        #Line 5 generates an error because "no module named hacks." To get hack_100_posters to be imported,
        #it looks like hack_100_posters still has to live in the game folder unfortunately!
        import sys
        #print(sys.path)
        #print(sys.version)
        import mock
        #print(mock.__name__)
        import StringIO
        import sys

        #nikos_hack.main() #no problems here. It has to do with mock , new_callable = StringIO.StringIO
        while True:
            try:
                hack_100_posters.main()
                hack_100_posters = reload(hack_100_posters)
                with mock.patch('sys.stdout', new_callable = StringIO.StringIO) as mock_stdout:
                    hack_100_posters.main()
                    if mock_stdout.getvalue() == 'Hello inside hack_100_posters main function\n':
                        renpy.say("Clara", "I am still locked out of my computer!")
                        renpy.say("Clara", "I wonder where Niko might have hidden his hack")
                    else:
                        break
            except Exception as e:
                renpy.say("Clara","Error with check_100_posters.py")
                renpy.say("Clara",str(e))
                #renpy.say("Clara","Press enter to restart")
                continue

        #$claras_computer_locked = False
        renpy.say("Clara", "You got into your computer!!")
        renpy.say("Clara", "Welcome Back Clara")

    return
