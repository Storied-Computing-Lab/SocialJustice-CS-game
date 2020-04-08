label check_nikos_hack:
    #show screen hidden_screen
    python:
        from __future__ import unicode_literals
        import nIKO_WUZ_HERE_LOL
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
                nIKO_WUZ_HERE_LOL.main()
                nIKO_WUZ_HERE_LOL = reload(nIKO_WUZ_HERE_LOL)
                with mock.patch('sys.stdout', new_callable = StringIO.StringIO) as mock_stdout:
                    nIKO_WUZ_HERE_LOL.main()
                    if mock_stdout.getvalue() == 'Niko wuz here\n':
                        renpy.say("Clara", "I am still locked out of my computer!")
                        renpy.say("Clara", "I wonder where {b}Niko{/b} might have hidden his hack")
                    else:
                        break
            except Exception as e:
                renpy.say("Clara","Error with nIKO_WUZ_HERE_LOL.py")
                renpy.say("Clara",str(e))
                #renpy.say("Clara","Press enter to restart")
                continue

        #$claras_computer_locked = False
        renpy.say("Clara", "You got into your computer!!")
        renpy.say("Clara", "Welcome Back Clara")

    return
