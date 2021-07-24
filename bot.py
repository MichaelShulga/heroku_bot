import logging

import random

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.vk_api import VkApiGroup


class VkWrapper:
    def __init__(self, group_id, token):
        self.id = group_id
        self.vk_session = VkApiGroup(token=token)

    def main_loop(self):
        longpoll = VkBotLongPoll(self.vk_session, self.id)
        for event in longpoll.listen():
            logging.debug(event)
            try:
                self.handle(event)
            except Exception as error:
                logging.error(error)

    def handle(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            self.message_new(
                message=event.obj.message['text'],
                from_id=event.obj.message['from_id'],
                event=event
            )
        if event.type == VkBotEventType.MESSAGE_TYPING_STATE:
            self.message_typing_state(
                from_id=event.obj.from_id,
                event=event
            )
        if event.type == VkBotEventType.GROUP_JOIN:
            self.group_join(
                user_id=event.obj.user_id,
                event=event
            )
        if event.type == VkBotEventType.GROUP_LEAVE:
            self.group_leave(
                user_id=event.obj.user_id,
                event=event
            )

    def message_new(self, message, from_id, event):
        if message == "Hello":
            answer = "Hello!"
        else:
            answer = "..."
        self.send_message(message=answer, to_id=from_id)

    def message_typing_state(self, from_id, event):
        pass

    def group_join(self, user_id, event):
        pass

    def group_leave(self, user_id, event):
        pass

    def send_message(self, message, to_id):
        vk = self.vk_session.get_api()
        vk.messages.send(
            user_id=to_id,
            message=message,
            random_id=random.randint(0, 2 ** 64)
        )
