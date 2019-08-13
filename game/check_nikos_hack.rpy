label check_nikos_hack:
    python:
        from __future__ import unicode_literals
        import nikos_hack
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
                nikos_hack.main()
                nikos_hack = reload(nikos_hack)
                with mock.patch('sys.stdout', new_callable = StringIO.StringIO) as mock_stdout:
                    nikos_hack.main()
                    if mock_stdout.getvalue() == 'Niko wuz here\n':
                        renpy.say("Clara", "I am still locked out of my computer!")
                        renpy.say("Clara", "I wonder where Niko might have hidden his hack")
                    else:
                        break
            except Exception as e:
                renpy.say("Clara","Error with nikos_hack.py")
                renpy.say("Clara",str(e))
                renpy.say("Clara","Press enter to restart")
                continue

        #$claras_computer_locked = False
        renpy.say("Clara", "You got into your computer!!")
        renpy.say("Clara", "Welcome Back Clara")

    return
