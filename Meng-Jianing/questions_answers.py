# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 12:48
# @Author  : Meng Jianing
# @FileName: questions_answers.py
# @Software: PyCharm
# @Versions: v0.9
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
CLUB = ('Студклубе', 'Student Club', '学生俱乐部')
ONLINE_COURSE = ('Онлайн-Класс', 'Online Course', '网课')
NEXT = ('Далее', 'Next', '下一页')
MANAGEMENT_CONTACTS = ('Контакты управления', 'Management contacts', '联系宿管')
ACCOMMODATION_RULES = ('Правила проживания', 'Accommodation rules', '住宿相关')  # TODO
COMPLEXES = ('Комплексы', 'Complexes', '宿舍分布')
ADVICE = ('Советы', 'Advice', '建议')  # TODO
FRONT = ('Назад', 'Back', '返回')
CHANGE_LANGUAGE = ('Сменить язык', 'Change language', '更改语言')
INTERNAL_REGULATIONS = ('Внутренний распорядок', 'Internal regulations', '内部规定')
TO_THE_BEGINING = ('В начало', 'To the begin', '返回主页')
LESNOY_PROSPECT = ('Лесной проспект', 'Lesnoy prospect', '森林大街')
COURAGE_SQUARE = ('Площадь Мужества', 'Courage Square', '勇气广场')
CIVIL_PROSPECT = ('Гражданский проспект', 'Civil Prospect', '公民大街')
SCIENCE_POLYTECH = ('Гостиницу “Наука-Политех”', 'Dorm “Science-Polytech”', '宾馆 “圣理工的科学”')  # TODO
COMPLEX_FOR_FURTHER_EDUCATION = (
    'Комплекс доп-ого обс-ия проживающих', 'Complex for further education', '非全日制学生住址')  # TODO
RELATIONSHIP_WITH = ('Взаимоотношения с...', 'Relationship with...', '联系...')
MOVING_TO_THE_DORM = ('Переезд в общежитие', 'Moving to dorm', '入住建议')
# INTERNAL_REGULATIONS = ('', '', '')
PAYMENT = ('Оплата', 'Pay', '支付')
DORM_SHORT = ('Общ-ие', 'Dorm', '宿舍')
DORM_LONG = ('Общежитие', 'Dormitory', '宿舍')
CHECK_IN_RULES = ('Правила заселения', 'Check-in rules', '入住规则')
ORDER_PASSAGE_PUBLIC = ('Порядок прохода в общ-ия', 'Order of passage to dorm', '进入宿舍的顺序')  # TODO
RESIDENTS_RIGHTS = ('Права проживающих', 'Residents\' rights', '行为准则')
DUTY_OF_RESIDENTS = ('Об-сти проживающих', 'Duty of residents', '住宿义务')
DUTY_OF_ADMIN = ('Об-сти админ-ии', 'Duty of admin', '宿管责任')
BODIES_OF_MANAGEMENT = ('Органы студ-ого управления', 'Student management bodies', '学生管理机构')  # TODO
RESPONSIBILITY_BREAKING_RULES = ('Ответ-сть за нарушение правил', 'Resp-ty for breaking rules', '违反规定后承担的责任')
NEIGHBORS = ('Соседями', 'Neighbors', '舍友')
ADMINISTRATION = ('Администрицией', 'Administration', '行政部门')  # TODO
COCKROACHES = ('Тараканами', 'Cockroaches', '除蟑螂')
WHAT_TO_TAKE_WITH_YOU = ('Что взять с собой', 'What to take with you', '随身带什么')
WHAT_TO_BUY_LOCALLY = ('Что купить на месте', 'What to buy locally', '需要购买的物品')

