init:
    $ money = 0 
    $ day = 1
    $ current_time = "morning"  # morning/evening
    $ days_worked = {"school": 1, "snowgirl": 1, "flyers": 1, "model": 1, "advertising": 1} 
    $ works_score = {"school": 0, "snowgirl": 0, "flyers": 0, "model": 0, "advertising": 0}

label room_screen:

screen room_morning:
    add "bg room morning.png"

    imagebutton:
        xpos 956
        ypos 725
        idle "heels idle.png"
        hover "heels hover.png"
        action Jump("school_day" + str(days_worked["school"]))
    
    imagebutton:
        xpos 207
        ypos 867
        idle "notebooks idle.png"
        hover "notebooks hover.png"
        action Jump("school_day" + str(days_worked["school"]))
    
    imagebutton:
        xpos 1186
        ypos 427
        idle "tv idle.png"
        hover "tv hover.png"
        action Jump("wardrobe")
    
    imagebutton:
        xpos 836
        ypos 128
        idle "wardrobe idle.png"
        hover "wardrobe hover.png"
        action Jump("wardrobe")

    imagebutton:
        xpos 361
        ypos 167
        idle "snowgirl idle.png"
        hover "snowgirl hover.png"
        action Jump("wardrobe")

    imagebutton:
        xpos 652
        ypos 925
        idle "flyers idle.png"
        hover "flyers hover.png"
        action Jump("wardrobe")
    
    use stats_display_morning

screen room_evening:
    add "bg room evening.png"

    imagebutton:
        xpos 956
        ypos 725
        idle "heels idle.png"
        hover "heels hover.png"
        action Jump("school_day")
    
    imagebutton:
        xpos 207
        ypos 867
        idle "notebooks idle.png"
        hover "notebooks hover.png"
        action Jump("school_day" + str(days_worked["school"]))
    
    imagebutton:
        xpos 1186
        ypos 427
        idle "tv idle.png"
        hover "tv hover.png"
        action Jump("wardrobe")
    
    imagebutton:
        xpos 836
        ypos 128
        idle "wardrobe idle.png"
        hover "wardrobe hover.png"
        action Jump("wardrobe")

    imagebutton:
        xpos 361
        ypos 167
        idle "snowgirl idle.png"
        hover "snowgirl hover.png"
        action Jump("wardrobe")

    imagebutton:
        xpos 652
        ypos 925
        idle "flyers idle.png"
        hover "flyers hover.png"
        action Jump("wardrobe")
    
    use stats_display_evening

screen stats_display_morning:
        frame:
            xalign 0.95
            yalign 0.05

            background "stats_frame.png"

            vbox:
                text "День: [int(day)]"
                text "Деньги: [money]"

screen stats_display_evening:
        frame:
            xalign 0.95
            yalign 0.05
            
            background "stats_frame.png"

            vbox:
                text "День: [int(day)]" color "#FFFFFF" font "gui/fonts/Pacifico-Regular.ttf"
                text "Деньги: [money]" color "#FFFFFF" font "gui/fonts/Pacifico-Regular.ttf"