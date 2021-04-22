#Add your code to the bottom of this file!
label ac_The_Meeting:

    "At the meeting, each activist reads out loud their question."
    "We believe this will cause a media stir, so the Navy will have to answer ALL our questions."
    "We hope to gather over 50,000 more questions, eventually, to  stall their plans even futher."
    "But for now, let's show them what we're made of."

    "In no particular order, the activists begin shouting their questions for all to hear."
    "You notice Niko and Esperansa added additional questions!"
    # python:
    #     activist_names = questions_dict.keys()
    #     first_activist_name = activist_names[0]
    #     renpy.say(first_activist_name, questions_dict[first_activist_name]) #The first activist speaks
    #     second_activist_name = activist_names[1]
    #     renpy.say(second_activist_name, questions_dict[second_activist_name]) #The second activist speaks
    python:
        questions_dict["Esperansa Calvo"] = "How do you realistically and specifically plan to 'move the fish' ?!"
        questions_dict["Niko Rubino"] = "Can we see the military expansion plans in their entirety, as required by law?"
        renpy.say("Esperansa Calvo", questions_dict["Esperansa Calvo"])
        renpy.say("Niko Rubino", questions_dict["Niko Rubino"])
        questions_dict.pop("Esperansa Calvo")
        questions_dict.pop("Niko Rubino")
        renpy.say("", "The following questions are the questions you generated. Check game/chapters/ac_The_Meeting.rpy to see how this was done!")
        for person, question in questions_dict.items():
            renpy.say(person, question)

    return
