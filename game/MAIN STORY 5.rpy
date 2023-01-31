#Act 3
label secondbattle:
    scene bg starry sky
    play music "audio/output1-2.mp3"
    show grace at right with None
    show haneko at topleft with None
    show karahara at left with None 
    g "Attention, Flamechaser unit."
    g "I trust you all understand the situation, but I will repeat myself to ensure we all understand what our responsibilities are."
    g "As of two days ago, your teammate stole the state of the art Phoenix Heart."
    g "She has fled into the nearby asteroid mining zone."
    g "Make no mistake - this is a betrayal of Iuryis, of us, and of you."
    hide karahara with None
    show kara shade at left with None
    k "{i}She didn't betray us.{/i}"
    k "{i}She couldn't have.{/i}"
    g "I want you to understand the gravity of the situation."
    g "The Flamechaser Unit is a part of the military."
    g "Being a part of the military means being subject to military regulations."
    g "Tsubasa will face court martial, and if there is reasonable evidence to suggest that she had co-conspirators, they too will face court martial."
    g "At the very worst, execution is possible."
    g "I am telling you these things because I want you to know the truth."
    g "She has committed a grave offense."
    g "Do you understand me?"
    show haneko at topleft with None
    h "Yes, ma'am!"
    show karahara at left with None
    k "...Yes, ma'am."
    g "So long as you do."
    g "Therefore our objective for this operation is to recapture the Phoenix Heart."
    g "You are to prioritize that objective above all others."
    g "Do you understand that?"
    show haneko at topleft with None
    h "...yes, ma'am."
    show karahara at left with None
    k "..."
    g "...May I remind you that many people have given you their trust, and expect great things of you."
    g "Compared to the weight of all those expectations, your own emotions are nothing."
    g "A certain allowance can be made for childishness, but you'll have to grow up eventually."
    g "So capture the Phoenix Heart intact."
    g "The plan details will be transmitted to you."
    g "Do not deviate from them without my permission."
    g "That's all. Dismissed."
    jump ODH

