label dededo:
    call screen dededo_imagemap
    "You are at dededo"
    $print("dededo day is: " + str(day))
    return

label fleamarket:
    scene flea_market
    "Dededo Flea Market"
    call aa_The_Disasters from _call_aa_The_Disasters #Hack2. Baby social justice for-loop.
    jump dededo
    return

label driving:
    scene driving
    "Driving around Guahan"
    jump dededo
    return

label skatepark:
    scene skatepark
    "Dededo Skatepark"
    jump dededo
    return
