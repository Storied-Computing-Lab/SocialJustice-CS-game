#Add your code to the bottom of this file!
label ac_The_Meeting:

    "At the meeting, each activist reads out loud their question."
    "We believe this will cause a media stir, so the Navy will have to answer ALL our questions."
    "We hope to gather over 50,000 more questions, eventually, to  stall their plans even futher."
    "But for now, let's show them what we're made of."

    "In no particular order, the activists begin shouting their questions for all to hear."
    python:
        activist_names = questions_dict.keys()
        first_activist_name = activist_names[0]
        renpy.say(first_activist_name, questions_dict[first_activist_name]) #The first activist speaks
        second_activist_name = activist_names[1]
        renpy.say(second_activist_name, questions_dict[second_activist_name]) #The second activist speaks
    "You notice Niko and Esperansa added additional questions!"
    python:
        questions_dict["Esperansa Calvo"] = "How do you realistically and specifically plan to 'move the fish' ?!"
        questions_dict["Niko Rubino"] = "Can we see the military expansion plans in their entirety, as required by law?"
        renpy.say("Esperansa Calvo", questions_dict["Esperansa Calvo"])
        renpy.say("Niko Rubino", questions_dict["Niko Rubino"])
    "The other activists keep this up for a while."
    "Ah, but the other three activists you added can not seem to find their words."

    python:
        """
        Your code here!
        Delete while loop code and get YOUR code running by hitting spacebar in the game!
        """
        while True:
            renpy.say("","Can you help the other three names you added to use their voice?")
            renpy.say("","Ah, but the other three activists you added can not seem to find their words.")
            renpy.say("", "Find out how the others spoke their questions in 'ac_The_Meeting.rpy' !")

    return