label ODH:
    scene bg charonchar
    play music "<loop 42.0>audio/karahararobotrapgodeminem.mp3"
    show grace at left with None
    show tsubasa at right with None
    g "I don't believe it'll do much good, but I'll offer anyways."
    g "Surrender, Tsubasa."
    g "We can overlook some childish indiscretions."
    "Grace had read Tsubasa all wrong."
    "Tsubasa was a genius."
    "Tsubasa was too proud to accept condescension."
    "And if Tsubasa thought that things were bad enough that she had to leave..."
    "I was thinking about whether she might not be right."
    "And that meant I had to wonder if Major Grace was {i}wrong{/i}."
    g "Very well. All forces pursue."
    scene bg asteroid field
    "But first."
    show penguin glowy at center with hpunch
    "I had to catch her."
    hide penguin glowy with vpunch
    scene bg asteroid field with fade
    show pheart at truecenter with moveintop:
        zoom .2
    show tsubasa at right with dissolve
    t "..."
    show pheart at truecenter with move:
        xpos 0.4 ypos 0.4 zoom .3
    show karaRage at left with dissolve
    k "Why did you run away?!"
    show pheart at truecenter with move:
        xpos 0.6 ypos 0.6 zoom .4
    t "..."
    hide karaRage with None
    hide tsubasa with None
    show pheart at truecenter with move:
        xpos 0.8 ypos 0.5 zoom .5
    "I knew it was probably pointless."
    show pheart at truecenter with move:
        xpos 0.4 ypos 0.8 zoom .6
    "Out in the open, there were some things that just couldn't be said."
    show pheart at truecenter with move:
        xpos 0.5 ypos 0.2 zoom .7
    "But still, some things can't just go unanswered."
    show tsubasa at right with None
    show karaRage at left with None
    show pheart at truecenter with move:
        xpos 0.55 ypos 0.3 zoom .8
    k "Come on, Tsubasa! Give me a real answer!"
    show pheart at truecenter with move:
        xpos 0.45 ypos 0.4 zoom .9
    t "I'm dangerous! Stay away!"
    show pheart at truecenter with move:
        xpos 0.55 ypos 0.5 zoom .9
    k "I won't accept that answer!"
    show pheart at truecenter with move:
        xpos 0.5 ypos 0.55 zoom .9
    k "If that's your answer, I'll chase you until you give me a better one!"
    show pheart at truecenter with move:
        xpos 0.45 ypos 0.5 zoom 1.0
    k "You and I both know that there's only one way that ends!"
    show pheart at truecenter with hpunch:
        zoom 1.0
    scene bg charonchar with fade
    show karaRage at left with None
    show tsubasa at right with None
    t "..."
    t "You're right."
    t "But I still can't."
    t "There's too many people listening, and I won't see you ruin yourself to save me."
    t "Hate me if you must. But..."
    t "Well, we've all chosen our paths."
    scene bg asteroid field with None
    show pheart at truecenter with None:
        zoom .5
    show karahara at left with None
    "I frowned."
    "She was distancing herself."
    "Physically and emotionally."
    hide karahara with None
    show kara shade at left with None
    show pheart at topright with move:
        zoom .5
    "But if she wanted, she could fly away at any moment."
    "Her machine was powerful enough that I'd never be able to catch up on my own."
    show pheart at top with None:
        zoom .5
    show explosion at topright with None:
    h "Tsk. Shot missed. Reloading."
    hide explosion with None
    show pheart at topright with None:
        zoom .5
    "She wanted to stay here, where she could come back and hit us."
    show pheart at truecenter with move:
        zoom .75
    "Where she could close the distance and reach us."
    show pheart at truecenter with move:
        zoom 1.0
    hide karashade with None
    show karahara at left with None
    show tsubasa at right with None
    "Even now she still felt something for us."
    k "Are you really sure?"
    t "Yes. I am."
    show pheart at truecenter with None:
        xpos 0.2
    "..."
    show explosion at topleft with None:
        zoom 0.3
    show pheart at truecenter with None:
        xpos 0.5
    h "I told you. Tsubasa's too stubborn to answer like that."
    g "Move to phase two, then."
    "Missiles fanned out, streaking towards Tsubasa."
    scene pheart_scary with None
    "Tsubasa's machine burned bright red."
    show pheart with None
    "I knew those moves."
    scene bg asteroid field with None
    show pheart at truecenter
    "Tsubasa had shown them to me enough, from the same side of the simulation battle."
    hide pheart with moveoutleft
    show explosion at truecenter with None
    "Her machine flashed right,"
    hide explosion with None
    show pheart at truecenter with moveinright:
        zoom .4
    show explosion at topright with None:
        zoom 0.3
    "then left,"
    scene explosion:
        zoom 2.0
    show pheart with None
    "and then she was through the cloud of missiles."
    scene bg asteroid field
    show pheart at truecenter with None
    "Closing the distance to where her radiance would blind us to anything -"
    scene pheart with None
    "- and everything else but her."
    scene bg charonchar with None
    show karaRage at left with None
    show tsubasa at right with None
    "But that was pointless."
    hide karaRage with None
    show penguin glowy at topleft with fade
    "I ramp up my thrusters as far as they go."
    hide penguin glowy at topleft with None
    show explosion at topleft with None
    show penguin glowy at topleft with None
    show karaRage at left with hpunch
    k "Then let's see who's more stubborn in the end!"
    scene pheart
    show tsubasa at center with None
    "Right now, all I can see is her."
    scene bg asteroid field
    show pheart at truecenter with None:
        zoom .5
    show tsubasa at right with hpunch
    show explosion at left with None
    "My cannon chatters in bracketing fire."
    show explosion at topleft with None
    "Forcing her to gain distance and slide to the right -"
    scene kingfisher
    "- where Haneko's gun is waiting."
    scene bg asteroid field
    show pheart at truecenter with None:
        zoom 0.75
    "But flamingly brilliant Tsubasa had her own way of evading the trap."
    show pheart at right with move:
        xzoom -1.0
    "Breaking through my cannonfire with her flaming sword."
    show explosion at truecenter with None:
        zoom 1.2 xpos 0.4
    "Refusing my half-hearted attempts to gain distance."
    scene bg charonchar
    show karaRage at left with None
    show tsubasa at right with None
    "Good. I didn't want to distance myself anyway."
    hide karaRage with None
    show tsubasa with None
    show penguin glowy at topleft with None
    show pheart at right with None
    show karaRage at left with None
    show tsubasa at right with None
    "If Tsubasa was going to come to me, I would meet her in the middle."
    show explosion at offscreenleft with hpunch
    "No more hesitation."
    hide explosion with hpunch
    "I wouldn't look away again."
    scene explosion
    "Her burning sword cut straight through my cannon."
    "The half that's left is a spike of molten slag."
    scene pheart with hpunch
    "I rammed the singed remains she's left me against her thick skull."
    scene bg asteroid field
    show pheart far with dissolve
    show explosion at truecenter with None:
        zoom .6 xpos 0.6 ypos 0.4
    "Haneko's cannon round, straight through the left wing spar."
    scene penguin
    "My unwieldy bulk holding onto a melted piece of scrap and a promise on my shield."
    scene pheart
    "Her slim radiance, one eye weeping and one wing missing, angelic even at its most monstrous."
    scene bg asteroid field
    show pheart at truecenter with None
    show karaRage at left with None
    show tsubasa at right with None
    "Major Grace said something."
    "I ignored it."
    "There was no way that was going to work."
    "Not against the Phoenix Heart."
    "Not against Tsubasa."
    hide pheart with moveoutleft
    show penguin at truecenter with moveinright
    "Me and Tsubasa circled each other."
    hide penguin with moveoutleft
    show pheart at truecenter with moveinright
    "I couldn't let her run away from me."
    scene bg charonchar
    show penguin at left with None
    show pheart at right with None
    "She couldn't let me take the lead."
    scene bg charonchar
    show karaRage at left with None
    show tsubasa at right with None
    "We couldn't take our eyes off of each other."
    scene bg asteroid field
    show pheart at truecenter with None:
        zoom 0.2
    show haneko at right with None
    show karaRage at left with None
    h "So, we've got to take that down."
    h "Do you have something in mind?"
    k "Yeah."
    k "<>"
    k "Got it?"
    h "Yeah."
    k "I'm counting on you, Haneko."
    h "You always are."
    "I smiled. That was Haneko. Always there for me."
    scene bg charonchar
    show explosion at topleft with None
    show penguin at left with None
    show pheart far at right with None
    "And because she was there for me, I fearlessly charged that red beast."
    scene bg asteroid field
    show penguin at left with None
    show pheart far at right with None
    "But -"
    hide pheart far with moveouttop
    "Rather than fight me, Tsubasa leapt up."
    show explosion at left with None:
        zoom 0.2
    h "Firing."
    hide explosion with None
    "I barely caught the dust plume Haneko's artillery fire made."
    hide penguin with moveouttop
    show pheart at truecenter with moveintop:
        zoom 0.7
    "I was too busy trying to catch up to Tsubasa's new attitude."
    show pheart at truecenter with dissolve:
        zoom 0.5
    "She rose quickly, but she rose elegantly."
    show pheart at truecenter with vpunch
    "I rose with the fury of a stampede."
    "She turned back to me a moment too late to react."
    scene explosion with hpunch
    "I slammed the lip of my shield into her right wing."
    show pheart at truecenter with dissolve:
        xzoom -1.0
    "The wing snapped halfway down, even as the wing's dying embers scorched my shield black."
    "Rather than cease fighting, she cast off her two broken wings and drew her sword once more."
    scene karaRage
    "I couldn't meet her raised sword with any less resolve."
    scene bg charonchar
    show karaRage at left with None
    show tsubasa at right with None
    "I charged her with my blackened shield."
    scene bg charonchar with hpunch
    "In one clash, she nearly cut through my dense shield."
    show karaRage at left with None
    show tsubasa at right with None
    k "If you want to break through..."
    "But her blade {i}stopped{/i}."
    k "You'll have to try much harder than that!"
    "I grabbed my shield with both hands and wrenched her sword out of her hands."
    show explosion at offscreenleft with hpunch
    show karaRage at left with move:
        xpos 0.4
    "If I had to throw away my shield too, that was fine."
    show tsubasa at right with move:
        xpos 0.6
    "Now there was just us."
    g "Alright, Karahara, that's enough! Haneko, take the shot!"
    h "But Grace -!"
    g "But nothing! Remember your objectives!"
    "..."
    scene bg asteroid field
    show tsubasa mech at center with None
    "I couldn't let her die like this."
    k "It's fine so long as we recover the Phoenix Heart, right?"
    scene bg charonchar
    show penguin glowy at left with None
    show pheart at right with hpunch
    "I raised my hands and charged Tsubasa, hand to hand."
    scene bg charonchar
    show karaRage at left with None
    show tsubasa at right with hpunch
    "She matched me, my equal and opposite."
    scene mechvsmech
    "The impact rattled me in my seat, as my thrusters contended against hers."
    "Machine against machine."
    "Woman against woman."
    "Talking with our hands since words had failed us."
    show karaRage at left with None:
        xpos 0.3
    show tsubasa at right with None
    k "You said that you had something to say to me, right?"
    k "Well, talk to me!"
    show MGRneutral at topleft with moveinleft
    t "It's still too dangerous! You should just run away, and forget about me!"
    hide MGRneutral with moveoutleft
    k "No! I refuse to run! I won't let you go!"
    k "I'm going to make you tell the truth from your own mouth!"
    "The Phoenix Heart's hands begin to glow."
    "Temperature warnings start popping up all over the HUD."
    "Heat was cycling through her hands so fast it was threatening to burn my own to ash."
    "But I didn't care about any of that."
    "I pushed my throttle just a little bit harder."
    "And in the pushing match, my thrusters were made to push my dense mass around."
    "Hers was only to keep her moving forward."
    "Now that she had melted away all the layers of armor, I was free to pursue what I wanted, with all of my strength."
    "I wanted her."
    "I wanted her to stay."
    "So even if my hands melted to slag from the heat, my chest slammed into hers as I shoved her against an asteroid."
    "She still had her sword."
    "She still had her machine at nearly peak form."
    "My own machine was melting where we touched."
    "I had no weapons. Nothing to protect myself from her."
    "But I embraced her burning spirit anyways, because I cared about her more than anything."
    scene bg desert with vpunch
    show karaRage at left with None
    show tsubasa at right with None
    "My arms had melted away, up to my elbows."
    "My main cockpit armor wasn't doing much better."
    k "Sorry, Penguin. Just a little longer."
    hide karaRage with None
    show kara conflicted at left with None
    "My cockpit heat warnings turned off."
    "Half the screens were black or cracking."
    "I secured my helmet and ejected."
    "My machine's hatch slammed me backwards and launched me out of the seat."
    show penguin at center with None
    show explosion at center with vpunch
    "The Penguin's last lights flickered off."
    hide kara conflicted with None
    hide penguin with None
    hide explosion with None
    show kara shade at left with None
    "Without me, my machine was nothing but metal."
    "At least its bulk would get in the Phoenix Heart's way, if she tried to escape."
    hide kara shade with None
    show karaRage at left with None
    "But it was okay. The Penguin had given me the chance I needed."
    "I had something else in mind for Tsubasa."
    "I raised my hand to my helmet flashlight, looking directly at the Phoenix Heart's eyes."
    "<CAN WE TALK NOW?>"
    jump MYMC1

    
