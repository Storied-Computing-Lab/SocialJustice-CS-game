label check_nikos_hack:
    #show screen hidden_screen
    init:
        $ style.hyperlink_text = Style(style.say_dialogue) # inherits from the default dialog look, so it'll look like the rest of the dialogue, and we'll just have to change the look of the link hovered
        $ style.hyperlink_text.hover_bold = True
    python:
        from __future__ import unicode_literals
        from game.hacks.ClarasComputer import NIKO_WUZ_HERE_LOL
        import sys
        #print(sys.path)
        #print(sys.version)
        import mock
        #print(mock.__name__)
        import StringIO
        import sys

        #nikos_hack.main() #no problems here. It has to do with mock , new_callable = StringIO.StringIO

        # save a variable print_value to print to the main stdout that is called into mock_stdout instead of the main stdout
        print_value = ""
        while True:
            reloaded_module = reload(NIKO_WUZ_HERE_LOL)
            print(reloaded_module)
            with mock.patch('sys.stdout', new_callable = StringIO.StringIO) as mock_stdout:
                NIKO_WUZ_HERE_LOL.main()
                print_value = mock_stdout.getvalue()
                if print_value == 'Niko wuz here\n':
                    renpy.say("Clara", "I am still locked out of my computer!")
                    renpy.say("Clara", "Cesar Cypher... shifted by 4? That should tell me where the hack is!")
                else:
                    break
            print(print_value)
        print(print_value)
        del NIKO_WUZ_HERE_LOL
        del StringIO
        del mock
        #$claras_computer_locked = False
        renpy.say("Clara", "You got into your computer!!")
        renpy.say("Clara", "Welcome Back Clara")

    return
