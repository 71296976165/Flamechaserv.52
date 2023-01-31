#Act 2

label chase:
    "(IMMEDIATE SCRAMBLE)"
    play music "audio/karahararobotrapgodeminem.mp3"
    #scene space with fade:
    #    ypos -0.5
    #show karahara mech with leftSide:
    #    ease 1.0 xpos 0.2
    #    ease 1.0 xpos 0.0
    #    repeat
    #show tsubasa mech with rightSide:
    #    ease 1.0 xpos 0.4
    #    ease 1.0 xpos 0.7
    #    repeat
    scene bg starry sky
    "What I see is exactly what I was afraid of."
    "The moment I heard the alarm."
    "The long stutter since I realized the Phoenix Heart wasn't in front of me."
    "Only two people on the base could pilot that thing."
    "Major Grace, and Tsubasa."
    "Major Grace was still in the command center."
    scene pheart_scary
    "So the person in that machine had to be..."
    scene bg starry sky
    show tsubasa at center
    t "Haneko."
    t "Karahara."
    t "Don't follow me."
    show pheart at center with None
    hide tsubasa at center with None
    show tsubasa at center with None
    "Her voice is leaden."
    "She's trying to cover up the regret with finality."
    show tsubasa at right with move
    show haneko at left with None
    h "Tsubasa, stand down or you will be fired upon on!"
    t "Then fire."
    t "I won't be hurt, and you won't be able to stop me."
    hide haneko with None
    show karahara at left with None
    k "Tsubasa, I don't understand!"
    k "Why are you doing this?"
    t "..."
    t "If I explain myself, it'll only make things harder."
    t "You need to give up."
    t "We're not teammates anymore."
    "Her arm snaps up."
    "Faster than I can think, a bolt of flame leaps up off the arm."
    scene bg starry sky
    show kingfisher at center with dissolve
    show penguin at center with moveinright
    "My shield snaps up as I jet in front of Haneko."
    show penguin at center with vpunch
    "The flame spatters against my shield."
    "It slams into me like a freight train,"
    scene pheart_scary
    "because if I hadn't been there, Haneko's machine would have melted."
    scene bg starry sky
    show pheart far at topright with None
    show penguin far at topleft with None
    show tsubasa at right with None
    show karahara at left with None
    t "There. Now you know I'm serious."
    "My breath hitches."
    k "Tsubasa, what are you {i}doing{/i}?"
    t "Didn't you hear me?!"
    t "The Flamechasers are done!"
    hide tsubasa with None
    hide pheart far with moveoutright
    show karahara at center with move
    g "Karahara, you heard her!"
    g "Tsubasa has betrayed the Flamechasers, and must be treated as an enemy!"
    g "If you don't shoot her down, you'll be shot down yourself!"
    hide karahara with None
    hide penguin far with None
    show karaRage with fade
    k "Fine! Be that way!"
    show penguin at left with dissolve
    "A cry tears itself from my throat as I charge forward."
    hide karaRage with None
    hide penguin with moveoutright
    show pheart with moveintop
    show pheart at center with hpunch
    "My cannon chatters futilely."
    show karaRage at left with None
    k "Just stay still!"
    hide pheart with moveoutleft
    hide karaRage with fade
    "The tracer fire flies through the dark of space."
    show pheart at right with moveinright
    "Like moths chasing after ball lightning."
    hide pheart with moveoutbottom
    "Seekers reaching for what cannot be touched."
    show pheart far at center with moveintop
    "From my fingers to the wisps of her trail."
    show pheart far at center with hpunch
    show tsubasa at right with None
    t "Didn't I teach you to be better than that?!"
    hide tsubasa with None
    hide pheart far with moveoutbottom
    show pheart at center with moveintop
    show pheart at center with hpunch
    "She rattles me, like the bucking of my cannon rattles my shoulders and sends tremors through my hands."
    hide pheart with moveoutright
    show penguin at center with moveinleft
    show penguin at center with hpunch
    "But my hands were shaking a long time ago."
    hide penguin with moveoutright
    show pheart with moveinleft
    show karaRage at left with None
    k "It's because {i}you{/i} taught me better than that!"
    show pheart at center with hpunch
    k "It doesn't have to be like this!"
    show tsubasa at right
    t "Then you don't understand anything!"
    scene pheart_scary with hpunch
    "I poured my hatred, my confusion, and all of my feelings into the throttle."
    scene penguin
    "The Penguin answered me."
    scene penguin glowy
    h "Wait for a better shot, Karahara!"
    scene bg starry sky
    show karaRage at left with None
    show pheart at right with moveinright
    k "That won't work against Tsubasa!"
    k "I need to {i}make{/i} my better shot!"
    hide karaRage with moveoutbottom
    hide pheart with moveoutleft
    "Tsubasa danced between our shots."
    show pheart far with moveinbottom
    "A whole sky of enemies would not be fit to be her opponent."
    hide pheart far with moveouttop
    "How could we imagine our two guns to be equal?"
    show pheart far at truecenter with moveinleft
    "But if my eyes weren't tricking me..."
    show pheart far at truecenter with move:
        ease 1.0 xpos 0.4
        ease 1.0 xpos 0.6
        repeat
    "She was just dodging us."
    "She only shot once."
    "Even if her whole body was aflame with heat, she didn't even respond once."
    "I knew she could have."
    "Was this just arrogance, or just a mask of anger?"
    "I didn't know."
    "I let go of the trigger."
    "For a moment, Tsubasa stopped too."
    show haneko at topleft with None
    show karahara at left with None
    show pheart far at truecenter with move
    k "...Haneko, are we getting anywhere with this?"
    h "..."
    jump tsucom1

