from vk_api.bot_longpoll import VkBotEventType


def handle(event, methods):
    if event.type == VkBotEventType.MESSAGE_NEW:
        message_new(
            methods=methods,
            message=event.obj.message['text'],
            from_id=event.obj.message['from_id'],
            event=event
        )
    if event.type == VkBotEventType.MESSAGE_TYPING_STATE:
        message_typing_state(
            methods=methods,
            from_id=event.obj.from_id,
            event=event
        )
    if event.type == VkBotEventType.GROUP_JOIN:
        group_join(
            methods=methods,
            from_id=event.obj.user_id,
            event=event
        )
    if event.type == VkBotEventType.GROUP_LEAVE:
        group_leave(
            methods=methods,
            from_id=event.obj.user_id,
            event=event
        )


def message_new(methods, message, from_id, event):
    if message == "Hello":
        answer = "Hello!"
    else:
        answer = "..."
    methods.send_message(message=answer, to_id=from_id)


def group_join(methods, from_id, event):
    pass


def message_typing_state(methods, from_id, event):
    pass


def group_leave(methods, from_id, event):
    pass
