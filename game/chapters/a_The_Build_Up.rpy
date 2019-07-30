label a_The_Build_Up:

    c "I would love to talk to Niko about this"

    screen planets: #Preparing the imagemap
        imagemap:
            ground "planets.png"
            hover "planets-hover.png"

            hotspot (62, 399, 90, 91) clicked Jump("mercury")
            hotspot (227, 302, 141, 137) clicked Jump("venus")
            hotspot (405, 218, 164, 118) clicked Jump("earth")
            hotspot (591, 78, 123, 111) clicked Jump("mars")

    # The game starts here.

    "This is an imagemap tutorial."
    jump solar_system

    label solar_system:
        call screen planets #Displaying the imagemap

    label mercury:
        "It is Mercury."
        jump solar_system

    label venus:
        "It is Venus."
        jump solar_system

    label earth:
        "It is Earth."
        jump solar_system

    label mars:
        "It is Mars."
        jump solar_system

    return
