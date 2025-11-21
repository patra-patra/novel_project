label rootine_school:
    $ days_worked["school"] += 1
    $ day += 0.5
    $ money += 50
    $ current_time = "evening"

    "Ничего нового просто школьный день"
    call screen room_evening
