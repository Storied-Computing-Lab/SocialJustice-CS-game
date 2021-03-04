label hint1:
    show screen ingamemenu
    n "Here for a hint eh?"
    n "Well think outside your current worldview!"
    n "I hid your hack at the source!"#{a=hint2}source{/a}"
    python:
        import time
        start_time = time.time()
        seconds = 30
        current_time = time.time()
        elapsed_time = current_time - start_time
        while (elapsed_time < seconds):
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time > seconds:
                renpy.say("Niko","I hid your hack at the source! If you want another hint click #{a=hint2}here{/a}")
                hint1_numLoops+=1
                if hint1_numLoops<2:
                    renpy.say("Niko","Have you checked the game folder?")
                else:
                    renpy.say("Niko","Have you checked the {a=hint2}game{/a} folder?")
            else:
                renpy.say("Niko","I hid your hack at the source!")
                renpy.say("","If you are still stuck press enter in about 30 seconds for another hint")
    return
