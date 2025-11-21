init:
    $ money = 0 
    $ day = 1
    $ current_time = "morning"  # morning/evening
    $ available_jobs = ["cleaner", "shop"]  # Доступные работы
    $ unlocked_jobs = []  # Открытые работы
    $ days_worked = {"cleaner": 0, "shop": 0, "bar": 0, "factory": 0}  # Статистика по работам

label room_screen:

screen room_morning:
    add "bg room morning.png"

    imagebutton:
        xpos 956
        ypos 725
        idle "heels idle.png"
        hover "heels hover.png"
        action Jump("school_day" + str(school_day))
    
    imagebutton:
        xpos 207
        ypos 867
        idle "notebooks idle.png"
        hover "notebooks hover.png"
        action Jump("school_day" + str(school_day))
    
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
        action Jump("school_day" + str(school_day))
    
    imagebutton:
        xpos 207
        ypos 867
        idle "notebooks idle.png"
        hover "notebooks hover.png"
        action Jump("school_day" + str(school_day))
    
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
                text "День: [day]"
                text "Деньги: [money]"

screen stats_display_evening:
        frame:
            xalign 0.95
            yalign 0.05
            
            background "stats_frame.png"

            vbox:
                text "День: [day]" color "#FFFFFF"
                text "Деньги: [money]" color "#FFFFFF"