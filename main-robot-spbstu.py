# -*- coding: utf-8 -*-
# @Time    : 2021/3/6
# @Author  : Meng Jianing
# @FileName: main-robot-spbstu.py
# @Software: Pycharm
# @Versions: v1.5
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
from key import TOKEN_API

MSG_WELCOME = 'Приветствуем в Политехе, студент! Заселяешься в общежитие и у тебя появились вопросы о проживание, ' \
              'хочешь узнать организационную информацию или получить полезные советы? Тогда ты пришел к правильному ' \
              'боту:)'
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
                answer = get_answer_from_dic(language, msg)
                print('[%s]: [INFO] Get msg from user VK-ID: [%d], Message: [%s], language: [%s]' % (
                    get_time(), user_id, msg, language))

                if keyboard is None and is_first_time_use(user_id):
                    sender(vk_session, 'user_id', user_id,
                           message=MSG_WELCOME,
                           keyboard=create_keyboard(CHANGE_LANGUAGE[Language.RUSSIAN.value].lower()))

                elif answer in MSG_NO_ANSWER:
                    sender(vk_session, 'user_id', user_id,
                           message=answer,
                           keyboard=None)

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
