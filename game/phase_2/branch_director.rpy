label branch_director:
    "ахххххххххххххх [works_score['school']] и [days_worked['school']]"

    if works_score["school"] >= 3 and days_worked["school"] >= 4:
        jump school_branch1
    elif works_score["snowgirl"] >= 3 and days_worked["snowgirl"] >= 4:
        jump snowgirl_branch1
    elif works_score["model"] >= 3 and days_worked["model"] >= 4:
        jump model_branch1
    elif works_score["advertising"] >= 3 and days_worked["advertising"] >= 4:
        jump advertising_branch1
    elif works_score["flyers"] >= 3 and days_worked["flyers"] >= 4:
        jump flyers_branch1
    else:
        "никуда не директит"