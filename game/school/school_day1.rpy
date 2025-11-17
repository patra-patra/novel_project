init:
    $ school_day = 1

label school_day1:
    $ school_day = school_day + 1
    $ day = day + 1

    scene bg director_office with fade
    show sveta_nervous_smart at center
    show director_serious at left

    "Кабинет директора пахнет старыми книгами и строгостью. Я сижу напротив женщины в очках, которая изучает моё резюме."

    direkt "Светлана Сергеевна, я вижу у вас филологическое образование... Но педагогического опыта нет."
    direkt "Скажите, почему вы хотите работать именно учителем? В Норильске много других вакансий."

    show sveta_hesitant with dissolve
    "В голове проносятся мысли: 'Потому что тётя Люда выгонит на улицу', 'Потому что нужно 5000 рублей до пятницы'..."

    show sveta_sincere with dissolve
    sveta "Я... я хочу, чтобы дети не были такими, как я. Чтобы они знали, кто они - даже если весь мир говорит, что они ничего не стоят."

    "Директор поднимает взгляд от бумаг. Её взгляд смягчается."

    direkt "У нас в 7 'А' как раз освободилась ставка учителя английского. Тема завтрашнего урока - 'Present Simple'."
    direkt "Можете начать с завтрашнего дня. Зарплата... две тысячи в неделю. Устраивает?"

    show sveta_relieved with dissolve
    sveta "Да! Спасибо большое! Я... я подготовлюсь!"

    scene bg aunt room night with fade
    show sveta_determined at center

    "Весь вечер я сижу над учебниками в тётиной комнате. На столе разложены карточки, тетради, грамматические таблицы."

    sveta "Present Simple... I work, you work, he works..."
    "Перевожу сложные правила на свой язык: 'Как в Доме-2 - они встречаются каждый день, это регулярное действие...'"

    "За окном уже давно ночь, но я продолжает делать пометки."
    sveta "Нужно, чтобы они меня поняли... Чтобы не смеялись..."

    scene black with fade
    "..."

    scene bg classroom with fade
    show sveta_nervous_school at center

    "Сердце выпрыгивает из груди, когда я вхожу в класс. 25 пар глаз смотрят на меня с любопытством и скепсисом."

    play sound "school_bell.mp3"
    
    student1 "О, новая!"
    student2 "Смотрите, какая прикид - прямо как у Пугачёвой в клипе!"
    student3 "Тише, это наша училка по английскому!"
    
    show sveta_uncertain_school with dissolve
    sveta "Здравствуйте... Меня зовут Светлана Сергеевна. Сегодня мы..."
    
    "Голос дрожит. Я замечаю насмешливые взгляды."
    
    show artem_mocking at right with moveinright
    artem "А вы точно учитель? Вы больше на певицу похожи!"
    
    "В классе смех. Ладони становятся влажными."
    
    show sveta_determined_school with dissolve
    sveta "А ты... как тебя зовут?"
    
    artem "Артём."
    
    sveta "Артём, а ты знаешь, как сказать 'насмешник' по-английски?"
    
    "Класс затихает. Артём теряется."
    
    sveta "Mockery. Запомни это слово. И знай - внешность обманчива."
    
    "Я поворачиваюсь к доске, рука всё ещё дрожит, но пишет мелом:"
    
    show text "PRESENT SIMPLE" at truecenter with dissolve
    pause 1.0
    hide text with dissolve

    sveta "Сегодня мы учимся говорить о том, что происходит регулярно. Как мои попытки сделать маникюр, который держится больше двух дней."

    "В классе слышится сдержанный смех. Несколько учеников улыбаются."

    show sveta_teaching with dissolve
    sveta "I teach English every day. You study at school. He plays football after classes..."
    "Объясняю правила, придумывая смешные примеры из жизни. Вижу, как постепенно лица детей становятся заинтересованными."

    "Когда звенит звонок, я не могу поверить - урок пролетел незаметно."

    hide artem_mocking with moveoutright
    show student_shy at right with moveinright
    student "Светлана Сергеевна, а вы завтра придёте?"

    show sveta_smiling with dissolve
    sveta "Конечно. Мы будем учить, как рассказывать о своих увлечениях."

    scene bg school corridor with fade
    show sveta_relieved at center

    "Выхожу в коридор, опираясь о стену. Ноги подкашиваются, но на душе - невероятное облегчение."

    sveta "Получилось... У меня получилось..."
    "В кармане пиджака лежит заработанная тысяча рублей - аванс. До пятницы ещё далеко, но появилась надежда."

    show director_smiling at left with moveinleft
    direkt "Светлана Сергеевна, я заглядывала на ваш урок. Хорошо держитесь. Завтра жду вас в это же время."

    show sveta_proud with dissolve
    sveta "Спасибо... Я обязательно подготовлюсь."

    scene black with fade
    "Впервые за долгое время я чувствую - я не просто 'норильская барби'. Я могу быть кем-то большим."

    call screen room_evening