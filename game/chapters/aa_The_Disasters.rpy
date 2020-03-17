label aa_The_Disasters:

    transform bounce:
        pause .15
        yoffset 0
        easein .175 yoffset -10
        easeout .175 yoffset 0
        easein .175 yoffset -4
        easeout .175 yoffset 0
        yoffset 0

    """
    Maybe a zoomed up picture of the city square, and the FNB table ?? instead of Tinian japaneseGate?
    """
    #
    #
    #
    #show Esperansa at lowered_right

    "You come to the table that says 'Food Not Bombs'"
    "People are serving food to anyone who walks by, for free."
    "Not a huge crowd. You see the girl with the braids."
    "Then she sees you."

    init python:
        global which_poster
    image resist_poster = im.Scale("images/misc/adahi_kottura-mami.png", 750, 500)
    image evacuate_poster = im.Scale("images/misc/famoksaiyan.png", 750, 500)
    #image num_posters = Text("0", size=40, color="#f00")
    menu:
        "We should resist. (Esperansa's approach)":
            "Respond affirming to Esperansa, and to Tita:trying to bring her over"
            $which_poster = "resist"
        "We should evacuate. (Tita's approach)":
            "Respond affirming to Tita, and to Esperansa: trying to bring her over"
            $which_poster = "evacuate"

    call check_100_posters from _call_check_100_posters

    show clara_neutral_eyes_open at lowered_left_2 with dissolve
    show neutral_face_arms_neutral at nb_lowered_right with dissolve
    e "Hi! I'm Esperansa."
    hide clara_neutral_eyes_open
    show clara_neutral_eyes_closed at lowered_left_2
    c "Hi! I'm Clara."
    hide clara_neutral_eyes_closed
    show clara_pointer_left_eyes_open at lowered_left_2
    show clara_pointer_left_eyes_open at bounce
    c "Niko mentioned you're involved in social justice movements here on our islands?"
    hide neutral_face_arms_neutral
    show closed_neutral_arms_neutral at nb_lowered_right
    e "That's right! I'm really passionate about social justice in all areas of life."
    hide clara_pointer_left_eyes_open
    show clara_neutral_eyes_open at lowered_left_2
    hide closed_neutral_arms_neutral
    show neutral_face_arms_neutral at nb_lowered_right
    e "So, Clara..What's your background with social justice issues?"
    hide neutral_face_arms_neutral
    show closed_neutral_arms_neutral at nb_lowered_right
    show closed_neutral_arms_neutral at bounce

    e "Or, like, what's got you interested?"
    hide closed_neutral_arms_neutral
    show neutral_face_arms_neutral at nb_lowered_right

    menu:
        "I've experienced gender inequality in hacking":
            e "That's real."
            c "Are you doing any work to address gender inequality?"
            e "Yes! That's something our community is really concerned with actually."
        "What's going on with the U.S. Military?":
            e "The U.S. military buildup is one big problem facing a lot of us now."
            c "Why is that?"
            e "Great question!!"
        "I'm not sure":
            e "No worries! I'm glad you're curious about social justice."
            e "There's a lot of ways to help out, and help is always needed."

    "Tita walks up to the table."
    image tita_neutral1= im.Scale("images/tita/tita_neutral.png", 500, 750) #Enter specific numbers <--
    image tita_concerned1 = im.Scale("images/tita/tita_concerned.png", 500, 750) #Enter specific numbers <--
    image tita_smiling1 = im.Scale("images/tita/tita_smiling.png", 500, 750) #Enter specific numbers <--

    show tita_neutral1 at center with dissolve
    e "Hey Tita, have you met Clara?"
    hide tita_neutral1
    show tita_smiling1 at center
    show tita_smiling1 at bounce
    t "Esperansa, Clara is my niece!"
    hide neutral_face_arms_neutral
    show closed_neutral_arms_neutral at nb_lowered_right
    show closed_neutral_arms_neutral at bounce
    e "Wow! Shoulda known."
    hide tita_smiling1
    show tita_neutral1 at center
    hide clara_neutral_eyes_open
    show clara_neutral_eyes_closed at lowered_left_2
    show clara_neutral_eyes_closed at bounce
    c "Why? Haha"
    hide closed_neutral_arms_neutral
    show neutral_face_arms_neutral at nb_lowered_right
    e "Tita, doesn't Clara know your work?"
    hide clara_neutral_eyes_closed
    show clara_pointer_left_eyes_open at lowered_left_2
    show clara_pointer_left_eyes_open at bounce
    c "No, I don't know!"
    hide tita_neutral1
    show tita_smiling1 at center
    t "Clara, will you walk with me?"
    hide clara_pointer_left_eyes_open
    show clara_neutral_eyes_open at lowered_left_2
    c "Sure."

    window hide #note, this command gets rid of all the sprites, too!
    python:
        renpy.scene()
        renpy.show("DisastersComic1", at_list=[Transform(yalign=0.5),Transform(xalign=0.5)])
        renpy.with_statement(dissolve)
        renpy.pause()
        def redraw_comic():
            renpy.scene()
            renpy.show("DisastersComic1", at_list=[Transform(yalign=0.5),Transform(xalign=0.5)])
            renpy.pause()
        while True:
            keep_reading = renpy.display_menu([("Keep Reading", True), ("Continue", False)])
            if keep_reading:
                renpy.pause(.5)
                redraw_comic()
            else:
                break
    scene tinian japaneseGate with dissolve
    "You return to the FNB table as Tita finishes speaking."
    show clara_neutral_eyes_open at lowered_left_2 with dissolve
    show tita_neutral1 at center with dissolve
    "Esperansa looks troubled."
    show angry_face_arms_crossed at nb_lowered_right with dissolve
    e "Tita why hasn’t the task force considered even more resistance?"
    hide angry_face_arms_crossed
    show closed_pursed_face_arms_crossed at nb_lowered_right
    e "We should fight for our right to stay, instead of giving up and fleeing as they thieve and demolish our ancestral land!"
    "Tita’s face turns grave"
    hide tita_neutral1
    show tita_concerned1 at center
    t "Esperansa I’ve told you a million times,"
    t "when lives are in danger, it\'s time to act pragmatically. When the time comes the Navy will get what they want."
    hide closed_pursed_face_arms_crossed
    show angry_face_arms_crossed at nb_lowered_right
    e "What if we expose these human rights violations? What if we can prove that the military buildup is death to our people? Clara, what do you think?"
    t "Clara, What do you think?"
    show tita_concerned1 at center
    show tita_concerned1 at bounce
    hide angry_face_arms_crossed
    show fierce_face_arms_neutral at nb_lowered_right














    e "and we need to spread the word. Would you help us?"
    c "Sure! I've got coding experience too if that helps"
    e "That's just what we need!"
    e "The printer's source code is bugged up. It only prints two posters!"
    e "Can you fix the printer's code? We need to print 100 posters!"
    #Extension or bonus, fix the printer so it can print any number of posters, not just 100
# PUT 100 flyers challenge here!!!!!!!!!!

#Then she does the hack of posters. Either 'EVACUATION. RIGHTS FOR REFUGEES' or 'RESIST. PROTECT THE LAND'
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
