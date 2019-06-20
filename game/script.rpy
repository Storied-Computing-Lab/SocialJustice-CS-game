# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Clara")
image tinian japaneseGate = "tinian japaneseGate.png"
define t = Character("Tita")

transform lowered_center:
    xalign 0.5
    yalign -0.1

transform lowered_left:
    xalign 0.0
    yalign -0.1

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene tinian japaneseGate

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show clara phone at lowered_center

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Hafa Adai, I'm Clara"

    show clara phone at lowered_left

    e "Whoa, I'm coming alive!"

    call appearing

    "Wow! Who are you?"
    e "It's magic! She comes and goes!"

    call Managed_Memory/kill_virus

    e "Well, now it's time to access the Navy's servers"

    call guessing_game2

    e "We can see their servers now. I should tell the other activists."

    "We see Teresita walking from the center of the {i}siudát{/i}, or city"
    "It's strange how similar the language is to Spanish..."
    "siudát sounds just like ciudad..."

    e "Hi Teresita! We just got a through to their servers"
    e "But we've only got a few hours before they notice us"
    e "After that we'll have to switch IP addresses again before our next hack."

    t "Clara, are you sure this is the best way you want to help our cause?"
    t "You just have so many talents other than hacking"
    t "Are you sure hacking really for {i}you{/i}?"

    '''
    MAYBE NOT HERE BUT PLAYER CAN CHOOSE FROM A FEW OPTIONS WHICH OTHER TALENTS CLARA HAS
    '''

    "{i}It seems that Teresita is uncomfortable with the idea of hacking the powerful US Navy.{/i}"
    "{i}Who wouldn't be?{/i}"

    #change Clara expression
    e "Don't worry Tita, we've set up security precautions"

    #change Tita expression
    t "That's good. You have a good team, but don't think you have to stay, Clara"
    t "I like those computer boys but if you ever feel your interests lie elsewhere..."

    #change
    e "....."
    e "....."
    "FOR DRAFTING ONLY : player choose how to respond to Tita"
    "FOR DRAFTING ONLY : Whatever player chooses to do next, still say:"

    "{i}Tita doesn't exactly encourage me to be a coder{/i}"
    "{i}That's for sure{/i}"
    "{i}Why can't I be one of those \"computer guys\" she likes?{/i}"
    e "Well..any social cause needs a diversity of approaches to activism"
    "DRAFTING ONLY: player chooses again whether or not to leave the hacking track here"
    # if hacking:
    # e "But I am the gal to get it done through coding! I wanna keep trying."
    # if 2nd time player affirms they wanna leave:
    # e "So I think it's time to try another approach!"






    # This ends the game.

    return
