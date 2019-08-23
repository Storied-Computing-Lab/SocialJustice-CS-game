label a_The_Build_Up:
    $claras_computer_locked = True

    show clara phone at lowered_center
    show niko_neutral_body at nb_lowered_right
    show niko_face_calm at nh_upper_right

    c "hey cousin"
    hide niko_face_calm
    show niko_face_raisedeyebrow at nh_upper_right
    n "hey clara"

    c "so how's it going with the hacker boys?"

    n "It's fine why are you so interested?"

    menu:
        "I've told ya before I've been working on my hacking and I wanna join too":
            n "and I've told YOU before that it might be weird if you're the only girl"
            label radical_convo1:
                c "C'mon Niko!"
                n "sorry, you're right. That's sexist. I'm sorry"
                c "and anyways, right now YOU're the only Chamoru in the group!"
                menu:
                    "With me that would make two Chamorus in the group":
                        c "With me that would make two Chamorus in the group!"
                        $ x = 1 #something to level up her breaking in and disrupting score I guess
                    "Maybe we should form a brand new hacker group of Chamorus!":
                        c "Maybe you and I could form a brand new Chamoru hacker group Niko"
                        c "It could focus on Chamoru specific issues. What do you think?"
                        n "That actually might be cool"
                        $ x = 1 #an animation to level up Clara's reimagining skill
                        $ x = 1 #< -- but Niko and the PLAYER still need to help her somehow reimagine ??
                        $ x = 1 #an animation to level up Niko's radicalization
                n "Hm. Yeah. But I don't think the hacker boys are _racist_..."
                #Here's a chance for player and clara to level up his critique ?????
                #maybe she comes in with higher critique ability over imagination <-- player needs to help us with this
        "I could ask you the same question. Aren't they just a bunch of white 'bros' ?":
            n "Yeah I guess I've got that 'man - advantage.'"
            n "or might I say, manvantage?"
            c "man-vantage? You're such a nerd!"
            n "Nuh-uh. You're the nerd!"
            c "We nerds should stick together. Don't ya think? I deserve a chance to be in the hacker boys!"
            n "But don't you think it would be weird if you were the only girl?"
            jump radical_convo1

    menu:
        "Why do you say they're not racist?": #use critical ability
            n "They don't say racist things or discriminate against me for being Chamoru"
            c "But isn't there a reason you said 'it might be cool' to just be Chamoru hackers together?"
            $ x = 1 #helping Niko be critical using her ability should be a reward somehow, unlock something? idk
            n "A reason? Yeah...I think we might be able to "
        "_Maybe he's right, but does he experience any discrimination?_": #learn or level up imagining ability by learning how to imagine together
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




    c "Well anyways, I really do want another challenge. They can't keep rejecting me after all the great programming I've done so far"

    n "Well I wasn't gonna say it but the new challenge is out if you're ready to try again."

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