label tsucom1:
    hide haneko with moveoutleft
    "I see."
    "Fine."
    hide pheart far with moveoutright
    "If she was willing to burst into flames to get away..."
    hide karahara with None
    show karaRage at left with None
    k "Disengaging heat limiters."
    scene penguin pulse
    show karaRage at left with None
    "I'd have to show that kind of resolve too."
    "I can't hold back if I want to bring her back."
    k "Disengaging all thrust restraints. Disengaging tracking adjustments. Disengaging flywheel stabilization."
    k "Hey, Penguin."
    k "Sorry."
    k "But it's going to get a little hot in here!"
    scene penguin glowy
    "My thrusters roar behind me."
    scene bg starry sky with hpunch
    show pheart far at truecenter with dissolve
    "A flamingly hot sprint heats my own machine to uncomfortable wamrth."
    show pheart at truecenter with dissolve
    "The exertion is making my machine's legs {i}burn{/i}."
    show pheart at truecenter with hpunch
    "And in the center of my eye I see her turn away."
    show karaRage at left with None
    k "No you don't!"
    k "Tsubasa, don't you dare look away!"
    "I flash the RAM-AEGIS in my collar at her."
    show pheart at topright with move
    "The brilliant light catches her eye."
    "It must have blinded her."
    "Temporarily, at least."
    show karaRage at center with move
    "I raise my tracer cannon and fire a burst."
    hide karaRage with None
    show penguin glowy at center with None:
        xzoom -1.0
    show pheart at topright with hpunch
    "I don't need to hit. I just need to convince her to stay!"
    show haneko at topleft with None
    h "Karahara, that's enough! I can't get a good shot!"
    hide haneko with None
    "But Tsubasa hangs in space, keeping our relative distance."
    show pheart at topright with hpunch
    "I can't hit her."
    show pheart at topright with hpunch
    "I'm shaking too badly."
    show pheart at topright with hpunch
    "But I can't catch her any other way."
    show tsubasa at right with None
    t "..."
    t "You always were so stubborn, Karahara."
    t "How far would you chase me?"
    k "As far as I need to!"
    t "...I see."
    t "Then I'm sorry."
    t "But I don't want to hurt you."
    t "And I don't want to let you be hurt."
    "Her hand snaps up, searingly bright light shining into my machine's eyes."
    scene bg starry sky
    "I turn away, blinded, and snap my shield up."
    "But when my eyes clear, I realize she's disappeared."
    "My stomach sinks."
    # camera pan motion
    "Not here, nor there."
    "I'd fallen for the same trick I used on her."
    "The one time she showed too much of herself, and I had the gall to look away."
    show penguin at truecenter with fade
    "I'm caught in indecision."
    "I don't know where she is."
    scene pheart_scary
    show penguin at truecenter with None
    "Her scorchingly hot body wraps around my own machine."
    "Where her hands go, my body melts."
    "She closes my vents, my thrusters, and steals away my attitude control."
    "I'm struggling in her grasp, at her mercy."
    t "I'm sorry, Karahara, but I have to do this."
    scene bg starry sky
    "She whispers it in my ears."
    "A prayer and an apology for the mess she's making out of me."
    scene bg starry sky with hpunch
    "My Penguin crumples under her searing touch."
    "Something explodes in the waist, and my machine folds itself over."
    scene bg starry sky with vpunch
    "I hear pipes burst, hydraulic fluid spilling out into space."
    "And then I feel her warmth leave me, battered and soaked."
    t "I'm sorry, I really am."
    show tsubasa at right with None
    t "But I have to go."
    show karahara at left with None
    k "Tsubasa, why?"
    k "Tsubasa, don't leave me!"
    hide tsubasa with None
    "But she leaves me anyway."
    "A streaking star in the night."
    "My breath leaves me with her departure, a sigh stealing itself away."
    "With her escape, I let go of the controls, and the Penguin..."
    scene penguin
    "The Penguin is like me."
    "Even if I wanted to, I can't pursue her now."
    "All I'm left with is a broken heart."
    jump debriefing

