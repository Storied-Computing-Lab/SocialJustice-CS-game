label a_The_Center2:
    c "Hey Niko"
    n "Hey Clara"
    n "I've been thinking about what you said, and I looked at your last hacker application. They should have let you in"
    c "Really?!? Why'd they reject me"
    n "Maybe discrimination is harder to see than we thought?"
    "A moment of quiet"
    c "What should we do?"
    n "I've got a new hacker challenge for you to try."

    scene black with dissolve
    "In this game you will have to hack your way to justice."
    "Try to fix niko's hack to continue on in the game."
    "You'll need those skills later"
    scene tinian japaneseGate with dissolve

    c "Well I'm glad you said something! I can do it today!"
    n "Well guess what? You're locked out of your computer!"
    c "what???"
    c "Oh my gosh. *Only you* would think of a hack like this Niko ya jerk!"
    show screen ingamemenu
    c "Let me get my notebook for this!"
    "Niko hands you a clue."
    #Scene Cypher is just a background that gets called... it contains the images of my proposed cypher and the instructions are then
    #told through niko via the games text below
    scene cypher1_mac
    #scene cypher1_pc commented out whichever one you need to call upon
    # For the sake of simplicity for the test run on 11/2 I think its best to leave the cypher as an actual screen rather than a hoverable, or else the user testers might miss it on their own
    n "Heres a clue, deciper this to reveal a hint for the location of your first hack!"
    n "It's a Caesar Cipher that is shifted by four... GOODLUCK!"
    #Then after this is shown up, we allow the users to first get their in game notebook, which is called below from script.rpy
    call check_nikos_hack from _call_check_nikos_hack

    #increment hack counter variable after hack is complete
    $hack_s += 2
    #call check_nikos_hack from _call_check_nikos_hack
    #Background of game is then reset after hack and cypher dissapears! :)
    scene tinian japaneseGate

    n "Nice one Clara! That was a pretty tough problem."
    n "It took me way longer to finish when I did it."
    n "I have to say, the Hacker Boyz are definitely going to reconsider your application"
    c "Yeah, or again, you and me, starting our own club!"

    n "Keep this cipher, and your notes from this exercise."
    n "They may come in handy, later."
    c "Thanks Niko. I'll keep them in my notebook!"
    "You just earned two new pages in your notebook!"

    n "Great work again, Clara."
    n "And I was thinking about what you said, about the Hacker Boyz and [hacker_boys_racist]."
    n "You know who you should talk to about this kind of stuff?"
    c "Who?"
    n "Esperansa. She's really into the whole social justice thing."
    c "Oh yeah?"
    n "Yeah, I always see her at the town center in Dededo. Giving out food to homeless people"
    c "Oh, wow!"
    n "I'm heading out, but let's talk more later"
    n "I underestimated you cousin!"
    "You're so excited about your first hack, you just want to keep nerding out with Niko."
    "But you're still concerned with the way the Hacker Boyz exclude girls."
    c "Maybe I should meet Esperansa. I could use someone to talk to about this."
    $renpy.call_screen("player_actions1")
