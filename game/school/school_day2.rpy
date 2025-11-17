label school_day2:
    "Второй день"
    $ school_day += 1

    $ day += 1
    $ money += 500
    $ current_time = "evening"

    scene bg school entrance snow with fade
    show sveta_coat_school at center

    "Третий день. Норильский ветер бьёт в лице ледяными иглами, но я иду твёрже. В руках - потрёпанная папка с конспектами и термос с чаем из 'Ролтона'."

    "У входа группа старшеклассников курит. Один из них кричит:"
    student "Эй, училка новая! Не замёрзла там?"
    "Но в его голосе уже нет насмешки - скорее, уважение."

    scene bg teachers room with fade
    show sveta_coat_school at center
    show elena_teacher at left

    "В учительской Елена Петровна разливает крепкий чай по стаканам."
    elena "Светлана, подходи. Греться. Сегодня у вас какой урок?"
    
    show sveta_confident with dissolve
    sveta "Неправильные глаголы. Go-went-gone..."
    elena "Ох, это они ненавидят. Дай совет - через песни. У 'Backstreet Boys' там полно неправильных глаголов."

    "За соседним столом физик Владимир Иванович хмурится:"
    vladimir "Опять эту попсу детям впариваете..."
    elena "Зато запоминают лучше, чем по вашим формулам!"

    "Я тихо улыбаюсь. Впервые чувствую себя частью этого мира."

    scene bg classroom day3 with fade
    show sveta_teaching at center

    "В классе - оживлённый шум. Артём что-то активно показывает одноклассникам на своём Nokia."
    
    show artem_excited at right with moveinright
    artem "Мисс! Смотрите, я 'yesterday' перевёл - это 'go-went' получается!"
    
    sveta "Правильно, Артём! Но 'go-went' - это 'ходить', а 'yesterday' - 'вчера'."
    
    "Класс смеётся. Но сегодня смех другой - не над учителем, а вместе с учителем."

    scene bg school corridor break with fade
    show sveta_talking with dissolve

    "На перемене ко мне подходит рыжая девочка - Лиза."
    
    show liza_shy at left with moveinleft
    liza "Светлана Сергеевна, а можно спросить?.. Как вы стали такой... стильной?"
    
    sveta "Лиза, в Норильске стиль - это не модная одежда. Это умение оставаться собой, когда за окном -35."
    
    liza "А английский правда поможет уехать?"
    
    sveta "Он поможет выбрать - уезжать или оставаться. Но уже не от безысходности."

    scene bg classroom day4 with fade
    "Четвёртый день. В классе появляются первые тетради с домашними заданиями."
    
    show sveta_surprised at center
    "Открываю тетрадь Артёма - он сделал не только упражнение, но и написал три предложения о своих планах на будущее."

    artem "I am going to visit Moscow. I want to see Red Square."
    "Простая фраза, но от неё щемит сердце."

    scene bg teachers room friday with fade
    show sveta_nervous at center
    show director_serious at left

    "Пятница. Перед последним уроком директор вызывает меня в кабинет."
    
    director "Светлана Сергеевна, неделя пробная прошла. Дети довольны, коллеги отзываются хорошо."
    director "Хотите остаться на постоянной основе? Зарплата - 3000 в неделю."

    show sveta_emotional with dissolve
    "Горло перехватывает. 3000 рублей... Это не просто спасение от тёти Люды. Это настоящая жизнь."
    
    sveta "Да... Я очень хочу."

    scene bg classroom final friday with fade
    show sveta_proud at center

    "Последний урок недели. Вхожу в класс - и замираю."
    
    "На доске мелом написано: 'We like our English teacher. She is the best.'"
    
    show artem_smiling at right with moveinright
    show liza_smiling at left with moveinleft
    
    artem "Это мы всем классом, мисс. Вы нас не подвели."
    
    "Лиза протягивает самодельную открытку: нарисованная учительница с указкой, а подпись: 'To our miss from 2000s'"

    sveta "Thank you... I... I won't let you down."
    "Голос срывается, но сегодня это не от страха."

    scene bg school exit evening with fade
    show sveta_happy_end at center

    "Выхожу из школы. В кармане - заветные 3000 рублей. До декабря ещё далеко, но я уже не боюсь норильской зимы."
    
    "Достаю Nokia - пишу Кристине: 'Остаюсь учителем. Дети выучили неправильные глаголы. Я - тоже.'"
    
    "На экране замигал ответ: 'Горжусь тобой! Но помни - в субботу дискотека в ПТ!'"

    sveta "Да уж... Из училки в диджея за один вечер. Welcome to Norilsk, 2000."
    
    scene black with fade
    "..."

    call screen room_evening