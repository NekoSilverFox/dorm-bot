# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 23:45
# @Author  : Meng Jianing
# @FileName: create_keyboard.py
# @Software: PyCharm
# @Versions: v0.7
# @Github  ：https://github.com/NekoSilverFox
# --------------------------------------------

from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from functions import Language, gl_id_list


to_scheme_1_1 = ['scheme-1-1', 'scheme-1', 'в начало', '菜单', '主菜单', 'main_menu', 'main',
                 'вассап', 'здрасте', 'приветик', 'начать', 'салом алейкум', 'здравствуйте',
                 'добрый день', 'доброе утро', 'добрый ночь', 'здравствуй', 'hi', 'hello',
                 '你好', '您好', '在吗', '早安', '嗨', '早上好', '晚上好', '中午好', 'назад']
to_scheme_1_2 = ['scheme-1-2', 'меню 1-2', '菜单 1-2', 'далее']
to_scheme_2 = ['scheme-2', 'меню 2', '菜单 2', 'общежите', '', '', '']
to_scheme_3 = ['scheme-3', 'меню 3', '菜单 3', 'комплексы', 'комплексы общежития', '', '']
to_scheme_4 = ['scheme-4', 'меню 4', '菜单 4', 'советы', '', '', '']
to_rules_of_residence = ['правила проживания', 'проживания правила', 'rules of residence']
to_dormitory_lesnoy_prospect = ['лесной проспект', 'лесной', 'лесная', 'lesnoy prospect', 'lesnoy', '']
to_dormitory_courage_square = ['площадь мужества', 'мужества', 'метро мужества', 'courage square', 'courage', '']
to_dormitory_civil_prospect = ['гражданский проспект', 'гражданский', 'академическая', 'civil prospect', 'civil', '']
to_internal_order = ['внутренний распорядок', 'распорядок', 'internal order', 'internal regulations', '']
to_relations_with = ['взаимоотношения с...', 'взаимоотношения', 'взаимоотношения с' 'relationship with...',
                     'relationships with...', 'relations with...']
to_moving_into_dorm = ['Переезд в общежитие', 'в общежитие', 'Переезд общежитие', '',
                       'Moving into a dormitory', 'Moving into dormitory', 'into dormitory',
                       'Moving into the dormitory', 'Moving into a dorm', 'Moving to a dormitory', '']
to_first_language = []

WEBSITE = ('Website', 'Сайт', '网站')
VK = ('VK', 'ВК', 'VK')
CLUB = ('Студклубе', 'Student Club', '学生俱乐部')
NEXT = ('Далее', 'Next', '下一页')
MANAGEMENT_CONTACTS = ('Контакты управления', 'Management contacts', '管理联络人')
ACCOMMODATION_RULES = ('Правила проживания', 'Accommodation rules', '住宿规则')
COMPLEXES = ('Комплексы', 'Complexes', '复合体')
ADVICE = ('Советы', 'Advice', '建议')
FROUNT = ('Назад', 'Back', '返回')
CHANGE_LANGUAGE = ('Сменить язык', 'Change language', '改变语言')
SET_RUSSIA = ('русский', '', '', '', '')
SET_ENGLISH = ('english', '', '', '', '')
SET_CHINESE = ('中文', '', '', '', '')
INTERNAL_REGULATIONS = ('Внутренний распорядок', 'Internal regulations', '内部规定')
TO_THE_BEGINING = ('В начало', 'To the begin', '主页')
LESNOY_PROSPECT = ('Лесной проспект', 'Lesnoy prospect', '森林大街')
COURAGE_SQUARE = ('Площадь Мужества', 'Courage Square', '勇气广场')
CIVIL_PROSPECT = ('Гражданский проспект', 'Civil Prospect', '公民大街')
SCIENCE_POLYTECH = ('Гостиницу "Наука-Политех"', 'Hotel "Science-Polytech"', '酒店“加工的科学”')
COMPLEX_OF_ADDITIONAL_SERVICES_FOR_RESIDENTS = ('омплекс доп-ого обс-ия проживающих', 'complex of additional services for residents', '为居民提供的其他服务综合体')
RELATIONSHIP_WITH = ('Взаимоотношения с...', 'Relationship with...', '联系...')
MOVING_TO_THE_DORM = ('Переезд в общежитие', 'Moving to the dorm', '搬到宿舍')
# INTERNAL_REGULATIONS = ('', '', '')
PAYMENT = ('Оплата', 'Pay', '支付')
DORM_SHORT = ('Общ-ие', 'Dorm', '宿舍')
DORM_LONG = ('Общежитие', 'Dormitory', '宿舍')
CHECK_IN_RULES = ('Правила заселения', 'Check-in rules', '入住规则')
ORDER_PASSAGE_PUBLIC = ('Порядок прохода в общ-ия', 'Order of passage to dorm', '进入宿舍的顺序')
RESIDENTS_RIGHTS = ('Права проживающих', 'Residents\' rights', '居民的权利')
COMMUNITY_OF_RESIDENTS = ('Об-сти проживающих', 'Community of residents', '居民社区')
COMMUNITY_OF_ADMINISTRATION = ('администрации', 'administration', '行政共同体')
BODIES_OF_THE_STUDIO_MANAGEMENT = ('Органы студ-ого управления', 'Student management bodies', '学生管理机构')
RESPONSIBILITY_FOR_BREAKING_THE_RULES = ('Ответ-сть за нарушение правил', 'Resp-ty for breaking rules', '违反规则的责任')
NEIGHBORS = ('Соседями', 'Neighbors', '邻居')
ADMINISTRATION = ('Администрицией', 'Administration', '行政')
COCKROACHES = ('Тараканами', 'Cockroaches', '蟑螂')
WHAT_TO_TAKE_WITH_YOU = ('Что взять с собой', 'What to take with you', '随身带什么')
WHAT_TO_BUY_LOCALLY = ('Что купить на месте', 'What to buy locally', '在当地买什么')

