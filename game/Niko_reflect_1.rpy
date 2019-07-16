label Niko_reflect_1:
    python:
        Niko_relation_reflect_1 = renpy.input("How did I feel about that conversation with Niko?")
        claras_conns = c.connections
        relate_with_Niko = claras_conns['Niko']
        relate_with_Niko['relation_reflect_1'] = Niko_relation_reflect_1
        statement1 = "I felt " + Niko_relation_reflect_1 + " about that"
        renpy.say("Clara", statement1)
        statement2 = "You've added '" + Niko_relation_reflect_1 + "' to your feelings of personal connection to Niko."
        renpy.say(None, statement2)
