label aa_The_Disasters:

    transform bounce:
        pause .15
        yoffset 0
        easein .175 yoffset -10
        easeout .175 yoffset 0
        easein .175 yoffset -4
        easeout .175 yoffset 0
        yoffset 0

    #
    #
    #
    #show Esperansa at lowered_right

    "You come to the table that says 'Food Not Bombs'"
    "People are serving food to anyone who walks by, for free."
    "Not a huge crowd. You see the girl with the braids."
    "Then she sees you."

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

    init python:
        def redraw_comic():
            renpy.scene()
            renpy.show("DisastersComic1", at_list=[Transform(yalign=0.5),Transform(xalign=0.5)])
            renpy.pause()
    window hide #note, this command gets rid of all the sprites, too!
    python:
        renpy.scene()
        renpy.show("DisastersComic1", at_list=[Transform(yalign=0.5),Transform(xalign=0.5)])
        renpy.with_statement(dissolve)
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

    init python:
        global which_poster
    image resist_poster = im.Scale("images/misc/adahi_kottura-mami.png", 750, 500)
    image evacuate_poster = im.Scale("images/misc/famoksaiyan.png", 750, 500)
    #image num_posters = Text("0", size=40, color="#f00")
    menu:
        "We should resist. (Esperansa's approach)":
            $which_poster = "resist"
            c "I think we should resist!"
            e "We have to demand an end to the military buildup!"
            c "Tita, we need all the help we can get."
            e "Clara's right, will the Tinian Evacuation Task force stand with the Land Protectors?"
            t "I'll have to ask at the next general meeting."
            t "It's important to fight back, I agree,"
            t "But I think the Task Force's central mission will remain to support fleeing refugees from Tinian and Pågan."
            e "Of course, any social justice or liberation movement also must support refugees!"
            c "But I think it's important that our first approach is the most direct!"
            c "No more land theft!"
            c "Not one more acre!!"
            e "Clara, we are gathering people to start protests and even striking."
            hide tita_concerned1
            show tita_neutral1 at center
            t "Yes, and the Tinian Evacuation Task force is voting to contribute to a strike fund"
            t "in solidarity with the Land Protectors."
            t "We still need to discuss the strike fund. Talk later Esperansa?"
            e "Sounds good."
            t "I'll be back in a few. Ayu'os Clara"
            c "Ayu'os Auntie Tita!"
            "Esperansa and you start discussing resistance and anti-colonialism as Tita returns to the Task Force building."
            hide tita_neutral1 with dissolve
            e "We are gathering together from all over the Northern Marianas Islands to protest against the buildup."
            e "However, we need to send the posters digitally through unofficial channels."
            e "One of our tactics is striking, and we want our organizing communications to remain confidential."
            e "Do you have any experience hacking source code? There may be a way to send 100 posters automatically"
            e "through a more secure channel."
            c "I do actually! Niko suggested that you all needed help with digital communications."
            c "And I do have experience hacking past an artificial block Niko put on my own machine."
            e "Niko locked you out of your computer? Typical Niko."
            e "Haha!"
            e "Is he still with the Hacker Boyz?"
            c "Yeah...."
            "You catch Esperansa up on your efforts to join the hacking club"
            #Consider inluding some of the choices Clara made from that FIRST
            #conversation here to come back around to the takeaways!!!!!!!!!!!!!!
            c "Niko was starting to understand that we need diverse hackers to achieve diverse goals"
            e "But he's still learning about social justice and hacking?"
            c "That's right"
            e "Yeah. I think when technology is used to steal and destroy land,"
            e "I don't care what gender of the person programming drone strikes and other A.I. that kills"
            e "But I do think we need a diversity of perspectives on how to USE technology..."
            e "Like for social justice rather than military expansion!"
            e "Anyways. We have to light a fire in people's hearts"
            e "So we all become Land Protectors!"
            e "Our language, our land, and our lives depend on it."
            e "But the U.S. military still holds a place in people's hearts."
            e "We have to expose their ugly side. They aren't the saviors of the Chamoru people"
            e "They can't keep expanding and taking more land and expect us to adore them ANY LONGER!"
            "You consider Esperansa's words"
            "A pang of guilt hits you right in the chest."
            "So many of your Chamoru family members have served in the U.S. Navy"
            c "Esperansa, you've given me a lot to think about"
            c "I still think it's important to stop the military buildup."
            c "But I don't know if they are the enemy"
            c "I'm still worried and considering it..."
            c "But I love this land. I want to protect it."
            c "Let me have a look at the remote printer's source code."
            c "I'll get those communications out as soon as possible."
        "We should evacuate. (Tita's approach)":
            $which_poster = "evacuate"
            c "I think we need to evacuate!"
            t "Refugees from Tinian and Pågan are our most vulnerable!"
            t "They include veterans, subsistence farmers, housing insecure people and people with disabilities."
            e "It's a tough choice, but I'm glad you'll be supporting the refugees Clara"
            hide fierce_face_arms_neutral
            show fierce_face_arms_crossed at nb_lowered_right
            e "I think we have to take a more direct approach and stop land theft NOW"
            e "But Evacuation is doing important work, too."
            hide fierce_face_arms_crossed
            show face_neutral_arms_crossed at nb_lowered_right
            c "Yeah. I think we need to gather supplies and support each other."
            c "We have to have....solidarity? With our most vulnerable."
            t "Yeah, more specifically this kind of work is called 'harm reduction', or 'mutual aid'!"
            e "I'll see you two around soon."
            e "I'm going to start cleaning up the Food Not Bombs table and dishes."
            hide face_neutral_arms_crossed
            show neutral_face_arms_neutral at nb_lowered_right
            e "Talk soon!"
            "Tita and you start discussing refugee mutual aid as Esperansa joins some other activists."
            hide neutral_face_arms_neutral with dissolve
            hide tita_concerned1
            show tita_neutral1 at center
            t "We are getting the word out to people on Tinian and Pågan about resources provided by the Task Force."
            t "However, we need to send the posters digitally through unofficial channels."
            t "One of our tactics is striking, and we want our organizing communications to remain confidential."
            t "Do you have any experience hacking source code? There may be a way to send 100 posters automatically"
            t "through a more secure channel."
            c "I do actually! Niko suggested that you all needed help with digital communications."
            c "And I do have experience hacking past an artificial block Niko put on my own machine."
            t "Niko Rubino, your cousin? What a rascal."
            t "I should talk to your Auntie about him! Is he also working against the military buildup crisis?"
            c "I'm not sure, he hasn't mentioned anything yet to me."
            "Some time passes as you and Tita catch up on life on the islands and your extended family's shenanigans"
            t "So many of my friends have left the islands. With climate change their sugarcane crops are suffering badly."
            t "The Navy has really impacted the land, Clara. Poisoned our soil, paved over graves."
            c "I'm here to help, Auntie Tita."
            c "Let me have a look at the remote printer's source code."
            c "I'll get those communications out as soon as possible."

    "You walk to the Center for Chamoru Rights and you find the printer and plug in your laptop"
    "You are able to extract the source code from the printer"
    c "Alright, time to get this working!"

    call check_100_posters from _call_check_100_posters
    #Extension or bonus, fix the printer so it can print any number of posters, not just 100

#Then she does the hack of posters. Either 'EVACUATION. RIGHTS FOR REFUGEES' or 'RESIST. PROTECT THE LAND'

    "You did it!"
    "End of Demo"
    "End of Demo"
    "End of Demo"
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
