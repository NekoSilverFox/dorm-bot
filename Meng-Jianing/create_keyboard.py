# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 23:45
# @Author  : Meng Jianing
# @FileName: create_keyboard.py
# @Software: PyCharm
# @Versions: v0.5
# @Github  ：https://github.com/NekoSilverFox
# --------------------------------------------

from vk_api.keyboard import VkKeyboard, VkKeyboardColor

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


def create_keyboard(keyword, is_one_time=False, is_inline=False):
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
