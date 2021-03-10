# -*- coding: utf-8 -*-
# @Time    : 2021/3/6
# @Author  : Meng Jianing
# @FileName: main-robot-spbstu.py
# @Software: Pycharm
# @Versions: v0.7
# @Github  ：https://github.com/NekoSilverFox
# ~~~~~~~~~~~~~~~~~~~
# This file is mainly for testing and use, not the final version
# ~~~~~~~~~~~~~~~~~~~

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from create_keyboard import create_keyboard, change_language, set_which_language, get_user_language
from create_keyboard import CHANGE_LANGUAGE
from functions import *

# API秘钥  Секретный ключ для входа
""" For test ↓ """
TOKEN_API = 'a6f3aed603c5e47cfdd0d1f4945082534e2cbea390f71b171bd0475132ddf572538a79a138c878dc9fa2c'

""" For use ↓ """
# TOKEN_API = '9ab7e183aa0bd0c1d7cb5e60cbb166db781b546abd17617bc7d2f815c36bbd9fd683883b0cfa76867f522'
MSG_WELCOME = 'Hi, I am Robot-Spbstu! You can use the keyboard or ask me questions!'
MSG_NO_ANSWER = 'Ой, я незнаю таких слов! (〃´-ω･) '


def main():
    print("[INFO] Login in to VK...")
    # 登录到VK  Вход в ВК
    vk_session = vk_api.VkApi(token=TOKEN_API)  # Авторизоваться как сообщество
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    print("[INFO] Successful connection")

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                msg = event.text.lower()  # 消息全部转小写  Перевести в нижний регистр
                user_id = event.user_id
                print("[INFO] Get msg from user [%d]: [%s]" % (user_id, msg))

                keyboard = create_keyboard(msg)
                if keyboard is None and is_first_time_use(user_id):
                    sender(vk_session, 'user_id', user_id,
                           message=MSG_WELCOME,
                           keyboard=create_keyboard('scheme-1-1'))

                elif keyboard is not None:
                    # msg_with_keyboard = ?  # TODO 当按钮发送时顺带发送的信息，以便为 `message` 进行替换
                    sender(vk_session, 'user_id', user_id, message='[info]Menu has created!', keyboard=keyboard)

                else:  # keyboard is None and is_first_time_use(user_id)=False:
                    if msg in CHANGE_LANGUAGE:
                        change_language(user_id, set_which_language(msg))
                        sender(vk_session, 'user_id', user_id, message='[info]Menu has created!', keyboard=create_keyboard('scheme-1-1'))
                    answer = get_answer_from_dec(msg)
                    if len(answer) == 0:
                        answer = MSG_NO_ANSWER
                    sender(vk_session, 'user_id', user_id, message=answer)


if __name__ == '__main__':
    try:
        main()
    except Exception as unknown:
        print('[ERROR] Catch exception: %s' % unknown)
        main()
        print('[WARNING] Robot restart')
