# -*- coding: utf-8 -*-
# @Time    : 2021/3/7 23:45
# @Author  : Meng Jianing
# @FileName: keyboard_functions.py
# @Software: PyCharm
# @Versions: v1.1
# @Github  ：https://github.com/NekoSilverFox
# --------------------------------------------

from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from questions_answers import *
from robot_functions import gl_user_dic, get_time


SET_RUSSIAN = ('русский', 'russian', 'russia', '俄语')
SET_ENGLISH = ('english', 'английский', 'английский язык', '英语', '英文')
SET_CHINESE = ('中文', 'chinese', 'китайский', 'китайский язык')
SET_LANGUAGE = ('русский', 'russian', 'russia', '俄语',
                'english', 'английский', 'английский язык', '英语', '英文',
                '中文', 'chinese', 'китайский', 'китайский язык',
                'язык', '设置语言')

WEBSITE_SPBSTU_HOSTEL = 'https://www.spbstu.ru/students/social-security/hostel/'
WEBSITE_VK = 'https://vk.com/studg'
WEBSITE_TEST = 'https://foxthere.com/spbstu/'


to_change_language = [CHANGE_LANGUAGE[Language.RUSSIAN.value].lower(),
                      CHANGE_LANGUAGE[Language.ENGLISH.value].lower(),
                      CHANGE_LANGUAGE[Language.CHINESE.value].lower(),
                      '更改语言']

to_scheme_1_1 = [FRONT[Language.RUSSIAN.value].lower(),
                 FRONT[Language.ENGLISH.value].lower(),
                 FRONT[Language.CHINESE.value].lower(),
                 'scheme-1-1', 'scheme-1', 'в начало', '菜单', '主菜单', 'main_menu', 'main']

to_scheme_1_2 = [NEXT[Language.RUSSIAN.value].lower(),
                 NEXT[Language.ENGLISH.value].lower(),
                 NEXT[Language.CHINESE.value].lower(),
                 'scheme-1-2', 'меню 1-2', '菜单 1-2']

to_scheme_2 = ['scheme-2', 'меню 2', '菜单 2', 'общежите']

to_scheme_3 = [COMPLEXES[Language.RUSSIAN.value].lower(),
               COMPLEXES[Language.ENGLISH.value].lower(),
               COMPLEXES[Language.CHINESE.value].lower(),
               'scheme-3', 'меню 3', '菜单 3', 'комплексы общежития', '', '', ]

to_scheme_4 = [ADVICE[Language.RUSSIAN.value].lower(),
               ADVICE[Language.ENGLISH.value].lower(),
               ADVICE[Language.CHINESE.value].lower(),
               'scheme-4', 'меню 4', '菜单 4']

to_rules_of_residence = [ACCOMMODATION_RULES[Language.RUSSIAN.value].lower(),
                         ACCOMMODATION_RULES[Language.ENGLISH.value].lower(),
                         ACCOMMODATION_RULES[Language.CHINESE.value].lower(),
                         'проживания правила', 'rules of residence']

to_dormitory_lesnoy_prospect = [LESNOY_PROSPECT[Language.RUSSIAN.value].lower(),
                                LESNOY_PROSPECT[Language.ENGLISH.value].lower(),
                                LESNOY_PROSPECT[Language.CHINESE.value].lower(),
                                'лесной', 'лесная', 'lesnoy', '']

to_dormitory_courage_square = [COURAGE_SQUARE[Language.RUSSIAN.value].lower(),
                               COURAGE_SQUARE[Language.ENGLISH.value].lower(),
                               COURAGE_SQUARE[Language.CHINESE.value].lower(),
                               'мужества', 'метро мужества', 'courage', '']

to_dormitory_civil_prospect = [CIVIL_PROSPECT[Language.RUSSIAN.value].lower(),
                               CIVIL_PROSPECT[Language.ENGLISH.value].lower(),
                               CIVIL_PROSPECT[Language.CHINESE.value].lower(),
                               'гражданский', 'академическая', 'civil', '']

to_internal_order = [INTERNAL_REGULATIONS[Language.RUSSIAN.value].lower(),
                     INTERNAL_REGULATIONS[Language.ENGLISH.value].lower(),
                     INTERNAL_REGULATIONS[Language.CHINESE.value].lower(),
                     'распорядок', 'internal order', '']

