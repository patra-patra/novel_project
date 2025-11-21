label branch_director:
    if works_score["school"] >= 3 and days_worked["school"] >= 4:
        jump school_branch1
    
    if works_score["snowgirl"] >= 3 and days_worked["snowgirl"] >= 4:
        jump snowgirl_branch1
    
    if works_score["model"] >= 3 and days_worked["model"] >= 4:
        jump model_branch1
    
    if works_score["advertising"] >= 3 and days_worked["advertising"] >= 4:
        jump advertising_branch1
    
    if works_score["flyers"] >= 3 and days_worked["flyers"] >= 4:
        jump flyers_branch1