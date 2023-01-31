# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Karahara", color=(0,0,255))
define h = Character("Haneko", color=(0,255,0))
define t = Character("Tsubasa", color=(255,0,0))
define r = Character("Rosie", color=(255,63,63))
define g = Character("Grace", color=(63,255,63))
define a = Character("All", color=(255,255,255))
define u = Character("UNKNOWN", color = (255,255,255))


init:

## MAJOR GRACE
    image MGRneutral:
        "Major Grace sprite draft.png"
        zoom .3
    image grace:
        "Major Grace sprite draft.png"
        zoom .3
    image grace crying:
        "Major Grace crying draft 1.png"
        zoom 0.3

## ROSIE

    image rosie:
        "Rosie sprite draft 1.png"
        zoom .3
    image rosie cont:
        "Rosie sprite contemplative.png"
        zoom .3

## TSUBASA

    image tsubasa:
        "tsubasa.png"
        zoom .3
    image tsubasa blushing:
        "Tsubasa sprite blushing.png"
        zoom 0.3

## HANEKO

    image haneko:
        "haneko.png"
        zoom .3
    image haneko Uni:
        "haneko uniform.png"
        zoom .3
    image haneko Uni blush:
        "haneko Sprite uniform blushing.png"
        zoom .3
    image haneko blushing:
        "Haneko Sprite pilot suit blushing.png"
        zoom 0.3

## KARAHARA

    image karahara:
        "karahara.png"
        zoom .3
    image karaRage:
        "Karahara Sprite pilot suit rage.png"
        zoom .3
    image kara Uni conflicted:
        "Karahara Sprite uniform conflicted_done.png"
        zoom .3
    image kara Uni:
        "karahara uniform.png"
        zoom .3
    image kara conflicted:
        "Karahara Sprite pilot suit conflicted_done.png"
        zoom .3
    image krage = "Karahara Sprite pilot suit rage.png"
    image kara shade:
        "Karahara Sprite pilot suit eyes shaded.png"
        zoom .3
    image kara blushing:
        "Karahara Sprite pilot suit blushing.png"
        zoom 0.3
    

## CHARACTER INTROS

    image karaharaIntro1:
        "karahara-intro1.png"
        zoom .3
    image hanekoIntro1:
        "haneko-intro1.png"
        zoom .3
    image tsubasaIntro1:
        "tsubasa-intro1.png"
        zoom .3

## MECHA COLLECTION


## FOR FLIPPING SPRITE:
    #xzoom -1.0

## FOR ROTATING SPRITE:
    #rotate(degrees)

## PENGUIN
# HEADSHOTS:
    #zoom 4.0 [xanchor 0.5] yanchor 0.0
# GUN COMMAND IS:
    #rotate(45) zoom 4.5 xalign 0.3 yalign 0.3
    #fire with hpunch
    #to get the explosions of three round burst
    #use explosion chain with hpunch at:
        #xalign 0.23 yalign 0.38 zoom 0.3
# SHIELD COMMAND IS:
    # zoom 2.5 xanchor 0.7 yalign 0.4

    image penguin:
        "penguin.png"
        zoom .2
    image penguin close:
        "penguin.png"
        zoom .225
    image penguin glowy:
        "penguin 34 glowy.png"
        zoom .2
    image penguin far:
        "penguin.png"
        zoom .15
    image penguin pulse:
        "penguin.png"
        zoom .2
        ease 0.5
        "penguin 34 glowy.png"
        zoom .2
        ease 0.5
        repeat

## KINGFISHER
# FOR HEADSHOTS
    #zoom 4.0 xanchor 0.7 yanchor 0.15
    image kingfisher:
        "kingfisher 34.png"
        zoom .2
    image kingfisher far:
        "kingfisher 34.png"
        zoom .15

# "BEGIN FIRING SEQUENCE."
#     show kingfisher with move:
#         ease 0.5 zoom 4.0 xanchor 0.7 yanchor 0.15
#     "AIM..."
#     show kingfisher with move:
#         ease 0.5 zoom 2.0 xanchor 0.2 yanchor 0.3
#     "FIRE!!!"
#     show kingfisher with vpunch:
#         ease 0.3 zoom 2.0 rotate(45) xanchor 0.2 yanchor 0.3
#     show kingfisher:
#         ease 0.5 zoom 1.0 rotate(0) xalign 0.5 yalign 0.5

## PHOENIX HEART
# FOR HEADSHOTS:
    #zoom 4.0 xanchor 0.5 yanchor 0.25
    image pheart:
        "Phoenix Heart 34 glowing.png"
        zoom .15
    image pheart far:
        "Phoenix Heart 34 glowing.png"
        zoom .1
    image pheart_scary:
        "Phoenix Heart 34 super cool silhouette-min.jpg"
        zoom .15

## WHITE RAVEN

    image white graven:
        "White Raven 34.png"
        zoom 0.17
    image white graven glowing:
        "White Raven 34 glowing.png"
        zoom 0.17

## VISUAL EFFECTS

    image bg charonchar:
        "bg char on char.png"

    #WARNING: REMOVE IN NEXT EDITIONS
    image explosion:
        "explosion.png"

    image explosion chain:
        "explosion.png"
        ease 0.1
        "tinyfiller.png"
        ease 0.1
        "explosion.png"
        ease 0.1
        "explosion.png"
        ease 0.1
        "explosion.png"
        ease 0.1
        "tinyfiller.png"
        ease 0.1

    image hanekobraceletcg:
        "bg Haneko bracelet exchange.jpg"
        zoom 0.3
    
    image mechvsmech:
        "bg mech vs mech.jpg"
        zoom 0.3
# The game starts here.

#Act 0
label start:
    define hanekoScore = 0
    define tsubasaScore = 0
    menu:
        
        "<LOADING MECHANIZED MEMORIES>":
            jump introductions

        #"new gallery thing":
        #    jump gallery

        #"Rebel against the system":
        #    jump void

        "Jump to current scene: test":
            jump test

    # This ends the game.

    return
