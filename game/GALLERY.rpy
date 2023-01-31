# Gallery

label gallery:
    scene allfivegirls
    #imagebutton auto "karahara-intro1_%s.png" action Jump("galleryKarahara")
    menu:
        "Karahara":
            jump galleryKarahara
        "Tsubasa":
            jump galleryTsubasa
        "Haneko":
            jump galleryHaneko
        "Mech vs Mech":
            jump MechvMech

    return

label galleryKarahara:
    show karahara-intro1
    hide karahara-intro1

    return

label galleryTsubasa:
    show tsubasa-intro1
    hide tsubasa-intro2

    return

label galleryHaneko:
    show haneko-intro1
    hide haneko-intro2

    return

label MechvMech:
    show mechvsmech
    hide mechvsmech

    return
