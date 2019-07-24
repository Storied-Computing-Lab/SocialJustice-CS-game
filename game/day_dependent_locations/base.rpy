label base:
    $print("base day is: " + str(day))

    if day == 3:
        e "We're going to a counter protest"
        menu:
            "what's that?":
                e "Certain people are trying to pass an anti-trans rights bill, and we're going to protest to show that more of us disagree than agree with this bill"
            "what for":
                e "show that there are more of us who support trans rights than those of us who want to deny trans rights"
    return