label hancom1:
    
    jump debriefing

label debriefing:
    scene bg starry sky
    jump haneoneyes

label beginning:
    jump mechanic

label haneoneyes:
    show kara Uni conflicted at left with dissolve
    show haneko Uni at right with dissolve
    "I lock my eyes on the ground, not daring to look up and see Haneko’s face right next to me."
    "I shake my head and try to push past her."
    "I screwed up the mission."
    "I know it’s partly my fault for getting seperated from them."
    "I don’t want to hear anything Haneko has to say." 
    "She would support me, and I couldn’t handle that." 
    "I don’t deserve any of it."
    "But as I tried to walk away, she grabbed my hand and stopped me in place."
    h "Kara, about the mission…"
    "I kept my head down." 
    k "{i}‘Don’t do this…’{/i}"
    h "I know you’re not feeling well now, but…"
    "I break my hand away from her grip."
    k "Haneko… I’m sorry, I need some time to myself right now…"
    "She starts saying something else, but I scowl and walk away. I think she’s finished, but then I hear a shout behind me."
    h "Kara, please! I just want you to feel better!"
    k "Leave me alone!"
    hide kara Uni conflicted with moveoutright
    "Quietly, I add “please,” but I doubt she heard me before I run off to my room."
    hide haneko Uni with fade
    show kara Uni conflicted at right with dissolve
    "I couldn’t get there any faster as I flop down on my bed and bury my head into the pillow, my thoughts a swirling mess."
    "Suddenly, I can’t understand why I pushed her away."
    "{i}‘Why do you keep doing this? She needed you too, didn’t see? You’re not the only one upset. You made the same mistake again.’{/i}"
    "An unwanted tear slips onto my pillow."
    "I’ve spent a few post-missions like this, in a self-pitying, miserable state."
    "It’s always my fault, isn’t it?"
    "I let the others down again, and I can’t remember the last time they did the same to me."
    "But before I can slip too far into my misery, a simple thought slips into my mind:"
    "{i}‘You can fix this. Not all hope is lost.’{/i}"
    "If Haneko needs me, all I need to do is go to her, right?"
    hide kara Uni conflicted at right with None
    show kara Uni at right with None
    "I sit up and wipe my face."
    "Melodramatic, aren’t I?"
    "Well, I shouldn’t dwell on it."
    "Haneko’s the one that’s important."
    "I open my door and resist jumping in surprise."
    "Haneko is already outside my door, looking as surprised as I am, albeit with a slight blush covering her face."
    show haneko Uni blush with None
    h "I-I, um, came to see you…"
    hide kara Uni with None
    show haneko Uni blush at center with move
    k "Same here…"
    "We stare at each other for a second before I shake my head."
    show haneko Uni blush at center with move:
        ease 0.5 xpos 0.4
        ease 0.5 xpos 0.6
        ease 0.5 xpos 0.5
    k "You can come in."
    "She walks in, and we both settle on my bed."
    "I quickly flip over my pillow to hide the tear stains."
    hide haneko Uni blush with None
    show haneko Uni with None
    h "Hey, Kara… You were coming to see me?"
    "I’m surprised again, this time to see her face full of resolve."
    k "Well, yeah… I was pretty rude to you, a-and you probably-"
    "Haneko suddenly places her hand on my face."
    h "Don’t worry about it. In fact, don’t say anything else. I’m here to comfort you, okay?"
    "The tears well up inside me again."
    k "But-"
    h "No buts. You’ve supported me up to this point. I’ve got you now."
    "All of a sudden, the tears are coming down again, worse than before."
    "Haneko pulls me into a hug, stroking my hair while I cry."
    "I hate to cry in front of her – she deserves a stronger wingmate than this."
    "But she doesn’t seem to care, comforting me the whole time."
    k "Thank you…"
    "She holds me tighter, and I become warm." 
    "I’m not sure how much time passes, but it doesn’t matter." 
    "Haneko is the only thing that does."

    jump mechanic
