from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.vk_api import VkApiGroup

from config import TOKEN, ID

vk_session = VkApiGroup(token=TOKEN)
longpoll = VkBotLongPoll(vk_session, ID)

for i in longpoll.listen():
    print(i)
