label room_screen:

screen room:
    add "bg room_day.png"
    "dsdsdsd"

    imagebutton:
        xpos 606
        ypos 718
        idle "school_idle.png"
        hover "school_hover.png"
        action Jump("school_day" + str(school_day))