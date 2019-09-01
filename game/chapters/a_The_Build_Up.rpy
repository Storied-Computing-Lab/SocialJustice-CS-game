label a_The_Build_Up:

    #This transform doesn't belong here, but for debugging and demo purposes:
    transform text_choice_effect:
        ypos -200
        linear 10 ypos 800
        pause 10

    transform bounce:
        pause .15
        yoffset 0
        easein .175 yoffset -10
        easeout .175 yoffset 0
        easein .175 yoffset -4
        easeout .175 yoffset 0
        yoffset 0

    show clara_neutral_eyes_open at lowered_left_2
    show niko_neutral_eyes_slight_smile at nb_lowered_right

    c "Hey cousin"
    #hide niko_neutral_eyes_neutral
    #show niko_neutral_eyes_slight_smile at nb_lowered_right
    #On second playthrough of this dialogue, Aug 26, I'm less horrified of the player choices, just need to be more rewarding or to really change responsive from Niko
    n "Hey Clara."
    c "So how's it going with the Hacker Boyz?"
    hide niko_neutral_eyes_slight_smile
    show niko_neutral_eyes_neutral at nb_lowered_right
    show niko_neutral_eyes_neutral at bounce
    n "It's fine why are you so interested?"
    hide clara_neutral_eyes_open
    show clara_pointer_left_eyes_open at lowered_left_2
    c "I've told ya before I've been working on my hacking and I wanna join too"
    hide niko_neutral_eyes_neutral
    show niko_neutral_eyes_worried at nb_lowered_right
    show niko_neutral_eyes_worried at bounce
    n "and I've told YOU before that it might be weird if you're the only girl..."
    hide clara_pointer_left_eyes_open
    show clara_neutral_eyes_closed at lowered_left_2
    c "C'mon Niko!"
    n "sorry..."
    hide clara_neutral_eyes_closed
    show clara_neutral_eyes_open at lowered_left_2
    c "Wouldn't it be better for everyone if the Hacker Boyz had a new perspective on the team?"
    n "I guess. I'm just worried about how you'd fit in with the guys"
    menu: #both choices need to have POSTIIVE and NEGATIVE clear consequences
        "I'm pretty flexible":
            #THIS ONE REALLY NEEDS SOME WORK:
            show text "+10% Stand your ground" at text_choice_effect
            n "I don't know Clara. I know you're smart, but the guys..."
            n "...."
            n "They just really... ACT like guys, you know?"
            c "I said I can handle it. Trust me."
            c "And you've got my back, right Niko?"
            n "--"
            n "----"
            n "yeah of course Cuz"
            "Niko's hesitation was kind of weird. So you try another angle"
            $pass #the change girls choice. The "cloak" coping(?) choice: (cloak switch armour, like Ariel & Michelle. Take up space other workplace 'hacks' see corkboard.)
        "They'd need to adjust to a new perspective":
            show text "+10% Challenging norms" at text_choice_effect
            c "Well as far as fitting in,"
            c "I acutally think THEY would need to do work to adjust and welecome a Chamoru, female perspective!"
            n "oh-- Do some work to adjust--? Adjust to you?"
            c "We each have to do the work so that we all 'fit in' together."
            $pass #the change the game choice. The

    #be explicit with the player how you leveled up yourself:
    #You just helped Clara cope with master's concerns cloak coping versus master is accountable. Both are anti-oppression work?)

    #Not really there yet, but eventually:
    #be explicit with the player how you leveled up Niko (internalized misogyny)
    hide clara_neutral_eyes_open
    show clara_pointer_left_eyes_closed at lowered_left_2
    show clara_pointer_left_eyes_closed at bounce
    c "and plus, right now YOU're the only Chamoru in the group!"
    hide niko_neutral_eyes_worried
    show niko_neutral_eyes_neutral at nb_lowered_right
    show niko_neutral_eyes_neutral at bounce
    n "So?"
    menu: #I'm mostly ok slash kinda excited about this player choice, I just want to make their input EVEN MORE CRUCIAL,
    #like the player choice that happens later in choosing Tita's evacuation versus Esperansa's stand and defend
    #In ^that case, it will really change the course of the story. What does THISv choice do?
        "With me that would make TWO Chamorus in the group!":
            show text "+10% Stand your ground" at text_choice_effect
            c "Soooo! Niko with me that would make TWO Chamorus in the group!"
            n "Hm. Maybe you're right that would improve things..."
            n "They do sometimes look at me weird whenever I question their jokes about people from Dededo"
            $ x = 1 #something to level up her breaking in and disrupting score I guess
            $ pass#No player choices need to interrupt, but here just like KK:H some reward for reimaging could fly into the air? idk it's a good plot point?
        "Maybe we should form a brand new hacker group of Chamorus!":
            show text "+10% Reclaim our imagination" at text_choice_effect
            c "Maybe you and I could form a brand new Chamoru hacker group Niko"
            c "It could focus on Chamoru specific issues. What do you think?"
            n "That actually might be cool"
            $ x = 1 #an animation to level up Clara's reimagining skill
            $ x = 1 #< -- but Niko and the PLAYER still need to help her somehow reimagine ??
            $ x = 1 #an animation to level up Niko's radicalization
    n "Hm. Yeah. But I don't think the hacker boys are 'racist'..."
    #Here's a chance for player and clara to level up his critique ?????
    #maybe she comes in with higher critique ability over imagination <-- player needs to help us with this
    menu:
        "Why do you say they're not racist?": #use critical ability
            show text "NEW ABILITY: CRITIQUE" at text_choice_effect
            n "They don't say racist things or discriminate against me for being Chamoru"
            c "But isn't there a reason you said 'it might be cool' to just be Chamoru hackers together?"
            $ x = 1 #helping Niko be critical using her ability should be a reward somehow, unlock something? idk
            n "A reason? Hm... It does piss me off when they say shit about the poorer parts of town."
        "Maybe he's right, but does he experience any discrimination?": #learn or level up imagining ability by learning how to imagine together
            show text "+10% Reclaim our imagination" at text_choice_effect
            c "Yeah, I guess it's hard to say if someone is racist or not. What do you think?"
            $ x = 1 #giving Niko the space to imagine together? Show his colors
            n "Well I was thinking about the Chamoru hacker group you mentioned."

    n "What if the Chamoru hackers really did a different type of hacking?"

    "A few days go by. Clara explores a little and comes back to the Center for Chamoru Rights"

    c "Hey Niko"
    n "Hey Clara"
    n "I've been thinking about what you said, and I looked at your last hacker application. They should have let you in"
    c "Really?!? Why'd they reject me"
    n "Maybe discrimination is harder to see than we thought?"
    "A moment of quiet"
    c "What should we do?"
    n "I've got a new hacker challenge for you to try."

    #c "Well anyways, I really do want another challenge. They can't keep rejecting me after all the great programming I've done so far"

    #n "Well I wasn't gonna say it but the new challenge is out if you're ready to try again."

    menu:
        "Well I'm glad you said something! I can do it today!":
            n "Sweet."
        "Hm.. I am SO ready to give a try, but I'm going to give a try later":
            n "Cool. Let's meet at the Center for Chamoru Rights when you're ready!"

    n "Well guess what? You're locked out of your computer!"

    c "what???"
    c "Oh my gosh. _Only you_ would think of a hack like this Niko ya jerk"

    call check_nikos_hack

    "You have two hours. Enough time to complete two actions"



    return
