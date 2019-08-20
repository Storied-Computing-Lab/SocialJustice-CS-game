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

    n "It's fine why are you so interested? Are you still practicing your hacking?"

    menu:
        "I've told ya before I've been working on my hacking and I wanna join too":
            n "and I've told YOU before that it might be weird if you're the only girl"
            c "C'mon Niko!"
            n "sorry, you're right. That's sexist. I'm sorry"
            c "and anyways, right now YOU're the only Chamoru in the group! With me that'd make two!"
            n "Hm. Yeah. But I don't think they're racist..."
        "I could ask you the same question. Aren't they all white 'bros' ?":
            n "Yeah I guess I've got that 'man-vantage.' They aren't 'racist' against Chamorus though..."
            c "man-vantage? You're such a nerd!"
            n "your a bigger nerd than me cuz!"
            c "you say they're not racist?"
            n "Hm. I don't think so..."

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
