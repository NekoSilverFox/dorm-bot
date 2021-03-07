# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 21:08
# @Author  : Meng Jianing
# @FileName: functions.py
# @Software: PyCharm
# @Versions: v0.5
# @Github  ：https://github.com/NekoSilverFox
# --------------------------------------------

import random

# 保存用户ID
# Сохранить ID пользователя
gl_id_list = []

# 键值对 <--> 问题（小写）和回答
# Пары ключ-значение <--> вопрос (НИЖНИЙ регистр) и ответ
gl_questions_answers = {
    # Attention! Questions should be in all lowercase!
    "студклубе": "Хотите узнать что-то ещё?",
    "контакты управления": "Хотите узнать что-то ещё?",
    "hello123": "Hello there",
    "help": "",
    "русский": "Текущим языком уже является русский",
    "english": "Скоро появится функция переключения языков!",
    "中文": "Скоро появится функция переключения языков!",
}


def sender(vk_session, id_type, id, message=None, keyboard=None, attachment=None):
    """ 发送消息或键盘

    :param vk_session: 用户组
    :param id_type: ID类型
    :param id: id
    :param message: [string] 要发送的信息
    :param keyboard: 键盘
    :param attachment: [可选]为了向老版本的应用兼容
    :return:
    """
    vk_session.method('messages.send',
                      {id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648),
                       'keyboard': keyboard, 'attachment': attachment})


def get_answer_from_dec(question):
    """ 从 xml 获取指定问题或关键字的回答并返回

    :param question: [string] 问题的字符串或者关键字
    :return: 匹配成功的字符串
    """
    try:
        answer = gl_questions_answers[question]
    except Exception as unknown:
        answer = ''
    return answer


def is_first_time_use(id):
    """ 检查用户是否首次使用

    :param id: 用户或组id
    :return: [boolen] 如果使用过即为True，未使用过为False
    """
    if id not in gl_id_list:
        gl_id_list.append(id)
        return True
    return False


def change_language(language):
    # TODO 把语言的对应表存放在集合当中，
    #  这样就不需要写新的函数，
    #  在调用时就可以完成语言的匹配
    """ 改变语言

    :param language: 语言
    :return: 无
    """
    pass