# 键值对 <--> 问题（小写）和回答
# Пары ключ-значение <--> вопрос (НИЖНИЙ регистр) и ответ
# Attention! Questions should be in all lowercase!
gl_questions_answers = {
    'hello123': 'Hello there',
    'help': 'We also need help qwq',
    'русский': 'Текущим языком уже является русский',
    'english': 'Changed language to English',
    '中文': '已将语言设置为简体中文',

    CLUB[V_RUSSIAN].lower(): 'Студклуб - это старейшее студенческое досуговое направление Политеха, которое более 85 '
                             'лет помогает студентам развивать и реализовывать свой творческий потенциал. Спектр '
                             'деятельности Студенческого клуба широк: студенты имеют возможность заниматься актёрским '
                             'мастерством, музыкой, танцами, цифровым дизайном, а также участвовать в организации '
                             'мероприятий. Если заинтересовался, то советуем пройти в группу Студклуба во ВКонтакте '
                             'для большей информации: vk.com/poly_studklub',
    CLUB[V_ENGLISH].lower(): 'Do you what know more?',
    CLUB[V_CHINESE].lower(): '想知道更多吗？',

    ONLINE_COURSE[V_RUSSIAN].lower(): 'no_answer_ONLINE_COURSE[V_RUSSIAN]',
    ONLINE_COURSE[V_ENGLISH].lower(): 'no_answer_ONLINE_COURSE[V_ENGLISH]',
    ONLINE_COURSE[V_CHINESE].lower(): 'no_answer_ONLINE_COURSE[V_CHINESE]',

    NEXT[V_RUSSIAN].lower(): 'Далее',
    NEXT[V_ENGLISH].lower(): 'Next',
    NEXT[V_CHINESE].lower(): '下一页',

    MANAGEMENT_CONTACTS[V_RUSSIAN].lower(): 'Директор Студгородка – Шнейдер Анатолий Альбертович:\n'
                                            '•	uprstg@spbstu.ru\n'
                                            '•	+7 (812) 290-95-02\n'
                                            '•	пр. Непокорённых, д.8, корп.2, общ. №14б\n\n'
                                            'Городская Служба Заселения Студентов:\n'
                                            '•	+7 (981) 805-32-40',
    MANAGEMENT_CONTACTS[V_ENGLISH].lower(): 'no_answer_MANAGEMENT_CONTACTS[V_ENGLISH]',
    MANAGEMENT_CONTACTS[V_CHINESE].lower(): 'no_answer_MANAGEMENT_CONTACTS[V_CHINESE]',

    ACCOMMODATION_RULES[V_RUSSIAN].lower(): 'Правила проживания',
    ACCOMMODATION_RULES[V_ENGLISH].lower(): 'Accommodation rules',
    ACCOMMODATION_RULES[V_CHINESE].lower(): '住宿相关',

    COMPLEXES[V_RUSSIAN].lower(): 'Комплексы',
    COMPLEXES[V_ENGLISH].lower(): 'Complexes',
    COMPLEXES[V_CHINESE].lower(): '宿舍分布',

    ADVICE[V_RUSSIAN].lower(): 'Советы',
    ADVICE[V_ENGLISH].lower(): 'Advice',
    ADVICE[V_CHINESE].lower(): '建议',

    FRONT[V_RUSSIAN].lower(): 'Назад',
    FRONT[V_ENGLISH].lower(): 'Back',
    FRONT[V_CHINESE].lower(): '返回',

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
                                        '•	Лесной пр., д. 67, корп.2, общ. №7',
    LESNOY_PROSPECT[V_ENGLISH].lower(): 'no_answer_LESNOY_PROSPECT[V_ENGLISH]',
    LESNOY_PROSPECT[V_CHINESE].lower(): 'no_answer_LESNOY_PROSPECT[V_CHINESE]',

    COURAGE_SQUARE[V_RUSSIAN].lower(): 'Начальник комплекса - Короткова Руфина Рауфовна:\n'
                                       '•	rrkorotkova@spbstu.ru\n'
                                       '•	+7 (812) 290-97-12\n'
                                       '•	пр. Непокорённых, д.8, корп.2, общ. №14б\n',
    COURAGE_SQUARE[V_ENGLISH].lower(): 'no_answer_COURAGE_SQUARE[V_ENGLISH]',
    COURAGE_SQUARE[V_CHINESE].lower(): 'no_answer_COURAGE_SQUARE[V_CHINESE]',

    CIVIL_PROSPECT[V_RUSSIAN].lower(): 'Начальник комплекса - Никулин Алексей Николаевич:\n'
                                       '•	nikulin@spbstu.ru\n'
                                       '•	+7 (812) 322-01-38\n'
                                       '•	Гражданский пр., д. 28, кабинет 114\n',
    CIVIL_PROSPECT[V_ENGLISH].lower(): 'no_answer_CIVIL_PROSPECT[V_ENGLISH]',
    CIVIL_PROSPECT[V_CHINESE].lower(): 'no_answer_CIVIL_PROSPECT[V_CHINESE]',

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
    SCIENCE_POLYTECH[V_ENGLISH].lower(): 'no_answer_SCIENCE_POLYTECH[V_ENGLISH]',
    SCIENCE_POLYTECH[V_CHINESE].lower(): 'no_answer_SCIENCE_POLYTECH[V_CHINESE]',

    COMPLEX_FOR_FURTHER_EDUCATION[V_RUSSIAN].lower(): 'no_answer_COMPLEX_FOR_FURTHER_EDUCATION[V_RUSSIAN]',
    COMPLEX_FOR_FURTHER_EDUCATION[V_ENGLISH].lower(): 'no_answer_COMPLEX_FOR_FURTHER_EDUCATION[V_ENGLISH]',
    COMPLEX_FOR_FURTHER_EDUCATION[V_CHINESE].lower(): 'no_answer_COMPLEX_FOR_FURTHER_EDUCATION[V_CHINESE]',

    RELATIONSHIP_WITH[V_RUSSIAN].lower(): 'Взаимоотношения с...',
    RELATIONSHIP_WITH[V_ENGLISH].lower(): 'Relationship with...',
    RELATIONSHIP_WITH[V_CHINESE].lower(): '联系...',

    MOVING_TO_THE_DORM[V_RUSSIAN].lower(): 'Переезд в общежитие',
    MOVING_TO_THE_DORM[V_ENGLISH].lower(): 'Moving to dorm',
    MOVING_TO_THE_DORM[V_CHINESE].lower(): '入住建议',

    PAYMENT[V_RUSSIAN].lower(): 'Когда происходит поселение в общежитие, ты подписываешь договор о найме жилья, '
                                'за которое необходимо платить в районе 1000 рублей в месяц.\n'
                                'Цена зависит от количества человек в комнате, за «уплотнение» чуть меньше.\n'
                                'Цена за общежитие в зимний и летний период немного отличается. Актуальную стоимость '
                                'ты можешь узнать на информационном стенде в общежитии.\n'
                                'Оплату можно производить по реквизитам в банках города (Сбербанк, СПБ) или на '
                                'pay.spbstu.ru. После оплаты по реквизитам нужно также показать квитанцию об оплате '
                                'администрации общежития.\n '
                                'За долг более 3000 рублей администрация студгородка может вызвать к себе, в случае '
                                'повторных нарушений возможен выговор.\n '
                                'Возможна оплата на несколько месяцев вперед.',
    PAYMENT[V_ENGLISH].lower(): 'no_answer_PAYMENT[V_ENGLISH]',
    PAYMENT[V_CHINESE].lower(): 'no_answer_PAYMENT[V_CHINESE]',

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
                                           '•	Lesnoy pr., д. 65, build.1\n'
                                           'Group on VKontakte – vk.com/spbstu_1\n'
                                           'Head of the hostel – Шевченко Ольга Николаевна',
    DORM_SHORT[V_ENGLISH].lower() + ' №3': 'Directorate:\n'
                                           '•	dorm3@spbstu.ru\n'
                                           '•	+7 (812) 775 05 30 #1448\n'
                                           '•	Lesnoy pr., д. 65, build. 3\n'
                                           'Group on VKontakte – vk.com/spbstu_3\n'
                                           'Head of the hostel – Киреева Наталья Викторовна',
    DORM_SHORT[V_ENGLISH].lower() + ' №4': 'Directorate:\n'
                                           '•	dorm4@spbstu.ru\n'
                                           '•	+7 (812) 775 05 30 #1451\n'
                                           '•	st. Pargolovskaya, д.11, build.1\n'
                                           'Group on VKontakte – vk.com/spbstu_4\n'
                                           'Head of the hostel – Мартынова Лариса Яковлевна',
    DORM_SHORT[V_ENGLISH].lower() + ' №4а': 'Directorate:\n'
                                            '•	dorm4a@spbstu.ru\n'
                                            '•	+7 (812) 775 05 30 #1453\n'
                                            '•	st. Pargolovskaya, д.11, build.1\n'
                                            'Group on VKontakte – vk.com/spbstu_4aa\n'
                                            'Head of the hostel – Гst.ва Ирианда Анатольевна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №5': 'Directorate:\n'
                                           '•	dorm5@spbstu.ru\n'
                                           '•	+7 (812) 295-47-25\n'
                                           '•	st. Pargolovskaya, д.11, build.2\n'
                                           'Group on VKontakte – vk.com/spbstu_5a | vk.com/spbstu_5b\n'
                                           'Head of the hostel – Мартьянова Милена Леонидовна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №6': 'Directorate:\n'
                                           '•	dorm6m@spbstu.ru\n'
                                           '•	+7 (812) 295-27-50\n'
                                           '•	st. Kharchenko, д. 16\n'
                                           'Group on VKontakte – vk.com/spbstu_6\n'
                                           'Head of the hostel – Егорова Ольга Адамовна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №7': 'Directorate:\n'
                                           '•	dorm7@spbstu.ru\n'
                                           '•	+7 (812) 775-05-30 #1442\n'
                                           '•	+7 (812) 775-05-30 #1443\n'
                                           '•	Lesnoy pr., д.67, build.2\n'
                                           'Head of the hostel – Кривошея Гst.нара Куртвелиевна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №8': 'Directorate:\n'
                                           '•	dorm8@spbstu.ru\n'
                                           '•	+7 (812) 297-43-50\n'
                                           '•	st. Khlopin, д.9, build.2\n'
                                           'Group on VKontakte – vk.com/spbstu_8\n'
                                           'Head of the hostel – Бернанс Ольга Ивановна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №10': 'Directorate:\n'
                                            '•	dorm10@spbstu.ru\n'
                                            '•	+7 (812) 297-16-78\n'
                                            '•	pl. Nepokopolychnye, д. 6, build.2\n'
                                            'Group on VKontakte – vk.com/spbstu_10\n'
                                            'Head of the hostel – Текучева Елена Ивановна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №11': 'Directorate:\n'
                                            '•	dorm11@spbstu.ru\n'
                                            '•	+7 (812) 295-00-28\n'
                                            '•	st. Kantemirovskaya, д. 24\n'
                                            'Group on VKontakte – vk.com/spbstu_11\n'
                                            'Head of the hostel – Медведева Людмила Алексеевна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №12': 'Directorate:\n'
                                            '•	dorm12@spbstu.ru\n'
                                            '•	+7 (812) 534-47-86\n'
                                            '•	st. Khlopin, д. 13, build. 1\n'
                                            'Group on VKontakte – vk.com/spbstu_12\n'
                                            'Head of the hostel – Пескова Ирина Викторовна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №14а': 'Directorate:\n'
                                             '•	dorm14a@spbstu.ru\n'
                                             '•	+7 (812) 596-26-67\n'
                                             '•	pl. Nepokobornye, д. 8, build.2\n'
                                             'Group on VKontakte – vk.com/spbstu__14a\n'
                                             'Head of the hostel – Константинова Лариса Юрьевна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №14б': 'Directorate:\n'
                                             '•	dorm14b@spbstu.ru\n'
                                             '•	+7 (812) 596-29-32\n'
                                             '•	pl. Nepokobornye, д. 8, build.2\n'
                                             'Group on VKontakte – vk.com/spbstu_14b\n'
                                             'Head of the hostel – Воронцова Ирина Петровна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №14ц': 'Directorate:\n'
                                             '•	dorm14c@spbstu.ru\n'
                                             '•	+7 (812) 534-48-93\n'
                                             '•	pl. Nepokobornye, д. 8, build.2\n'
                                             'Group on VKontakte – vk.com/spbstu_14c\n'
                                             'Head of the hostel – Солнцева Ирина Викторовна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №17': 'Directorate:\n'
                                            '•	dorm17@spbstu.ru\n'
                                            '•	+7 (812) 555-23-32\n'
                                            '•	st. Vavilovs, д.10, build. 2\n'
                                            'Group on VKontakte – vk.com/spbstu_17\n'
                                            'Head of the hostel – Назаревская Марина Викторовна\n',
    DORM_SHORT[V_ENGLISH].lower() + ' №18': 'Directorate:\n'
                                            '•	dorm18@spbstu.ru\n'
                                            '•	+7 (812) 555-76-97\n'
                                            '•	st. Vavilovs, д.10, build. 3\n'
                                            'Group on VKontakte – vk.com/spbstu_18\n'
                                            'Head of the hostel – Емельнова Юлия Геннадьевна\n',

    DORM_SHORT[V_CHINESE].lower() + ' №1': 'no_answer №1',
    DORM_SHORT[V_CHINESE].lower() + ' №3': 'no_answer №3',
    DORM_SHORT[V_CHINESE].lower() + ' №4': 'no_answer №4',
    DORM_SHORT[V_CHINESE].lower() + ' №4а': 'no_answer №4',
    DORM_SHORT[V_CHINESE].lower() + ' №5': 'no_answer №5',
    DORM_SHORT[V_CHINESE].lower() + ' №6': 'no_answer №6',
    DORM_SHORT[V_CHINESE].lower() + ' №7': 'no_answer №7',
    DORM_SHORT[V_CHINESE].lower() + ' №8': 'no_answer №8',
    DORM_SHORT[V_CHINESE].lower() + ' №10': 'no_answer №1',
    DORM_SHORT[V_CHINESE].lower() + ' №11': 'no_answer №1',
    DORM_SHORT[V_CHINESE].lower() + ' №12': 'no_answer №1',
    DORM_SHORT[V_CHINESE].lower() + ' №14а': 'no_answer №1',
    DORM_SHORT[V_CHINESE].lower() + ' №14б': 'no_answer №1',
    DORM_SHORT[V_CHINESE].lower() + ' №14ц': 'no_answer №1',
    DORM_SHORT[V_CHINESE].lower() + ' №17': 'no_answer №1',
    DORM_SHORT[V_CHINESE].lower() + ' №18': 'no_answer №1',

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
                                           '•	pl. Civilian, д. 30\n'
                                           'Group on VKontakte – vk.com/spbstu_13\n'
                                           'Head of the hostel – Кургут Наталья Юрьевна\n',
    DORM_LONG[V_ENGLISH].lower() + ' №15': 'Directorate:\n'
                                           '•	dorm15@spbstu.ru\n'
                                           '•	+7 (812) 534-03-58\n'
                                           '•	Civilian pl., д. 28\n'
                                           'Head of the hostel – Седакова Екатерина Валерьевна\n',
    DORM_LONG[V_ENGLISH].lower() + ' №16': 'Directorate:\n'
                                           '•	dorm16@spbstu.ru\n'
                                           '•	+7 (812) 517-87-66\n'
                                           '•	pl. Engels, д. 129, корп. 4\n'
                                           'Group on VKontakte – vk.com/spbstu_16\n'
                                           'Head of the hostel – Пипия Отари Силованович\n',
    DORM_LONG[V_ENGLISH].lower() + ' №19': 'Directorate:\n'
                                           '•	dorm19@spbstu.ru\n'
                                           '•	+7 (812) 373-67-96\n'
                                           '•	st. Gastello, д.20\n'
                                           'Group on VKontakte – vk.com/spbstu_19\n'
                                           'Head of the hostel – Бойко Оксана Валентиновна\n',
    DORM_LONG[V_ENGLISH].lower() + ' №20': 'Directorate:\n'
                                           '•	dorm20@spbstu.ru\n'
                                           '•	+7 (812) 316-55-08\n'
                                           '•	Malodetskoselsky pl., 27\n'
                                           'Group on VKontakte – vk.com/spbstu_20\n'
                                           'Head of the hostel – Лошкарева Ольга Евгеньевна\n',

    DORM_LONG[V_CHINESE].lower() + ' №13': 'no_answer №13',
    DORM_LONG[V_CHINESE].lower() + ' №15': 'no_answer №15',
    DORM_LONG[V_CHINESE].lower() + ' №16': 'no_answer №16',
    DORM_LONG[V_CHINESE].lower() + ' №19': 'no_answer №19',
    DORM_LONG[V_CHINESE].lower() + ' №20': 'no_answer №20',

    CHECK_IN_RULES[V_RUSSIAN].lower(): 'Для поселения в общежитие абитуриентам необходимо:'
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
    CHECK_IN_RULES[V_ENGLISH].lower(): 'no_answer',
    CHECK_IN_RULES[V_CHINESE].lower(): 'no_answer',

    ORDER_PASSAGE_PUBLIC[V_RUSSIAN].lower(): 'Вход в общежитие осуществляется по единому именному пропуску Политеха, '
                                             'который получает каждый студент при поступлении в вуз. Вход и выход для '
                                             'студента, проживающего в общежитии осуществляется круглосуточно. За '
                                             'соблюдением режима следят сотрудники службы безопасности и камеры '
                                             'наблюдения.\n '
                                             'Гостей можно проводить с собой по будням с 14:00 до 22:00, по выходным '
                                             'с 10:00 до 22:00. Гости должны покинуть общагу до 23:00. На время '
                                             'пандемии гостей не пускают:(',
    ORDER_PASSAGE_PUBLIC[V_ENGLISH].lower(): 'no_answer',
    ORDER_PASSAGE_PUBLIC[V_CHINESE].lower(): 'no_answer',

    RESIDENTS_RIGHTS[V_RUSSIAN].lower(): 'Проживающие в общежитии, имеют право:\n'
                                         '1.	Переселиться из одной жилой комнаты в другую после согласования с '
                                         'администрацией общежития;\n'
                                         '2.	Пользоваться помещениями для самостоятельных занятий и помещениями '
                                         'культурно-бытового назначения, оборудованием, инвентарем общежития;\n'
                                         '3.	Обращаться к администрации общежития с просьбами о своевременном '
                                         'ремонте, замене оборудования и инвентаря;\n'
                                         '4.	Участвовать в формировании студенческого совета общежития и быть '
                                         'избранным в его состав, участвовать через совет в решении вопросов '
                                         'общежития;\n'
                                         '5.	Пользоваться бытовой техникой при условии соблюдения правил ее '
                                         'эксплуатации и правил пожарной безопасности.',
    RESIDENTS_RIGHTS[V_ENGLISH].lower(): 'no_answer',
    RESIDENTS_RIGHTS[V_CHINESE].lower(): 'no_answer',

    DUTY_OF_RESIDENTS[
        V_RUSSIAN].lower(): 'Общежитие живет по правилам внутреннего распорядка. В них нет ничего сложного, достаточно делать то, чего от тебя ждут:\n'
                            '1.	Не курить и не употреблять алкоголь/наркотики на территории университета (в том числе и общежития);\n'
                            '2.	Не мусорить в местах общего пользования: на кухне, в коридорах, в умывалках, в туалетах. Бережно относиться к общему имуществу;\n'
                            '3.	Вовремя убираться в своей комнате, не запускать ее. В общежитии действует санитарная комиссия, которая следит за чистотой в комнатах;\n'
                            '4.	Не проводить незнакомцев в общежитие. Проводить знакомых только в отведенное время;\n'
                            '5.	Соблюдать режим тишины: не шуметь по ночам и рано утром.\n',
    DUTY_OF_RESIDENTS[V_ENGLISH].lower(): 'no_answer',
    DUTY_OF_RESIDENTS[V_CHINESE].lower(): 'no_answer',

    DUTY_OF_ADMIN[V_RUSSIAN].lower(): 'Администрация студенческого общежития обязана:\n'
                                      '1.	Обеспечить предоставление документов для регистрации проживающих по месту пребывания;\n'
                                      '2.	Содержать помещения общежитий в соответствии с установленными санитарными правилами;\n'
                                      '3.	Укомплектовывать общежития мебелью, оборудованием, постельными принадлежностями и другим инвентарем;\n'
                                      '4.	Обеспечить проведение текущего ремонта общежитий, инвентаря, оборудования, содержать в надлежащем порядке закрепленную за Студгородком территорию, зеленые насаждения;\n'
                                      '5.	Оперативно устранять неисправности в системах канализации, электроснабжения водоснабжения общежитий;\n'
                                      '6.	Обеспечить предоставление проживающим в общежитиях необходимых помещений для самостоятельных занятий, комнат отдыха, бытовых помещений;\n'
                                      '7.	В случае заболевания несовершеннолетних проживающих переселять их в другое изолированное помещение по рекомендации лечащего врача;\n'
                                      '8.	Обеспечить ежедневный обход всех помещений общежитий их заведующими и работниками соответствующих эксплуатационных служб с целью выявления недостатков по их эксплуатации и санитарному содержанию и принимать меры по их устранению;\n'
                                      '9.	Предоставить проживающим в общежитии право пользоваться бытовой техникой и аппаратурой при условии соблюдения ими техники безопасности и инструкций по пользованию бытовыми электроприборами;\n'
                                      '10.	Содействовать работе студенческих советов по вопросам улучшения условий проживания, быта и отдыха проживающих;\n'
                                      '11.	Принимать меры по реализации предложений проживающих, информировать их о принятых решениях;\n'
                                      '12.	Обеспечивать проживающих необходимым оборудованием, инвентарем, инструментом и материалами для проведения на добровольной основе работ по уборке общежитий и закрепленной за Студгородком территории;\n'
                                      '13.	Обеспечивать противопожарную и общественную безопасность проживающих в общежитиях и персонала.\n',
    DUTY_OF_ADMIN[V_ENGLISH].lower(): 'no_answer',
    DUTY_OF_ADMIN[V_CHINESE].lower(): 'no_answer',

    BODIES_OF_MANAGEMENT[V_RUSSIAN].lower(): 'В каждом общежитии проживающими избирается орган самоуправления – '
                                             'студенческий совет общежития. В каждом блоке общежития Студгородка '
                                             'избирается староста. Староста блока следит за бережным отношением '
                                             'проживающих к имуществу и оборудованию, организует и контролирует '
                                             'работы по содержанию блока в чистоте и порядке. Студсовет общежития '
                                             'руководит работой старост, организует работу по привлечению в '
                                             'добровольном порядке проживающих к выполнению общественно-полезных '
                                             'работ в общежитии Студгородка (уборка и ремонт жилых комнат, '
                                             'мелкий ремонт мебели) и на прилегающей территории, '
                                             'помогает администрации в организации контроля за соблюдением настоящих '
                                             'правил и сохранностью материальных ценностей, закрепленных за '
                                             'проживающими, организует проведение культурно-массовой работы в '
                                             'общежитии. Студсовет совместно с администрацией общежития в пределах '
                                             'своих полномочий участвует в расселении студентов нового приема, '
                                             'распределении новой мебели и оборудования между проживающими, '
                                             'сохранность закрепленной жилой площади. Для координации работы во всех '
                                             'общежитиях Студгородка есть Объединенный студенческий совет общежитий, '
                                             'в состав которого включаются все председатели Студсоветов общежитий, '
                                             'представители профсоюзной организации студентов, других общественных '
                                             'студенческих организаций, администрации СПбПУ.',
    BODIES_OF_MANAGEMENT[V_ENGLISH].lower(): 'no_answer',
    BODIES_OF_MANAGEMENT[V_CHINESE].lower(): 'no_answer',

    RESPONSIBILITY_BREAKING_RULES[V_RUSSIAN].lower(): 'За соблюдением правил следит администрация, студенческий '
                                                      'совет, а также служба безопасности студгородка. По заявлению '
                                                      'любого из этих органов со студента могут потребовать '
                                                      'объяснительную и применить один из методов дисциплинарного '
                                                      'взыскания: замечание, выговор, отчисление из университета. При '
                                                      'этом, если у студента будет три выговора, то его автоматически '
                                                      'отчислят из университета.',
    RESPONSIBILITY_BREAKING_RULES[V_ENGLISH].lower(): 'no_answer',
    RESPONSIBILITY_BREAKING_RULES[V_CHINESE].lower(): 'no_answer',

    NEIGHBORS[
        V_RUSSIAN].lower(): 'Ты только что приехал в общагу, заселился. На пороге появились твои соседи. Пора определяться, как следить за порядком, кто прибирается и выносит мусор, как делить бытовую технику. Вот несколько советов.\n'
                            'В первые месяцы жизни студенты часто покупают вещи в комнату для совместного использования. Многие покупают технику совместно с соседями. Но жизнь в общежитии на самом деле непредсказуема. Вы можете переехать в другую комнату или общежитие.\n'
                            'Наш совет: пусть каждый купит что-то в комнату сам. Тогда при неожиданных ситуациях вы сможете забрать технику себе или перепродать ее. Это поможет избежать конфликтов с соседями.\n'
                            'Если именно тебе необходим фен, утюг, мультиварка и т.д., то ты можешь этим пользоваться как индивидуально (это же твои вещи) или просить/делиться с соседями по комнате.\n'
                            'Между соседями часто возникают конфликты при выполнении тех или иных обязанностей. Поэтому обрати внимание на следующие советы:\n'
                            '•	Уборка. Составьте график уборки, определите последовательность и периодичность уборки. Определите, что будет входить в обязанности дежурного. Например, подмести и вымыть пол, вытереть пыль с бытовых приборов.\n'
                            '•	Вынос мусора. Мусор необходимо выносить каждый день. Скопление в мусорном ведре пищевых отходов влечет за собой неприятный запах в комнате, а еще появляются тараканы. \n'
                            'Договоритесь, кто за кем выносит мусор. Прикрепите на дверь график дежурств и выноса мусора. Это поможет соблюдать порядок и дисциплину в комнате.\n'
                            'У каждого человека свои особенности питания. Поэтому важно уважать вкусовые предпочтения соседа, если даже он каждый вечер заваривает лапшу быстрого приготовления.\n'
                            'Многие в самом начале жизни в общаге стараются покупать продукты и готовить вместе. Но вскоре это становится неудобным из-за расписания или пожелания в еде. Поэтому мы рекомендуем избегать конфликтов по поводу количества съеденного и питаться отдельно. Но никто не запрещает угощать соседей своим фирменным блюдом.\n',
    NEIGHBORS[V_ENGLISH].lower(): 'no_answer',
    NEIGHBORS[V_CHINESE].lower(): 'no_answer',

    ADMINISTRATION[
        V_RUSSIAN].lower(): 'Не ссорьтесь с ней, здоровайтесь при встрече, участвуйте в жизни общежития, платите вовремя и у вас будут отличные отношения с администрацией. Проверено:)\n',
    ADMINISTRATION[V_ENGLISH].lower(): 'no_answer',
    ADMINISTRATION[V_CHINESE].lower(): 'no_answer',

    COCKROACHES[
        V_RUSSIAN].lower(): 'В общежитии в некоторых комнатах много тараканов, а где-то их вовсе нет. Какие простые правила стоит соблюдать, чтобы избежать встречи с тараканами?\n'
                            'Не стоит засорять комнату. Это грозит не только появлением проблем с санитарной комиссией общежития, но и скоплением тараканов в вашей комнате.\n'
                            '•	Посуда. Мойте посуду сразу после еды. Не оставляйте продукты в открытом виде.\n'
                            '•	Хранение продуктов. Заранее продумайте, как хранить сыпучие сухие изделия (макароны, крупы). Рекомендуем приобрести контейнеры для каждой крупы отдельно. Так же стоит купить большую пластиковую коробку для всех контейнеров поменьше. Кроме того, можно покупать коробки с крупами, в которых предусмотрено плотное закрытие.\n'
                            '•	Уборка. Необходимо протирать пыль, проветривать комнату.\n'
                            '•	Чистый пол — залог порядка, поэтому мойте полы раз в неделю или чаще. Тараканы могут прятаться в стопке бумаг и мусора, поэтому все ненужное необходимо выкидывать, поддерживать чистоту. Разбирайте шкафы и наводите порядок.\n'
                            '•	Подрядчик. В общежитии можно заказать травлю тараканов/клопов. Для этого нужно оставить заявку на вахте. Если потравили тараканов плохо, то необходимо сообщить Студсовету или администрации общежития.\n'
                            'Тараканы не любят, когда их беспокоят и часто они поселяются там, куда вы реже всего заглядываете, особенно если там тепло или влажно. Часто тараканов можно встретить за холодильником, в точке доступа Wi-Fi или под чайником.\n'
                            'Вообще, тараканам очень важна вода, поэтому лучше нигде не оставлять воду в открытом виде — кружки, тарелки после мытья. Если надолго уезжаете, то лучше слить воду из чайника и фильтра.\n'
                            'экономить и покупать самые дешевые средства, обычно они оказываются бесполезными. Стоит брать известные, марки такие как «Машенька», «Дохлокс», «Раптор», «Комбат» и др... Их можно найти в любом магазине за приемлемую цену.\n'
                            '•	Если вы только заехали в общагу и у вас еще нет мебели, то стоит промазать гелем плинтус.\n'
                            '•	Рекомендуем раз в месяц обрабатывать зону под холодильником и кухонным шкафом. Это самое любимое место тараканов. При возможности отодвигайте холодильники и шкафы.\n'
                            '•	Приобретите ловушки и разложите по всей комнате. Не забудьте зоны батареи, под кроватью и столом, холодильником. Ловушки необходимо менять раз в три-шесть месяцев.\n'
                            '•	Если тараканы завелись в тумбочке, то стоит разобрать ее полностью и обработать.\n'
                            'В нашем общежитии предоставляется услуга химической обработки от тараканов. Чтобы на нее записаться, нужно прийти на вахту и попросить записать комнату на данную процедуру. Обычно дезинсектор приходит в конце месяца рано утром, так что будьте готовы и заранее подумайте, что именно вам нужно обработать. Сама обработка занимает не больше 5 минут, но после лучше уйти из комнаты на 2-3 часа.\n'
                            'В случае плохой травли — сообщите Студсовету или администрации общежития.\n'
                            'Кроме того, можно вызвать ту службу дезинсекции, которая вам приглянется.\n',
    COCKROACHES[V_ENGLISH].lower(): 'no_answer',
    COCKROACHES[V_CHINESE].lower(): 'no_answer',

    WHAT_TO_TAKE_WITH_YOU[V_RUSSIAN].lower(): 'Да хрен его знает, купить можно все на месте кекв',
    WHAT_TO_TAKE_WITH_YOU[V_ENGLISH].lower(): 'no_answer',
    WHAT_TO_TAKE_WITH_YOU[V_CHINESE].lower(): 'no_answer',

    WHAT_TO_BUY_LOCALLY[V_RUSSIAN].lower(): 'Вот, что вам может понадобиться:\n'
                                            '•	холодильник\n'
                                            '•	чайник\n'
                                            '•	точка доступа в интернет\n'
                                            '•	микроволновка\n'
                                            '•	ведро и швабра, веник и совок\n'
                                            '•	тряпки\n'
                                            '•	моющие средства (для пола, окон, посуды) \n'
                                            '•	губки для посуды \n'
                                            '•	мусорные мешки\n'
                                            '•	столовые принадлежности (ложка, вилка, нож) \n'
                                            '•	кружки (к тебе могут прийти гости)\n'
                                            '•	сковорода\n'
                                            '•	кастрюля \n'
                                            '•	другое: терка, венчик, дуршлаг — все это на твое усмотрение и личный вкус. \n'
                                            'Стиральные машины, сушилки, плиты, спортинвентарь есть в каждом общежитие, так что беспокоиться о их отсутствии не придется.\n',
    WHAT_TO_BUY_LOCALLY[V_ENGLISH].lower(): 'no_answer',
    WHAT_TO_BUY_LOCALLY[V_CHINESE].lower(): 'no_answer'
}
