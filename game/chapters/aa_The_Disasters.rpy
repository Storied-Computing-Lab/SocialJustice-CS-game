label aa_The_Disasters:
    return
    menu:
        "Explore the sugarcane crops":
            $day = 1
            call sugarcane from _call_sugarcane
        "Meet cousin Niko at the Center for CHamoru Rights":
            $day = 2
            call center from _call_center
        "Explore the Joint Region Marianas Naval Base":
            $day = 3
            call base from _call_base
        "Meet Auntie Tita at the Food Not Bombs in Dededo":
            $day = 4
            call dededo from _call_dededo

    e "We made it to the fields"
    menu:
        "Explore the sugarcane crops":
            c "Let's see if we can talk to anyone about their experiences with this new weather"
        "Collect some data":
            c "Where can we collect some data for our report?"
            e "There a couple of possibilites"
            menu:
                "Take temperature data over the next few hours, hey at least it's pretty here":
                    e "Sounds good. Let's take temperature readings"
                "Interview sugarcane farmers":
                    e "Ok. Let's see if we can talk to anyone about their experiences with this new weather" #set Esperansa_revisit_gender_binary = True
                "Take photographs":
                    e "Great idea. Our report will need visual evidence of the destruction of sugarcane" #points towards some quest or unlocking of Ma'ase ?
    return
