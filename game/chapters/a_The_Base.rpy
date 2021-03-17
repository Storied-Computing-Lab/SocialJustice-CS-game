label a_The_Base:
    e "Clara, we have a problem!"
    c "Oh no, what's wrong Esperansa?"
    e "The navy is trying to poison the soil."
    c "What do you mean?"
    e "The navy wants to turn our land into firing ranges which is known to poison the soil"
    e "This will cause all of our crops and food to die, along with the surrounding fish. They said they'll 'move the fish', whatever that means"
    c "That's terrible! They really don't think we're smart. Is there anything we can do to stop them?"
    e "The best thing we can do stall them"
    c "How?"
    e "Under the National Environmental Policy Act, the navy is required to tell us about this stuff"
    e "So, we have the right to petition and ask a lot of questions"
    e "The only problem is, we need a lot of questions and they need to come from real people"
    c "Hmm, if everyone were to get at least five questions from different people, would that be enough?"
    e "Yes, I think it would be!"

    scene tinian japaneseGate with dissolve
    show clara_neutral_eyes_open at lowered_left_2 with dissolve
    show niko_neutral_eyes_slight_smile at nb_lowered_right with dissolve
    c "Niko, I need your help! The navy are trying to poison our soil."
    n "Uh oh, but how would I help?"
    c "If everyone comes up with at least 5 questions, we can stall them for a while"
    n "I see, I have an idea for what we can do."

    show screen ingamemenu
    c "Let me get my notebook for this!"
    n "We can use something called a dictionary which allows us to store key, value pairs"
    c "So we could store the name and the question?"
    n "Exactly! Look for hack_add_questions.py for more instructions!"

    call check_questions_hack from _call_check_questions_hack

    hide clara_neutral_eyes_open
    hide niko_neutral_eyes_slight_smile
    #increment hack counter variable after hack is complete
    $hack_s += 2
    #call check_nikos_hack from _call_check_nikos_hack
    #Background of game is then reset after hack and cypher dissapears! :)
    scene front_gate with dissolve
    e "Good job Clara! That should stall them for a long time!"

    call ac_The_Meeting

    "We did it! We used our voices!"
    "We collectively delayed the military plans!"
    "How did feel?"
    "What did you learn?"
    "How will you take further action in your community?"

    $renpy.call_screen("player_actions1")
