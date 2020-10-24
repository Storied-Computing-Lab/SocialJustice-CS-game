# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image tinian japaneseGate = "misc/tinian-japaneseGate.png"
image claras_computer_screen = "claras_computer_screen.png"
image DisastersComic1 = "misc/TheDisastersComic1.png"
#image clara_desktop = "clara_desktop.png"
image atom_opened = "atom-opened.png"
image center library_space = "library_computer_lab.png"
image skatepark = "dededo_skatepark.jpg"
image flea_market = "dededo_fleamarket1.jpg"
image driving = "driving.jpg"
image cypher = "firstcypher.jpg"

define t = Character("Tita")
default stand_s = 0
default imagine_s = 0
default norms_s = 0
default hack_s = 1
default notebook_images = ["notebook.jpg", "firstcypher_copy.jpg"]


$ config.console = True
$ config.developer = True #is this actually persisting during build? because of stdout_line needs it to be True
$ config.debug = True

init -999 python:
    config.console = True
    config.developer = True #is this actually persisting during build? because of stdout_line needs it to be True
    config.debug = True
    pic_index = {"picture_index": 0}

transform lowered_center:
    xalign 0.5
    yalign -0.1

transform lowered_left_2:
    xalign -0.3
    yalign 1.0

transform lowered_left_icls:
    xalign 0.0
    yalign 0.5

transform lowered_left:
    xalign -0.1
    yalign -0.1

transform nb_lowered_right: #works with Niko's body
    xalign 1.0
    yalign -0.1 #aparently not?? #negative moves it down, positive moves it up. Recompile all of renpy

transform t_lowered_right: #works with Tita's body
    xalign 1.0
    yalign -.1

transform t_icls:
    xalign 0.9
    yalign -1.8

transform nh_upper_right: #works with Niko's head?
    xalign .835
    yalign -.01 #more negative moves it up?

init python:
    build.name = "Guaiya_MayDEBUG"
    build.directory_name = "Guaiya_MayDEBUG"
    build.executable_name = "Guaiya_Means_Love.MayDEBUG"

init python:

    import utilities.BaseStatsObject_CharacterStats as BS_CS

    class Connections(object):
        def __init__(self):
            self.connections = {}
            self.connections.connections = {}


    class CharacterStats(BS_CS.BaseStatsObject):

        # Set the store.{prefix}.character_id value
        # STORE_PREFIX = "character_stats"

        # Boolean toggle for validation - defaults both True
        # VALIDATE_VALUES = False
        # COERCE_VALUES = False

        STAT_DEFAULTS = {
            'gender' : 'f',
            'location' : 'airport',
            'connections' : {}
        }


default test_name = "Clara"
define character.c = Character("[test_name]")
#default c = CharacterStats("c", location='japaneseGate', connections = {'Niko': {},'Tita': {}})
#July 16th programming tangent: this 'connections' web 'who knows who' needs to be maintained in another script, datastructure??

define character.n = Character("Niko")
#default n = CharacterStats("n", connections = {'Andrew':{},'Tita':{}, 'Clara':{}})

define character.b = Character("Braelin")
#default b = CharacterStats("n", connections = {'Andrew':{}})

define character.e = Character("Esperansa")
#default e = CharacterStats("e", connections = {'Andrew':{},'Tita':{}, 'Clara':{}, 'Cdr Rubino':{}, 'deRoche':{}, 'MaAse':{}})


# The game starts here.
#Used to make the text bigger for better screenshots:
#define gui.choice_button_text_size = 60


#testing screen

    #show tinianJapanese-gate
    #show cipher-screen
    #show tinianJapanese-gate



#The code for the screen called in the in game pop up below
#This is just an image of an example notebook that I have thrown into the images directory

#Have an internal notebook counter variable saved in pic_index dictionary to dictate picture shown in notebook
#making sure that variable doesn't go over the variable that indicates the hack that you are on/under 0
#foward/back buttons increment/decrement internal counter variable and refresh notebook so that a new picture is loaded
screen notebook():
    modal True
    python:
        def picture_inc():
            if pic_index["picture_index"] == hack_s - 1:
                pic_index["picture_index"] = hack_s - 1;
            else:
                pic_index["picture_index"] += 1
        def picture_dec():
            if pic_index["picture_index"] <= 0:
                pic_index["picture_index"] = 0
            else:
                pic_index["picture_index"] -= 1
    add notebook_images[pic_index["picture_index"]]
    vbox xalign 0.668 yalign 0.0:
        imagebutton auto "exit_%s.png" action Hide("notebook", dissolve)

    vbox xalign 0.658 yalign 0.92:
        imagebutton auto "foward_button_%s.png" action picture_inc, Show("notebook")
    vbox xalign 0.0 yalign 0.92:
        imagebutton auto "backwards_button_%s.png" action picture_dec, Show("notebook")

    

# clickable icon
#This clickable icon is called in /chapters/a_The_Buid_Up
#It essentially adds the icon to the top left and allows it to be clicked
#However it needs to be able to be closed !!! Potential fix: Add .png of a red 'x' to the side thats clickable
#FIX ME
screen ingamemenu:
    vbox xalign 0.0 yalign 0.0: #vbox can call on where the pop up will be. Theyre coordinates
        imagebutton auto "notebookicon_%s.png" action Show("notebook", dissolve)
    
        #vbox xalign 0.668 yalign 0.0:
            #imagebutton auto "exit_%s.png" action renpy.hide_screen("ingamemenu")
            #imagebutton auto takes in the notebook icon photo in the image directory
            #you have to have two images in order for it to work, hence the "_%s"
            #this then shows the notebook screen which is in line 124
        
        




label start:
    $day = 0
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    #scene cypher
    #"Niko: Get to your hack!"

    scene tinian japaneseGate
    $ print("Hello world japaneseGate")

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show screen player_actions
    #show screen simple_screen



    #show screen ingamemenu

    #THIS NEXT LINE SHOULD BE THE FIRST CHAPTER!!!!!!!!!!!!!!!!!
    call a_The_Build_Up from _call_a_The_Build_Up #Hack1. Get in the code, cousin's prank.
    $ import os; print(os.environ)

    $ print("Hello from inside the first call to print")
    $ import sys; sys.stdout.write("Hello sys.stdout.write just ran\n")
    call aa_The_Disasters from _call_aa_The_Disasters #Hack2. Baby social justice for-loop.

    call ab_The_Clash from _call_ab_The_Clash

    call ac_The_Meeting from _call_ac_The_Meeting

    call ad_The_Demands from _call_ad_The_Demands

    call ae_The_Resistance from _call_ae_The_Resistance

    call af_The_Translation from _call_af_The_Translation

    call ag_The_Silence from _call_ag_The_Silence

    call ah_The_Renewal from _call_ah_The_Renewal

    call ai_The_News from _call_ai_The_News

    call aj_The_Takeover from _call_aj_The_Takeover

    call ak_The_Reach from _call_ak_The_Reach

    call al_The_End from _call_al_The_End


    show clara phone at lowered_left
    show tita_neutral at t_lowered_right

    "Here ends the DEMO"
    "THANK YOU FOR PLAYING!"
    "GOODBYE"

    # This ends the game.

    return