label MYMC1:
    scene bg desert
    show karahara at left with fade
    k "..."
    show tsubasa at right with fade
    t "..."
    play music "<loop 42.0>audio/karahararobotrapgodeminem.mp3"
    k "So."
    t "So. Are we going to fight here too?"
    k "Are you going to run away again?"
    t "Even if I wanted to, you’d follow. That doggedness was always your most annoying trait."
    hide karahara at left with None
    show karaRage at left with None
    k "How mean, senpai."
    hide karaRage with None
    show karahara at left with None
    t "Don’t call me that."
    k "Are you not?"
    t "I didn’t say that."
    k "Then why would you run away, you big coward?!"
    t "..."
    t "You were always more right than you knew."
    t "You remember what I taught you, right?"
    k "How could I forget?"
    t "Then come with me. This is still too exposed."
    k "Of course."
    hide tsubasa with moveoutright
    hide karahara with moveoutright
    scene bg charonchar with fade
    show tsubasa at right with None
    show kara conflicted at left with None
    t "That face isn’t cute on you."
    t "You’ve got something to say, right?"
    hide kara conflicted with None
    show karaRage at left with None
    k "Is this another one of your jokes?"
    t "I wouldn’t joke about something like that."
    k "Then was all of our time together a joke?"
    t "Never. I just…"
    t "Have you ever had to make a choice between two horrible options?"
    hide karaRage with None
    show karahara at left with None
    k "..."
    t "It doesn’t look like Major Grace can hear us. Record this, or don’t. I don’t particularly care."
    menu:
        "Trust the plan. Disable the microphone.":
            jump recorderOff

        "Only one way to be sure: Take off your helmet completely":
            jump helmetoff

    label recorderOff:
        k "So. What’s so desperate that you needed to abandon us?"
        t "Do you know why we were assigned to the Flamechaser unit?"
        hide karahara with None
        show karaRage at left with None
        k "Because Grace knew that we were the best."
        k "Haneko’s brains, your skills, me."
        k "We are - no, we were the best team in the whole universe!"
        hide karaRage with None
        show kara conflicted at left with None
        k "We were inseparable!"
        t "Exactly, and that’s the problem."
        k "What?"
        t "Do you know what the Phoenix Heart is?"
        hide kara conflicted with None
        show karaRage at left with None
        k "Don’t play dumb. Just because I act stupid doesn’t mean I actually am."
        t "I know. I’ve always known. But I need to say it, because there’s something you haven’t thought through."
        hide karaRage with None
        show karahara at left with None
        t "That Phoenix Heart was made with technology we don’t understand, the YURI core."
        t "Major Grace was assigned by the government to find out just how powerful it is, but it’s been years without results."
        t "She hasn’t been able to stabilize it, to make the output consistent."
        t "All we’ve found so far is that it grows stronger the more powerful the emotions of the pilot."
        k "So what’s the problem? We were picked because we {i}could{/i} find it!"
        t "You {i}still{/i} don’t get it! We {i}can{/i} is not the same thing as we {i}will{/i}, and the former isn’t good enough for the government,
            so it’s not good enough for the Major!"
        t "I found out the real plan for us Flamechasers. Flamechaser 1 was assigned to the Phoenix Heart, and 2 and 3 would be escort fighters."
        hide karahara at left with None
        show kara conflicted at left with None
        t "The Major specifically planned for Flamechaser 3 - for you - to die to unleash the Phoenix Heart’s full power,
            just like that time fifteen years ago."
        t "But there’s one big problem with this plan: How does the Commodore know when Flamechaser 3 would die?"
        k "..."
        t "It’s obvious, isn’t it? Major Grace {i}set it up{/i}. There’s a bomb planted in your machine, and if that doesn’t work, she’ll just shoot you."
        k "But if you knew, couldn’t you do something about it?"
        t "This is the best I could do, okay?"
        t "I’m not…I’m not like you, Karahara."
        t "I’m not that dumb."
        hide kara conflicted with None
        show karaRage at left with None
        t "I’m not that trusting…"
        hide karaRage with None
        show karahara at left with None
        k "Then you should’ve told us."
        k "That’s why we’re a team, right?"
        k "If you couldn’t do it, {i}we{/i} might have!"
        t "..."
        "I sigh."
        if hanekoScore > tsubasaScore:
            k "Well, what’s done is done."
            k "Thanks for telling us that, Tsubasa. But you’re not alone, and neither am I."
        else:
            hide karahara with None
            show kara conflicted at left with None
            k "You know, I wish you would've just told me this from the start."
            k "Because now...now there's no way to stop this."
            "Karahara exchanges a meaningful look with Tsubasa, before fiddling with her mic."
        t "...!"
        scene kingfisher
        show haneko at left with dissolve
        k "That’s our Haneko. Give it up, Tsubasa. The gambit’s over."
        jump capture

    label helmetoff:
        "You feel so free, without your helmet. Everything seems to be so clear, without the tint of your visor. The feeling of cool space on your skin,
            your hair flapping in the breeze. The sight of Tsubasa’s concern for you takes your breath away."
        "Oh wait."
        "That’s the vacuum. You’re literally choking from lack of air.
            That breeze is just your air pressure system failing to keep up with the demands of the vacuum."
        "Hm."
        "Taking your helmet off in space sure was a dumb way to die, wasn’t it."
        play music "audio/robloxdeathsound.mp3"
        jump credits