to_relations_with = [RELATIONSHIP_WITH[Language.RUSSIAN.value].lower(),
                     RELATIONSHIP_WITH[Language.ENGLISH.value].lower(),
                     RELATIONSHIP_WITH[Language.CHINESE.value].lower(),
                     'взаимоотношения', 'взаимоотношения с', 'relationships with...', 'relations with...']

to_moving_into_dorm = [MOVING_TO_THE_DORM[Language.RUSSIAN.value].lower(),
                       MOVING_TO_THE_DORM[Language.ENGLISH.value].lower(),
                       MOVING_TO_THE_DORM[Language.CHINESE.value].lower(),
                       'в общежитие', 'переезд общежитие', 'moving into a dormitory', 'moving into dormitory',
                       'into dormitory', 'moving into the dormitory', 'moving into a dorm', 'moving to a dormitory', '']


def create_keyboard(keyword, is_one_time=False, is_inline=False, language=Language.RUSSIAN):
    """ Create the keyboard

    :param keyword: The keywords used to create the keyboard are recorded in the list above (to_XXXXX_XXX)
    :param is_one_time: Whether to hide the keyboard after the user has used it
    :param is_inline: Whether to present the keyboard as a message (in a bubble)
    :param language: Language of text in buttons
    :return: keyboard
    """

    language = language.value

    # Change language
    if keyword in to_change_language:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button('Русский', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('English', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('中文', color=VkKeyboardColor.POSITIVE)

    # Схема №1, первый часть
    elif keyword in to_scheme_1_1:
        # [ATTENTION] on first row ONLY can put 2 button!
        keyboard = VkKeyboard(one_time=is_one_time, inline=is_inline)
        keyboard.add_openlink_button(WEBSITE[language], WEBSITE_SPBSTU_HOSTEL)
        keyboard.add_openlink_button(VK[language], WEBSITE_VK)
        keyboard.add_line()
        # keyboard.add_openlink_button(ONLINE_COURSE[language], WEBSITE_TEST)
        keyboard.add_button(CLUB[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(CHANGE_LANGUAGE[language], color=VkKeyboardColor.POSITIVE)
        keyboard.add_button(NEXT[language], color=VkKeyboardColor.NEGATIVE)

    # Схема №1, второй часть
    elif keyword in to_scheme_1_2:
        keyboard = VkKeyboard(one_time=is_one_time, inline=is_inline)
        keyboard.add_button(MANAGEMENT_CONTACTS[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(ACCOMMODATION_RULES[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(COMPLEXES[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(ADVICE[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(FRONT[language], color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button(CHANGE_LANGUAGE[language], color=VkKeyboardColor.POSITIVE)

    # Схема №2
    elif keyword in to_scheme_2:
        keyboard = VkKeyboard(one_time=is_one_time, inline=is_inline)
        keyboard.add_button(MANAGEMENT_CONTACTS[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(INTERNAL_REGULATIONS[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        # keyboard.add_button(FRONT[language], color=VkKeyboardColor.NEGATIVE)
        # keyboard.add_button(TO_THE_BEGINING[language], color=VkKeyboardColor.NEGATIVE)
        # keyboard.add_button(CHANGE_LANGUAGE[language], color=VkKeyboardColor.POSITIVE)

    # Схема №3
    elif keyword in to_scheme_3:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button(LESNOY_PROSPECT[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(COURAGE_SQUARE[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(CIVIL_PROSPECT[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(SCIENCE_POLYTECH[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(COMPLEX_FOR_FURTHER_EDUCATION[language], color=VkKeyboardColor.PRIMARY)

    # Схема №4
    elif keyword in to_scheme_4:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button(RELATIONSHIP_WITH[language], color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button(MOVING_TO_THE_DORM[language], color=VkKeyboardColor.POSITIVE)

    # Правила проживания -->
    elif keyword in to_rules_of_residence:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button(INTERNAL_REGULATIONS[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(PAYMENT[language], color=VkKeyboardColor.POSITIVE)

    # Лесной проспект -->
    elif keyword in to_dormitory_lesnoy_prospect:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button(DORM_SHORT[language] + ' №1', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(DORM_SHORT[language] + ' №3', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(DORM_SHORT[language] + ' №4', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(DORM_SHORT[language] + ' №4а', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(DORM_SHORT[language] + ' №5', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(DORM_SHORT[language] + ' №6', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(DORM_SHORT[language] + ' №7', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(DORM_SHORT[language] + ' №11', color=VkKeyboardColor.PRIMARY)

    # Площадь Мужества -->
    elif keyword in to_dormitory_courage_square:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button(DORM_SHORT[language] + ' №8', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(DORM_SHORT[language] + ' №10', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(DORM_SHORT[language] + ' №12', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(DORM_SHORT[language] + ' №14а', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(DORM_SHORT[language] + ' №14б', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(DORM_SHORT[language] + ' №14ц', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(DORM_SHORT[language] + ' №17', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(DORM_SHORT[language] + ' №18', color=VkKeyboardColor.PRIMARY)

    # Гражданский проспект -->
    elif keyword in to_dormitory_civil_prospect:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button(DORM_LONG[language] + ' №13', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(DORM_LONG[language] + ' №15', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(DORM_LONG[language] + ' №16', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(DORM_LONG[language] + ' №19', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(DORM_LONG[language] + ' №20', color=VkKeyboardColor.PRIMARY)

    # Внутренний распорядок -->
    elif keyword in to_internal_order:
        keyboard = VkKeyboard(inline=True)
        # Max 6 rows!
        keyboard.add_button(CHECK_IN_RULES[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(ORDER_PASSAGE_PUBLIC[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(RESIDENTS_RIGHTS[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(DUTY_OF_RESIDENTS[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(DUTY_OF_ADMIN[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(BODIES_OF_MANAGEMENT[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(RESPONSIBILITY_BREAKING_RULES[language], color=VkKeyboardColor.PRIMARY)

    # Взаимоотношения с... -->
    elif keyword in to_relations_with:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button(NEIGHBORS[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(ADMINISTRATION[language], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(COCKROACHES[language], color=VkKeyboardColor.PRIMARY)

    # Переезд в общежитие -->
    # elif keyword in to_moving_into_dorm:
    #     keyboard = VkKeyboard(inline=True)
    #     keyboard.add_button(WHAT_TO_TAKE_WITH_YOU[language], color=VkKeyboardColor.PRIMARY)
    #     keyboard.add_line()
    #     keyboard.add_button(WHAT_TO_BUY_LOCALLY[language], color=VkKeyboardColor.PRIMARY)

    # 关键字未匹配成功 - Ключевое слово не совпало
    else:
        return None

    return keyboard.get_keyboard()


def get_user_language(key_vk_id):
    """ Get user language from the Dictionary

    :param key_vk_id: vk ID, will search in [Dictionary] gl_user_dic
    :return: [Language] language type in enum `Language` (NOT A INTEGER VALUE)
    """
    if key_vk_id in gl_user_dic:
        return gl_user_dic[key_vk_id].get_language()
    else:
        print('[%s]: [WARNING] Can not find user in `get_user_language`, set language to RUSSIA' % get_time())
        return Language.RUSSIAN


def change_language(key_vk_id, language):
    """ Change language in the class `UserInfo`

    :param key_vk_id: vk ID, will search in [Dictionary] gl_user_dic
    :param language:  Which need to change
    :return: None
    """

    if language not in Language:
        print("[%s]: [WARNING] Can't change language" % get_time())

    if key_vk_id in gl_user_dic:
        gl_user_dic[key_vk_id].set_language(language)
    else:
        print("[%s]: [WARNING] Can't find user in function `change_language`" % get_time())


def set_which_language(keyword):
    """ Use the received keywords to determine which language the setting is in

    :param keyword: Keyword used to match which language (written in SET_XXXXXX, e.g. SET_ENGLISH)
    :return: None
    """
    if keyword in SET_RUSSIAN:
        return Language.RUSSIAN
    elif keyword in SET_ENGLISH:
        return Language.ENGLISH
    elif keyword in SET_CHINESE:
        return Language.CHINESE
    else:
        print('[%s]: [WARNING] Cannot match language in `set_which_language`' % get_time())
