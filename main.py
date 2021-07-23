from vk_api.vk_api import VkApiGroup
from vk_api.bot_longpoll import VkBotLongPoll

from config import *
from handle import handle
from methods import Methods


def main_loop(longpoll, methods, errors):
    for event in longpoll.listen():
        print(event)
        try:
            handle(event, methods)
        except Exception as error:
            errors.append(error)


def main():
    vk_session = VkApiGroup(token=TOKEN)
    methods = Methods(vk_session)
    errors = []

    main_loop(VkBotLongPoll(vk_session, ID), methods, errors)


if __name__ == '__main__':
    main()
