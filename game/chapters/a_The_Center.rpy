label a_The_Center:

    #This transform doesn't belong here, but for debugging and demo purposes:
    transform text_choice_effect:
        ypos -200
        linear 10 ypos 800
        pause 10

    transform bounce1:
        pause .15
        yoffset 0
        easein .175 yoffset -10
        easeout .175 yoffset 0
        easein .175 yoffset -4
        easeout .175 yoffset 0
        yoffset 0

    "You walk into the Center for Chamoru Rights and look out the window."

    "The green fronds of palm trees sway lazily in the wind."
    "An innoncence and beauty that frustrates you"
    "Because you don't know how to protect it."
    "You shut your eyes for a moment to hold the picture in your mind."
    scene black with dissolve

    c "The U.S. military buildup and bombing is set to steal and destroy even more of our ancestral homeland"
    c "What can my people do to stop this?"

    scene tinian japaneseGate
    "You turn from the window to see your cousin Niko, dressed like a White kid."
    "Again."
    "A little more formal, a little less Chamoru. His style draws attention away from his olive skin and stout islander features."
    "Your mind turns to the matter at hand."

    show clara_neutral_eyes_open at lowered_left_2 with dissolve
    show niko_neutral_eyes_slight_smile at nb_lowered_right with dissolve

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
            $stand_s += .10
            n "I don't know Clara. I know you're smart, but the guys..."
            n "...."
            n "They just really... ACT like guys, you know?"
            c "I said I can handle it. Trust me."
            c "And you've got my back, right Niko?"
            n "--"
            n "----"
            n "yeah of course Cuz"
            "Niko's hesitation was kind of weird. So you try another angle" #the change girls choice. The "cloak" coping(?) choice: (cloak switch armour, like Ariel & Michelle. Take up space other workplace 'hacks' see corkboard.)
        "They'd need to adjust to a new perspective":
            show text "+10% Challenging norms" at text_choice_effect
            $norms_s += .10
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
    hide clara_pointer_left_eyes_closed
    show clara_neutral_eyes_open at lowered_left_2
    n "So?"
    menu: #I'm mostly ok slash kinda excited about this player choice, I just want to make their input EVEN MORE CRUCIAL,
    #like the player choice that happens later in choosing Tita's evacuation versus Esperansa's stand and defend
    #In ^that case, it will really change the course of the story. What does THISv choice do?
        "With me that would make TWO Chamorus in the group!":
            show text "+10% Stand your ground" at text_choice_effect
            $stand_s += .10 #something to level up her breaking in and disrupting score I guess
            c "Soooo! Niko with me that would make TWO Chamorus in the group!"
            n "Hm. Maybe you're right that would improve things..."
            n "They do sometimes look at me weird whenever I question their jokes about poor Chamoru communities in Dededo"
            $ you_the_only_Chamoru = "with me that makes two"
            $ pass#No player choices need to interrupt, but here just like KK:H some reward for reimaging could fly into the air? idk it's a good plot point?
        "Maybe we should form a brand new hacker group of Chamorus!":
            show text "+10% Reclaim our imagination" at text_choice_effect
            $imagine_s += .10#an animation to level up Clara's reimagining skill
            $ you_the_only_Chamoru = "with us as Chamoru hackers"
            c "Maybe you and I could form a brand new Chamoru hacker group Niko"
            c "It could focus on Chamoru specific issues. What do you think?"
            n "That actually might be cool"
            $ x = 1 #< -- but Niko and the PLAYER still need to help her somehow reimagine ??
            $ x = 1 #an animation to level up Niko's radicalization
    n "Hm. Yeah. But I don't think the hacker boys are 'racist'..."
    #Here's a chance for player and clara to level up his critique ?????
    #maybe she comes in with higher critique ability over imagination <-- player needs to help us with this
    menu:
        "Why do you say they're not racist?": #use critical ability
            show text "NEW ABILITY: CRITIQUE" at text_choice_effect
            c "Why do you say they aren't racist?"
            n "They don't say racist things or discriminate against me for being Chamoru"
            $ x = 1 #helping Niko be critical using her ability should be a reward somehow, unlock something? idk
            n "I mean, it does piss me off when they say shit about the poorer parts of town."
            n "..and those parts of town have a lot more Chamorus..."
            n "but they never say anything to me."
            $ hacker_boys_racist = "the shit they say about poorer folks in Dededo"
        "Do they encourage your Chamoru side?": #learn or level up imagining ability by learning how to imagine together
            show text "+10% Reclaim our imagination" at text_choice_effect
            $imagine_s += .10 #giving Niko the space to imagine together? Show his colors
            c "Do you think they encourage your Chamoru side?"
            c "Or do they only like your ideas that make them comfortable?"
            "Niko shifts his weight from left to right."
            "So you try to open him up one more time"
            $ hacker_boys_racist = "experiencing discrimination"

    c "Do you experience any other type of discrimination?"
    if you_the_only_Chamoru == "with me that makes two":
        n "Well I was thinking about having two Chamorus in the group, like you said"
        n "Would that really be enough to combat discrimination?"
        c "We could look out for each other."
        c "What if Chamoru hackers really did a different type of hacking?"
    else:
        n "Well I was thinking about the Chamoru hacker group you mentioned."
        n "What if Chamoru hackers really did a different type of hacking?"
    hide niko_neutral_eyes_neutral
    hide clara_neutral_eyes_open
    "A few days go by. Clara explores a little and comes back to the Center for Chamoru Rights"
    $renpy.call_screen("player_actions1")
    "A few days go by. Clara explores a little and comes back to the Center for Chamoru Rights"


    return
