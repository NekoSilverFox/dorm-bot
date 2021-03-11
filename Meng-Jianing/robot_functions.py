# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 21:08
# @Author  : Meng Jianing
# @FileName: robot_functions.py
# @Software: PyCharm
# @Versions: v0.7
# @Github  ：https://github.com/NekoSilverFox
# --------------------------------------------

import random
from enum import Enum

# 保存用户 Info
# Сохранить Info пользователя
# key - vk ID
# Value - UserInfo
""" Key: Value <--> vk_id: UserInfo """
gl_user_dic = {}

# 键值对 <--> 问题（小写）和回答
# Пары ключ-значение <--> вопрос (НИЖНИЙ регистр) и ответ
# Attention! Questions should be in all lowercase!
gl_questions_answers = {
    'студклубе': 'Хотите узнать что-то ещё?',
    'контакты управления': 'Хотите узнать что-то ещё?',
    'hello123': 'Hello there',
    'help': 'We also need help qwq',
    'русский': 'Текущим языком уже является русский',
    'english': 'Changed language to English',
    '中文': '已将语言设置为简体中文',
}

MSG_NO_ANSWER = 'Ой, я незнаю таких слов! (〃´-ω･) '


class Language(Enum):
    RUSSIA = 0
    ENGLISH = 1
    CHINESE = 2


class UserInfo(object):
    """Class for save user info"""

    __count = 0

    def __init__(self, vk_id):
        self.__vk_id = vk_id
        self.__language = Language.RUSSIA
        UserInfo.__count += 1
        self.__count_id = UserInfo.__count
        print("[INFO] user [%s] has create, UID: %05d" % (vk_id, UserInfo.__count))

    def __str__(self):
        return "id: %s, language: %s, UID: %05d" % (self.__vk_id, self.__language, UserInfo.__count)

    def get_vk_id(self):
        return self.__vk_id

    def get_count_id(self):
        return self.__count_id

    def get_number_of_users(self):
        return UserInfo.__count

    def set_language(self, language):
        self.__language = language

    def get_language(self):
        return self.__language


def sender(vk_session, id_type, vk_id, message=None, keyboard=None, attachment=None):
    """ Send message and keyboard

    :param vk_session: user group
    :param id_type: Type of ID
    :param vk_id: vk ID
    :param message: [string] message which need to send
    :param keyboard: keyboard which need to send
    :param attachment: [Optional] For compatibility with older versions of the application
    :return: None
    """
    vk_session.method('messages.send',
                      {id_type: vk_id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648),
                       'keyboard': keyboard, 'attachment': attachment})


def get_answer_from_dic(question):
    """ Get the answer to the specified question or keyword from the Dictionary and return it

    :param question: [string] String or keyword of the question
    :return: Matching successful string (answer)
    """
    try:
        answer = gl_questions_answers[question]
    except Exception as unknown:
        answer = MSG_NO_ANSWER  # TODO Change here?
    return answer


def is_first_time_use(key_vk_id):
    """ Check if the user is using it for the first time

    :param key_vk_id: User Id or Group ID, also is key in Dictionary
    :return: [boolean] True if used, False if not used, and add the record
    """
    if key_vk_id in gl_user_dic:
        return False
    else:
        gl_user_dic[key_vk_id] = UserInfo(key_vk_id)
        return True
