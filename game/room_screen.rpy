init:
    $ money = 0 
    $ day = 1
    $ current_time = "morning"  # morning/evening
    $ available_jobs = ["cleaner", "shop"]  # Доступные работы
    $ unlocked_jobs = []  # Открытые работы
    $ days_worked = {"cleaner": 0, "shop": 0, "bar": 0, "factory": 0}  # Статистика по работам

label room_screen:

screen room_morning:
    add "bg room_day.png"

    imagebutton:
        xpos 606
        ypos 718
        idle "school_idle.png"
        hover "school_hover.png"
        action Jump("school_day" + str(school_day))
    
    imagebutton:
        xpos 638
        ypos 0
        idle "wardrobe_idle.png"
        hover "wardrobe_hover.png"
        action Jump("school_day" + str(school_day))
    
    use stats_display_morning

screen room_evening:
    add "bg room_evening.png"

    imagebutton:
        xpos 325
        ypos 163
        idle "adv_idle.png"
        hover "adv_hover.png"
        action Jump("school_day" + str(school_day))

    imagebutton:
        xpos 638
        ypos 0
        idle "wardrobe_idle.png"
        hover "wardrobe_hover.png"
        action Jump("school_day" + str(school_day))
    
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