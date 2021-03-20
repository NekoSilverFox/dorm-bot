# -*- coding: utf-8 -*-
# @Time    : 2021/3/6
# @Author  : Meng Jianing
# @FileName: main-robot-spbstu.py
# @Software: Pycharm
# @Versions: v0.8
# @Github  ：https://github.com/NekoSilverFox
# ~~~~~~~~~~~~~~~~~~~
# This file is mainly for testing and use, not the final version
# ~~~~~~~~~~~~~~~~~~~

import traceback
from time import sleep
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from robot_functions import *
from keyboard_functions import *

# API秘钥  Секретный ключ для входа
""" For test ↓ """
TOKEN_API = 'a6f3aed603c5e47cfdd0d1f4945082534e2cbea390f71b171bd0475132ddf572538a79a138c878dc9fa2c'

""" For use ↓ """
# TOKEN_API = '9ab7e183aa0bd0c1d7cb5e60cbb166db781b546abd17617bc7d2f815c36bbd9fd683883b0cfa76867f522'
MSG_WELCOME = 'Hi, I am Robot-Spbstu! You can use the keyboard or ask me questions!'
RESTART_WAIT_TIME = 10


def main():
    # Login in to VK
    print('[%s]: [INFO] Login in to VK...' % get_time())
    vk_session = vk_api.VkApi(token=TOKEN_API)  # Авторизоваться как сообщество
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    print('[%s]: [INFO] Successful connection' % get_time())

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:

                msg = event.text.lower()  # 消息全部转小写  Перевести в нижний регистр
                user_id = event.user_id
                language = get_user_language(user_id)
                keyboard = create_keyboard(msg, language=language)
                answer = get_answer_from_dic(msg)
                print('[%s]: [INFO] Get msg from user VK-ID: [%d], Message: [%s], language: [%s]' % (
                    get_time(), user_id, msg, language))

                if keyboard is None and is_first_time_use(user_id):
                    sender(vk_session, 'user_id', user_id,
                           message=MSG_WELCOME,
                           keyboard=create_keyboard(CHANGE_LANGUAGE[Language.RUSSIAN.value].lower()))

                elif keyboard is not None:
                    # msg_with_keyboard = get_answer_from_dec(msg)
                    sender(vk_session, 'user_id', user_id,
                           message=answer,
                           keyboard=keyboard)

                else:  # [keyboard is None and is_first_time_use(user_id)==False]
                    if msg in SET_LANGUAGE:
                        language = set_which_language(msg)
                        change_language(user_id, language=language)
                        sender(vk_session, 'user_id', user_id,
                               message=answer,
                               keyboard=create_keyboard('scheme-1-1', language=language))
                        print('[%s]: [INFO] Set user [%d] to [%s]' % (get_time(), user_id, language))
                        continue
                    sender(vk_session, 'user_id', user_id, message=answer)


if __name__ == '__main__':
    try:
        main()
    except Exception as unknown:
        print('[%s]: [ERROR] Catch exception: %s' % (get_time(), unknown))
        print('[%s]: [ERROR] Exception on line:[%s]' % (get_time(), traceback.print_exc()))
        print('[%s]: [WARNING] Ready to restart >>>>>')
        i = RESTART_WAIT_TIME
        while i > 0:
            print(">>> %d %s" % (i, ('.' * i)))
            sleep(1)
            i -= 1
        main()
        print('[%s]: [WARNING] Robot restart' % get_time())
