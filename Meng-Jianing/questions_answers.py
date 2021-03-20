# -*- coding: utf-8 -*-
# @Time    : 2021/3/20 12:48
# @Author  : Meng Jianing
# @FileName: questions_answers.py
# @Software: PyCharm
# @Versions: v0.8
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
SCIENCE_POLYTECH = ('Гостиницу "Наука-Политех"', 'Dorm "Science-Polytech"', '圣理工的科学')  # TODO
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
BODIES_OF_THE_STUDIO_MANAGEMENT = ('Органы студ-ого управления', 'Student management bodies', '学生管理机构')  # TODO
RESPONSIBILITY_FOR_BREAKING_THE_RULES = ('Ответ-сть за нарушение правил', 'Resp-ty for breaking rules', '违反规定后承担的责任')
NEIGHBORS = ('Соседями', 'Neighbors', '舍友')
ADMINISTRATION = ('Администрицией', 'Administration', '行政部门')  # TODO
COCKROACHES = ('Тараканами', 'Cockroaches', '除蟑螂')
WHAT_TO_TAKE_WITH_YOU = ('Что взять с собой', 'What to take with you', '随身带什么')
WHAT_TO_BUY_LOCALLY = ('Что купить на месте', 'What to buy locally', '需要购买的物品')

# 键值对 <--> 问题（小写）和回答
# Пары ключ-значение <--> вопрос (НИЖНИЙ регистр) и ответ
# Attention! Questions should be in all lowercase!
gl_questions_answers = {
    'контакты управления': 'Хотите узнать что-то ещё?',
    'hello123': 'Hello there',
    'help': 'We also need help qwq',
    'русский': 'Текущим языком уже является русский',
    'english': 'Changed language to English',
    '中文': '已将语言设置为简体中文',
    CLUB[V_RUSSIAN].lower(): 'Хотите узнать что-то ещё?',
    CLUB[V_ENGLISH].lower(): 'Do you what know more?',
    CLUB[V_CHINESE].lower(): '想知道更多吗？',
    ONLINE_COURSE[V_RUSSIAN].lower(): 'no_answer_ONLINE_COURSE[V_RUSSIAN]',
    ONLINE_COURSE[V_ENGLISH].lower(): 'no_answer_ONLINE_COURSE[V_ENGLISH]',
    ONLINE_COURSE[V_CHINESE].lower(): 'no_answer_ONLINE_COURSE[V_CHINESE]',
    NEXT[V_RUSSIAN].lower(): 'no_answer_NEXT[V_RUSSIAN]',
    NEXT[V_ENGLISH].lower(): 'no_answer_NEXT[V_ENGLISH]',
    NEXT[V_CHINESE].lower(): 'no_answer_NEXT[V_CHINESE]',
    MANAGEMENT_CONTACTS[V_RUSSIAN].lower(): 'no_answer_MANAGEMENT_CONTACTS[V_RUSSIAN]',
    MANAGEMENT_CONTACTS[V_ENGLISH].lower(): 'no_answer_MANAGEMENT_CONTACTS[V_ENGLISH]',
    MANAGEMENT_CONTACTS[V_CHINESE].lower(): 'no_answer_MANAGEMENT_CONTACTS[V_CHINESE]',
    ACCOMMODATION_RULES[V_RUSSIAN].lower(): 'no_answer_ACCOMMODATION_RULES[V_RUSSIAN]',
    ACCOMMODATION_RULES[V_ENGLISH].lower(): 'no_answer_ACCOMMODATION_RULES[V_ENGLISH]',
    ACCOMMODATION_RULES[V_CHINESE].lower(): 'no_answer_ACCOMMODATION_RULES[V_CHINESE]',
    COMPLEXES[V_RUSSIAN].lower(): 'no_answer_COMPLEXES[V_RUSSIAN]',
    COMPLEXES[V_ENGLISH].lower(): 'no_answer_COMPLEXES[V_ENGLISH]',
    COMPLEXES[V_CHINESE].lower(): 'no_answer_COMPLEXES[V_CHINESE]',
    ADVICE[V_RUSSIAN].lower(): 'no_answer_ADVICE[V_RUSSIAN]',
    ADVICE[V_ENGLISH].lower(): 'no_answer_ADVICE[V_ENGLISH]',
    ADVICE[V_CHINESE].lower(): 'no_answer_ADVICE[V_CHINESE]',
    FRONT[V_RUSSIAN].lower(): 'no_answer_FRONT[V_RUSSIAN]',
    FRONT[V_ENGLISH].lower(): 'no_answer_FRONT[V_ENGLISH]',
    FRONT[V_CHINESE].lower(): 'no_answer_FRONT[V_CHINESE]',
    CHANGE_LANGUAGE[V_RUSSIAN].lower(): 'no_answer_CHANGE_LANGUAGE[V_RUSSIAN]',
    CHANGE_LANGUAGE[V_ENGLISH].lower(): 'no_answer_CHANGE_LANGUAGE[V_ENGLISH]',
    CHANGE_LANGUAGE[V_CHINESE].lower(): 'no_answer_CHANGE_LANGUAGE[V_CHINESE]',
    INTERNAL_REGULATIONS[V_RUSSIAN].lower(): 'no_answer_INTERNAL_REGULATIONS[V_RUSSIAN]',
    INTERNAL_REGULATIONS[V_ENGLISH].lower(): 'no_answer_INTERNAL_REGULATIONS[V_ENGLISH]',
    INTERNAL_REGULATIONS[V_CHINESE].lower(): 'no_answer_INTERNAL_REGULATIONS[V_CHINESE]',
    TO_THE_BEGINING[V_RUSSIAN].lower(): 'no_answer_TO_THE_BEGINING[V_RUSSIAN]',
    TO_THE_BEGINING[V_ENGLISH].lower(): 'no_answer_TO_THE_BEGINING[V_ENGLISH]',
    TO_THE_BEGINING[V_CHINESE].lower(): 'no_answer_TO_THE_BEGINING[V_CHINESE]',
    LESNOY_PROSPECT[V_RUSSIAN].lower(): 'no_answer_LESNOY_PROSPECT[V_RUSSIAN]',
    LESNOY_PROSPECT[V_ENGLISH].lower(): 'no_answer_LESNOY_PROSPECT[V_ENGLISH]',
    LESNOY_PROSPECT[V_CHINESE].lower(): 'no_answer_LESNOY_PROSPECT[V_CHINESE]',
    COURAGE_SQUARE[V_RUSSIAN].lower(): 'no_answer_COURAGE_SQUARE[V_RUSSIAN]',
    COURAGE_SQUARE[V_ENGLISH].lower(): 'no_answer_COURAGE_SQUARE[V_ENGLISH]',
    COURAGE_SQUARE[V_CHINESE].lower(): 'no_answer_COURAGE_SQUARE[V_CHINESE]',
    CIVIL_PROSPECT[V_RUSSIAN].lower(): 'no_answer_CIVIL_PROSPECT[V_RUSSIAN]',
    CIVIL_PROSPECT[V_ENGLISH].lower(): 'no_answer_CIVIL_PROSPECT[V_ENGLISH]',
    CIVIL_PROSPECT[V_CHINESE].lower(): 'no_answer_CIVIL_PROSPECT[V_CHINESE]',
    SCIENCE_POLYTECH[V_RUSSIAN].lower(): 'no_answer_SCIENCE_POLYTECH[V_RUSSIAN]',
    SCIENCE_POLYTECH[V_ENGLISH].lower(): 'no_answer_SCIENCE_POLYTECH[V_ENGLISH]',
    SCIENCE_POLYTECH[V_CHINESE].lower(): 'no_answer_SCIENCE_POLYTECH[V_CHINESE]',
    COMPLEX_FOR_FURTHER_EDUCATION[V_RUSSIAN].lower(): 'no_answer_COMPLEX_FOR_FURTHER_EDUCATION[V_RUSSIAN]',
    COMPLEX_FOR_FURTHER_EDUCATION[V_ENGLISH].lower(): 'no_answer_COMPLEX_FOR_FURTHER_EDUCATION[V_ENGLISH]',
    COMPLEX_FOR_FURTHER_EDUCATION[V_CHINESE].lower(): 'no_answer_COMPLEX_FOR_FURTHER_EDUCATION[V_CHINESE]',
    RELATIONSHIP_WITH[V_RUSSIAN].lower(): 'no_answer_RELATIONSHIP_WITH[V_RUSSIAN]',
    RELATIONSHIP_WITH[V_ENGLISH].lower(): 'no_answer_RELATIONSHIP_WITH[V_ENGLISH]',
    RELATIONSHIP_WITH[V_CHINESE].lower(): 'no_answer_RELATIONSHIP_WITH[V_CHINESE]',
    MOVING_TO_THE_DORM[V_RUSSIAN].lower(): 'no_answer_MOVING_TO_THE_DORM[V_RUSSIAN]',
    MOVING_TO_THE_DORM[V_ENGLISH].lower(): 'no_answer_MOVING_TO_THE_DORM[V_ENGLISH]',
    MOVING_TO_THE_DORM[V_CHINESE].lower(): 'no_answer_MOVING_TO_THE_DORM[V_CHINESE]',
    PAYMENT[V_RUSSIAN].lower(): 'no_answer_PAYMENT[V_RUSSIAN]',
    PAYMENT[V_ENGLISH].lower(): 'no_answer_PAYMENT[V_ENGLISH]',
    PAYMENT[V_CHINESE].lower(): 'no_answer_PAYMENT[V_CHINESE]',
    DORM_SHORT[V_RUSSIAN].lower() + ' №7': 'no_answer №7',
    DORM_SHORT[V_RUSSIAN].lower() + ' №1': 'no_answer №1',
    DORM_SHORT[V_RUSSIAN].lower() + ' №3': 'no_answer №3',
    DORM_SHORT[V_RUSSIAN].lower() + ' №4': 'no_answer №4',
    DORM_SHORT[V_RUSSIAN].lower() + ' №4а': 'no_answer №4',
    DORM_SHORT[V_RUSSIAN].lower() + ' №5': 'no_answer №5',
    DORM_SHORT[V_RUSSIAN].lower() + ' №6': 'no_answer №6',
    DORM_SHORT[V_RUSSIAN].lower() + ' №11': 'no_answer №1',
    DORM_SHORT[V_RUSSIAN].lower() + ' №17': 'no_answer №1',
    DORM_SHORT[V_RUSSIAN].lower() + ' №18': 'no_answer №1',
    DORM_SHORT[V_RUSSIAN].lower() + ' №8': 'no_answer №8',
    DORM_SHORT[V_RUSSIAN].lower() + ' №10': 'no_answer №1',
    DORM_SHORT[V_RUSSIAN].lower() + ' №12': 'no_answer №1',
    DORM_SHORT[V_RUSSIAN].lower() + ' №14а': 'no_answer №1',
    DORM_SHORT[V_RUSSIAN].lower() + ' №14б': 'no_answer №1',
    DORM_SHORT[V_RUSSIAN].lower() + ' №14ц': 'no_answer №1',

    DORM_SHORT[V_ENGLISH].lower() + ' №7': 'no_answer №7',
    DORM_SHORT[V_ENGLISH].lower() + ' №1': 'no_answer №1',
    DORM_SHORT[V_ENGLISH].lower() + ' №3': 'no_answer №3',
    DORM_SHORT[V_ENGLISH].lower() + ' №4': 'no_answer №4',
    DORM_SHORT[V_ENGLISH].lower() + ' №4а': 'no_answer №4',
    DORM_SHORT[V_ENGLISH].lower() + ' №5': 'no_answer №5',
    DORM_SHORT[V_ENGLISH].lower() + ' №6': 'no_answer №6',
    DORM_SHORT[V_ENGLISH].lower() + ' №11': 'no_answer №1',
    DORM_SHORT[V_ENGLISH].lower() + ' №17': 'no_answer №1',
    DORM_SHORT[V_ENGLISH].lower() + ' №18': 'no_answer №1',
    DORM_SHORT[V_ENGLISH].lower() + ' №8': 'no_answer №8',
    DORM_SHORT[V_ENGLISH].lower() + ' №10': 'no_answer №1',
    DORM_SHORT[V_ENGLISH].lower() + ' №12': 'no_answer №1',
    DORM_SHORT[V_ENGLISH].lower() + ' №14а': 'no_answer №1',
    DORM_SHORT[V_ENGLISH].lower() + ' №14б': 'no_answer №1',
    DORM_SHORT[V_ENGLISH].lower() + ' №14ц': 'no_answer №1',

    DORM_SHORT[V_CHINESE].lower() + ' №7': 'no_answer №7',
    DORM_SHORT[V_CHINESE].lower() + ' №1': 'no_answer №1',
    DORM_SHORT[V_CHINESE].lower() + ' №3': 'no_answer №3',
    DORM_SHORT[V_CHINESE].lower() + ' №4': 'no_answer №4',
    DORM_SHORT[V_CHINESE].lower() + ' №4а': 'no_answer №4',
    DORM_SHORT[V_CHINESE].lower() + ' №5': 'no_answer №5',
    DORM_SHORT[V_CHINESE].lower() + ' №6': 'no_answer №6',
    DORM_SHORT[V_CHINESE].lower() + ' №11': 'no_answer №1',
    DORM_SHORT[V_CHINESE].lower() + ' №17': 'no_answer №1',
    DORM_SHORT[V_CHINESE].lower() + ' №18': 'no_answer №1',
    DORM_SHORT[V_CHINESE].lower() + ' №8': 'no_answer №8',
    DORM_SHORT[V_CHINESE].lower() + ' №10': 'no_answer №1',
    DORM_SHORT[V_CHINESE].lower() + ' №12': 'no_answer №1',
    DORM_SHORT[V_CHINESE].lower() + ' №14а': 'no_answer №1',
    DORM_SHORT[V_CHINESE].lower() + ' №14б': 'no_answer №1',
    DORM_SHORT[V_CHINESE].lower() + ' №14ц': 'no_answer №1',

    DORM_LONG[V_RUSSIAN].lower() + ' №13': 'no_answer №13',
    DORM_LONG[V_RUSSIAN].lower() + ' №15': 'no_answer №15',
    DORM_LONG[V_RUSSIAN].lower() + ' №16': 'no_answer №16',
    DORM_LONG[V_RUSSIAN].lower() + ' №19': 'no_answer №19',
    DORM_LONG[V_RUSSIAN].lower() + ' №20': 'no_answer №20',

    DORM_LONG[V_ENGLISH].lower() + ' №13': 'no_answer №13',
    DORM_LONG[V_ENGLISH].lower() + ' №15': 'no_answer №15',
    DORM_LONG[V_ENGLISH].lower() + ' №16': 'no_answer №16',
    DORM_LONG[V_ENGLISH].lower() + ' №19': 'no_answer №19',
    DORM_LONG[V_ENGLISH].lower() + ' №20': 'no_answer №20',

    DORM_LONG[V_CHINESE].lower() + ' №13': 'no_answer №13',
    DORM_LONG[V_CHINESE].lower() + ' №15': 'no_answer №15',
    DORM_LONG[V_CHINESE].lower() + ' №16': 'no_answer №16',
    DORM_LONG[V_CHINESE].lower() + ' №19': 'no_answer №19',
    DORM_LONG[V_CHINESE].lower() + ' №20': 'no_answer №20',

    CHECK_IN_RULES[V_RUSSIAN].lower(): 'no_answer',
    CHECK_IN_RULES[V_ENGLISH].lower(): 'no_answer',
    CHECK_IN_RULES[V_CHINESE].lower(): 'no_answer',
    ORDER_PASSAGE_PUBLIC[V_RUSSIAN].lower(): 'no_answer',
    ORDER_PASSAGE_PUBLIC[V_ENGLISH].lower(): 'no_answer',
    ORDER_PASSAGE_PUBLIC[V_CHINESE].lower(): 'no_answer',
    RESIDENTS_RIGHTS[V_RUSSIAN].lower(): 'no_answer',
    RESIDENTS_RIGHTS[V_ENGLISH].lower(): 'no_answer',
    RESIDENTS_RIGHTS[V_CHINESE].lower(): 'no_answer',
    DUTY_OF_RESIDENTS[V_RUSSIAN].lower(): 'no_answer',
    DUTY_OF_RESIDENTS[V_ENGLISH].lower(): 'no_answer',
    DUTY_OF_RESIDENTS[V_CHINESE].lower(): 'no_answer',
    DUTY_OF_ADMIN[V_RUSSIAN].lower(): 'no_answer',
    DUTY_OF_ADMIN[V_ENGLISH].lower(): 'no_answer',
    DUTY_OF_ADMIN[V_CHINESE].lower(): 'no_answer',
    BODIES_OF_THE_STUDIO_MANAGEMENT[V_RUSSIAN].lower(): 'no_answer',
    BODIES_OF_THE_STUDIO_MANAGEMENT[V_ENGLISH].lower(): 'no_answer',
    BODIES_OF_THE_STUDIO_MANAGEMENT[V_CHINESE].lower(): 'no_answer',
    RESPONSIBILITY_FOR_BREAKING_THE_RULES[V_RUSSIAN].lower(): 'no_answer',
    RESPONSIBILITY_FOR_BREAKING_THE_RULES[V_ENGLISH].lower(): 'no_answer',
    RESPONSIBILITY_FOR_BREAKING_THE_RULES[V_CHINESE].lower(): 'no_answer',
    NEIGHBORS[V_RUSSIAN].lower(): 'no_answer',
    NEIGHBORS[V_ENGLISH].lower(): 'no_answer',
    NEIGHBORS[V_CHINESE].lower(): 'no_answer',
    ADMINISTRATION[V_RUSSIAN].lower(): 'no_answer',
    ADMINISTRATION[V_ENGLISH].lower(): 'no_answer',
    ADMINISTRATION[V_CHINESE].lower(): 'no_answer',
    COCKROACHES[V_RUSSIAN].lower(): 'no_answer',
    COCKROACHES[V_ENGLISH].lower(): 'no_answer',
    COCKROACHES[V_CHINESE].lower(): 'no_answer',
    WHAT_TO_TAKE_WITH_YOU[V_RUSSIAN].lower(): 'no_answer',
    WHAT_TO_TAKE_WITH_YOU[V_ENGLISH].lower(): 'no_answer',
    WHAT_TO_TAKE_WITH_YOU[V_CHINESE].lower(): 'no_answer',
    WHAT_TO_BUY_LOCALLY[V_RUSSIAN].lower(): 'no_answer',
    WHAT_TO_BUY_LOCALLY[V_ENGLISH].lower(): 'no_answer',
    WHAT_TO_BUY_LOCALLY[V_CHINESE].lower(): 'no_answer'
}
