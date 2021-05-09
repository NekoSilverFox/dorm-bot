# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 12:48
# @Author  : Meng Jianing
# @FileName: questions_answers.py
# @Software: PyCharm
# @Versions: v1.5
# @Github  ：https://github.com/NekoSilverFox
# --------------------------------------------

from enum import Enum, unique


@unique
class Language(Enum):
    RUSSIAN = 0
    ENGLISH = 1
    CHINESE = 2


V_RUSSIAN = Language.RUSSIAN.value
V_ENGLISH = Language.ENGLISH.value
V_CHINESE = Language.CHINESE.value

# ---------------------------------------------
# 有几种语言就有有几个下标，意义对应关系，进制调换顺序
# 对应的翻译：
# index == 0 == Language.RUSSIAN.value
# index == 1 == Language.ENGLISH.value
# index == 2 == Language.CHINESE.value
# ---------------------------------------------

# 按钮中的文本
# Текст в кнопках
WEBSITE = ('Сайт', 'Website', '网站')
VK = ('ВК', 'VK', 'VK')
CLUB = ('Студклуб', 'Student Club', '学生俱乐部')
ONLINE_COURSE = ('Порталы', 'Portals', '教育资源')
NEXT = ('Далее', 'Next', '下一页')
MANAGEMENT_CONTACTS = ('Контакты управления', 'Manager contacts', '联系宿管')
ACCOMMODATION_RULES = ('Правила проживания', 'Accommodation rules', '住宿相关')
COMPLEXES = ('Комплексы', 'Complexes', '宿舍分布')
ADVICE = ('Советы', 'Advice', '建议')
FRONT = ('Назад', 'Back', '返回')
CHANGE_LANGUAGE = ('Сменить язык', 'Change language', '更改语言')
INTERNAL_REGULATIONS = ('Внутренний распорядок', 'Internal regulations', '内部规定')
TO_THE_BEGINING = ('В начало', 'To the begin', '返回主页')
LESNOY_PROSPECT = ('Лесной проспект', 'Lesnoy prospect', '森林大街')
COURAGE_SQUARE = ('Площадь Мужества', 'Courage Square', '勇气广场')
CIVIL_PROSPECT = ('Гражданский проспект', 'Civil Prospect', '公民大街')
SCIENCE_POLYTECH = ('Гостиницу “Наука-Политех”', 'Dorm “Science-Polytech”', '宾馆 “圣理工的科学”')
COMPLEX_FOR_FURTHER_EDUCATION = (
    'Дополнительное обслуживание', 'Additional service', '附加服务')
RELATIONSHIP_WITH = ('Взаимоотношения с...', 'Relationship with...', '联系...')
MOVING_TO_THE_DORM = ('Переезд в общежитие', 'Moving to dorm', '入住建议')
# INTERNAL_REGULATIONS = ('', '', '')
PAYMENT = ('Оплата', 'Pay', '支付')
DORM_SHORT = ('Общ', 'Dorm', '宿舍')
DORM_LONG = ('Общежитие', 'Dormitory', '宿舍')
CHECK_IN_RULES = ('Правила заселения', 'Check-in rules', '入住规则')
ORDER_PASSAGE_PUBLIC = ('Порядок прохода в общ', 'Order of passage to dorm', '进入宿舍的顺序')
RESIDENTS_RIGHTS = ('Права проживающих', 'Residents\' rights', '行为准则')
DUTY_OF_RESIDENTS = ('Проживающие должны', 'Duty of residents', '住宿义务')
DUTY_OF_ADMIN = ('Администрация должна', 'Duty of admin', '宿管责任')  # TODO
BODIES_OF_MANAGEMENT = ('Студсовет', 'Student Union', '学生会')
RESPONSIBILITY_BREAKING_RULES = ('Нарушение правил', 'Break the rules', '违反舍规')
NEIGHBORS = ('Соседями', 'Neighbors', '舍友')
ADMINISTRATION = ('Администрицией', 'Administration', '行政部门')
COCKROACHES = ('Тараканами', 'Cockroaches', '除蟑螂')
WHAT_TO_TAKE_WITH_YOU = ('Что взять с собой', 'What to take with you', '随身带什么')
WHAT_TO_BUY_LOCALLY = ('Что купить на месте', 'What to buy locally', '需要购买的物品')