def get_button_string(language):
    pass



def create_keyboard(keyword, is_one_time=False, is_inline=False, language=Language.RUSSIA):
    # Схема №1, первый часть
    if keyword in to_scheme_1_1:
        # [ATTENTION] on first row ONLY can put 2 button!
        keyboard = VkKeyboard(one_time=is_one_time, inline=is_inline)
        keyboard.add_openlink_button('Сайт', 'https://spbstu.ru')
        keyboard.add_openlink_button('ВК', 'https://vk.com/pgpuspb')
        keyboard.add_line()
        keyboard.add_button('Студклубе', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Далее', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button('Русский', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('English', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('中文', color=VkKeyboardColor.POSITIVE)

    # Схема №1, второй часть
    elif keyword in to_scheme_1_2:
        keyboard = VkKeyboard(one_time=is_one_time, inline=is_inline)
        keyboard.add_button('Контакты управления', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Правила проживания', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Комплексы', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Советы', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Сменить язык', color=VkKeyboardColor.POSITIVE)

    # Схема №2
    elif keyword in to_scheme_2:
        keyboard = VkKeyboard(one_time=is_one_time, inline=is_inline)
        keyboard.add_button('Контакты управления', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Внутренний распорядок', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('В начало', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Сменить язык', color=VkKeyboardColor.POSITIVE)

    # Схема №3
    elif keyword in to_scheme_3:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button('Лесной проспект', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Площадь Мужества', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Гражданский проспект', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Гостиницу "Наука-Политех"', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('омплекс доп-ого обс-ия проживающих', color=VkKeyboardColor.PRIMARY)

    # Схема №4
    elif keyword in to_scheme_4:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button('Взаимоотношения с...', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Переезд в общежитие', color=VkKeyboardColor.POSITIVE)

    # Правила проживания -->
    elif keyword in to_rules_of_residence:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button('Внутренний распорядок', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Оплата', color=VkKeyboardColor.POSITIVE)

    # Лесной проспект -->
    elif keyword in to_dormitory_lesnoy_prospect:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button('Общ-ие №7', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Общ-ие №1', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Общ-ие №3', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Общ-ие №4', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Общ-ие №4а', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Общ-ие №5', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Общ-ие №6', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Общ-ие №11', color=VkKeyboardColor.PRIMARY)

    # Площадь Мужества -->
    elif keyword in to_dormitory_courage_square:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button('Общ-ие №17', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Общ-ие №18', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Общ-ие №8', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Общ-ие №10', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Общ-ие №12', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Общ-ие №14а', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Общ-ие №14б', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Общ-ие №14ц', color=VkKeyboardColor.PRIMARY)

    # Гражданский проспект -->
    elif keyword in to_dormitory_civil_prospect:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button('Общежитие №13', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Общежитие №15', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Общежитие №16', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Общежитие №19', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Общежитие №20', color=VkKeyboardColor.PRIMARY)

    # Внутренний распорядок -->
    elif keyword in to_internal_order:
        keyboard = VkKeyboard(inline=True)
        # Max 6 rows!
        keyboard.add_button('Правила заселения', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Порядок прохода в общ-ия', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Права проживающих', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Об-сти проживающих', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('администрации', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Органы студ-ого управления', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Ответ-сть за нарушение правил', color=VkKeyboardColor.PRIMARY)

    # Взаимоотношения с... -->
    elif keyword in to_relations_with:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button('Соседями', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Администрицией', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Тараканами', color=VkKeyboardColor.PRIMARY)

    # Переезд в общежитие -->
    elif keyword in to_moving_into_dorm:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button('Что взять с собой', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Что купить на месте', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()

    # 关键字未匹配成功 - Ключевое слово не совпало
    else:
        return None

    return keyboard.get_keyboard()


def get_user_language(id):
    for event in gl_id_list:
        if event.get_id() == id:
            return event.get_language
    else:
        print('[ERROR] Can not find user in `get_user_language`')


def change_language(id, language):
    # TODO 把语言的对应表存放在集合当中，
    #  这样就不需要写新的函数，
    #  在调用时就可以完成语言的匹配
    """ 改变语言

    :param language: 语言
    :return: 无
    """
    if language not in Language:
        print("[ERROR] Can't change language")
    for event in gl_id_list:
        if event.get_id() == id:
            event.set_language(language)
    else:
        print("[ERROR] Can't find user in function `change_language`")


def set_which_language(key_world):
    if key_world in SET_RUSSIA:
        return Language.RUSSIA
    elif key_world in SET_ENGLISH:
        return Language.ENGLISH
    elif key_world in Language.CHINESE:
        return Language.CHINESE
    else:
        print('[ERROR] Cannot match language in `set_which_language`')