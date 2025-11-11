init:
    $ money = 2000 
    $ day = 1
    $ current_time = "morning"  # morning/evening
    $ available_jobs = ["cleaner", "shop"]  # Доступные работы
    $ unlocked_jobs = []  # Открытые работы
    $ days_worked = {"cleaner": 0, "shop": 0, "bar": 0, "factory": 0}  # Статистика по работам

label room_screen:

screen room:
    add "bg room_day.png"

    imagebutton:
        xpos 606
        ypos 718
        idle "school_idle.png"
        hover "school_hover.png"
        action Jump("school_day" + str(school_day))
    
    use stats_display

screen stats_display:
        frame:
            # Optional: Add a background image or color for the stats frame
            # background "stats_frame.png"
            xalign 0.95 # Adjust position as needed
            yalign 0.05

            vbox:
                text "День: [day]"
                text "Деньги: [money]"