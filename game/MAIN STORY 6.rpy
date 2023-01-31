#Act 4
label capture:
    menu:
        "Spend time with Tsubasa":
            $ tsubasaScore = tsubasaScore + 1
            jump tsubasacapture
        "Spend time with Haneko":
            $ hanekoScore = hanekoScore + 1
            jump hanekocapture

label tsubasacapture:
    scene bg asteroid field
    show karahara at left with dissolve
    show tsubasa at right with dissolve
    t "You look like you have a question you want to ask."
    k "What I want to know..."
    k "Why didn't you trust us?"
    t "Who else was I supposed to trust?"
    t "I found out about the Flamechasers, you know. The first team."
    t "I knew Rosie and the Major had to be much closer than I - than we thought."
    t "I knew that Rosie would just let it slip to the Major."
    t "So I couldn't trust them."
    t "Then I thought about whether I'd feel comfortable risking you or Haneko."
    show karahara at left with move:
        xpos 0.2
    t "Major Revelation was already planning to kill one of us for her sick science experiment."
    t "If she found that you knew and were planning against it, what would stop her?"
    show karahara at left with move:
        xpos 0.3
    k "..."
    t "So if I got you involved in my plan..."
    show karahara at left with move:
        xpos 0.4
    t "and put you in danger..."
    "She's crying. Softly, but she's crying."
    show karahara at left with move:
        xpos 0.5
    t "Plus, Haneko's Haneko..."
    t "And you're you."
    show karahara at left with move:
        xpos 0.6
    t "If I wanted to protect - to save! all of us, I had to do it myself!"
    t "But look at where that's gotten us."
    show karahara at left with move:
        xpos 0.7
    t "Right back to square one, except now we can't even run away any more."
    "I take a deep breath."
    show tsubasa at topright with move:
        ease 0.2
    show tsubasa at right with move
    k "If you're done, then I think it's my turn to talk. Hope you're okay with that."
    hide tsubasa with None
    show tsubasa blushing at right with None:
        xzoom -1.0
    t "- Huh?!"
    k "Tsubasa, you idiot."
    k "Did you forget our promise?"
    t "I...I couldn't ever forget."
    k "Then act like it."
    k "When we made that promise, we knew something."
    k "We knew we'd be each other's wings."
    k "We knew we couldn't do it alone."
    k "I'm an idiot."
    k "Haneko can't break the rules to save her life."
    k "You're afraid."
    k "So afraid you pushed us away."
    k "So afraid you insisted it would be better to be alone forever than risk anything."
    k "Risk any of us having any chance to make our own mistakes."
    k "The thing is, you're right, Tsubasa."
    k "Haneko's Haneko."
    k "I'm me."
    k "And you're you."
    k "We're each other's wings, Tsubasa."
    k "I need you, and you need me."
    if tsubasaScore > hanekoScore:
        k "So my wings, my sky, I'll put my life in your hands."
        k "Make sure you catch me, alright?"
        t "But why? Why trust me like this?"
        k "Because..."
        k "Because I love you, Tsubasa."
        k "I want to be with you."
        k "Can you answer me?"
        t "..."
        t "I...love you too, Karahara! I'll catch you, no matter what!"
        t "So please!"
        t "Don't you {i}dare{/i} die!"
        k "I won't."
        k "After all, I'm coming home to you."
    jump finalBattle

label hanekocapture:
    scene bg desert
    show karahara at left with dissolve
    show haneko at right with dissolve
    "Haneko looks at me, confused."
    h "Do you think that Tsubasa’s telling the truth? That there’s some sort of conspiracy?"
    "I run my hands through my hair."
    "Thinking through all the information that's been dropped in my lap is hard."
    k "I know she called herself our enemy, but..." 
    k "I don't think she'd lie to us."
    k "In fact, given what we know about the situation at this point..."
    k "My gut's saying what she was saying's true."
    "She thinks quietly for a moment, her finger tracing the shape of her perfectly polished water bottle."
    h "Assuming what she says is true… If we really are just pawns to be sacrificed to some grand plan, then I won't obey."
    h "I joined to fight for justice, but I also joined to fight for you...and Tsubasa."
    h "I don't care about some shadowy government that wants my...friends dead."
    h "I care about you because I know you care about me."
    "I'm getting a weird feeling, a small hunch. Why is Haneko saying things like 'I don't care about the rules'?"
    k "Thanks, Haneko. Me too."
    hide haneko with None
    show haneko blushing at right with None
    "Haneko gives me a bright smile."
    h "Do you really mean that?"
    show haneko blushing at right with move:
        xpos 0.7
    "She asks with a keen to her voice, some desperation she hasn't been able to keep out of her voice."
    "I smile back, thinking of the girl who's saved me more times than I can count."
    show haneko blushing at right with move:
        xpos 0.5
    "Big trouble or little trouble, she always came to help me."
    k "Yeah, I do. Why wouldn't I like the girl who always comes to bail me out?"
    hide haneko blushing with None
    show haneko at right with None:
        xpos 0.5
    show haneko at right with move:
        xpos 0.6
    h "Is that all I am to you?"
    k "No, of course not, Haneko."
    hide karahara with None
    show karahara blushing at left with None
    hide haneko with None
    show haneko blushing at right with None:
        xpos 0.6
    show haneko blushing at right with move:
        xpos 0.4
    "Crap, why is my face red now?"
    h "Then what am I to you?"
    k "I..."
    "Haneko is..."
    k "...my rock."
    hide haneko blushing with None
    show haneko at right with None:
        xpos 0.4
    show haneko at right with move
    k "Wait, sorry, I haven't finished!"
    k "I mean, you're the one person I can can always depend on."
    show haneko at right with move:
        xpos 0.6
    k "You're always there when we set out, and you're always there when we come home."
    k "If any of us need you for anything, you're always there!"
    show haneko at right with move:
        xpos 0.4
    k "...And...I think I need you now. More than ever."
    hide karahara blushing with None
    show kara conflicted at left with None
    k "Major Grace or Tsubasa might have betrayed us. They both might have betrayed us."
    k "I'm told I can't let either one go. I can't forgive either one of them."
    k "What am I supposed to think? What am I supposed to do?"
    k "I...don't know."
    k "All I know is that you won't betray us."
    k "You won't ever go back on your word."
    k "And that means more to me than you could ever know."
    hide kara conflicted with None
    show kara blushing at left with None
    h "...stand up, Karahara."
    k "...hu - "
    show haneko at right with move:
        xpos 0.3 xzoom -1.0
    "She grabs my face and pulls me into a searing kiss."
    "My thoughts melt away."
    "She's warm and soft and firm in all the ways in all the right places."
    "But more than that she's {i}here{/i} and holding me and I let myself go."
    "I don't know how long it takes."
    "I don't know how long we're there."
    "I don't care."
    "Haneko's kisses have a way of making me realize nothing else is important."
    "But even if I would be happy staying like this forever -"
    show haneko at right with move:
        xpos 0.4
    h "It’s almost time to head out. Are you ready?"
    "we break away, just like that, her face still showing shades of crimson."
    "My brain isn't working."
    "All I'm recognizing is her hand."
    "I take it."
    "We walk back to the command center, hand in hand."
    jump finalBattle