import random


class Methods:
    def __init__(self, vk_session):
        self.vk_session = vk_session

    def send_message(self, message, to_id):
        vk = self.vk_session.get_api()
        vk.messages.send(user_id=to_id,
                         message=message,
                         random_id=random.randint(0, 2 ** 64))
