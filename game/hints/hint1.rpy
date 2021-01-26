label hint1:
    show screen ingamemenu
    n "Here for a hint eh?"
    n "Well think outside your current worldview!"
    n "I hid your hack at the source!"#{a=hint2}source{/a}"
    python:
        hint1_numLoops+=1
        if hint1_numLoops<2:
            renpy.say("Niko","Have you checked the game folder?")
        else:
            renpy.say("Niko","Have you checked the {a=hint2}game{/a} folder?")
    return
