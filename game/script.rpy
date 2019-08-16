# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image tinian japaneseGate = "tinian japaneseGate.png"
image claras_computer_screen = "claras_computer_screen.png"
#image clara_desktop = "clara_desktop.png"
image atom_opened = "atom-opened.png"
image center library_space = "library_computer_lab.png"
image skatepark = "dededo_skatepark.jpg"
image flea_market = "dededo_fleamarket1.jpg"
image driving = "driving.jpg"
define t = Character("Tita")

$ config.console = True

transform lowered_center:
    xalign 0.5
    yalign -0.1

transform lowered_left:
    xalign 0.0
    yalign -0.1

transform nb_lowered_right: #works with Niko's body
    xalign 1.0
    yalign -1.5 #negative moves it down, positive moves it up. Recompile all of renpy

transform t_lowered_right: #works with Tita's body
    xalign 1.0
    yalign -.1

transform nh_upper_right: #works with Niko's head?
    xalign .835
    yalign -.01 #more negative moves it up?

init python:

    import BaseStatsObject_CharacterStats

    class Connections(object):
        def __init__(self):
            self.connections = {}
            self.connections.connections = {}


    class CharacterStats(BaseStatsObject):

        # Set the store.{prefix}.character_id value
        # STORE_PREFIX = "character_stats"

        # Boolean toggle for validation - defaults both True
        # VALIDATE_VALUES = False
        # COERCE_VALUES = False

        STAT_DEFAULTS = {
            'gender' : 'f',
            'age' : 22,
            'location' : 'airport',
            'connections' : {}
        }

default test_name = "Clara"
define character.c = Character("[test_name]")
default c = CharacterStats("c", location='japaneseGate', age=21, connections = {'Niko': {},'Tita': {}})
#July 16th programming tangent: this 'connections' web 'who knows who' needs to be maintained in another script, datastructure??

define character.n = Character("Niko")
default n = CharacterStats("n", age = 21, connections = {'Andrew':{},'Tita':{}, 'Clara':{}})

define character.b = Character("Braelin")
default b = CharacterStats("n", age = 21, connections = {'Andrew':{}})

define character.e = Character("Esperansa")
default e = CharacterStats("e", connections = {'Andrew':{},'Tita':{}, 'Clara':{}, 'Cdr Rubino':{}, 'deRoche':{}, 'MaAse':{}})


# The game starts here.

label start:
    $day = 0
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene tinian japaneseGate
    #$ print("Hello world japaneseGate")

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show screen player_actions

    call a_The_Build_Up

    call aa_The_Disasters

    call ab_The_Clash

    call ac_The_Meeting

    call ad_The_Demands

    call ae_The_Resistance

    call af_The_Translation

    call ag_The_Silence

    call ah_The_Renewal

    call ai_The_News

    call aj_The_Takeover

    call ak_The_Reach

    call al_The_End

    $how_much_tita_likes_me = c.connections['Tita']
    $claras_conns = c.connections
    $print("Clara's conns: " + str(claras_conns.keys()))
    $print("Who Clara Knows: " + str(claras_conns.keys())) #returns [u'Tita', u'Niko']
    $print(str(claras_conns.keys()[0]))

    $print("Who Niko Knows: " + str(n.connections.keys()))

    $hwtl = str(how_much_tita_likes_me) #doesn't make sense anymore because Tita now points to a dictionary, not an int
    e "Hafa Adai, I'm Esperansa, 'she, her, and hers'"

    "Esperansa offers you a tired smile"

    menu:
        "I'm Clara, she, her, hers":
            e "Great to meet you Clara!"
        "I'm Clara":
            e "Great to meet you Clara!"
        "I'm Clara, why'd you list those pronouns?":
            e "Great question Clara, I'm trying not to assume someone's gender when I first meet them"
            menu:
                "But isn't it more polite to assume just looking at me that I'm a girl?":
                    e "I think gender is a spectrum, and male/female boxes restrict people. What do you think?"
                "I still don't understand":
                    e "That's ok, we can talk again soon!" #set Esperansa_revisit_gender_binary = True
                "I think I understand":
                    e "I'm still learning, too, but I think saying pronouns can mean a lot to people" #points towards some quest or unlocking of Ma'ase ?

    call Niko_reflect_1

    "Expected: Clara 21 japaneseGate\nReceived: [c.name] [c.age] [c.location]"
    # trouble getting [c.connections['MC']] to work, actually it doesn't like [e.connections.keys] either, I think

    show clara phone at lowered_left

    c "Whoa, I'm coming alive!"

    call appearing

    "Wow! Who are you?"
    c "It's magic! She comes and goes!"

    c "Begin the root_virus challenge"

    #This call didn't work (June 20)
    call kill_virus

    c "At this point, you should have finished the virus challenge"



    #This call is having trouble (July 3)
    #call Managed_Memory/kill_virus


    c "Well, now it's time to access the Navy's servers"

    call guessing_game2

    c "We can see their servers now. I should tell the other activists."

    "We see Teresita walking from the center of the {i}siudát{/i}, or city"
    "It's strange how similar the language is to Spanish..."
    "siudát sounds just like ciudad..."

    show tita_neutral at t_lowered_right

    c "Hi Teresita! We just got a through to their servers"
    c "But we've only got a few hours before they notice us"
    c "After that we'll have to switch IP addresses again before our next hack."

    t "Clara, are you sure this is the best way you want to help our cause?"
    t "You just have so many talents other than hacking"
    t "Are you sure hacking really for {i}you{/i}?"

    '''
    MAYBE NOT HERE BUT PLAYER CAN CHOOSE FROM A FEW OPTIONS WHICH OTHER TALENTS CLARA HAS
    '''

    "{i}It seems that Teresita is uncomfortable with the idea of hacking the powerful US Navy.{/i}"
    "{i}Who wouldn't be?{/i}"

    #change Clara expression
    c "Don't worry Tita, we've set up security precautions"

    #change Tita expression
    t "That's good. You have a good team, but don't think you have to stay, Clara"
    t "I like those computer boys but if you ever feel your interests lie elsewhere..."

    #change
    c "....."
    c "....."
    "FOR DRAFTING ONLY : player choose how to respond to Tita"
    "FOR DRAFTING ONLY : Whatever player chooses to do next, still say:"

    "{i}Tita doesn't exactly encourage me to be a coder{/i}"
    "{i}That's for sure{/i}"
    "{i}Why can't I be one of those \"computer guys\" she likes?{/i}"
    c "Well..any social cause needs a diversity of approaches to activism"
    "DRAFTING ONLY: player chooses again whether or not to leave the hacking track here"
    # if hacking:
    # c "But I am the gal to get it done through coding! I wanna keep trying."
    # if 2nd time player affirms they wanna leave:
    # c "So I think it's time to try another approach!"






    # This ends the game.

    return
