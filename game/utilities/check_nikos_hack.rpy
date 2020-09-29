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

        print_value = ""
        while True:
            #try:
            reload(NIKO_WUZ_HERE_LOL)
            with mock.patch('sys.stdout', new_callable = StringIO.StringIO) as mock_stdout:
                NIKO_WUZ_HERE_LOL.main()
                """
                if user doesnt print, set print_value to a "print something statement"
                """
                print_value = mock_stdout.getvalue()
                if print_value == 'Niko wuz here\n':
                    renpy.say("Clara", "I am still locked out of my computer!")
                    renpy.say("Clara", "I wonder where {a=hint1}Niko{/a} might have hidden his hack")
                else:
                    break
            print(print_value)
            """except Exception as e:
                renpy.say("Clara","Error with nIKO_WUZ_HERE_LOL.py")
                renpy.say("Clara",str(e))
                #renpy.say("Clara","Press enter to restart")
                continue"""
        print(print_value)
        del NIKO_WUZ_HERE_LOL
        del StringIO
        del mock
        #$claras_computer_locked = False
        renpy.say("Clara", "You got into your computer!!")
        renpy.say("Clara", "Welcome Back Clara")

    return
