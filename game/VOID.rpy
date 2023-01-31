init python:
    def slide_function1(trans, st, at):
        if st > 1.5:
            trans.xalign = 1.5
            return None
        else:
            trans.xalign = st
            trans.yalign = st
            return 0

    def slide_function2(trans, st, at):
        if st > 1.5:
            trans.xalign = -1.5
            return None
        else:
            trans.xalign = st
            trans.yalign = -st
            return 0

label void:
    play sound robloxdeathsound
    show amogus:
        function slide_function1
        function slide_function2
        repeat
    "You entered the void of unwritten story."

    jump credits

label test:
    "<ENTERING TESTING GROUNDS>"
    show pheart at center with None
    "TEST FILLER"
    show pheart at center with None:
        xalign 0.5 yalign 0.5
    "EYES."
    show pheart with None:
        ease 0.5 zoom 4.0 xanchor 0.5 yanchor 0.25
    "SWORD."
    show pheart with None:
        ease 0.5 rotate(45) zoom 2.0 xanchor 0.5 yanchor 0.3
    scene hanekobraceletcg
    "<TEST COMPLETE.>"
