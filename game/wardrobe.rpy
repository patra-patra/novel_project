init python:
    characters = {
        "teacher": {
            "name": "Учительница",
            "description": "Элегантный наряд для строгой учительницы.",
            "idle_image": "cloth_teacher_idle.png",
            "hover_image": "cloth_teacher_idle.png",
            "locked_image": "cloth_teacher_locked.png",
            "story_label": "emi_story",
            "unlocked": False
        },

        "snowgirl": {
            "name": "Снегурочка",
            "description": "Изящный наряд внучки деда Мороза",
            "idle_image": "cloth_snowgirl_idle.png",
            "hover_image": "cloth_snowgirl_idle.png",
            "locked_image": "cloth_snowgirl_locked.png",
            "story_label": "emi_story",
            "unlocked": True
        },

        "ророро": {
            "name": "лллл",
            "description": "Элегантный наряд для строгой учительницы.",
            "idle_image": "cloth_teacher_idle.png",
            "hover_image": "cloth_teacher_idle.png",
            "locked_image": "cloth_teacher_locked.png",
            "story_label": "emi_story",
            "unlocked": False
        },
    }


    
# This is the default index for the character currently being viewed.
default character_index = 0

# Screen to switch between character stories.
screen character_selection():
    add "bg room.jpg" # Replace with your actual background image file path

    # Left navigation arrow
    if character_index > 0:

        imagebutton:
            idle "images/arrow_left.png"
            hover "images/arrow_left_hover.png" # Replace with your actual hover image file path
            action SetVariable("character_index", character_index - 1)
            xalign 0.0
            yalign 0.5

    # Character image in the center bottom
    $ char_id, char_info = list(characters.items())[character_index]
    $ image_to_display = char_info["idle_image"] if char_info["unlocked"] else char_info["locked_image"]
    $ hover_image = char_info["hover_image"] if char_info["unlocked"] else image_to_display
    $ action = Jump(char_info["story_label"]) if char_info["unlocked"] else None

    imagebutton:
        idle image_to_display
        hover hover_image
        action action
        xalign 0.5
        yalign 1.0

    
    # Right navigation arrow.
    if character_index < len(characters) - 1:

        imagebutton:
            idle "images/arrow_right.png"
            hover "images/arrow_right_hover.png" # Replace with your actual hover image file path
            action SetVariable("character_index", character_index + 1)
            xalign 1.0
            yalign 0.5

    # ImageButton for quit the game.
    frame:
        xalign 1.0
        yalign 0.0
        imagebutton:
            idle "images/quit_idle.png"
            hover "images/quit_hover.png" # Replace with your actual hover image file path
            action MainMenu()
            xalign 1.0
            yalign 0.5


# Label for start the game and show the screen with characters selection and their story.
label wardrobe:
    call screen character_selection
    return

# Labels for character stories.
label lyra_story:
    $ characters["emi"]["unlocked"] = True # unlock Emi
    "~Unlock Emi story"
    jump start

label emi_story:
    "~Thank you sooo much for watching and for your support!"
    jump start