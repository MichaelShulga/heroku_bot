import logging

from bot import VkWrapper

from config import ID, TOKEN


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        encoding='utf-8',
        format='%(asctime)s %(levelname)-8s %(message)s'
    )

    vk_wrapper = VkWrapper(ID, TOKEN)
    vk_wrapper.main_loop()


if __name__ == '__main__':
    main()
