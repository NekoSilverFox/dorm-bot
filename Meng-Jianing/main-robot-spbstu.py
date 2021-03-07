# -*- coding: utf-8 -*-
# @Time    : 2021/3/6
# @Author  : Meng Jianing
# @FileName: main-robot-spbstu.py
# @Software: Pycharm
# @Versions: v0.2
# @Github  ：https://github.com/NekoSilverFox
# ~~~~~~~~~~~~~~~~~~~
# This file is mainly for testing and use, not the final version
# ~~~~~~~~~~~~~~~~~~~

import vk_api
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from functions import *

# API秘钥  Секретный ключ для входа
TOKEN_API = 'a6f3aed603c5e47cfdd0d1f4945082534e2cbea390f71b171bd0475132ddf572538a79a138c878dc9fa2c'
# TOKEN_API = '9ab7e183aa0bd0c1d7cb5e60cbb166db781b546abd17617bc7d2f815c36bbd9fd683883b0cfa76867f522'
# public203029730

to_scheme_1_1 = ['scheme-1-1', 'scheme-1', 'в начало', '菜单', '主菜单', 'main_menu', 'main'
                                                                                 'вассап', 'здрасте', 'приветик',
                 'начать', 'салом алейкум', 'здравствуйте',
                 'добрый день', 'доброе утро', 'добрый ночь', 'здравствуй', 'hi', 'hello',
                 '你好', '您好', '在吗', '早安', '嗨', '早上好', '晚上好', '中午好'
    , 'назад']

to_scheme_1_2 = ['scheme-1-2', 'меню 1-2', '菜单 1-2', '', 'далее']
to_scheme_2 = ['scheme-2', 'меню 2', '菜单 2', 'общежите', '', '', '']
to_scheme_3 = ['scheme-3', 'меню 3', '菜单 3', 'комплексы', 'комплексы общежития', '', '']
to_scheme_4 = ['scheme-4', 'меню 4', '菜单 4', 'советы', '', '', '']
to_rules_of_residence = ['правила проживания', 'проживания правила', 'rules of residence']
gl_index_menu = 1


def create_keyboard(keyword, is_one_time=False, is_inline=False):
    keyboard = VkKeyboard(one_time=is_one_time, inline=is_inline)

    # Схема №1, первый часть
    if keyword in to_scheme_1_1:
        # [ATTENTION] on first row ONLY can put 2 button!
        keyboard.add_openlink_button('Сайт', 'https://spbstu.ru')
        keyboard.add_openlink_button('ВК', 'https://vk.com/pgpuspb')
        keyboard.add_line()
        keyboard.add_button('Студклубе', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Далее', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button('Русский', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('English', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('中文', color=VkKeyboardColor.POSITIVE)

    elif keyword in to_scheme_1_2:
        keyboard.add_button('Контакты управления', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Правила проживания', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Комплексы', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Советы', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Сменить язык', color=VkKeyboardColor.POSITIVE)

    elif keyword in to_scheme_2:
        keyboard.add_button('Контакты управления', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Внутренний распорядок', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('В начало', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Сменить язык', color=VkKeyboardColor.POSITIVE)

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

    elif keyword in to_scheme_4:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button('Взаимоотношения с...', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Переезд в общежитие', color=VkKeyboardColor.POSITIVE)

    elif keyword in to_rules_of_residence:
        keyboard = VkKeyboard(inline=True)
        keyboard.add_button('Внутренний распорядок', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Оплата', color=VkKeyboardColor.POSITIVE)

    else:
        return None

    return keyboard.get_keyboard()


def main():
    print("Login in to VK...")
    # 登录到VK  Вход в ВК
    vk_session = vk_api.VkApi(token=TOKEN_API)  # Авторизоваться как сообщество
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    print("Successful connection")

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                msg = event.text.lower()  # 消息全部转小写  Перевести в нижний регистр
                user_id = event.user_id
                print("Get msg from user [%d]: [%s]" % (user_id, msg))

                keyboard = create_keyboard(msg)
                if keyboard is None and is_first_time_use(user_id):
                    sender(vk_session, 'user_id', user_id,
                           message='Hi, I am Robot-Spbstu! You can use the keyboard or ask me questions!'
                           , keyboard=create_keyboard('scheme-1-1'))

                elif keyboard is not None:
                    sender(vk_session, 'user_id', user_id, message='Menu has created!', keyboard=keyboard)

                else:  # keyboard is None and is_first_time_use(user_id)=False:
                    answer = get_answer_from_dec(msg)
                    if len(answer) == 0:
                        answer = 'Ой, я незнаю таких слов! (〃´-ω･) '
                    sender(vk_session, 'user_id', user_id, message=answer)


if __name__ == '__main__':
    main()
