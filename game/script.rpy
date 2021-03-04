# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image tinian japaneseGate = "misc/tinian-japaneseGate.png"
image claras_computer_screen = "misc/claras_computer_screen.png"
image DisastersComic1 = "misc/TheDisastersComic1.png"
#image clara_desktop = "clara_desktop.png"
image atom_opened = "misc/atom-opened.png"
image center library_space = "misc/library_computer_lab.png"
image skatepark = "misc/dededo_skatepark.jpg"
image flea_market = "misc/dededo_fleamarket1.jpg"
image driving = "misc/driving.jpg"
image front_gate = "misc/front_gate.png"
image banana_fields = "misc/banana_fields.png"
#assign cypher1 image depending on OS
# DOES NOT WORK RIGHT NOW
#init python:
    #import platform
    #os_name=platform.system()
#assign cypher1 image depending on OS
# DOES NOT WORK RIGHT NOW. Need python block?
#Is there an easier way to automate this
#So we can assign a lot of variables
#Dependent on the OS and not have to
#Go through and change Os-dependent artwor
#Manually?
#if os_name == "Darwin":
#    image cypher1 = "Hack_1_Mac.jpg"
#else:
#    image cypher1 = "Hack_1_PC.jpg"
image cypher1_mac = "Hack_1_Mac.jpg"
image cypher1_pc = "Hack_1_PC.jpg"
image cypher2 = "Hack_2.jpg"
define t = Character("Tita")
default stand_s = 0
default imagine_s = 0
default norms_s = 0
default hack_s = 6
default notebook_images = [ "cesarcy.png", "print_statement.png", "regular_methods.png", "class_methods.png","for_loop.png", "black_notes_page.png"]


$ config.console = True
$ config.developer = True #is this actually persisting during build? because of stdout_line needs it to be True
$ config.debug = True

init -999 python:
    config.console = True
    config.developer = True #is this actually persisting during build? because of stdout_line needs it to be True
    config.debug = True
    pic_index = {"picture_index": 0}
    hack1_complete=False
    hint1_numLoops=0

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
    build.name = "Guaiya_Fall20"
    build.directory_name = "Guaiya_Fall20"
    build.executable_name = "Guaiya_Means_Love.Guaiya_Fall20"

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


label start:
    $day = 0
    #scene tinian japaneseGate
    #$ print("Hello world japaneseGate")
    #show screen simple_screen
    #show screen ingamemenu

    #THIS NEXT LINE SHOULD BE THE FIRST CHAPTER!!!!!!!!!!!!!!!!!
    call a_The_Center from _call_a_The_Center #Hack1. Get in the code, cousin's prank.
    #This is the first instance in which cypher 1 for PC or MAC is called ^
    $ import os; print(os.environ)

    $ print("Hello from inside the first call to print")
    $ import sys; sys.stdout.write("Hello sys.stdout.write just ran\n")
    #call aa_The_Disasters from _call_aa_The_Disasters #Hack2. Baby social justice for-loop.
    #call ab_The_Clash from _call_ab_The_Clash
    #call ac_The_Meeting from _call_ac_The_Meeting
    #call ad_The_Demands from _call_ad_The_Demands
    #call ae_The_Resistance from _call_ae_The_Resistance
    #call af_The_Translation from _call_af_The_Translation
    #call ag_The_Silence from _call_ag_The_Silence
    #call ah_The_Renewal from _call_ah_The_Renewal
    #call ai_The_News from _call_ai_The_News
    #call aj_The_Takeover from _call_aj_The_Takeover
    #call ak_The_Reach from _call_ak_The_Reach
    #call al_The_End from _call_al_The_End

    #"Here ends the DEMO"
    #"THANK YOU FOR PLAYING!"
    #"GOODBYE"

    # This ends the game.

    return
