# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Clara")
image tinian japaneseGate = "tinian japaneseGate.png"

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

    call guessing_game2

    # This ends the game.

    return
