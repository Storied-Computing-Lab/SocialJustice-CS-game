label dededo:
    call screen dededo_imagemap
    "You are at dededo"
    $print("dededo day is: " + str(day))

    return

label fleamarket:
    scene flea_market
    "Dededo Flea Market"
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