# 键值对 <--> 问题（小写）和回答
# Пары ключ-значение <--> вопрос (НИЖНИЙ регистр) и ответ
# Attention! Questions should be in all lowercase!
gl_questions_answers = {
    'hello123': 'Hello there',
    'help': 'We also need help qwq',
    'русский': 'Текущим языком является русский',
    'english': 'The current language is English',
    '中文': '已将语言设置为简体中文',

    CLUB[V_RUSSIAN].lower(): 'Студклуб – это место твоего яркого студенчества!\n'
                             'В Студклубе ты найдешь 15 студий и объединений для твоего творческого развития, которые работают совершенно бесплатно! Спектр деятельности Студенческого клуба широк: студенты имеют возможность заниматься актёрским мастерством, музыкой, танцами, цифровым дизайном и участвовать в организации мероприятий. Также в Клубе работает уютная зона PrimeTime, где можно собраться с друзьями за настолками или просто приятно отдохнуть!\n'
                             'Если заинтересовался, то советуем пройти в группу Студклуба во ВКонтакте для большей информации: vk.com/poly_studklub.',
    CLUB[V_ENGLISH].lower(): 'The Student Club is your vibrant place as a student!\n'
                             'At the Student Club you will find 15 studios and associations for your creative development, which are free of charge! The range of activities available in the Student Club is wide: students can take part in acting, music, dance, digital design and events. The Club also has a cosy PrimeTime zone, where you can get together with friends for board games or just have a good time!\n'
                             'If you\'re interested, visit the Studklub group on VKontakte for more information: vk.com/poly_studklub.',
    CLUB[V_CHINESE].lower(): '学生俱乐部是你充满活力的学生生活的地方!\n'
                             '在学生俱乐部，你可以找到15个工作室和协会，用于你的创意发展，这些都是完全免费的 学生俱乐部的活动范围很广：学生可以参加表演、音乐、舞蹈、数字设计和活动组织。俱乐部里还有一个舒适的PrimeTime区，你可以和你的朋友一起玩棋盘游戏，或者只是玩个痛快。\n'
                             '如果你有兴趣，欢迎访问VKontakte中的Studklub群，了解更多信息：vk.com/poly_studklub。',

    ONLINE_COURSE[V_RUSSIAN].lower(): 'Go!',
    ONLINE_COURSE[V_ENGLISH].lower(): 'Go!',
    ONLINE_COURSE[V_CHINESE].lower(): 'Go!',

    # NEXT[V_RUSSIAN].lower(): '&#13;',
    NEXT[V_RUSSIAN].lower(): 'Показываю другие кнопки',
    NEXT[V_ENGLISH].lower(): 'Show other buttons',
    NEXT[V_CHINESE].lower(): '显示其他按钮',

    MANAGEMENT_CONTACTS[V_RUSSIAN].lower(): 'Директор Студгородка – Шнейдер Анатолий Альбертович:\n'
                                            '•	uprstg@spbstu.ru\n'
                                            '•	+7 (812) 290-95-02\n'
                                            '•	пр. Непокорённых, д.8, корп.2, общ. №14б\n\n'
                                            'Городская Служба Заселения Студентов:\n'
                                            '•	+7 (981) 805-32-40',
    MANAGEMENT_CONTACTS[V_ENGLISH].lower(): 'Campus Director – Шнейдер Анатолий Альбертович:\n'
                                            '•	uprstg@spbstu.ru\n'
                                            '•	+7 (812) 290-95-02\n'
                                            '•	пр. Непокорённых, д.8, корп.2, общ. №14б\n\n'
                                            'City Student Accommodation Service:\n'
                                            '•	+7 (981) 805-32-40',
    MANAGEMENT_CONTACTS[V_CHINESE].lower(): '校园主任 – Шнейдер Анатолий Альбертович:\n'
                                            '•	uprstg@spbstu.ru\n'
                                            '•	+7 (812) 290-95-02\n'
                                            '•	пр. Непокорённых, д.8, корп.2, общ. №14б\n\n'
                                            ' 城市学生住宿服务:\n'
                                            '•	+7 (981) 805-32-40',

    ACCOMMODATION_RULES[V_RUSSIAN].lower(): 'Правила проживания',
    ACCOMMODATION_RULES[V_ENGLISH].lower(): 'Accommodation rules',
    ACCOMMODATION_RULES[V_CHINESE].lower(): '住宿相关',

    COMPLEXES[V_RUSSIAN].lower(): 'Комплексы',
    COMPLEXES[V_ENGLISH].lower(): 'Complexes',
    COMPLEXES[V_CHINESE].lower(): '宿舍分布',

    ADVICE[V_RUSSIAN].lower(): 'Советы',
    ADVICE[V_ENGLISH].lower(): 'Advice',
    ADVICE[V_CHINESE].lower(): '建议',

    FRONT[V_RUSSIAN].lower(): 'Показываю другие кнопки',
    FRONT[V_ENGLISH].lower(): 'Show other buttons',
    FRONT[V_CHINESE].lower(): '显示其他按钮',

    CHANGE_LANGUAGE[V_RUSSIAN].lower(): 'Пожалуйста, выберите',
    CHANGE_LANGUAGE[V_ENGLISH].lower(): 'Please select',
    CHANGE_LANGUAGE[V_CHINESE].lower(): '请选择',

    INTERNAL_REGULATIONS[V_RUSSIAN].lower(): 'Внутренний распорядок',
    INTERNAL_REGULATIONS[V_ENGLISH].lower(): 'Internal regulations',
    INTERNAL_REGULATIONS[V_CHINESE].lower(): '内部规定',

    TO_THE_BEGINING[V_RUSSIAN].lower(): 'В начало',
    TO_THE_BEGINING[V_ENGLISH].lower(): 'To the begin',
    TO_THE_BEGINING[V_CHINESE].lower(): '返回主页',

    LESNOY_PROSPECT[V_RUSSIAN].lower(): 'Начальник комплекса - Ядрышников Александр Аркадьевич:\n'
                                        '•	aayadrishnikov@spbstu.ru\n'
                                        '•	Лесной пр., д.67, корп.2, общ.№7',
    LESNOY_PROSPECT[V_ENGLISH].lower(): 'Chief of complex - Ядрышников Александр Аркадьевич:\n'
                                        '•	aayadrishnikov@spbstu.ru\n'
                                        '•	Лесной пр., д.67, корп.2, общ.№7',
    LESNOY_PROSPECT[V_CHINESE].lower(): '复杂事务主管 - Ядрышников Александр Аркадьевич:\n'
                                        '•	aayadrishnikov@spbstu.ru\n'
                                        '•	Лесной пр., д.67, корп.2, общ.№7',

    COURAGE_SQUARE[V_RUSSIAN].lower(): 'Начальник комплекса - Короткова Руфина Рауфовна:\n'
                                       '•	rrkorotkova@spbstu.ru\n'
                                       '•	+7 (812) 290-97-12\n'
                                       '•	пр. Непокорённых, д.8, корп.2, общ. №14б\n',
    COURAGE_SQUARE[V_ENGLISH].lower(): 'Chief of complex - Короткова Руфина Рауфовна:\n'
                                       '•	rrkorotkova@spbstu.ru\n'
                                       '•	+7 (812) 290-97-12\n'
                                       '•	пр. Непокорённых, д.8, корп.2, общ. №14б\n',
    COURAGE_SQUARE[V_CHINESE].lower(): '复杂事务主管 - Короткова Руфина Рауфовна:\n'
                                       '•	rrkorotkova@spbstu.ru\n'
                                       '•	+7 (812) 290-97-12\n'
                                       '•	пр. Непокорённых, д.8, корп.2, общ. №14б\n',

    CIVIL_PROSPECT[V_RUSSIAN].lower(): 'Начальник комплекса - Никулин Алексей Николаевич:\n'
                                       '•	nikulin@spbstu.ru\n'
                                       '•	+7 (812) 322-01-38\n'
                                       '•	Гражданский пр., д.28, кабинет 114\n',
    CIVIL_PROSPECT[V_ENGLISH].lower(): 'Chief of complex - Никулин Алексей Николаевич:\n'
                                       '•	nikulin@spbstu.ru\n'
                                       '•	+7 (812) 322-01-38\n'
                                       '•	Гражданский пр., д.28, кабинет 114\n',
    CIVIL_PROSPECT[V_CHINESE].lower(): '复杂事务主管 - Никулин Алексей Николаевич:\n'
                                       '•	nikulin@spbstu.ru\n'
                                       '•	+7 (812) 322-01-38\n'
                                       '•	Гражданский пр., д.28, кабинет 114\n',

    SCIENCE_POLYTECH[V_RUSSIAN].lower(): 'Дирекция:\n'
                                         '•	+7 (812) 553-00-00\n'
                                         '•	+7 (812) 293-84-55\n'
                                         '•	пр. Энгельса, дом 65, литера А\n\n'
                                         'Заведующая - Муртазина Марина Вячеславовна\n'
                                         'Комплекс дополнительного обслуживания проживающих\n'
                                         'Начальник комплекса - Рублева Юлия Аркадьевна:\n'
                                         '•	rubleva@spbstu.ru\n'
                                         '•	+7 (812) 534-13-68\n'
                                         '•	+7 (812) 606-62-38\n'
                                         '•	Гражданский пр., д. 28, кабинет 104\n\n'
                                         'Старший администратор комплекса - Белаш Лилия Анатольевна:\n'
                                         '•	hotel@spbstu.ru\n'
                                         '•	+7 (812) 534-13-68\n'
                                         '•	пр. Гражданский, д. 28\n\n'
                                         'Телефоны для бронирования номеров в вечернее время и выходные дни:\n'
                                         '•	+7 (812) 321-61-00 (Гражданский пр., д.28)\n'
                                         '•	+7 (812) 295-36-37 (Лесной пр., д.65/1 и д.67/2)\n\n'
                                         'Номера повышенной комфортности в общежитиях:\n'
                                         '•	№1 телефон дежурной: +7 (812) 295-36-37\n'
                                         '•	№7 телефон дежурной: +7 (921) 561-13-29\n'
                                         '•	№8 телефон дежурной: +7 (812) 297-43-50\n'
                                         '•	№15 телефон дежурной: +7 (812) 321-61-00\n',
    SCIENCE_POLYTECH[V_ENGLISH].lower(): 'Directorate:\n'
                                         '•	+7 (812) 553-00-00\n'
                                         '•	+7 (812) 293-84-55\n'
                                         '•	пр. Энгельса, дом 65, литера А\n\n'
                                         'Head - Murtazina Marina Vyacheslavovna\n'
                                         'Complex of additional services for residents\n'
                                         'Chief of complex - Рублева Юлия Аркадьевна:\n'
                                         '•	rubleva@spbstu.ru\n'
                                         '•	+7 (812) 534-13-68\n'
                                         '•	+7 (812) 606-62-38\n'
                                         '•	Гражданский пр., д. 28, кабинет 104\n\n'
                                         'Senior Complex Administrator - Белаш Лилия Анатольевна:\n'
                                         '•	hotel@spbstu.ru\n'
                                         '•	+7 (812) 534-13-68\n'
                                         '•	пр. Гражданский, д. 28\n\n'
                                         'Evening and weekend room reservations phone numbers:\n'
                                         '•	+7 (812) 321-61-00 (Гражданский пр., д.28)\n'
                                         '•	+7 (812) 295-36-37 (Лесной пр., д.65/1 и д.67/2)\n\n'
                                         'Superior rooms in dormitories:\n'
                                         '•	№1 emergency phone: +7 (812) 295-36-37\n'
                                         '•	№7 emergency phone: +7 (921) 561-13-29\n'
                                         '•	№8 emergency phone: +7 (812) 297-43-50\n'
                                         '•	№15 emergency phone: +7 (812) 321-61-00\n',
    SCIENCE_POLYTECH[V_CHINESE].lower(): '管理局:\n'
                                         '•	+7 (812) 553-00-00\n'
                                         '•	+7 (812) 293-84-55\n'
                                         '•	пр. Энгельса, дом 65, литера А\n\n'
                                         '经理 - Муртазина Марина Вячеславовна\n'
                                         '额外的居民服务配套\n'
                                         '复杂事务主任 - Рублева Юлия Аркадьевна:\n'
                                         '•	rubleva@spbstu.ru\n'
                                         '•	+7 (812) 534-13-68\n'
                                         '•	+7 (812) 606-62-38\n'
                                         '•	Гражданский пр., д. 28, кабинет 104\n\n'
                                         '综合楼高级管理员 - Белаш Лилия Анатольевна:\n'
                                         '•	hotel@spbstu.ru\n'
                                         '•	+7 (812) 534-13-68\n'
                                         '•	пр. Гражданский, д. 28\n\n'
                                         '晚上和周末的房间预订电话:\n'
                                         '•	+7 (812) 321-61-00 (Гражданский пр., д.28)\n'
                                         '•	+7 (812) 295-36-37 (Лесной пр., д.65/1 и д.67/2)\n\n'
                                         '宿舍的高级客房:\n'
                                         '•	№1 紧急电话: +7 (812) 295-36-37\n'
                                         '•	№7 紧急电话: +7 (921) 561-13-29\n'
                                         '•	№8 紧急电话: +7 (812) 297-43-50\n'
                                         '•	№15 紧急电话: +7 (812) 321-61-00\n',

    COMPLEX_FOR_FURTHER_EDUCATION[V_RUSSIAN].lower(): 'Начальник комплекса - Рублева Юлия Аркадьевна:\n'
                                                      '•	rubleva@spbstu.ru\n'
                                                      '•	+7 (812) 534-13-68\n'
                                                      '•	+7 (812) 606-62-38\n'
                                                      '•	Гражданский пр., д. 28, кабинет 104\n'
                                                      'Старший администратор комплекса - Белаш Лилия Анатольевна:\n'
                                                      '•	hotel@spbstu.ru\n'
                                                      '•	+7 (812) 534-13-68\n'
                                                      '•	пр. Гражданский, д. 28\n'
                                                      'Телефоны для бронирования номеров в вечернее время и выходные дни:\n'
                                                      '•	+7 (812) 321-61-00 (Гражданский пр., д.28)\n'
                                                      '•	+7 (812) 295-36-37 (Лесной пр., д.65/1 и д.67/2)\n'
                                                      'Номера повышенной комфортности в общежитиях:\n'
                                                      '•	№1 телефон дежурной: +7 (812) 295-36-37\n'
                                                      '•	№7 телефон дежурной: +7 (921) 561-13-29\n'
                                                      '•	№8 телефон дежурной: +7 (812) 297-43-50\n'
                                                      '•	№15 телефон дежурной: +7 (812) 321-61-00\n',
    COMPLEX_FOR_FURTHER_EDUCATION[V_ENGLISH].lower(): 'The head of the complex - Рублева Юлия Аркадьевна:\n'
                                                      '•	rubleva@spbstu.ru\n'
                                                      '•	+7 (812) 534-13-68\n'
                                                      '•	+7 (812) 606-62-38\n'
                                                      '•	Гражданский пр., д. 28, кабинет 104\n'
                                                      'Senior administrator of the complex - Белаш Лилия Анатольевна:\n'
                                                      '•	hotel@spbstu.ru\n'
                                                      '•	+7 (812) 534-13-68\n'
                                                      '•	пр. Гражданский, д. 28\n'
                                                      'Evening and weekend room reservation phones:\n'
                                                      '•	+7 (812) 321-61-00 (Гражданский пр., д.28)\n'
                                                      '•	+7 (812) 295-36-37 (Лесной пр., д.65/1 и д.67/2)\n'
                                                      'Superior rooms in the dormitories:\n'
                                                      '•	№1  phone on duty: +7 (812) 295-36-37\n'
                                                      '•	№7  phone on duty: +7 (921) 561-13-29\n'
                                                      '•	№8  phone on duty: +7 (812) 297-43-50\n'
                                                      '•	№15 phone on duty: +7 (812) 321-61-00\n',
    COMPLEX_FOR_FURTHER_EDUCATION[V_CHINESE].lower(): '总负责人 - Рублева Юлия Аркадьевна:\n'
                                                      '•	rubleva@spbstu.ru\n'
                                                      '•	+7 (812) 534-13-68\n'
                                                      '•	+7 (812) 606-62-38\n'
                                                      '•	Гражданский пр., д. 28, кабинет 104\n'
                                                      '高级管理员 - Белаш Лилия Анатольевна:\n'
                                                      '•	hotel@spbstu.ru\n'
                                                      '•	+7 (812) 534-13-68\n'
                                                      '•	пр. Гражданский, д. 28\n'
                                                      '晚间和周末房间预订电话:\n'
                                                      '•	+7 (812) 321-61-00 (Гражданский пр., д.28)\n'
                                                      '•	+7 (812) 295-36-37 (Лесной пр., д.65/1 и д.67/2)\n'
                                                      '旅舍的高级房间:\n'
                                                      '•	№1 值班电话: +7 (812) 295-36-37\n'
                                                      '•	№7 值班电话: +7 (921) 561-13-29\n'
                                                      '•	№8 值班电话: +7 (812) 297-43-50\n'
                                                      '•	№15 值班电话: +7 (812) 321-61-00\n',

    RELATIONSHIP_WITH[V_RUSSIAN].lower(): 'Взаимоотношения с...',
    RELATIONSHIP_WITH[V_ENGLISH].lower(): 'Relationship with...',
    RELATIONSHIP_WITH[V_CHINESE].lower(): '联系...',

    # MOVING_TO_THE_DORM[V_RUSSIAN].lower(): 'Переезд в общежитие',
    # MOVING_TO_THE_DORM[V_ENGLISH].lower(): 'Moving to dorm',
    # MOVING_TO_THE_DORM[V_CHINESE].lower(): '入住建议',

    MOVING_TO_THE_DORM[
        V_RUSSIAN].lower(): 'В общежитии понадобится большое количество вещей, можем вам посоветовать, что будет нужно 100%.\n\n'
                            'Вещи для обустройства комнаты: шторы, прикроватный коврик, тёплый плед, тряпку для протирки пыли.\n\n'
                            'Одежда: столько, сколько нужно на месяц, в общежитие есть прачечная, несколько вешалок, одежда для занятий физкультурой. Из верхней одежды возьмите осенние вещи, зимние в первое время берите. Их можно будет привести или переслать позже, если вдруг наступит плохая погода, в Санкт-Петербурге не очень холодные зимы (по сравнению с Сибирью).\n\n'
                            'Обувь: желательно взять по две пары “летней” и межсезонной обуви, не забудьте взять сушилку для обуви. Зимнюю обувь также можно прислать позже. Потребуются кроссовки для занятий физкультурой. Также необходимы тапочки/шлепки для общаги и резиновые шлепки для похода в душ.\n\n'
                            'Гигиенические и косметические средства: шампунь, гель для тела, мочалка (если нужна), мыло, порошок/гель для стирки (машинки в прачечной нужно засыпать своим средством), зубная щётка, зубная паста, туалетная бумага, косметические средства, ножницы для ногтей, полотенца.\n\n'
                            'Аптечка: средство от боли, средства для решения проблем с животом, бинт, пластырь бактерицидный, мазь антисептическая, лекарства, которые тебе нужны, спрей от насморка, противопростудные и жаропонижающие препараты.\n\n'
                            'Продукты: немного чая или кофе, немного сахара, готовая еда (котлеты, овощи и т.п.) которой хватит на 2 раза покушать (один раз перекусить пока будешь заселяться и один раз на ужин).\n\n'
                            'Электронные приборы: ноутбук (ты будешь его носить на учебу и для того чтобы ноутбук дольше служил, заведи для него сумку), удлинители (розетки могут находиться на расстоянии от стола/кровати, либо их просто будет не хватать), точка доступа в интернет (при заселении нужно будет подписать договор с интернет компанией для подключения интернета, но модем покупать самим).\n\n'
                            'Документы для заселения в общежитие: паспорт, парочку фотографий 3*4, результаты флюорографии, сведения о медицинских прививках.\n\n'
                            'Кухонные принадлежности: кастрюля, сковорода (не покупайте новые, старые помогут вам потренироваться в начале), глубокая и обычная тарелка, вилки, ложки, нож, черпак, средства для мытья и чистки посуды, спички или зажигалка.\n\n'
                            'Бытовая техника: электрический чайник, микроволновая печь, холодильник, мультиварка (все это лучше купить на месте, также это можно купить у выезжающих студентов, что будет выгоднее).\n',
    MOVING_TO_THE_DORM[
        V_ENGLISH].lower(): 'In the dormitory will need a lot of things, we can advise you what you will need 100%.\n\n'
                            'Things to furnish your room: curtains, a bedside rug, a warm plaid, a rag to wipe off dust.\n\n'
                            'Clothes: as much as you need for a month, the dormitory has a laundry room, some hangers, clothes for physical training. From outer clothing take autumn clothes, take winter clothes at first. They can be brought or sent later if suddenly bad weather comes, in St. Petersburg winters are not very cold (compared with Siberia).\n\n'
                            'Footwear: it is advisable to take two pairs of "summer" and interseasonal shoes each, and don\'t forget to take a shoe dryer. Winter shoes can also be sent later. Sneakers will be needed for physical education classes. Dorm slippers/slippers and rubber slippers for showering are also needed.\n\n'
                            'Hygiene and beauty supplies: shampoo, body gel, washcloth (if needed), soap, laundry detergent/gel (the machines in the laundry room need to be filled with their own detergent), toothbrush, toothpaste, toilet paper, beauty products, nail clippers, towels.\n\n'
                            'First aid kit: pain reliever, remedies for stomach problems, bandages, bactericidal bandage, antiseptic ointment, medications you need, runny nose spray, cold and fever medications.\n\n'
                            'Food: some tea or coffee, some sugar, ready-made food (cutlets, vegetables, etc.) which is enough for two meals (one snack while you\'re checking in and one for dinner).\n\n'
                            'Electronic devices: laptop (you\'ll be carrying him to school and in order to laptop longer serve, have a bag for him), extension cords (outlets may be at a distance from the desk / bed, or they just won\'t be enough), the point of Internet access (at check in will need to sign a contract with an Internet company to connect the Internet, but the modem buy it yourself).\n\n'
                            'Documents for moving into the dormitory: passport, a couple of photos 3*4, the results of fluorography, information about medical vaccinations.\n\n'
                            'Kitchen utensils: saucepan, frying pan (don\'t buy new ones, the old ones will help you practice in the beginning), deep and plain plates, forks, spoons, knife, scoop, dishwashing and cleaning supplies, matches or a lighter.\n\n'
                            'Home appliances: electric kettle, microwave oven, refrigerator, multicooker (all these things are better to buy on the spot, you can also buy them from visiting students, which will be more profitable).\n',
    MOVING_TO_THE_DORM[V_CHINESE].lower(): '宿舍需要很多东西，我们可以向你建议100%需要的东西\n\n'
                                           '装饰房间的东西：窗帘、床头地毯、温暖的格子布、擦拭灰尘的抹布。\n\n'
                                           '衣服：一个月需要多少就有多少，宿舍有一个洗衣房，有几个衣架，体育课用的衣服。从外衣中取出秋天的衣服，冬天的一开始就取出。如果坏天气突然来临，他们可以稍后带来或发送，在圣彼得堡的冬天不是很冷（与西伯利亚相比）。\n\n'
                                           '鞋类：最好带两双 "夏季 "和跨季的鞋子，别忘了带一个烘鞋器。冬鞋也可以稍后发送。需要穿上体育课的运动鞋。还需要有宿舍拖鞋/拖鞋和洗澡用的橡胶拖鞋。\n\n'
                                           '卫生和美容用品：洗发水、沐浴露、毛巾（如果需要的话）、肥皂、洗衣粉/凝胶（洗衣房的机器需要自己装洗涤剂）、牙刷、牙膏、卫生纸、化妆品、指甲刀、毛巾。\n\n'
                                           '急救箱：止痛药、治疗胃病的药、绷带、杀菌绷带、消毒药膏、你需要的药品、喷鼻剂、感冒和发烧药。\n\n'
                                           '食物：一些茶或咖啡，一些糖，现成的饭菜（肉丸子、蔬菜等），足够两顿饭吃的（一份是入住前的点心，一份是晚餐）。\n\n'
                                           '电子设备：笔记本电脑（你要带着他去学校，为了让笔记本电脑更长时间的服务，要给他准备一个包），延长线（插座可能离书桌或床有一定的距离，否则就是不够用），互联网接入点（在入住时需要和互联网公司签订合同，连接互联网，但路由器要自己买）。\n\n'
                                           '入住宿舍的文件：护照、几张3*4的照片、透视检查结果、医疗疫苗接种信息。\n\n'
                                           '厨房用具：汤锅、煎锅（不要买新的，旧的可以在开始时帮助你练习）、深色和普通的盘子、叉子、勺子、刀、勺子、洗涤和清洁用具、火柴或打火机\n\n'
                                           '家用电器：电热水壶、微波炉、冰箱、多用电饭煲（这些东西最好是当场购买，也可以向离校的学生购买，这样会省一笔）\n',

    PAYMENT[
        V_RUSSIAN].lower(): 'Когда происходит поселение в общежитие, ты подписываешь договор о найме жилья, за которое необходимо платить около 1000 рублей в месяц. Цена зависит от количества человек в комнате, за «уплотнение» чуть меньше.\n'
                            'Цена за общежитие в зимний и летний период немного отличается. Актуальную стоимость ты можешь узнать на информационном стенде в общежитии.\n'
                            'Оплату можно производить по реквизитам в банках города (Сбербанк, СПБ) или на pay.spbstu.ru. После оплаты по реквизитам нужно также показать квитанцию об оплате администрации общежития. Возможна оплата на несколько месяцев вперед.\n'
                            'За долг более 3000 рублей администрация студгородка может вызвать к себе, в случае повторных нарушений возможен выговор.',
    PAYMENT[
        V_ENGLISH].lower(): 'When you move into a dormitory, you sign a tenancy agreement for which you have to pay about 1,000 roubles a month. The price depends on the number of people in the room; for \'compacting\' it is slightly less.\n'
                            'The price of a hostel is slightly different during the winter and summer. You can get the current price from the information board in the dormitory.\n'
                            'You can pay at any bank in the city (Sberbank, St. Petersburg) or pay.spbstu.ru. After the payment has been made, you will have to show the administration of the hostel the receipt of payment. It is possible to pay for several months in advance.\n'
                            'If you owe more than 3,000 roubles, the administration of the campus may summon you to their office and you may be reprimanded in case of repeated violations.',
    PAYMENT[V_CHINESE].lower(): '当你搬进宿舍时，你会签署一份租赁协议，为此你必须每月支付约1000卢布。价格取决于房间里的人数，对于 "压缩 "来说要少一点。\n'
                                '旅舍的价格在冬季和夏季略有不同。目前的费用可以在宿舍的信息板上找到。\n'
                                '可以在城市的银行（Sberbank, SPB）或pay.spbstu.ru上根据要求进行支付。还需要向宿舍管理部门出示付款收据。可以提前支付几个月的费用。\n'
                                '对于超过3000卢布的债务，校园管理部门可以向自己叫板，如果屡次违规，就有可能被训斥。',

    DORM_SHORT[V_RUSSIAN].lower() + ' №1': 'Дирекция:\n'
                                           '•	dorm1@spbstu.ru\n'
                                           '•	+7 (812) 775 05 30 #1444\n'
                                           '•	+7 (812) 775 05 30 #1445\n'
                                           '•	Лесной пр., д. 65, корп.1\n'
                                           'Группа во ВКонтакте – vk.com/spbstu_1\n'
                                           'Заведующий общежитием – Шевченко Ольга Николаевна',
    DORM_SHORT[V_RUSSIAN].lower() + ' №3': 'Дирекция:\n'
                                           '•	dorm3@spbstu.ru\n'
                                           '•	+7 (812) 775 05 30 #1448\n'
                                           '•	Лесной пр., д. 65, корп. 3\n'
                                           'Группа во ВКонтакте – vk.com/spbstu_3\n'
                                           'Заведующий общежитием – Киреева Наталья Викторовна',
    DORM_SHORT[V_RUSSIAN].lower() + ' №4': 'Дирекция:\n'
                                           '•	dorm4@spbstu.ru\n'
                                           '•	+7 (812) 775 05 30 #1451\n'
                                           '•	ул. Парголовская, д.11, корп.1\n'
                                           'Группа во ВКонтакте – vk.com/spbstu_4\n'
                                           'Заведующий общежитием – Мартынова Лариса Яковлевна',
    DORM_SHORT[V_RUSSIAN].lower() + ' №4а': 'Дирекция:\n'
                                            '•	dorm4a@spbstu.ru\n'
                                            '•	+7 (812) 775 05 30 #1453\n'
                                            '•	ул. Парголовская, д.11, корп.1\n'
                                            'Группа во ВКонтакте – vk.com/spbstu_4aa\n'
                                            'Заведующий общежитием – Гулева Ирианда Анатольевна\n',
    DORM_SHORT[V_RUSSIAN].lower() + ' №5': 'Дирекция:\n'
                                           '•	dorm5@spbstu.ru\n'
                                           '•	+7 (812) 295-47-25\n'
                                           '•	ул. Парголовская, д.11, корп.2\n'
                                           'Группы во ВКонтакте – vk.com/spbstu_5a | vk.com/spbstu_5b\n'
                                           'Заведующий общежитием – Мартьянова Милена Леонидовна\n',
    DORM_SHORT[V_RUSSIAN].lower() + ' №6': 'Дирекция:\n'
                                           '•	dorm6m@spbstu.ru\n'
                                           '•	+7 (812) 295-27-50\n'
                                           '•	ул. Харченко, д. 16\n'
                                           'Группа во ВКонтакте – vk.com/spbstu_6\n'
                                           'Заведующий общежитием – Егорова Ольга Адамовна\n',
    DORM_SHORT[V_RUSSIAN].lower() + ' №7': 'Дирекция:\n'
                                           '•	dorm7@spbstu.ru\n'
                                           '•	+7 (812) 775-05-30 #1442\n'
                                           '•	+7 (812) 775-05-30 #1443\n'
                                           '•	Лесной пр., д.67, корп.2\n'
                                           'Заведующий общежитием – Кривошея Гульнара Куртвелиевна\n',
    DORM_SHORT[V_RUSSIAN].lower() + ' №8': 'Дирекция:\n'
                                           '•	dorm8@spbstu.ru\n'
                                           '•	+7 (812) 297-43-50\n'
                                           '•	ул. Хлопина, д.9, корп.2\n'
                                           'Группа во ВКонтакте – vk.com/spbstu_8\n'
                                           'Заведующий общежитием – Бернанс Ольга Ивановна\n',
    DORM_SHORT[V_RUSSIAN].lower() + ' №10': 'Дирекция:\n'
                                            '•	dorm10@spbstu.ru\n'
                                            '•	+7 (812) 297-16-78\n'
                                            '•	пр. Непокоренных, д. 6, корп.2\n'
                                            'Группа во ВКонтакте – vk.com/spbstu_10\n'
                                            'Заведующий общежитием – Текучева Елена Ивановна\n',
    DORM_SHORT[V_RUSSIAN].lower() + ' №11': 'Дирекция:\n'
                                            '•	dorm11@spbstu.ru\n'
                                            '•	+7 (812) 295-00-28\n'
                                            '•	ул. Кантемировская, д. 24\n'
                                            'Группа во ВКонтакте – vk.com/spbstu_11\n'
                                            'Заведующий общежитием – Медведева Людмила Алексеевна\n',
    DORM_SHORT[V_RUSSIAN].lower() + ' №12': 'Дирекция:\n'
                                            '•	dorm12@spbstu.ru\n'
                                            '•	+7 (812) 534-47-86\n'
                                            '•	ул. Хлопина, д. 13, корп. 1\n'
                                            'Группа во ВКонтакте – vk.com/spbstu_12\n'
                                            'Заведующий общежитием – Пескова Ирина Викторовна\n',
    DORM_SHORT[V_RUSSIAN].lower() + ' №14а': 'Дирекция:\n'
                                             '•	dorm14a@spbstu.ru\n'
                                             '•	+7 (812) 596-26-67\n'
                                             '•	пр. Непокоренных, д. 8, корп.2\n'
                                             'Группа во ВКонтакте – vk.com/spbstu__14a\n'
                                             'Заведующий общежитием – Константинова Лариса Юрьевна\n',
    DORM_SHORT[V_RUSSIAN].lower() + ' №14б': 'Дирекция:\n'
                                             '•	dorm14b@spbstu.ru\n'
                                             '•	+7 (812) 596-29-32\n'
                                             '•	пр. Непокоренных, д. 8, корп.2\n'
                                             'Группа во ВКонтакте – vk.com/spbstu_14b\n'
                                             'Заведующий общежитием – Воронцова Ирина Петровна\n',
    DORM_SHORT[V_RUSSIAN].lower() + ' №14ц': 'Дирекция:\n'
                                             '•	dorm14c@spbstu.ru\n'
                                             '•	+7 (812) 534-48-93\n'
                                             '•	пр. Непокоренных, д. 8, корп.2\n'
                                             'Группа во ВКонтакте – vk.com/spbstu_14c\n'
                                             'Заведующий общежитием – Солнцева Ирина Викторовна\n',
    DORM_SHORT[V_RUSSIAN].lower() + ' №17': 'Дирекция:\n'
                                            '•	dorm17@spbstu.ru\n'
                                            '•	+7 (812) 555-23-32\n'
                                            '•	ул. Вавиловых, д.10, корп. 2\n'
                                            'Группа во ВКонтакте – vk.com/spbstu_17\n'
                                            'Заведующий общежитием – Назаревская Марина Викторовна\n',
    DORM_SHORT[V_RUSSIAN].lower() + ' №18': 'Дирекция:\n'
                                            '•	dorm18@spbstu.ru\n'
                                            '•	+7 (812) 555-76-97\n'
                                            '•	ул. Вавиловых, д.10, корп. 3\n'
                                            'Группа во ВКонтакте – vk.com/spbstu_18\n'
                                            'Заведующий общежитием – Емельнова Юлия Геннадьевна\n',

    DORM_SHORT[V_ENGLISH].lower() + ' №1': 'Directorate:\n'
                                           '•	dorm1@spbstu.ru\n'
                                           '•	+7 (812) 775 05 30 #1444\n'
                                           '•	+7 (812) 775 05 30 #1445\n'
                                           '•	Лесной пр., д. 65, корп.1\n'
                                           'Group on VKontakte – vk.com/spbstu_1\n'
                                           'Head of the hostel – Шевченко Ольга Николаевна',
    DORM_SHORT[V_ENGLISH].lower() + ' №3': 'Directorate:\n'
                                           '•	dorm3@spbstu.ru\n'
                                           '•	+7 (812) 775 05 30 #1448\n'
                                           '•	Лесной пр., д. 65, корп. 3\n'
                                           'Group on VKontakte – vk.com/spbstu_3\n'
                                           'Head of the hostel – Киреева Наталья Викторовна',
    DORM_SHORT[V_ENGLISH].lower() + ' №4': 'Directorate:\n'
                                           '•	dorm4@spbstu.ru\n'
                                           '•	+7 (812) 775 05 30 #1451\n'
                                           '•	ул. Парголовская, д.11, корп.1\n'
                                           'Group on VKontakte – vk.com/spbstu_4\n'
                                           'Head of the hostel – Мартынова Лариса Яковлевна',
    DORM_SHORT[V_ENGLISH].lower() + ' №4а': 'Directorate:\n'
                                            '•	dorm4a@spbstu.ru\n'
                                            '•	+7 (812) 775 05 30 #1453\n'
                                            '•	ул. Парголовская, д.11, корп.1\n'
                                            'Group on VKontakte – vk.com/spbstu_4aa\n'
                                            'Head of the hostel – Гst.ва Ирианда Анатольевна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №5': 'Directorate:\n'
                                           '•	dorm5@spbstu.ru\n'
                                           '•	+7 (812) 295-47-25\n'
                                           '•	ул. Парголовская, д.11, корп.2\n'
                                           'Group on VKontakte – vk.com/spbstu_5a | vk.com/spbstu_5b\n'
                                           'Head of the hostel – Мартьянова Милена Леонидовна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №6': 'Directorate:\n'
                                           '•	dorm6m@spbstu.ru\n'
                                           '•	+7 (812) 295-27-50\n'
                                           '•	ул. Харченко, д. 16\n'
                                           'Group on VKontakte – vk.com/spbstu_6\n'
                                           'Head of the hostel – Егорова Ольга Адамовна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №7': 'Directorate:\n'
                                           '•	dorm7@spbstu.ru\n'
                                           '•	+7 (812) 775-05-30 #1442\n'
                                           '•	+7 (812) 775-05-30 #1443\n'
                                           '•	Лесной пр., д.67, корп.2\n'
                                           'Head of the hostel – Кривошея Гst.нара Куртвелиевна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №8': 'Directorate:\n'
                                           '•	dorm8@spbstu.ru\n'
                                           '•	+7 (812) 297-43-50\n'
                                           '•	ул. Хлопина, д.9, корп.2\n'
                                           'Group on VKontakte – vk.com/spbstu_8\n'
                                           'Head of the hostel – Бернанс Ольга Ивановна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №10': 'Directorate:\n'
                                            '•	dorm10@spbstu.ru\n'
                                            '•	+7 (812) 297-16-78\n'
                                            '•	пр. Непокоренных, д. 6, корп.2\n'
                                            'Group on VKontakte – vk.com/spbstu_10\n'
                                            'Head of the hostel – Текучева Елена Ивановна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №11': 'Directorate:\n'
                                            '•	dorm11@spbstu.ru\n'
                                            '•	+7 (812) 295-00-28\n'
                                            '•	ул. Кантемировская, д. 24\n'
                                            'Group on VKontakte – vk.com/spbstu_11\n'
                                            'Head of the hostel – Медведева Людмила Алексеевна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №12': 'Directorate:\n'
                                            '•	dorm12@spbstu.ru\n'
                                            '•	+7 (812) 534-47-86\n'
                                            '•	ул. Хлопина, д. 13, корп. 1\n'
                                            'Group on VKontakte – vk.com/spbstu_12\n'
                                            'Head of the hostel – Пескова Ирина Викторовна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №14а': 'Directorate:\n'
                                             '•	dorm14a@spbstu.ru\n'
                                             '•	+7 (812) 596-26-67\n'
                                             '•	пр. Непокоренных, д. 8, корп.2\n'
                                             'Group on VKontakte – vk.com/spbstu__14a\n'
                                             'Head of the hostel – Константинова Лариса Юрьевна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №14б': 'Directorate:\n'
                                             '•	dorm14b@spbstu.ru\n'
                                             '•	+7 (812) 596-29-32\n'
                                             '•	пр. Непокоренных, д. 8, корп.2\n'
                                             'Group on VKontakte – vk.com/spbstu_14b\n'
                                             'Head of the hostel – Воронцова Ирина Петровна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №14ц': 'Directorate:\n'
                                             '•	dorm14c@spbstu.ru\n'
                                             '•	+7 (812) 534-48-93\n'
                                             '•	пр. Непокоренных, д. 8, корп.2\n'
                                             'Group on VKontakte – vk.com/spbstu_14c\n'
                                             'Head of the hostel – Солнцева Ирина Викторовна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №17': 'Directorate:\n'
                                            '•	dorm17@spbstu.ru\n'
                                            '•	+7 (812) 555-23-32\n'
                                            '•	ул. Вавиловых, д.10, корп. 2\n'
                                            'Group on VKontakte – vk.com/spbstu_17\n'
                                            'Head of the hostel – Назаревская Марина Викторовна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №18': 'Directorate:\n'
                                            '•	dorm18@spbstu.ru\n'
                                            '•	+7 (812) 555-76-97\n'
                                            '•	ул. Вавиловых, д.10, корп. 3\n'
                                            'Group on VKontakte – vk.com/spbstu_18\n'
                                            'Head of the hostel – Емельнова Юлия Геннадьевна\n',

    DORM_SHORT[V_CHINESE].lower() + ' №1': '管理局:\n'
                                           '•	dorm1@spbstu.ru\n'
                                           '•	+7 (812) 775 05 30 #1444\n'
                                           '•	+7 (812) 775 05 30 #1445\n'
                                           '•	Лесной пр., д. 65, корп.1\n'
                                           'VK群 – vk.com/spbstu_1\n'
                                           '宿舍负责人 – Шевченко Ольга Николаевна',
    DORM_SHORT[V_CHINESE].lower() + ' №3': '管理局:\n'
                                           '•	dorm3@spbstu.ru\n'
                                           '•	+7 (812) 775 05 30 #1448\n'
                                           '•	Лесной пр., д. 65, корп. 3\n'
                                           'VK群 – vk.com/spbstu_3\n'
                                           '宿舍负责人 – Киреева Наталья Викторовна',
    DORM_SHORT[V_CHINESE].lower() + ' №4': '管理局:\n'
                                           '•	dorm4@spbstu.ru\n'
                                           '•	+7 (812) 775 05 30 #1451\n'
                                           '•	ул. Парголовская, д.11, корп.1\n'
                                           'VK群 – vk.com/spbstu_4\n'
                                           '宿舍负责人 – Мартынова Лариса Яковлевна',
    DORM_SHORT[V_CHINESE].lower() + ' №4а': '管理局:\n'
                                            '•	dorm4a@spbstu.ru\n'
                                            '•	+7 (812) 775 05 30 #1453\n'
                                            '•	ул. Парголовская, д.11, корп.1\n'
                                            'VK群 – vk.com/spbstu_4aa\n'
                                            '宿舍负责人 – Гулева Ирианда Анатольевна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №5': '管理局:\n'
                                           '•	dorm5@spbstu.ru\n'
                                           '•	+7 (812) 295-47-25\n'
                                           '•	ул. Парголовская, д.11, корп.2\n'
                                           'VK群 – vk.com/spbstu_5a | vk.com/spbstu_5b\n'
                                           '宿舍负责人 – Мартьянова Милена Леонидовна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №6': '管理局:\n'
                                           '•	dorm6m@spbstu.ru\n'
                                           '•	+7 (812) 295-27-50\n'
                                           '•	ул. Харченко, д. 16\n'
                                           'VK群 – vk.com/spbstu_6\n'
                                           '宿舍负责人 – Егорова Ольга Адамовна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №7': '管理局:\n'
                                           '•	dorm7@spbstu.ru\n'
                                           '•	+7 (812) 775-05-30 #1442\n'
                                           '•	+7 (812) 775-05-30 #1443\n'
                                           '•	Лесной пр., д.67, корп.2\n'
                                           '宿舍负责人 – Кривошея Гульнара Куртвелиевна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №8': '管理局:\n'
                                           '•	dorm8@spbstu.ru\n'
                                           '•	+7 (812) 297-43-50\n'
                                           '•	ул. Хлопина, д.9, корп.2\n'
                                           'VK群 – vk.com/spbstu_8\n'
                                           '宿舍负责人 – Бернанс Ольга Ивановна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №10': '管理局:\n'
                                            '•	dorm10@spbstu.ru\n'
                                            '•	+7 (812) 297-16-78\n'
                                            '•	пр. Непокоренных, д. 6, корп.2\n'
                                            'VK群 – vk.com/spbstu_10\n'
                                            '宿舍负责人 – Текучева Елена Ивановна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №11': '管理局:\n'
                                            '•	dorm11@spbstu.ru\n'
                                            '•	+7 (812) 295-00-28\n'
                                            '•	ул. Кантемировская, д. 24\n'
                                            'VK群 – vk.com/spbstu_11\n'
                                            '宿舍负责人 – Медведева Людмила Алексеевна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №12': '管理局:\n'
                                            '•	dorm12@spbstu.ru\n'
                                            '•	+7 (812) 534-47-86\n'
                                            '•	ул. Хлопина, д. 13, корп. 1\n'
                                            'VK群 – vk.com/spbstu_12\n'
                                            '宿舍负责人 – Пескова Ирина Викторовна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №14а': '管理局:\n'
                                             '•	dorm14a@spbstu.ru\n'
                                             '•	+7 (812) 596-26-67\n'
                                             '•	пр. Непокоренных, д. 8, корп.2\n'
                                             'VK群 – vk.com/spbstu__14a\n'
                                             '宿舍负责人 – Константинова Лариса Юрьевна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №14б': '管理局:\n'
                                             '•	dorm14b@spbstu.ru\n'
                                             '•	+7 (812) 596-29-32\n'
                                             '•	пр. Непокоренных, д. 8, корп.2\n'
                                             'VK群 – vk.com/spbstu_14b\n'
                                             '宿舍负责人 – Воронцова Ирина Петровна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №14ц': '管理局:\n'
                                             '•	dorm14c@spbstu.ru\n'
                                             '•	+7 (812) 534-48-93\n'
                                             '•	пр. Непокоренных, д. 8, корп.2\n'
                                             'VK群 – vk.com/spbstu_14c\n'
                                             '宿舍负责人 – Солнцева Ирина Викторовна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №17': '管理局:\n'
                                            '•	dorm17@spbstu.ru\n'
                                            '•	+7 (812) 555-23-32\n'
                                            '•	ул. Вавиловых, д.10, корп. 2\n'
                                            'VK群 – vk.com/spbstu_17\n'
                                            '宿舍负责人 – Назаревская Марина Викторовна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №18': '管理局:\n'
                                            '•	dorm18@spbstu.ru\n'
                                            '•	+7 (812) 555-76-97\n'
                                            '•	ул. Вавиловых, д.10, корп. 3\n'
                                            'VK群 – vk.com/spbstu_18\n'
                                            '宿舍负责人 – Емельнова Юлия Геннадьевна\n',

    DORM_LONG[V_RUSSIAN].lower() + ' №13': 'Дирекция:\n'
                                           '•	dorm13@spbstu.ru\n'
                                           '•	+7 (812) 534-46-65\n'
                                           '•	пр. Гражданский, д. 30\n'
                                           'Группа во ВКонтакте – vk.com/spbstu_13\n'
                                           'Заведующий общежитием – Кургут Наталья Юрьевна\n',
    DORM_LONG[V_RUSSIAN].lower() + ' №15': 'Дирекция:\n'
                                           '•	dorm15@spbstu.ru\n'
                                           '•	+7 (812) 534-03-58\n'
                                           '•	Гражданский пр., д. 28\n'
                                           'Заведующий общежитием – Седакова Екатерина Валерьевна\n',
    DORM_LONG[V_RUSSIAN].lower() + ' №16': 'Дирекция:\n'
                                           '•	dorm16@spbstu.ru\n'
                                           '•	+7 (812) 517-87-66\n'
                                           '•	пр. Энгельса, д. 129, корп. 4\n'
                                           'Группа во ВКонтакте – vk.com/spbstu_16\n'
                                           'Заведующий общежитием – Пипия Отари Силованович\n',
    DORM_LONG[V_RUSSIAN].lower() + ' №19': 'Дирекция:\n'
                                           '•	dorm19@spbstu.ru\n'
                                           '•	+7 (812) 373-67-96\n'
                                           '•	ул. Гастелло, д.20\n'
                                           'Группа во ВКонтакте – vk.com/spbstu_19\n'
                                           'Заведующий общежитием – Бойко Оксана Валентиновна\n',
    DORM_LONG[V_RUSSIAN].lower() + ' №20': 'Дирекция:\n'
                                           '•	dorm20@spbstu.ru\n'
                                           '•	+7 (812) 316-55-08\n'
                                           '•	Малодетскосельский пр., 27\n'
                                           'Группа во ВКонтакте – vk.com/spbstu_20\n'
                                           'Заведующий общежитием – Лошкарева Ольга Евгеньевна\n',

    DORM_LONG[V_ENGLISH].lower() + ' №13': 'Directorate:\n'
                                           '•	dorm13@spbstu.ru\n'
                                           '•	+7 (812) 534-46-65\n'
                                           '•	пр. Гражданский, д. 30\n'
                                           'Group on VKontakte – vk.com/spbstu_13\n'
                                           'Head of the hostel – Кургут Наталья Юрьевна\n',
    DORM_LONG[V_ENGLISH].lower() + ' №15': 'Directorate:\n'
                                           '•	dorm15@spbstu.ru\n'
                                           '•	+7 (812) 534-03-58\n'
                                           '•	Гражданский пр., д. 28\n'
                                           'Head of the hostel – Седакова Екатерина Валерьевна\n',
    DORM_LONG[V_ENGLISH].lower() + ' №16': 'Directorate:\n'
                                           '•	dorm16@spbstu.ru\n'
                                           '•	+7 (812) 517-87-66\n'
                                           '•	пр. Энгельса, д. 129, корп. 4\n'
                                           'Group on VKontakte – vk.com/spbstu_16\n'
                                           'Head of the hostel – Пипия Отари Силованович\n',
    DORM_LONG[V_ENGLISH].lower() + ' №19': 'Directorate:\n'
                                           '•	dorm19@spbstu.ru\n'
                                           '•	+7 (812) 373-67-96\n'
                                           '•	ул. Гастелло, д.20\n'
                                           'Group on VKontakte – vk.com/spbstu_19\n'
                                           'Head of the hostel – Бойко Оксана Валентиновна\n',
    DORM_LONG[V_ENGLISH].lower() + ' №20': 'Directorate:\n'
                                           '•	dorm20@spbstu.ru\n'
                                           '•	+7 (812) 316-55-08\n'
                                           '•	Малодетскосельский пр., 27\n'
                                           'Group on VKontakte – vk.com/spbstu_20\n'
                                           'Head of the hostel – Лошкарева Ольга Евгеньевна\n',

    DORM_LONG[V_CHINESE].lower() + ' №13': '管理局:\n'
                                           '• dorm13@spbstu.ru\n'
                                           '• +7 (812) 534-46-65\n'
                                           '•	пр. Гражданский, д. 30\n'
                                           'VK群 – vk.com/spbstu_13\n'
                                           '宿舍负责人 – Кургут Наталья Юрьевна\n',
    DORM_LONG[V_CHINESE].lower() + ' №15': '管理局:\n'
                                           '• dorm15@spbstu.ru\n'
                                           '• +7 (812) 534-03-58\n'
                                           '•	Гражданский пр., д. 28\n'
                                           '宿舍负责人 – Седакова Екатерина Валерьевна\n',
    DORM_LONG[V_CHINESE].lower() + ' №16': '管理局:\n'
                                           '• dorm16@spbstu.ru\n'
                                           '• +7 (812) 517-87-66\n'
                                           '•	пр. Энгельса, д. 129, корп. 4\n'
                                           'VK群 – vk.com/spbstu_16\n'
                                           '宿舍负责人 – Пипия Отари Силованович\n',
    DORM_LONG[V_CHINESE].lower() + ' №19': '管理局:\n'
                                           '• dorm19@spbstu.ru\n'
                                           '• +7 (812) 373-67-96\n'
                                           '•	ул. Гастелло, д.20\n'
                                           'VK群 – vk.com/spbstu_19\n'
                                           '宿舍负责人 – Бойко Оксана Валентиновна\n',
    DORM_LONG[V_CHINESE].lower() + ' №20': '管理局:\n'
                                           '• dorm20@spbstu.ru\n'
                                           '• +7 (812) 316-55-08\n'
                                           '•	Малодетскосельский пр., 27\n'
                                           'VK群 – vk.com/spbstu_20\n'
                                           '宿舍负责人 – Лошкарева Ольга Евгеньевна\n',

    CHECK_IN_RULES[V_RUSSIAN].lower(): 'Чтобы заселиться в общежитие тебе нужно:'
                                       '•	Получить направление приемной комиссии;\n'
                                       '•	Иметь при себе документ, удостоверяющий личность;\n'
                                       '•	Иметь медицинскую справку форма 086у с обязательной отметкой о '
                                       'флюорографическом обследовании или отдельную справку о флюорографическом '
                                       'обследовании;\n'
                                       '•	Абитуриентам, не достигшим возраста 18 лет и прибывшим без '
                                       'сопровождения родителей или иных законных представителей на срок более '
                                       'трёх суток, необходимо иметь нотариально заверенное согласие родителей ('
                                       'одного из родителей) или иных законных представителей на действия, '
                                       'связанные с поселением и регистрацией. В документе должен быть указан '
                                       'вид действия, на которое даётся согласие: «Я, (Ф.И.О.), даю разрешение '
                                       'на регистрацию по месту пребывания и проживания моего '
                                       'несовершеннолетнего сына (дочери) (паспортные данные и данные '
                                       'свидетельства о рождении) в общежитии ФГАО ВО «Санкт – Петербургский '
                                       'политехнический университет Петра Великого» на период прохождения '
                                       'вступительных испытаний или на период обучения в вышеуказанном '
                                       'университете»;\n'
                                       '•	При заселении также нужно оформить временную регистрацию. Регистрация '
                                       'оформляется в полуавтоматическом режиме. В определенный момент твоя '
                                       'фамилия появится в специальном списке, ты сдашь паспорт и через '
                                       'несколько дней получишь его обратно вместе со временной регистрацией. '
                                       'Регистрация обязательна для всех, это закон. Регистрационный пункт для '
                                       'общежития №6 находится в общежитии №1 СПбПУ (Лесной проспект, д.65 к.1).',
    CHECK_IN_RULES[V_ENGLISH].lower(): 'To be placed in a dormitory, applicants must:\n'
                                       '•	Receive a referral from the Admissions Committee;\n'
                                       '•	Have a document proving your identity;\n'
                                       '•	To have the medical certificate of form 086y forme with obligatory mark about fluorographic examination or the separate certificate about fluorographic examination;\n'
                                       '•	The entrants who have not reached the age of 18 and arrived without parents or other legal representatives for more than three days, it is necessary to have the notarized consent of parents (one of parents) or other legal representatives for the actions connected with settlement and registration. The document must specify the type of action for which consent is given: "I, (full name), give permission to register at the place of stay and residence of my minor son (daughter)(passport data and data of the birth certificate) in the dormitory of the Federal State Educational Institution of Higher Education "Saint-Petersburg Peter the Great University" for the period of admission tests or for the period of study at the above mentioned university";\n'
                                       '•	When you move in also need to issue a temporary registration. Registration is issued in semi-automatic mode. At some point your name will appear on a special list, you will surrender your passport and in a few days you will receive it back together with your temporary registration. Registration is mandatory for everyone, it\'s the law. The registration office for dormitory #6 is located in dormitory #1 of SPbPU (Lesnoy Prospect, 65 k.1).\n',
    CHECK_IN_RULES[V_CHINESE].lower(): '为了被安排在宿舍，申请人必须：\n'
                                       '•	接受招生委员会的推荐。\n'
                                       '•	有证明其身份的文件；\n'
                                       '•	拥有医学证明，并附有心电图，或单独的心电图证明。\n'
                                       '•	未满18周岁的参赛者，在没有父母或其他法定代理人的情况下到达现场3天以上的，必须要有父母（父母一方）或其他法定代理人的公证同意，才能办理落户和报名手续。文件必须说明同意的行动类型："我，（全名），允许我的未成年儿子（女儿）在通过入学考试期间或在上述大学学习期间，联邦国家高等教育自治教育机构 "彼得大帝圣彼得堡理工大学"的宿舍登记（护照数据和出生证数据）。\n'
                                       '•	迁入时还需要开具临时登记。登记以半自动方式处理。到了某个时候，你的名字会出现在一份特殊的名单上，你会把护照还给你，几天后，你会收到护照和你的临时登记。注册是每个人的义务，这是法律规定的。6号宿舍的报名处设在圣彼得堡彼得大帝理工大学的1号宿舍（Lesnoy Prospect，65k.1）。\n',

    ORDER_PASSAGE_PUBLIC[V_RUSSIAN].lower(): 'Вход в общежитие осуществляется по единому именному пропуску Политеха, '
                                             'который получает каждый студент при поступлении в вуз. Вход и выход для '
                                             'студента, проживающего в общежитии осуществляется круглосуточно. За '
                                             'соблюдением режима следят сотрудники службы безопасности и камеры '
                                             'наблюдения.\n '
                                             'Гостей можно проводить с собой по будням с 14:00 до 22:00, по выходным '
                                             'с 10:00 до 22:00. Гости должны покинуть общагу до 23:00. На время '
                                             'пандемии гостей не пускают:(',
    ORDER_PASSAGE_PUBLIC[V_ENGLISH].lower(): 'Entrance to the dormitory is carried out on a single personal pass of '
                                             'Polytechnic, which each student receives upon admission to the '
                                             'university. Entrance and exit for students living in the dormitory is '
                                             '24 hours a day. Security officers and security cameras monitor '
                                             'compliance with the regime.\n '
                                             'Guests can walk in and out on weekdays from 2 p.m. to 10 p.m. and on weekends from 10 a.m. to 10 p.m. Guests must leave the dorm by 11:00 p.m. Guests are not allowed in during the pandemic:(',
    ORDER_PASSAGE_PUBLIC[V_CHINESE].lower(): '宿舍的入学手续由理工学院个人统一办理，每位学生在入学时都会收到一张理工学院的个人通行证。住在宿舍的学生出入口实行24'
                                             '小时值班。保安人员和安全摄像机监测该制度的遵守情况。\n '
                                             '平日14:00至22:00，周末10:00至22:00，均可护送客人。客人必须在23:00之前离开宿舍。疫情期间不允许客人进入 QAQ',

    RESIDENTS_RIGHTS[V_RUSSIAN].lower(): 'Проживающие в общежитии, имеют право:\n'
                                         '•	Переселиться из одной жилой комнаты в другую после согласования с '
                                         'администрацией общежития;\n'
                                         '•	Пользоваться помещениями для самостоятельных занятий и помещениями '
                                         'культурно-бытового назначения, оборудованием, инвентарем общежития;\n'
                                         '•	Обращаться к администрации общежития с просьбами о своевременном '
                                         'ремонте, замене оборудования и инвентаря;\n'
                                         '•	Участвовать в формировании студенческого совета общежития и быть '
                                         'избранным в его состав, участвовать через совет в решении вопросов '
                                         'общежития;\n'
                                         '•	Пользоваться бытовой техникой при условии соблюдения правил ее '
                                         'эксплуатации и правил пожарной безопасности.',
    RESIDENTS_RIGHTS[V_ENGLISH].lower(): 'Residents of the dormitory have the right to:\n'
                                         '•	To move from one living room to another after agreement with the administration of the dormitory;\n'
                                         '•	Use the rooms for independent studies and rooms for cultural and household purposes, equipment and inventory of the dormitory;\n'
                                         'to apply to the administration of the hostel with requests for timely repair, equipment and inventory replacement;\n'
                                         '•	Participate in the formation of the student council of the hostel and be elected to it, participate through the council in solving the problems of the hostel;\n'
                                         '•	To use household appliances under the condition of observing the rules of their operation and fire safety rules.\n',
    RESIDENTS_RIGHTS[V_CHINESE].lower(): '宿舍居民有权：\n'
                                         '•	在与宿舍管理部门达成协议后，从一个房间搬到另一个房间。\n'
                                         '•	将房间用于自主学习和文化及家庭用途的房间，设备和宿舍清单；\n'
                                         '•	向宿舍管理部门提出申请，要求及时维修、更换设备和库存。\n'
                                         '•	参与创建宿舍的学生会，并当选为学生会成员，通过学生会参与解决宿舍的问题。\n'
                                         '•	在遵守家用电器操作规则和消防安全规则的条件下，使用家用电器。\n',

    DUTY_OF_RESIDENTS[
        V_RUSSIAN].lower(): 'Общежитие живет по правилам внутреннего распорядка. В них нет ничего сложного, достаточно делать то, чего от тебя ждут:\n'
                            '•	Не курить и не употреблять алкоголь/наркотики на территории университета (в том числе и общежития);\n'
                            '•	Не мусорить в местах общего пользования: на кухне, в коридорах, в умывалках, в туалетах. Бережно относиться к общему имуществу;\n'
                            '•	Вовремя убираться в своей комнате, не запускать ее. В общежитии действует санитарная комиссия, которая следит за чистотой в комнатах;\n'
                            '•	Не проводить незнакомцев в общежитие. Проводить знакомых только в отведенное время;\n'
                            '•	Не шуметь по ночам и рано утром\n',
    DUTY_OF_RESIDENTS[
        V_ENGLISH].lower(): 'The dormitory lives by house rules. There is nothing complicated about them, just do what is expected of you: \n'
                            '•	No smoking or use of alcohol/drugs on campus (including the dormitory);\n'
                            '•	Do not litter in common areas: in the kitchen, corridors, washrooms, toilets. Take care of the common property;\n'
                            '•	To clean one\'s room in time and not to run it. A sanitary commission operates in the dormitory, which monitors the cleanliness of the rooms;\n'
                            '•	Not to bring strangers into the dormitory. To accompany acquaintances only at the allotted time;\n'
                            '•	No noise at night and early in the morning',
    DUTY_OF_RESIDENTS[V_CHINESE].lower(): '寝室的生活是有规定的。他们没有什么复杂的，你只需要做你所期望的事情。\n'
                                          '•	不在大学内（包括宿舍）吸烟、酗酒、吸毒。\n'
                                          '•	不在公共区域乱扔垃圾：厨房、走廊、盥洗室、厕所。照顾好共同财产。\n'
                                          '•	要及时打扫自己的房间，不要把房间弄脏。宿舍里有一个卫生委员会，负责监视房间的清洁。\n'
                                          '•	不带陌生人进宿舍。要在规定的时间内才能见到熟人。\n'
                                          '•	要遵守静默制度：晚上和清晨不喧哗。\n',

    DUTY_OF_ADMIN[V_RUSSIAN].lower(): 'Администрация студенческого общежития обязана:\n'
                                      '•	Обеспечить предоставление документов для регистрации проживающих по месту пребывания;\n'
                                      '•	Содержать помещения общежитий в соответствии с установленными санитарными правилами;\n'
                                      '•	Укомплектовывать общежития мебелью, оборудованием, постельными принадлежностями и другим инвентарем;\n'
                                      '•	Обеспечить проведение текущего ремонта общежитий, инвентаря, оборудования, содержать в надлежащем порядке закрепленную за Студгородком территорию, зеленые насаждения;\n'
                                      '•	Оперативно устранять неисправности в системах канализации, электроснабжения водоснабжения общежитий;\n'
                                      '•	Обеспечить предоставление проживающим в общежитиях необходимых помещений для самостоятельных занятий, комнат отдыха, бытовых помещений;\n'
                                      '•	В случае заболевания несовершеннолетних проживающих переселять их в другое изолированное помещение по рекомендации лечащего врача;\n'
                                      '•	Обеспечить ежедневный обход всех помещений общежитий их заведующими и работниками соответствующих эксплуатационных служб с целью выявления недостатков по их эксплуатации и санитарному содержанию и принимать меры по их устранению;\n'
                                      '•	Предоставить проживающим в общежитии право пользоваться бытовой техникой и аппаратурой при условии соблюдения ими техники безопасности и инструкций по пользованию бытовыми электроприборами;\n'
                                      '•	Содействовать работе студенческих советов по вопросам улучшения условий проживания, быта и отдыха проживающих;\n'
                                      '•	Принимать меры по реализации предложений проживающих, информировать их о принятых решениях;\n'
                                      '•	Обеспечивать проживающих необходимым оборудованием, инвентарем, инструментом и материалами для проведения на добровольной основе работ по уборке общежитий и закрепленной за Студгородком территории;\n'
                                      '•	Обеспечивать противопожарную и общественную безопасность проживающих в общежитиях и персонала.\n',
    DUTY_OF_ADMIN[V_ENGLISH].lower(): 'The administration of the student dormitory is obliged to:\n'
                                      '•	Ensure the provision of documents for the registration of residents at the place of residence;\n'
                                      '•	Maintain the dormitory premises in accordance with the established sanitary rules;\n'
                                      '•	To equip dormitories with furniture, equipment, bedding and other inventory;\n'
                                      '•	To provide the current repair of dormitories, inventory, equipment, to keep in proper order the territory assigned to the Student campus, green areas;\n'
                                      '•	Promptly eliminate failures in the systems of sewerage, electricity and water supply of the dormitories;\n'
                                      '•	Ensure the provision of the necessary rooms for self-study, recreation rooms, amenity rooms for residents in the dormitories;\n'
                                      '•	In case of illness of underage residents to move them to another isolated room on the recommendation of the attending doctor;\n'
                                      '•	To provide a daily inspection of all dormitory premises by their managers and employees of the relevant operational services in order to identify shortcomings in their operation and sanitary maintenance and to take measures to eliminate them;\n'
                                      '•	To give dwellers in the dormitory the right to use household appliances and equipment on condition that they comply with safety regulations and instructions for using household appliances;\n'
                                      '•	To promote the work of student councils on improving the living conditions, everyday life and recreation of residents;\n'
                                      '•	To take measures for the implementation of residents\' proposals and inform them of the decisions made;\n'
                                      '•	to provide the residents with the necessary equipment, tools and materials for the voluntary cleaning works in the dormitories and the territory assigned to the Studeburgh;\n'
                                      '•	Ensure fire and public safety of the residents and staff in the dormitories.\n',
    DUTY_OF_ADMIN[V_CHINESE].lower(): '学生宿舍的管理部门有义务：\n'
                                      '•	确保在居住地提供居民登记证件。\n'
                                      '•	按照规定的卫生规则，维护好宿舍楼的卫生。\n'
                                      '•	为旅馆配备家具、设备、床上用品和其他库存；\n'
                                      '•	宿舍进行现修、清点、设备，保持校园领地的秩序，对其进行绿化种植。\n'
                                      '•	及时排除宿舍下水道系统、供电、供水系统的故障。\n'
                                      '•	为住在宿舍的居民提供必要的独立学习室、娱乐室、家庭场所。\n'
                                      '•	如有未成年住客患病，根据主治医生的建议，将其转移到另一间隔离房。\n'
                                      '•	由管理人员和相应的经营服务人员每天对旅馆的所有房舍进行检查，以发现其经营和卫生维护方面的不足，并采取措施予以消除；\n'
                                      '•	宿舍的住客有权使用家用电器和设备，但必须遵守安全措施和家用电器的使用说明。\n'
                                      '•	协助学生会关于改善居民生活条件、日常生活和休闲的工作。\n'
                                      '•	采取措施落实居民的建议，并将决定告知居民。\n'
                                      '•	为住户提供必要的设备、工具和材料，以便在宿舍和分配给学生城的区域内进行义务清洁工作。\n'
                                      '•	为确保宿舍内住户和工作人员的消防和公共安全。\n',

    BODIES_OF_MANAGEMENT[
        V_RUSSIAN].lower(): 'В каждом общежитии проживающими избирается орган самоуправления – студенческий совет общежития. \n\n'
                            'В каждом блоке общежития Студгородка избирается староста. Староста блока следит за бережным отношением проживающих к имуществу и оборудованию, организует и контролирует работы по содержанию блока в чистоте и порядке.\n\n'
                            'Также в каждом общежитии избирается председатель Студсовета общежития. Председатель возглавляет Студсовет, занимается защитой прав студентов, а также ответственен за все мероприятия в общаге от Студсовета.\n\n'
                            'Для координации работы во всех общежитиях Студгородка есть Объединенный студенческий совет общежитий, в состав которого включаются все председатели Студсоветов общежитий, представители профсоюзной организации студентов, других общественных студенческих организаций, администрации СПбПУ.\n\n'
                            'Студсовет совместно с администрацией общежития в пределах своих полномочий участвует в расселении студентов нового приема, распределении новой мебели и оборудования между проживающими, сохранность закрепленной жилой площади. \n',
    BODIES_OF_MANAGEMENT[
        V_ENGLISH].lower(): 'In each dorm residents elect a body of self-government - the student council of the dormitory. \n\n'
                            'Each dormitory unit elects a student warden. The Head of the block makes sure that the residents are careful with the property and equipment, organizes and supervises the maintenance of the block in a clean and orderly manner.\n\n'
                            'Also each dormitory elects a Chair of the Dormitory Student Council. The Chairperson heads the Student Council, protects students\' rights, and is responsible for all activities in the dormitory from the Student Council.\n\n'
                            'To coordinate the work in all dormitories of the campus, there is a Joint Student Council of dormitories, which includes all Chairmen of dormitory Student Councils, representatives of the students\' trade union organization, other public student organizations, and the administration of SPbPU.\n\n'
                            'The Student Council together with the administration of the dormitory within the limits of its authority participates in the settlement of students of the new admission, the distribution of new furniture and equipment among the residents, the preservation of the assigned living space. \n',
    BODIES_OF_MANAGEMENT[
        V_CHINESE].lower(): '每个宿舍选出一个自治机构--宿舍的学生会。\n\n'
                            '校园的每个宿舍区都会选出一名学生舍监。街区负责人确保居民认真对待财产和设备，组织和监督街区的清洁和有序的维护。\n\n'
                            '另外，每个宿舍都会选出一名宿舍学生会主席。主席领导学生会，保护学生的权利，并负责学生会在宿舍的所有活动。\n\n'
                            '为了协调校园内所有宿舍的工作，有一个宿舍联合学生会，其中包括所有宿舍学生会主席、学生工会组织的代表、其他公共学生组织、SPbPU的行政部门。\n\n'
                            '学生会与宿舍管理部门在其权限范围内共同参与新入学学生的安置工作，在住户中分配新的家具和设备，确保分配的生活空间的安全。\n',

    RESPONSIBILITY_BREAKING_RULES[V_RUSSIAN].lower(): 'За соблюдением правил следит администрация, студенческий '
                                                      'совет, а также служба безопасности студгородка. По заявлению '
                                                      'любого из этих органов со студента могут потребовать '
                                                      'объяснительную и применить один из методов дисциплинарного '
                                                      'взыскания: замечание, выговор, отчисление из университета. При '
                                                      'этом, если у студента будет три выговора, то его автоматически '
                                                      'отчислят из университета.',
    RESPONSIBILITY_BREAKING_RULES[
        V_ENGLISH].lower(): 'The administration, student council, and campus security office monitor compliance. Upon the request of any of these bodies, students may be required to provide an explanation and may be subjected to one of the following disciplinary methods: a reprimand, a warning, or expulsion from the university. In this case, if a student has three reprimands, he or she will automatically be expelled from the university.',
    RESPONSIBILITY_BREAKING_RULES[
        V_CHINESE].lower(): '行政部门、学生会和校园安保部门负责监督该政策的遵守情况。经上述任何一个机构申请，可以要求学生作出解释，并适用纪律处分的方法之一：训斥、训诫、开除学籍。在这种情况下，如果学生受到三次训斥，将被自动开除学籍。',

    NEIGHBORS[
        V_RUSSIAN].lower(): 'Взаимоотношения – сложная штука. Просто так нельзя расписать все тонкости, чтобы никогда не возникали конфликты. Но их можно свести к минимуму, что мы и поможем тебе сделать с помощью следующих советов.\n\n'
                            'В первые месяцы жизни студенты закупают вещи в комнату. Многие покупают технику совместно с соседями. Но жизнь в общежитии на самом деле непредсказуема, вы можете переехать в другую комнату или общежитие.\n\n'
                            'Поэтому советуем, чтобы каждый купит что-то в комнату сам. Тогда, если именно тебе необходим фен, утюг, мультиварка и т.д., то ты можешь пользоваться этим индивидуально или же делиться с соседями по комнате, если им вдруг понадобится. Также, при неожиданных ситуациях, вы сможете забрать технику себе или перепродать ее. Это поможет избежать конфликтов с соседями.\n\n'
                            'Между соседями часто возникают конфликты при выполнении тех или иных обязанностей. Поэтому обрати внимание на следующие советы:\n'
                            '•	Составьте график уборки, определите последовательность и периодичность уборки. Решите, что будет входить в обязанности дежурного. Например, подмести и вымыть пол, вытереть пыль с бытовых приборов.\n'
                            '•	Мусор необходимо выносить каждый день. Скопление в мусорном ведре пищевых отходов влечет за собой неприятный запах в комнате, а также появление тараканов. Договоритесь, кто за кем выносит мусор. Прикрепите на дверь график дежурств и выноса мусора. Это поможет соблюдать порядок и дисциплину в комнате.\n\n'
                            'У каждого человека свои особенности питания. Поэтому важно уважать вкусовые предпочтения соседа, если даже он каждый вечер заваривает лапшу быстрого приготовления:)\n\n'
                            'Многие в самом начале жизни в общаге стараются покупать продукты и готовить вместе. Но вскоре это становится неудобным из-за расписания или пожеланий в еде. Поэтому мы рекомендуем питаться отдельно, чтобы избежать конфликтов по поводу количества съеденного. Но никто не запрещает угощать соседей своим фирменным блюдом.\n',
    NEIGHBORS[
        V_ENGLISH].lower(): 'Relationships are complicated things. You just can\'t spell out all the subtleties so that conflicts never arise. But they can be minimized, which we\'ll help you do with the following tips.\n\n'
                            'In the first few months of life, students shop for things in their room. Many buy appliances jointly with their roommates. But dorm life is really unpredictable, you may move to another room or dorm.\n\n'
                            'So it is advised that everyone buy something in the room on their own. Then, if you\'re the one who needs a hair dryer, iron, multicooker, etc., you can use it individually or you can share it with your roommates if they suddenly need it. Also, in case of unexpected situations, you will be able to take the appliances for yourself or resell them. This will help you avoid conflicts with your neighbors.\n\n'
                            'There are often conflicts between roommates when performing certain duties. Therefore, pay attention to the following tips:\n'
                            '•	Make a cleaning schedule, determine the sequence and frequency of cleaning. Decide what will be part of the duties of the person on duty. For example, sweep and mop the floor, wipe dust off appliances.\n'
                            '•	Garbage must be taken out every day. The accumulation of food waste in the garbage can causes an unpleasant smell in the room, as well as the appearance of cockroaches. Agree on who takes out the garbage for whom. Put a schedule of duty and trash pickup on the door. This will help keep the room orderly and disciplined.\n'
                            'Each person has different eating habits. So it is important to respect the taste preferences of your neighbor, even if he makes instant noodles every night:)\n\n'
                            'Many in the beginning of life in the dorm try to buy groceries and cook together. But soon it becomes inconvenient because of the schedule or food preferences. So we recommend eating separately to avoid conflicts over the amount eaten. But no one forbids treating your neighbors to your special meal.\n',
    NEIGHBORS[V_CHINESE].lower(): '关系是复杂的事情。你就是不能把所有的微妙之处都说出来，这样就不会出现冲突。但它们可以被保持在最低限度，我们将通过以下提示帮助你做到这一点。\n\n'
                                  '在生活的头几个月，学生们在自己的房间里买东西。许多人与室友一起购买电器。但宿舍生活真的是不可预测的，你可能会搬到另一个房间或宿舍。\n\n'
                                  '所以我们建议大家在房间里自己买点东西。然后，如果你是那个需要吹风机、熨斗、多孔锅等的人，你可以单独使用，或者在你的室友突然需要时与他们分享。此外，如果出现意外情况，你将能够把电器据为己有或转卖。这将帮助你避免与你的室友发生冲突。\n\n'
                                  '在履行某些职责时，室友之间经常会有冲突。因此，请注意以下提示。\n'
                                  '•	制定一个清洁时间表，确定清洁的顺序和频率。决定值班人员的职责是什么。例如，扫地和拖地，擦拭电器上的灰尘。\n'
                                  '•	垃圾需要每天倒出。垃圾中的食物残渣堆积会导致房间里出现难闻的气味，也会出现蟑螂。就谁为谁倒垃圾达成一致。在门上贴上值班和捡拾垃圾的时间表。这将有助于保持房间的秩序和纪律。\n\n'
                                  '每个人都有不同的饮食习惯。因此，必须尊重你的邻居的口味偏好，即使他每天晚上都做方便面:)\n\n'
                                  '许多人在宿舍生活的开始阶段，尝试着一起买菜和做饭。但很快就因为日程安排或食物偏好而变得不方便了。因此，我们建议分开吃，以避免在吃的数量上发生冲突。但是没有人禁止用你的特别餐来招待你的邻居。\n',

    ADMINISTRATION[
        V_RUSSIAN].lower(): 'Тебе не так часто придется взаимодействовать с администрацией, так что советов не так много. Не ссорься с администрацией, здоровайся при встрече, участвуй в жизни общежития, плати вовремя и у тебя будут отличные отношения с ней. Проверено:)\n',
    ADMINISTRATION[
        V_ENGLISH].lower(): 'You won\'t have to interact with the administration very often, so there\'s not much advice. Don\'t quarrel with the administration, say hello when you meet them, participate in dorm life, pay on time and you\'ll have a great relationship with them. Tested:)',
    ADMINISTRATION[
        V_CHINESE].lower(): '你不会经常与行政部门打交道，所以没有什么建议。不要与管理部门争吵，遇到他们时要打招呼，参与宿舍生活，按时付款，你就会与他们建立良好的关系。亲测(*･ω-q) ',

    COCKROACHES[
        V_RUSSIAN].lower(): 'В общежитии в некоторых комнатах много тараканов, а где-то их вовсе нет. Следующие правила помогут тебе избежать встречи с ними.\n'
                            'Не стоит засорять комнату. Это грозит не только появлением проблем с санитарной комиссией общежития, но и скоплением тараканов в вашей комнате.\n'
                            '•	Мойте посуду сразу после еды. Не оставляйте продукты в открытом виде.\n'
                            '•	Заранее продумайте, как хранить сыпучие сухие изделия (макароны, крупы). Рекомендуем приобрести контейнеры для каждой крупы отдельно. Так же стоит купить большую пластиковую коробку для всех контейнеров поменьше.\n'
                            '•	Необходимо протирать пыль, проветривать комнату.\n'
                            '•	Чистый пол — залог порядка, поэтому мойте полы раз в неделю или чаще. Тараканы могут прятаться в стопке бумаг и мусора, поэтому все ненужное необходимо выкидывать.\n'
                            '•	В общежитии можно заказать травлю тараканов/клопов. Для этого нужно оставить заявку на вахте. Если потравили тараканов плохо, то необходимо сообщить Студсовету или администрации общежития.\n'
                            'Тараканы не любят, когда их беспокоят и часто они поселяются там, куда вы реже всего заглядываете, особенно если там тепло или влажно. Часто тараканов можно встретить за холодильником, в точке доступа Wi-Fi или под чайником.\n'
                            'Вообще, тараканам очень важна вода, поэтому лучше нигде не оставлять воду в открытом виде — кружки, тарелки после мытья. Если надолго уезжаете, то лучше слить воду из чайника и фильтра.\n'
                            'Не советуем покупать самые дешевые средства против тараканов, обычно они оказываются бесполезными. Стоит брать такие марки как «Машенька», «Дохлокс», «Раптор», «Комбат» и др. Их можно найти в любом магазине за приемлемую цену.\n'
                            '•	Если вы только заехали в общагу и у вас еще нет мебели, то стоит промазать гелем плинтус.\n'
                            '•	Рекомендуем раз в месяц обрабатывать зону под холодильником и кухонным шкафом. Это самое любимое место тараканов. При возможности отодвигайте холодильники и шкафы.\n'
                            '•	Приобретите ловушки и разложите по всей комнате. Не забудьте зоны батареи, под кроватью и столом, холодильником. Ловушки необходимо менять раз в 3-6 месяцев.\n'
                            '•	Если тараканы завелись в тумбочке, то стоит разобрать ее полностью и обработать.\n',
    COCKROACHES[
        V_ENGLISH].lower(): 'In the dormitory, some rooms are full of cockroaches and some are not at all. The following rules will help you avoid meeting them.\n'
                            'You should not litter your room. This threatens not only the appearance of problems with the sanitary commission of the hostel, but also the accumulation of cockroaches in your room.\n'
                            '•	Wash dishes immediately after meals. Do not leave food open.\n'
                            '•	Consider in advance how to store loose dry goods (pasta, cereals). We recommend buying containers for each cereal separately. It is also worth buying a large plastic box for all the smaller containers.\n'
                            '•	It is necessary to wipe dust and air the room.\n'
                            '•	A clean floor is the key to order, so wash the floors once a week or more often. Cockroaches can hide in stacks of papers and trash, so anything unnecessary should be thrown out.\n'
                            '•	You can order cockroach/bug extermination in your dormitory. To do this, you need to leave an application on the watch. If the cockroach control is bad, it is necessary to inform the student council or the administration of the dormitory.\n'
                            'Cockroaches don\'t like to be disturbed and often settle where you look the least, especially if it\'s warm or humid. Cockroaches can often be found behind the refrigerator, in the Wi-Fi hotspot, or under the kettle.\n'
                            'In general, roaches are very important to water, so it\'s best not to leave water anywhere open - mugs, plates after washing. If you go away for a long time, it is better to drain the water from the kettle and the filter.\n'
                            'We do not advise to buy the cheapest anti-cockroach products, they usually turn out to be useless. It is worth taking brands such as "Mashenka", "Dohloks", "Raptor", "Combat" and others. You can find them in any store for a reasonable price.\n'
                            '•	If you have just moved into the dorm and you do not yet have furniture, it is worth dabbing gel on the baseboard.\n'
                            '•	We recommend treating the area under the refrigerator and kitchen cabinet once a month. This is the roaches\' favorite spot. Move refrigerators and cabinets away if possible.\n'
                            '•	Purchase traps and place them around the room. Don\'t forget the battery area, under the bed and table, and the refrigerator. Traps should be changed every 3-6 months.\n'
                            '•	If the cockroaches are in the nightstand, it is worth taking it apart completely and treating it.\n',
    COCKROACHES[V_CHINESE].lower(): '在宿舍里，有些房间有很多蟑螂，有些房间没有。以下规则将帮助你避免遇到这些情况。\n'
                                    '你不应该乱扔你的房间。这不仅有可能造成宿舍卫生委员会的问题，而且还有可能在你的房间里积聚蟑螂。\n'
                                    '•	饭后立即清洗餐具。不要将食物敞开。\n'
                                    '•	提前考虑如何储存散装干货（面食、谷物）。我们建议为每个项目单独购买一个容器。还要买一个大的塑料盒来装所有的小容器。\n'
                                    '•	有必要擦掉灰尘并给房间通风。\n'
                                    '•	干净的地板对秩序是至关重要的，所以每周拖一次或更频繁地拖地。蟑螂可以藏在成堆的文件和垃圾中，所以任何不必要的东西都应该被扔掉。\n'
                                    '•	你可以在你的宿舍里订购灭蟑螂/虫子。要做到这一点，你必须在宿舍大厅留下申请。如果蟑螂控制得不好，有必要通知学生会或宿舍管理部门。\n'
                                    '蟑螂不喜欢被打扰，经常在你最不愿意看到的地方定居，尤其是在温暖或潮湿的环境中。蟑螂经常可以在冰箱后面、路由器里或水壶下面找到。\n'
                                    '一般来说，蟑螂对水非常重视，所以最好不要把水放在露天的任何地方--杯子、盘子洗完后。如果你离开很长时间，最好把水壶和过滤器里的水放掉。\n'
                                    '我们不建议购买最便宜的防蟑螂产品，因为它们通常会变成无用的。值得采取的品牌有 "Mashenka"、"Dohloks"、"Raptor"、"Combat "和其他。你可以在任何商店找到它们，而且价格合理。\n'
                                    '•	如果你刚搬进宿舍，还没有家具，那么给底板上胶是值得的。\n'
                                    '•	我们建议每月对冰箱和厨房橱柜下面的区域进行处理一次。这是蟑螂们最喜欢的地方。如果可能的话，将冰箱和橱柜移开。\n'
                                    '•	购买陷阱并将其放置在房间周围。不要忘了电池区、床下和桌子，以及冰箱。疏水阀必须每3-6个月更换一次。\n'
                                    '•	如果蟑螂在床头柜里，就把它完全拆开并进行处理。\n',

    WHAT_TO_TAKE_WITH_YOU[
        V_RUSSIAN].lower(): 'В общежитии понадобится большое количество вещей, можем вам посоветовать, что будет нужно 100%.\n\n'
                            'Вещи для обустройства комнаты: шторы, прикроватный коврик, тёплый плед, тряпку для протирки пыли.\n\n'
                            'Одежда: столько, сколько нужно на месяц, в общежитие есть прачечная, несколько вешалок, одежда для занятий физкультурой. Из верхней одежды возьмите осенние вещи, зимние в первое время берите. Их можно будет привести или переслать позже, если вдруг наступит плохая погода, в Санкт-Петербурге не очень холодные зимы (по сравнению с Сибирью).\n\n'
                            'Обувь: желательно взять по две пары “летней” и межсезонной обуви, не забудьте взять сушилку для обуви. Зимнюю обувь также можно прислать позже. Потребуются кроссовки для занятий физкультурой. Также необходимы тапочки/шлепки для общаги и резиновые шлепки для похода в душ.\n\n'
                            'Гигиенические и косметические средства: шампунь, гель для тела, мочалка (если нужна), мыло, порошок/гель для стирки (машинки в прачечной нужно засыпать своим средством), зубная щётка, зубная паста, туалетная бумага, косметические средства, ножницы для ногтей, полотенца.\n\n'
                            'Аптечка: средство от боли, средства для решения проблем с животом, бинт, пластырь бактерицидный, мазь антисептическая, лекарства, которые тебе нужны, спрей от насморка, противопростудные и жаропонижающие препараты.\n\n'
                            'Продукты: немного чая или кофе, немного сахара, готовая еда (котлеты, овощи и т.п.) которой хватит на 2 раза покушать (один раз перекусить пока будешь заселяться и один раз на ужин).\n\n'
                            'Электронные приборы: ноутбук (ты будешь его носить на учебу и для того чтобы ноутбук дольше служил, заведи для него сумку), удлинители (розетки могут находиться на расстоянии от стола/кровати, либо их просто будет не хватать), точка доступа в интернет (при заселении нужно будет подписать договор с интернет компанией для подключения интернета, но модем покупать самим).\n\n'
                            'Документы для заселения в общежитие: паспорт, парочку фотографий 3*4, результаты флюорографии, сведения о медицинских прививках.\n\n'
                            'Кухонные принадлежности: кастрюля, сковорода (не покупайте новые, старые помогут вам потренироваться в начале), глубокая и обычная тарелка, вилки, ложки, нож, черпак, средства для мытья и чистки посуды, спички или зажигалка.\n\n'
                            'Бытовая техника: электрический чайник, микроволновая печь, холодильник, мультиварка (все это лучше купить на месте, также это можно купить у выезжающих студентов, что будет выгоднее).\n',
    WHAT_TO_TAKE_WITH_YOU[
        V_ENGLISH].lower(): 'In the dormitory will need a lot of things, we can advise you what you will need 100%.\n\n'
                            'Things to furnish your room: curtains, a bedside rug, a warm plaid, a rag to wipe off dust.\n\n'
                            'Clothes: as much as you need for a month, the dormitory has a laundry room, some hangers, clothes for physical training. From outer clothing take autumn clothes, take winter clothes at first. They can be brought or sent later if suddenly bad weather comes, in St. Petersburg winters are not very cold (compared with Siberia).\n\n'
                            'Footwear: it is advisable to take two pairs of "summer" and interseasonal shoes each, and don\'t forget to take a shoe dryer. Winter shoes can also be sent later. Sneakers will be needed for physical education classes. Dorm slippers/slippers and rubber slippers for showering are also needed.\n\n'
                            'Hygiene and beauty supplies: shampoo, body gel, washcloth (if needed), soap, laundry detergent/gel (the machines in the laundry room need to be filled with their own detergent), toothbrush, toothpaste, toilet paper, beauty products, nail clippers, towels.\n\n'
                            'First aid kit: pain reliever, remedies for stomach problems, bandages, bactericidal bandage, antiseptic ointment, medications you need, runny nose spray, cold and fever medications.\n\n'
                            'Food: some tea or coffee, some sugar, ready-made food (cutlets, vegetables, etc.) which is enough for two meals (one snack while you\'re checking in and one for dinner).\n\n'
                            'Electronic devices: laptop (you\'ll be carrying him to school and in order to laptop longer serve, have a bag for him), extension cords (outlets may be at a distance from the desk / bed, or they just won\'t be enough), the point of Internet access (at check in will need to sign a contract with an Internet company to connect the Internet, but the modem buy it yourself).\n\n'
                            'Documents for moving into the dormitory: passport, a couple of photos 3*4, the results of fluorography, information about medical vaccinations.\n\n'
                            'Kitchen utensils: saucepan, frying pan (don\'t buy new ones, the old ones will help you practice in the beginning), deep and plain plates, forks, spoons, knife, scoop, dishwashing and cleaning supplies, matches or a lighter.\n\n'
                            'Home appliances: electric kettle, microwave oven, refrigerator, multicooker (all these things are better to buy on the spot, you can also buy them from visiting students, which will be more profitable).\n',
    WHAT_TO_TAKE_WITH_YOU[V_CHINESE].lower(): '宿舍需要很多东西，我们可以向你建议100%需要的东西\n\n'
                                              '装饰房间的东西：窗帘、床头地毯、温暖的格子布、擦拭灰尘的抹布。\n\n'
                                              '衣服：一个月需要多少就有多少，宿舍有一个洗衣房，有几个衣架，体育课用的衣服。从外衣中取出秋天的衣服，冬天的一开始就取出。如果坏天气突然来临，他们可以稍后带来或发送，在圣彼得堡的冬天不是很冷（与西伯利亚相比）。\n\n'
                                              '鞋类：最好带两双 "夏季 "和跨季的鞋子，别忘了带一个烘鞋器。冬鞋也可以稍后发送。需要穿上体育课的运动鞋。还需要有宿舍拖鞋/拖鞋和洗澡用的橡胶拖鞋。\n\n'
                                              '卫生和美容用品：洗发水、沐浴露、毛巾（如果需要的话）、肥皂、洗衣粉/凝胶（洗衣房的机器需要自己装洗涤剂）、牙刷、牙膏、卫生纸、化妆品、指甲刀、毛巾。\n\n'
                                              '急救箱：止痛药、治疗胃病的药、绷带、杀菌绷带、消毒药膏、你需要的药品、喷鼻剂、感冒和发烧药。\n\n'
                                              '食物：一些茶或咖啡，一些糖，现成的饭菜（肉丸子、蔬菜等），足够两顿饭吃的（一份是入住前的点心，一份是晚餐）。\n\n'
                                              '电子设备：笔记本电脑（你要带着他去学校，为了让笔记本电脑更长时间的服务，要给他准备一个包），延长线（插座可能离书桌或床有一定的距离，否则就是不够用），互联网接入点（在入住时需要和互联网公司签订合同，连接互联网，但路由器要自己买）。\n\n'
                                              '入住宿舍的文件：护照、几张3*4的照片、透视检查结果、医疗疫苗接种信息。\n\n'
                                              '厨房用具：汤锅、煎锅（不要买新的，旧的可以在开始时帮助你练习）、深色和普通的盘子、叉子、勺子、刀、勺子、洗涤和清洁用具、火柴或打火机\n\n'
                                              '家用电器：电热水壶、微波炉、冰箱、多用电饭煲（这些东西最好是当场购买，也可以向离校的学生购买，这样会省一笔）\n',

    WHAT_TO_BUY_LOCALLY[
        V_RUSSIAN].lower(): 'Кухонные принадлежности: кастрюля, сковорода (не покупайте новые, старые помогут вам потренироваться в начале), глубокая и обычная тарелка, вилки, ложки, нож, черпак, средства для мытья и чистки посуды, спички или зажигалка.\n'
                            'Бытовая техника: электрический чайник, микроволновая печь, холодильник, мультиварка (все это лучше купить на месте, также это можно купить у выезжающих студентов, что будет выгоднее).\n',
    WHAT_TO_BUY_LOCALLY[
        V_ENGLISH].lower(): 'Kitchen utensils: saucepan, frying pan (don\'t buy new ones, the old ones will help you practice in the beginning), deep and plain plates, forks, spoons, knife, scoop, dishwashing and cleaning supplies, matches or a lighter.\n'
                            'Home appliances: electric kettle, microwave oven, refrigerator, multicooker (all these things are better to buy on the spot, you can also buy them from visiting students, which will be more profitable).\n',
    WHAT_TO_BUY_LOCALLY[V_CHINESE].lower(): '厨房用具：汤锅、煎锅（不要买新的，旧的可以在开始时帮助你练习）、深色和普通的盘子、叉子、勺子、刀、勺子、洗涤和清洁用具、火柴或打火机\n'
                                            '家用电器：电热水壶、微波炉、冰箱、多用电饭煲（这些东西最好是当场购买，也可以向离校的学生购买，这样会省一笔）\n'
}
