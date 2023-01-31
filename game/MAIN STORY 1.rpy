#Act 1
label introductions:
    play music "audio/output1-2.mp3"
    scene bg asteroid field
    show MGRneutral at center
    g "Good morning, Flamechasers."
    g "This is the final shakedown mission before the show of force mission in one month, so I expect you to fight like you’re fighting for real."
    g "I know what your team scores say, but I can still withdraw your pride of place at any time."
    g "My superiors can withdraw you from the Phoenix Heart mission team at any point, and ship you off to the most distant pebble in our solar system."
    g "That’s just how our society works. You have to work to earn your pay."
    g "Your objective in this mission is either elimination of all hostiles or successful escort of all dignitaries from combat area. Are we clear?"
    a "Yes, ma’am!"
    g "Sound off."
    k "(fiddles with a switch above her instrument panel)"
    hide MGRneutral with dissolve
    jump karaharaIntro

label karaharaIntro:
    play music "audio/output1-2.mp3" if_changed
    show karaharaIntro1 at right with dissolve
    show penguin at left with dissolve
    k "I don’t know what to say here! I’m just a normal girl trying to keep up with those two. I guess when the going gets tough,
        I’ve always been able to catch up - even if it’s just by the skin of my teeth."
    k "I just don’t want to ever give this up."
    hide karaharaIntro1 with dissolve
    hide penguin with dissolve
    jump hanekoIntro

label hanekoIntro:
    play music "audio/output1-2.mp3" if_changed
    show hanekoIntro1 at left with dissolve
    show kingfisher at right with dissolve
    k "Haneko is our cool squadron leader. She’s straight-laced and meticulous, but if you ever get into trouble,
        she’ll never fail to get you out. It’s because she’s there that I have a place to return to."
    hide hanekoIntro1 with dissolve
    hide kingfisher with dissolve
    jump tsubasaIntro

label tsubasaIntro:
    play music "audio/output1-2.mp3" if_changed
    show tsubasaIntro1 at left with dissolve
    show pheart at right with dissolve
    k "Tsubasa is our squadron ace. She’s fiery and passionate. She’s the best pilot of our squad, and a genius besides.
        It’s because she’s ahead of me that I have somewhere to reach for."
    hide tsubasaIntro1 with dissolve
    hide pheart with dissolve
    jump graceIntro

label graceIntro:
    play music "audio/output1-2.mp3" if_changed
    show MGRneutral at center with dissolve
    k "Our commanding officer is Major Grace Revelation. She’s twenty years a veteran, and it shows.
        She’s the spitting image of a professional,
        and even if she doesn’t pilot anymore I get the feeling that that’s because she doesn’t want to."
    k "But something has always felt off about her to me."
    hide MGRneutral with dissolve
    jump simulationBattle

label simulationBattle:
    play music "audio/output1-2.mp3" if_changed
    g "Very well. Begin simulation."
    show penguin at center with fade
    "Radar lock warnings blare."
    show penguin glowy at center with None
    k "I jet backwards, covering Haneko and Tsubasa by pure instinct. That’s my job. I’m their shield."
    show penguin at center with None
    hide penguin glowy with None
    show penguin at center with None
    k "The missile warnings blare. I’ve gotten used to them by this point, and with a flick of a switch, the jammers and flares disperse."
    hide penguin with moveoutright
    show kingfisher far at top with dissolve
    show penguin at center with moveinleft
    k "Chaff flares, chaff flares."
    show penguin at center with hpunch
    hide penguin with moveoutright
    hide kingfisher far with None
    show kingfisher at center with fade
    h "Roger, acquiring firing solution. Main cannon firing."
    show kingfisher at center with hpunch
    k "I exist to create space for Haneko and her big gun. She’s steady and reliable,
        and her gun marks the start of our own offensive. If I had to trust one person with my back, Haneko would be it."
    h "Enemies down."
    k "But even though I’ve got the big shield, and Haneko’s got the big guns,"
    hide kingfisher with moveoutbottom
    scene pheart_scary
    k "we’re not the kill leaders."
    scene bg asteroid field
    k "We exist to create space for Tsubasa."
    scene bg asteroid field
    show pheart at center with moveintop
    show pheart at center with vpunch
    k "Tsubasa, and her Phoenix Heart."
    hide pheart with moveouttop
    k "But you know, you can’t take your eyes off any one of us."
    show pheart at center with moveinright
    show pheart at center with hpunch
    k "If you stop watching Tsubasa, she cuts you apart before you can even blink."
    hide pheart with moveoutleft
    show kingfisher at center with moveinleft
    show kingfisher at center with hpunch
    k "If you stop watching Haneko, she’ll get a firing solution and blast you apart."
    hide kingfisher with moveoutright
    k "But I guess you can’t really ignore me, either."
    show penguin glowy with moveintop
    k "Because if you spend all your time looking at them…"
    hide penguin glowy with None
    show penguin close at center with vpunch
    k "You forget about me."
    hide penguin close with fade
    show penguin far at right with moveintop
    show kingfisher far at left with moveinright
    show pheart at top with moveintop
    k "We cover each other’s weaknesses."
    k "We magnify each other’s strengths."
    hide pheart with moveoutbottom
    hide kingfisher far with moveoutright
    hide penguin far with moveoutleft
    scene bg starry sky
    k "Even if every star in the sky becomes our enemy…"
    k "There’s nothing we can’t do."
    "< MISSION COMPLETE >"
    scene bg asteroid field
    show MGRneutral at center with fade
    g "Very well. A passable performance."
    show tsubasa at left with None
    t "It’s still not the highest score, is it?"
    g "As far as this simulation is concerned, it is the highest score."
    k "But we can all hear what she really means. The first Flamechaser team would have done better."
    k "Major Grace’s first Flamechaser team."
    show rosie at right with dissolve
    r "Ah cheer up kids, that was a damn fine performance!"
    jump rosieIntro

label rosieIntro:
    play music "audio/output1-2.mp3" if_changed
    k "Here’s Rosie! Rosie Palms is our favorite mechanic. She’s been working these machines for the past twenty years,
        and although she’s a bit rough around the edges, she always means well. She basically lives in the hangar bays now
        - even moved a cot down here and all."
    hide tsubasa with moveoutleft
    show MGRneutral at left with move
    k "Something’s weird between her and the Major, though…"
    show haneko at center with dissolve
    show rosie at top with move
    h "(winces)"
    h "Please don’t muss my hair again…"
    r "(Smiling menacingly)"
    g "Enough."
    hide haneko with moveoutbottom
    show rosie at right with move
    show MGRneutral at center with move
    g "Make sure you’re well rested."
    g "In two weeks, we’ll have our all-up test of the Phoenix Heart. I need you all to be sharp and ready for that."
    r "Gr-"
    g "Engineer Palms."
    r "- Major Revelation. That’s too soon, we haven’t tuned the Y receivers to an acceptable level.."
    g "It will have to be soon enough."
    g "You should all be prepared for anything."
    jump majordebriefing
