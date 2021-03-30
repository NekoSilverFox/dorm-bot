# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 12:48
# @Author  : Meng Jianing
# @FileName: questions_answers.py
# @Software: PyCharm
# @Versions: v1.0
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
    CLUB[V_ENGLISH].lower(): 'The Student Club is the oldest student recreational activity at Polytechnic University, '
                             'which has been helping students develop and realize their creative potential for over '
                             '85 years. The range of activities of the Student Club is wide: students have the '
                             'opportunity to engage in acting, music, dance, digital design, as well as to '
                             'participate in the organization of events. If you are interested, you can visit the '
                             'Student Club group in VKontakte for more information: vk.com/poly_studklub',
    CLUB[V_CHINESE].lower(): '学生会是理工大学历史最悠久的学生休闲活动，85年来一直帮助学生开发和发挥他们的创造潜能。'
                             '学生俱乐部的活动范围很广：学生有机会参与表演、音乐、舞蹈、数码设计，以及参与组织活动。如果你有兴趣，'
                             '我们建议你去VKontakte的学生俱乐部组了解更多信息：vk.com/poly_studklub',

    ONLINE_COURSE[V_RUSSIAN].lower(): 'Go!',
    ONLINE_COURSE[V_ENGLISH].lower(): 'Go!',
    ONLINE_COURSE[V_CHINESE].lower(): 'Go!',

    NEXT[V_RUSSIAN].lower(): 'Далее',
    NEXT[V_ENGLISH].lower(): 'Next',
    NEXT[V_CHINESE].lower(): '下一页',

    MANAGEMENT_CONTACTS[V_RUSSIAN].lower(): 'Директор Студгородка – Шнейдер Анатолий Альбертович:\n'
                                            '•	uprstg@spbstu.ru\n'
                                            '•	+7 (812) 290-95-02\n'
                                            '•	пр. Непокорённых, д.8, корп.2, общ. №14б\n\n'
                                            'Городская Служба Заселения Студентов:\n'
                                            '•	+7 (981) 805-32-40',
    MANAGEMENT_CONTACTS[V_ENGLISH].lower(): 'Campus Director – Шнейдер Анатолий Альбертович:\n'
                                            '•	uprstg@spbstu.ru\n'
                                            '•	+7 (812) 290-95-02\n'
                                            '•	pl. Nepokoryonye, d.8, build.2, dorm. №14б\n\n'
                                            'City Student Accommodation Service:\n'
                                            '•	+7 (981) 805-32-40',
    MANAGEMENT_CONTACTS[V_CHINESE].lower(): '校园主任 – Шнейдер Анатолий Альбертович:\n'
                                            '•	uprstg@spbstu.ru\n'
                                            '•	+7 (812) 290-95-02\n'
                                            '•	pl. Nepokoryonye, 街道号:8, 2号楼, 宿舍№14б\n\n'
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
                                        '•	Лесной пр., д.67, корп.2, общ.№7',
    LESNOY_PROSPECT[V_ENGLISH].lower(): 'Chief of complex - Ядрышников Александр Аркадьевич:\n'
                                        '•	aayadrishnikov@spbstu.ru\n'
                                        '•	Lesnoy pl., d.67, build.2, dorm.№7',
    LESNOY_PROSPECT[V_CHINESE].lower(): '复杂事务主管 - Ядрышников Александр Аркадьевич:\n'
                                        '•	aayadrishnikov@spbstu.ru\n'
                                        '•	森林大街, 67号, 2号楼, 宿舍№7',

    COURAGE_SQUARE[V_RUSSIAN].lower(): 'Начальник комплекса - Короткова Руфина Рауфовна:\n'
                                       '•	rrkorotkova@spbstu.ru\n'
                                       '•	+7 (812) 290-97-12\n'
                                       '•	пр. Непокорённых, д.8, корп.2, общ. №14б\n',
    COURAGE_SQUARE[V_ENGLISH].lower(): 'Chief of complex - Короткова Руфина Рауфовна:\n'
                                       '•	rrkorotkova@spbstu.ru\n'
                                       '•	+7 (812) 290-97-12\n'
                                       '•	pl. Nepokornykh, d.8, build.2, dorm.№14б\n',
    COURAGE_SQUARE[V_CHINESE].lower(): '复杂事务主管 - Короткова Руфина Рауфовна:\n'
                                       '•	rrkorotkova@spbstu.ru\n'
                                       '•	+7 (812) 290-97-12\n'
                                       '•	Nepokornykh街, 8号, 2号楼, 宿舍№14б\n',

    CIVIL_PROSPECT[V_RUSSIAN].lower(): 'Начальник комплекса - Никулин Алексей Николаевич:\n'
                                       '•	nikulin@spbstu.ru\n'
                                       '•	+7 (812) 322-01-38\n'
                                       '•	Гражданский пр., д.28, кабинет 114\n',
    CIVIL_PROSPECT[V_ENGLISH].lower(): 'Chief of complex - Никулин Алексей Николаевич:\n'
                                       '•	nikulin@spbstu.ru\n'
                                       '•	+7 (812) 322-01-38\n'
                                       '•	Grazhdansky Ave., d.28, office 114\n',
    CIVIL_PROSPECT[V_CHINESE].lower(): '复杂事务主管 - Никулин Алексей Николаевич:\n'
                                       '•	nikulin@spbstu.ru\n'
                                       '•	+7 (812) 322-01-38\n'
                                       '•	公民大街, д.28, 办公室114\n',

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
                                         '•	avenue. 65 Engelsa House, Letter A\n\n'
                                         'Head - Murtazina Marina Vyacheslavovna\n'
                                         'Complex of additional services for residents\n'
                                         'Chief of complex - Рублева Юлия Аркадьевна:\n'
                                         '•	rubleva@spbstu.ru\n'
                                         '•	+7 (812) 534-13-68\n'
                                         '•	+7 (812) 606-62-38\n'
                                         '•	28 Grazhdansky Ave., office 104\n\n'
                                         'Senior Complex Administrator - Белаш Лилия Анатольевна:\n'
                                         '•	hotel@spbstu.ru\n'
                                         '•	+7 (812) 534-13-68\n'
                                         '•	 Grazhdansky Ave. 28\n\n'
                                         'Evening and weekend room reservations phone numbers:\n'
                                         '•	+7 (812) 321-61-00 (Grazhdansky Ave. 28)\n'
                                         '•	+7 (812) 295-36-37 (Lesnoy Ave. 65/1 and 67/2)\n\n'
                                         'Superior rooms in dormitories:\n'
                                         '•	№1 emergency phone: +7 (812) 295-36-37\n'
                                         '•	№7 emergency phone: +7 (921) 561-13-29\n'
                                         '•	№8 emergency phone: +7 (812) 297-43-50\n'
                                         '•	№15 emergency phone: +7 (812) 321-61-00\n',
    SCIENCE_POLYTECH[V_CHINESE].lower(): '管理局:\n'
                                         '•	+7 (812) 553-00-00\n'
                                         '•	+7 (812) 293-84-55\n'
                                         '•	大道 65 Engelsa Str., Letter A\n\n'
                                         '经理 - Муртазина Марина Вячеславовна\n'
                                         '额外的居民服务配套\n'
                                         '复杂事务主任 - Рублева Юлия Аркадьевна:\n'
                                         '•	rubleva@spbstu.ru\n'
                                         '•	+7 (812) 534-13-68\n'
                                         '•	+7 (812) 606-62-38\n'
                                         '•	公民大街, 28号, 办公室104\n\n'
                                         '综合楼高级管理员 - Белаш Лилия Анатольевна:\n'
                                         '•	hotel@spbstu.ru\n'
                                         '•	+7 (812) 534-13-68\n'
                                         '•	公民大街, 28号\n\n'
                                         '晚上和周末的房间预订电话:\n'
                                         '•	+7 (812) 321-61-00 (公民大街, 28号)\n'
                                         '•	+7 (812) 295-36-37 (森林大街, 65/1号 和 67/2号)\n\n'
                                         '宿舍的高级客房:\n'
                                         '•	№1 紧急电话: +7 (812) 295-36-37\n'
                                         '•	№7 紧急电话: +7 (921) 561-13-29\n'
                                         '•	№8 紧急电话: +7 (812) 297-43-50\n'
                                         '•	№15 紧急电话: +7 (812) 321-61-00\n',

    COMPLEX_FOR_FURTHER_EDUCATION[V_RUSSIAN].lower(): 'Комплекс дополнительного обслуживания проживающих',
    COMPLEX_FOR_FURTHER_EDUCATION[V_ENGLISH].lower(): 'Complex of additional services for residents',
    COMPLEX_FOR_FURTHER_EDUCATION[V_CHINESE].lower(): '额外的居民服务配套',

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
    PAYMENT[
        V_ENGLISH].lower(): 'When you move into a dormitory, you sign a rental agreement, for which you have to pay '
                            'around 1000 rubles per month.\n '
                            'The price depends on the number of people in the room, for "sealing" a little less.\n'
                            'The price for the dormitory in winter and summer is slightly different. The current cost '
                            'you can find out at the information booth in the dormitory.\n '
                            'You can pay at any bank in the city (Sberbank, St. Petersburg) or pay.spbstu.ru. After '
                            'you pay according to the requisites it is also necessary to show the receipt of payment '
                            'to the administration of the hostel.\n '
                            'The administration of the campus may summon the student to his/her house in case of debt '
                            'over 3000 rubles, and in case of repeated violations he/she can be reprimanded.\n '
                            'It is possible to pay for several months in advance',
    PAYMENT[V_CHINESE].lower(): '当你搬进宿舍时，你要签订一份租房协议，每月要支付1000卢布左右。\n'
                                '价格要看房间里的人数，对于 "紧凑 "一点的。\n'
                                '冬夏两季的民宿价格略有不同。目前的费用你可以在宿舍的信息台了解。\n'
                                '可以在市内银行（Sberbank, SPB）或pay.spbstu.ru上按要求付款。在按照要求付款后，必须向宿舍管理部门出示付款收据。\n'
                                '假如欠债超越3000卢布，校园管理部门可将学生传唤到其家中，如屡次违背，可给予训诫。\n'
                                '可以提前几个月付款',

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

    DORM_SHORT[V_CHINESE].lower() + ' №1': '管理局:\n'
                                           '•	dorm1@spbstu.ru\n'
                                           '•	+7 (812) 775 05 30 #1444\n'
                                           '•	+7 (812) 775 05 30 #1445\n'
                                           '•	森林大街, 街道号: 65, 楼号:1\n'
                                           'VK群 – vk.com/spbstu_1\n'
                                           '宿舍负责人 – Шевченко Ольга Николаевна',
    DORM_SHORT[V_CHINESE].lower() + ' №3': '管理局:\n'
                                           '•	dorm3@spbstu.ru\n'
                                           '•	+7 (812) 775 05 30 #1448\n'
                                           '•	森林大街, 街道号: 65, 楼号: 3\n'
                                           'VK群 – vk.com/spbstu_3\n'
                                           '宿舍负责人 – Киреева Наталья Викторовна',
    DORM_SHORT[V_CHINESE].lower() + ' №4': '管理局:\n'
                                           '•	dorm4@spbstu.ru\n'
                                           '•	+7 (812) 775 05 30 #1451\n'
                                           '•	Pargolovskaya路, 街道号:11, 楼号:1\n'
                                           'VK群 – vk.com/spbstu_4\n'
                                           '宿舍负责人 – Мартынова Лариса Яковлевна',
    DORM_SHORT[V_CHINESE].lower() + ' №4а': '管理局:\n'
                                            '•	dorm4a@spbstu.ru\n'
                                            '•	+7 (812) 775 05 30 #1453\n'
                                            '•	Pargolovskaya路, 街道号:11, 楼号:1\n'
                                            'VK群 – vk.com/spbstu_4aa\n'
                                            '宿舍负责人 – Гулева Ирианда Анатольевна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №5': '管理局:\n'
                                           '•	dorm5@spbstu.ru\n'
                                           '•	+7 (812) 295-47-25\n'
                                           '•	Pargolovskaya路, 街道号:11, 楼号:2\n'
                                           'VK群 – vk.com/spbstu_5a | vk.com/spbstu_5b\n'
                                           '宿舍负责人 – Мартьянова Милена Леонидовна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №6': '管理局:\n'
                                           '•	dorm6m@spbstu.ru\n'
                                           '•	+7 (812) 295-27-50\n'
                                           '•	Kharchenko路, 街道号: 16\n'
                                           'VK群 – vk.com/spbstu_6\n'
                                           '宿舍负责人 – Егорова Ольга Адамовна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №7': '管理局:\n'
                                           '•	dorm7@spbstu.ru\n'
                                           '•	+7 (812) 775-05-30 #1442\n'
                                           '•	+7 (812) 775-05-30 #1443\n'
                                           '•	森林大街, 街道号:67, 楼号:2\n'
                                           '宿舍负责人 – Кривошея Гульнара Куртвелиевна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №8': '管理局:\n'
                                           '•	dorm8@spbstu.ru\n'
                                           '•	+7 (812) 297-43-50\n'
                                           '•	Khlopin街, 街道号:9, 楼号:2\n'
                                           'VK群 – vk.com/spbstu_8\n'
                                           '宿舍负责人 – Бернанс Ольга Ивановна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №10': '管理局:\n'
                                            '•	dorm10@spbstu.ru\n'
                                            '•	+7 (812) 297-16-78\n'
                                            '•	Nekonkorniye街, 街道号: 6, 楼号:2\n'
                                            'VK群 – vk.com/spbstu_10\n'
                                            '宿舍负责人 – Текучева Елена Ивановна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №11': '管理局:\n'
                                            '•	dorm11@spbstu.ru\n'
                                            '•	+7 (812) 295-00-28\n'
                                            '•	ул. Кантемировская, 街道号: 24\n'
                                            'VK群 – vk.com/spbstu_11\n'
                                            '宿舍负责人 – Медведева Людмила Алексеевна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №12': '管理局:\n'
                                            '•	dorm12@spbstu.ru\n'
                                            '•	+7 (812) 534-47-86\n'
                                            '•	Khlopin街, 街道号: 13, 楼号: 1\n'
                                            'VK群 – vk.com/spbstu_12\n'
                                            '宿舍负责人 – Пескова Ирина Викторовна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №14а': '管理局:\n'
                                             '•	dorm14a@spbstu.ru\n'
                                             '•	+7 (812) 596-26-67\n'
                                             '•	Nekonkorniye街, 街道号: 8, 楼号:2\n'
                                             'VK群 – vk.com/spbstu__14a\n'
                                             '宿舍负责人 – Константинова Лариса Юрьевна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №14б': '管理局:\n'
                                             '•	dorm14b@spbstu.ru\n'
                                             '•	+7 (812) 596-29-32\n'
                                             '•	Nekonkorniye街, 街道号: 8, 楼号:2\n'
                                             'VK群 – vk.com/spbstu_14b\n'
                                             '宿舍负责人 – Воронцова Ирина Петровна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №14ц': '管理局:\n'
                                             '•	dorm14c@spbstu.ru\n'
                                             '•	+7 (812) 534-48-93\n'
                                             '•	Nekonkorniye街, 街道号: 8, 楼号:2\n'
                                             'VK群 – vk.com/spbstu_14c\n'
                                             '宿舍负责人 – Солнцева Ирина Викторовна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №17': '管理局:\n'
                                            '•	dorm17@spbstu.ru\n'
                                            '•	+7 (812) 555-23-32\n'
                                            '•	Vavilovs路, 街道号:10, 楼号: 2\n'
                                            'VK群 – vk.com/spbstu_17\n'
                                            '宿舍负责人 – Назаревская Марина Викторовна\n',
    DORM_SHORT[V_CHINESE].lower() + ' №18': '管理局:\n'
                                            '•	dorm18@spbstu.ru\n'
                                            '•	+7 (812) 555-76-97\n'
                                            '•	Vavilovs路, 街道号:10, 楼号: 3\n'
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

    DORM_LONG[V_CHINESE].lower() + ' №13': '管理局:\n'
                                           '• dorm13@spbstu.ru\n'
                                           '• +7 (812) 534-46-65\n'
                                           '• 公民大街, 街道号:30\n'
                                           'VK群 – vk.com/spbstu_13\n'
                                           '宿舍负责人 – Кургут Наталья Юрьевна\n',
    DORM_LONG[V_CHINESE].lower() + ' №15': '管理局:\n'
                                           '• dorm15@spbstu.ru\n'
                                           '• +7 (812) 534-03-58\n'
                                           '• 公民大街, 街道号:28\n'
                                           '宿舍负责人 – Седакова Екатерина Валерьевна\n',
    DORM_LONG[V_CHINESE].lower() + ' №16': '管理局:\n'
                                           '• dorm16@spbstu.ru\n'
                                           '• +7 (812) 517-87-66\n'
                                           '• Engelsa街, 街道号:129, корп. 4\n'
                                           'VK群 – vk.com/spbstu_16\n'
                                           '宿舍负责人 – Пипия Отари Силованович\n',
    DORM_LONG[V_CHINESE].lower() + ' №19': '管理局:\n'
                                           '• dorm19@spbstu.ru\n'
                                           '• +7 (812) 373-67-96\n'
                                           '• Gastello街, 街道号:20\n'
                                           'VK群 – vk.com/spbstu_19\n'
                                           '宿舍负责人 – Бойко Оксана Валентиновна\n',
    DORM_LONG[V_CHINESE].lower() + ' №20': '管理局:\n'
                                           '• dorm20@spbstu.ru\n'
                                           '• +7 (812) 316-55-08\n'
                                           '• Malodetskoselsky街, 27\n'
                                           'VK群 – vk.com/spbstu_20\n'
                                           '宿舍负责人 – Лошкарева Ольга Евгеньевна\n',

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
    CHECK_IN_RULES[V_ENGLISH].lower(): 'To be placed in a dormitory, applicants must:\n'
                                       '- Receive a referral from the Admissions Committee;\n'
                                       '- Have a document proving your identity;\n'
                                       '- To have the medical certificate of form 086у with obligatory mark about fluorographic examination or the separate certificate about fluorographic examination;\n'
                                       '- The entrants who have not reached the age of 18 and arrived without parents or other legal representatives for more than three days, it is necessary to have the notarized consent of parents (one of parents) or other legal representatives for the actions connected with settlement and registration. The document must specify the type of action for which consent is given: "I, (full name), give permission to register at the place of stay and residence of my minor son (daughter)(passport data and data of the birth certificate) in the dormitory of the Federal State Educational Institution of Higher Education "Saint-Petersburg Peter the Great University" for the period of admission tests or for the period of study at the above mentioned university";\n'
                                       '- When you move in also need to issue a temporary registration. Registration is issued in semi-automatic mode. At some point your name will appear on a special list, you will surrender your passport and in a few days you will receive it back together with your temporary registration. Registration is mandatory for everyone, it\'s the law. The registration office for dormitory #6 is located in dormitory #1 of SPbPU (Lesnoy Prospect, 65 k.1).\n',
    CHECK_IN_RULES[V_CHINESE].lower(): '为了被安排在宿舍，申请人必须：\n'
                                       '- 接受招生委员会的推荐。\n'
                                       '- 有证明其身份的文件；\n'
                                       '- 拥有086у表的医学证明，并附有心电图，或单独的心电图证明。\n'
                                       '- 未满18周岁的参赛者，在没有父母或其他法定代理人的情况下到达现场3天以上的，必须要有父母（父母一方）或其他法定代理人的公证同意，才能办理落户和报名手续。文件必须说明同意的行动类型："我，（全名），允许我的未成年儿子（女儿）在通过入学考试期间或在上述大学学习期间，在FSEI VE "彼得大帝圣彼得堡理工大学 "的宿舍登记（护照数据和出生证数据）。\n'
                                       '- 迁入时还需要开具临时登记。登记以半自动方式处理。到了某个时候，你的名字会出现在一份特殊的名单上，你会把护照还给你，几天后，你会收到护照和你的临时登记。注册是每个人的义务，这是法律规定的。6号宿舍的报名处设在SPbPU的1号宿舍（Lesnoy Prospect，65k.1）。\n',

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
    RESIDENTS_RIGHTS[V_ENGLISH].lower(): 'Residents of the dormitory have the right to:\n'
                                         '1.  To move from one living room to another after agreement with the administration of the dormitory;\n'
                                         '2.  Use the rooms for independent studies and rooms for cultural and household purposes, equipment and inventory of the dormitory;\n'
                                         'to apply to the administration of the hostel with requests for timely repair, equipment and inventory replacement;\n'
                                         '4.  Participate in the formation of the student council of the hostel and be elected to it, participate through the council in solving the problems of the hostel;\n'
                                         '5.  To use household appliances under the condition of observing the rules of their operation and fire safety rules.\n',
    RESIDENTS_RIGHTS[V_CHINESE].lower(): '宿舍居民有权：\n'
                                         '1.  在与宿舍管理部门达成协议后，从一个房间搬到另一个房间。\n'
                                         '2.  将房间用于自主学习和文化及家庭用途的房间，设备和宿舍清单；\n'
                                         '3.向宿舍管理部门提出申请，要求及时维修、更换设备和库存。\n'
                                         '4.  参与创建宿舍的学生会，并当选为学生会成员，通过学生会参与解决宿舍的问题。\n'
                                         '5.  在遵守家用电器操作规则和消防安全规则的条件下，使用家用电器。\n',

    DUTY_OF_RESIDENTS[
        V_RUSSIAN].lower(): 'Общежитие живет по правилам внутреннего распорядка. В них нет ничего сложного, достаточно делать то, чего от тебя ждут:\n'
                            '1.	Не курить и не употреблять алкоголь/наркотики на территории университета (в том числе и общежития);\n'
                            '2.	Не мусорить в местах общего пользования: на кухне, в коридорах, в умывалках, в туалетах. Бережно относиться к общему имуществу;\n'
                            '3.	Вовремя убираться в своей комнате, не запускать ее. В общежитии действует санитарная комиссия, которая следит за чистотой в комнатах;\n'
                            '4.	Не проводить незнакомцев в общежитие. Проводить знакомых только в отведенное время;\n'
                            '5.	Соблюдать режим тишины: не шуметь по ночам и рано утром.\n',
    DUTY_OF_RESIDENTS[
        V_ENGLISH].lower(): 'The dormitory lives by house rules. There is nothing complicated about them, just do what is expected of you: \n'
                            '1.  No smoking or use of alcohol/drugs on campus (including the dormitory);\n'
                            '2.  Do not litter in common areas: in the kitchen, corridors, washrooms, toilets. Take care of the common property;\n'
                            '3.  To clean one\'s room in time and not to run it. A sanitary commission operates in the dormitory, which monitors the cleanliness of the rooms;\n'
                            '4.  Not to bring strangers into the dormitory. To accompany acquaintances only at the allotted time;\n'
                            '5.  To observe the regime of silence: not to make noise at night and early in the morning. \n',
    DUTY_OF_RESIDENTS[V_CHINESE].lower(): '寝室的生活是有规定的。他们没有什么复杂的，你只需要做你所期望的事情。\n'
                                          '1.  不在大学内（包括宿舍）吸烟、酗酒、吸毒。\n'
                                          '2.  不在公共区域乱扔垃圾：厨房、走廊、盥洗室、厕所。照顾好共同财产。\n'
                                          '3.  要及时打扫自己的房间，不要把房间弄脏。宿舍里有一个卫生委员会，负责监视房间的清洁。\n'
                                          '4.  不带陌生人进宿舍。要在规定的时间内才能见到熟人。\n'
                                          '5.  要遵守静默制度：晚上和清晨不喧哗。\n',

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
    DUTY_OF_ADMIN[V_ENGLISH].lower(): 'The administration of the student dormitory is obliged to:\n'
                                      '1. Ensure the provision of documents for the registration of residents at the place of residence;\n'
                                      '2.  Maintain the dormitory premises in accordance with the established sanitary rules;\n'
                                      '3.  To equip dormitories with furniture, equipment, bedding and other inventory;\n'
                                      '4. to provide the current repair of dormitories, inventory, equipment, to keep in proper order the territory assigned to the Student campus, green areas;\n'
                                      '5.  Promptly eliminate failures in the systems of sewerage, electricity and water supply of the dormitories;\n'
                                      '6.  Ensure the provision of the necessary rooms for self-study, recreation rooms, amenity rooms for residents in the dormitories;\n'
                                      '7.  In case of illness of underage residents to move them to another isolated room on the recommendation of the attending doctor;\n'
                                      '8.  To provide a daily inspection of all dormitory premises by their managers and employees of the relevant operational services in order to identify shortcomings in their operation and sanitary maintenance and to take measures to eliminate them;\n'
                                      '9.  To give dwellers in the dormitory the right to use household appliances and equipment on condition that they comply with safety regulations and instructions for using household appliances;\n'
                                      '10. To promote the work of student councils on improving the living conditions, everyday life and recreation of residents;\n'
                                      '11. To take measures for the implementation of residents\' proposals and inform them of the decisions made;\n'
                                      '12. to provide the residents with the necessary equipment, tools and materials for the voluntary cleaning works in the dormitories and the territory assigned to the Studeburgh;\n'
                                      '13. Ensure fire and public safety of the residents and staff in the dormitories.\n',
    DUTY_OF_ADMIN[V_CHINESE].lower(): '学生宿舍的管理部门有义务：\n'
                                      '1.确保在居住地提供居民登记证件。\n'
                                      '2.  按照规定的卫生规则，维护好宿舍楼的卫生。\n'
                                      '3.  为旅馆配备家具、设备、床上用品和其他库存；\n'
                                      '4）对宿舍进行现修、清点、设备，保持校园领地的秩序，对其进行绿化种植。\n'
                                      '5.  及时排除宿舍下水道系统、供电、供水系统的故障。\n'
                                      '6.  为住在宿舍的居民提供必要的独立学习室、娱乐室、家庭场所。\n'
                                      '7.  如有未成年住客患病，根据主治医生的建议，将其转移到另一间隔离房。\n'
                                      '8.  由管理人员和相应的经营服务人员每天对旅馆的所有房舍进行检查，以发现其经营和卫生维护方面的不足，并采取措施予以消除；\n'
                                      '9.  宿舍的住客有权使用家用电器和设备，但必须遵守安全措施和家用电器的使用说明。\n'
                                      '10. 协助学生会关于改善居民生活条件、日常生活和休闲的工作。\n'
                                      '11. 采取措施落实居民的建议，并将决定告知居民。\n'
                                      '12. 为住户提供必要的设备、工具和材料，以便在宿舍和分配给学生城的区域内进行义务清洁工作。\n'
                                      '13. 为确保宿舍内住户和工作人员的消防和公共安全。\n',

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
    BODIES_OF_MANAGEMENT[
        V_ENGLISH].lower(): 'In each dorm residents elect a body of self-government - the student council of the dormitory. Each dormitory unit elects a student warden. The student leader oversees the residents\' careful attitude towards the property and equipment, organizes and supervises the maintenance of the block in a clean and orderly manner. The Student Council of the dormitory supervises the work of the warden, organizes work on the voluntary involvement of residents to perform community service in the dormitory campus (cleaning and repairing of living rooms, small repairs of furniture) and in the surrounding area, helps the administration in organizing control of compliance with these rules and the safety of material values assigned to residents, organizes cultural work in the dormitory. The Student Council together with the administration of the hostel within the limits of its powers participates in the placement of students of the new intake, the distribution of new furniture and equipment among the residents, the safety of assigned living space. To coordinate the work in all dormitories of the campus, there is the United Students Council of dormitories, which includes all chairmen of dormitory student councils, representatives of the student trade union organization, other public student organizations, and the administration of SPbPU.',
    BODIES_OF_MANAGEMENT[
        V_CHINESE].lower(): '在每个宿舍，住户都会选出一个自治机构--宿舍学生会。校园各宿舍楼选出一名学生舍长。小区负责人要认真对待住户的财产和设备，组织和督促小区的维护工作，做到整洁有序。宿舍的学生会监督Starostas的工作，组织学生在自愿的基础上参与社会有益的工作，在学生校园的宿舍（清洁和修理客厅，小型修理家具）和相邻地区的工作，帮助行政部门组织控制这些规则的遵守和分配给学生的物质价值的安全，组织宿舍的文化和社区工作。学生会与宿舍管理部门在其权力范围内共同参与新生的安置、新家具和设备的分配、指定生活区的维护。为了协调校园内所有宿舍的工作，成立了宿舍联合学生会，其成员包括所有宿舍学生会主席、学生工会组织代表、其他公共学生组织和SPbPU的管理部门。',

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
    NEIGHBORS[
        V_ENGLISH].lower(): 'You have just arrived at your dorm, checked in. Your roommates show up on your doorstep. It\'s time to decide how to keep order, who cleans and takes out the trash, how to share appliances. Here are some tips.\n'
                            'In the first few months of life, students often buy things to share in a room. Many buy appliances together with roommates. But dorm life is really unpredictable. You may move to another room or dorm.\n'
                            'Our advice: let everyone buy something for the room themselves. Then in case of unexpected situations you will be able to take the equipment for yourself or resell it. This will help avoid conflicts with roommates.\n'
                            'If you\'re the one who needs a hairdryer, iron, multicooker, etc., you can use it individually (it\'s your stuff) or you can ask/share it with your roommates.\n'
                            'There are often conflicts between roommates when doing certain chores. So pay attention to the following tips:\n'
                            '- Cleaning. Make a cleaning schedule, determine the sequence and frequency of cleaning. Determine what will be the duties of the person on duty. For example, sweep and mop the floor, wipe dust off appliances.\n'
                            '- Taking out the trash. Garbage must be taken out every day. The accumulation of food waste in the garbage can causes an unpleasant smell in the room, and cockroaches appear as well. \n'
                            'Agree on who takes out the trash for whom. Put a schedule of duty and trash pickup on the door. This will help keep order and discipline in the room.\n'
                            'Each person has different eating habits. Therefore, it is important to respect the taste preferences of your neighbor, even if he makes instant noodles every night.\n'
                            'Many in the beginning of life in the dorm try to buy groceries and cook together. But soon it becomes uncomfortable because of the schedule or the desire for food. So we recommend avoiding conflicts over the amount eaten and eating separately. But no one forbids treating your neighbors with your specialty.\n',
    NEIGHBORS[V_CHINESE].lower(): '你刚到宿舍，办理了入住手续。你的室友出现在你家门口。是时候决定如何维持秩序，谁打扫卫生和倒垃圾，如何共享家用电器了。这里有一些小技巧。\n'
                                  '在刚开始的几个月里，学生们经常会买一些东西放在房间里分享。很多人和室友一起买家电。但宿舍生活真的是不可预知的。你可以搬到其他房间或宿舍。\n'
                                  '我们的建议是：让大家自己给房间买点东西。那么在遇到突发情况时，你就可以将设备据为己有或者转卖。这将有助于避免与邻居的冲突。\n'
                                  '如果是你需要电吹风、电熨斗、多用炉等，你可以单独使用（这是你的东西），也可以向室友要/分享。\n'
                                  '在做某些家务时，室友之间经常会有矛盾。所以要注意以下的技巧。\n'
                                  '- 清洁； 制定清洁计划，确定清洁的顺序和频率。确定值班人员的职责是什么。比如，扫地拖地，擦拭电器上的灰尘。\n'
                                  '- 垃圾清理。垃圾必须每天都要倒掉。垃圾桶里的食物垃圾堆积会导致房间里有难闻的气味，还可能出现蟑螂。\n'
                                  '同意谁去倒垃圾。把垃圾值班和垃圾清运的时间表放在门上。这将有助于保持房间的秩序和纪律。\n'
                                  '每个人的饮食习惯不同。因此，即使邻居每天晚上做方便面，也要尊重他的口味喜好。\n'
                                  '宿舍生活之初，很多人都会尝试一起买菜做饭。但很快就因为时间安排或对食物的渴望而变得不方便。所以我们建议避免在吃的量上发生冲突，分开吃。但没有人禁止用你的特别餐点来招待你的邻居。\n',

    ADMINISTRATION[
        V_RUSSIAN].lower(): 'Не ссорьтесь с ней, здоровайтесь при встрече, участвуйте в жизни общежития, платите вовремя и у вас будут отличные отношения с администрацией. Проверено:)\n',
    ADMINISTRATION[
        V_ENGLISH].lower(): 'Don\'t quarrel with her, say hello when you meet her, participate in the life of the hostel, pay on time and you will have a great relationship with the administration. Tested:)',
    ADMINISTRATION[V_CHINESE].lower(): '不要和她吵架，见了她就打招呼，参加宿舍生活，按时交钱，你会和管理部门有很好的关系。经测试：)',

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
    COCKROACHES[
        V_ENGLISH].lower(): 'In the dormitory, some rooms have a lot of cockroaches and some have none at all. What simple rules should you follow to avoid encountering cockroaches?\n'
                            'You should not litter the room. It threatens not only the appearance of problems with the sanitary commission of the hostel, but also the accumulation of cockroaches in your room.\n'
                            '- Dishes. Wash dishes immediately after meals. Don\'t leave food out in the open.\n'
                            '- Food Storage. Consider in advance how to store loose dry goods (pasta, cereals). We recommend buying containers for each cereal separately. It is also worth buying a large plastic box for all the smaller containers. In addition, you can buy cereal boxes that have a tight closure.\n'
                            '- Cleaning. It is necessary to wipe the dust, air the room.\n'
                            '- A clean floor is the key to order, so wash the floors once a week or more often. Cockroaches can hide in a pile of papers and trash, so all unnecessary stuff should be thrown out, keep it clean. Sort out closets and put things in order.\n'
                            '- Contractor. You can order cockroach/bug extermination in your dormitory. To do this, you need to leave an application on the watch. If the cockroaches are poisoned badly, it is necessary to inform the Student Council or the administration of the dormitory.\n'
                            'Cockroaches don\'t like to be disturbed and often settle where you look the least, especially if it\'s warm or humid. Cockroaches can often be found behind the refrigerator, in the Wi-Fi hotspot, or under the kettle.\n'
                            'In general, roaches are very important to water, so it\'s best not to leave water anywhere open - mugs, plates after washing. If you go away for a long time, it is better to drain the water from the kettle and the filter.\n'
                            'Saving up and buying the cheapest means, they usually turn out to be useless. It is worth to take well-known brands such as "Mashenka", "Dohloks", "Raptor", "Combat" and others... You can find them in any store for a reasonable price.\n'
                            '- If you have just moved into the dorm and you do not yet have furniture, it is worth to gel the baseboard.\n'
                            '- We recommend treating the area under the refrigerator and kitchen cabinet once a month. This is the roaches\' favorite spot. Move refrigerators and cabinets away if possible.\n'
                            '- Purchase traps and place them around the room. Don\'t forget the battery area, under the bed and table, and the refrigerator. Traps should be changed every three to six months.\n'
                            '- If cockroaches are infested in the nightstand, it is worth disassembling it completely and treating it.\n'
                            'Our dormitory has a chemical treatment service for cockroaches. To sign up for it, you have to come to the hall and ask to have the room signed up for this procedure. Usually the exterminator comes at the end of the month early in the morning, so be prepared and think in advance about what you need to treat. The treatment itself takes no more than 5 minutes, but after it is better to leave the room for 2-3 hours.\n'
                            'In case of bad poisoning - inform the Student Council or the administration of the dormitory.\n'
                            'In addition, you can call that disinfestation service that you like.\n',
    COCKROACHES[V_CHINESE].lower(): '宿舍里有的房间蟑螂多，有的房间没有。避免蟑螂应该遵循哪些简单的规则？\n'
                                    '在房间里乱扔垃圾是不好的。它不仅威胁到了宿舍卫生委员会问题的出现，也威胁到了蟑螂在你房间里的积累。\n'
                                    '- 菜品。饭后马上洗碗。不要把食物放在没有盖子的地方。\n'
                                    '- 食物储存。提前考虑如何储存散装干货（面食、谷类）。我们建议单独购买每个物品的容器。你还应该买一个大的塑料盒来装所有的小容器。另外，你也可以购买密封性好的麦片盒。\n'
                                    '- 清洁； 需要擦掉灰尘，给房间通风。\n'
                                    '- 干净的地面是秩序的关键，所以每周或更频繁地拖地一次。蟑螂会藏在纸堆和垃圾堆里，所以一切不必要的东西都应该扔掉，保持清洁。整理橱柜，把东西摆放整齐。\n'
                                    '- 承包商： 可以在宿舍里订购灭蟑螂/虫子。要做到这一点，你需要在手表上留下一个应用程序。如果蟑螂防治效果不好，需要通知学生会或宿舍管理处。\n'
                                    '蟑螂不喜欢被打扰，经常在你最不注意的地方定居，尤其是在温暖或潮湿的地方。蟑螂经常可以在冰箱后面、Wi-Fi热点或者水壶下面找到。\n'
                                    '一般来说，蟑螂对水是非常重视的，所以最好不要把水放在任何地方，比如洗完后的杯子、盘子。如果长时间外出，最好将水壶和过滤器的水放掉。\n'
                                    '攒钱买最便宜的手段，结果通常都是无用功。值得借鉴的是 "玛申卡"、"多乐士"、"猛禽"、"康比特 "等知名品牌......。在任何一家商店都可以找到它们，而且价格合理。\n'
                                    '- 如果你刚搬进宿舍，还没有家具，不妨把底板胶化。\n'
                                    '- 我们建议每月对冰箱和厨柜下面的区域进行一次处理。这里是蟑螂最喜欢的地方。如果可能的话，将冰箱和橱柜移开。\n'
                                    '- 购买陷阱，并将其放置在房间周围。不要忘记电池区、床下和桌子、冰箱。陷阱应每3至6个月更换一次。\n'
                                    '- 如果床头柜上有蟑螂出没，不妨将其彻底拆解处理。\n'
                                    '我们宿舍对蟑螂有化学处理服务。要报名的话，需要到大厅里问清楚这个待遇的报名房间。一般灭虫师会在月底一大早来，所以要提前做好准备，想好自己需要处理的事情。疗程本身不超过5分钟，但疗程结束后最好离开房间2-3小时。\n'
                                    '如果发生不良中毒事件--通知学生会或宿舍管理处。\n'
                                    '也可以拨打自己喜欢的消杀服务电话。\n',

    WHAT_TO_TAKE_WITH_YOU[V_RUSSIAN].lower(): 'Да хрен его знает, купить можно все на месте кекв',
    WHAT_TO_TAKE_WITH_YOU[V_ENGLISH].lower(): 'I don\'t know, you can buy everything on the spot kekv',
    WHAT_TO_TAKE_WITH_YOU[V_CHINESE].lower(): '我不知道，你可以在现场买任何东西。',

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
    WHAT_TO_BUY_LOCALLY[V_ENGLISH].lower(): 'Here\'s what you might need:\n'
                                            '- refrigerator\n'
                                            '- kettle\n'
                                            '- Internet access point\n'
                                            '- microwave\n'
                                            '- bucket and mop, broom and dustpan\n'
                                            '- rags\n'
                                            '- detergents (for floors, windows, dishes) \n'
                                            '- dish sponges \n'
                                            '- garbage bags\n'
                                            '- cutlery (spoon, fork, knife) \n'
                                            '- mugs (you might have visitors)\n'
                                            '- frying pan\n'
                                            '- saucepan \n'
                                            '- other things: grater, whisk, colander - all at your discretion and personal taste. \n'
                                            'Washing machines, dryers, stoves, and sports equipment are in every dorm, so you don\'t have to worry about their absence.\n',
    WHAT_TO_BUY_LOCALLY[V_CHINESE].lower(): '这是你可能需要的东西。\n'
                                            '- 冰箱\n'
                                            '- 釜\n'
                                            '- 网点\n'
                                            '- 微波\n'
                                            '- 桶和拖把、扫帚和簸箕。\n'
                                            '- 褴褛\n'
                                            '- 洁具 \n'
                                            '- 餐巾纸 \n'
                                            '- 垃圾袋\n'
                                            '- 餐具(勺、叉、刀) \n'
                                            '- 杯子\n'
                                            '- 炒锅\n'
                                            '- 炖锅 \n'
                                            '洗衣机、烘干机、炉灶、运动器材每个宿舍都有，不用担心没有。\n'
}
