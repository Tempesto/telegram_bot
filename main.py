from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from send_msg import sender
from config import TG_TOKEN
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup


CALLBACK_BUTTON1_LEFT = "ddd"

TITLE = {
    CALLBACK_BUTTON1_LEFT:"САЙТ",
}


def do_start(bot: Bot, update: Update):
    print('chat_id = ', update.message.chat_id)
    bot.send_message(
        chat_id=update.message.chat_id,
        # text = update.message.chat_id,
    )

key = [
    [
        InlineKeyboardButton('ddd', url='https://airsofter.world/images/product-image/9/6/6/5cfebb6cbfea8.jpg')
    ]
]

key1 = InlineKeyboardMarkup(key)

def do_echo(bot: Bot, update: Update):
    print('chat_id = ', update.message.chat_id)
    text = update.message.chat_id
    # print(key1)
    # bot.send_message(
    #     chat_id=update.message.chat_id,
    #     text='dddd',
    #     reply_markup=key1,
        # reply_markup= {'inline_keyboard': [[{'text': 'САЙТ', 'url': 'https://airsofter.world/images/product-image/9/6/6/5cfebb6cbfea8.jpg'}]]},

    # )
    # photo = 'https://airsofter.world/images/product-image/9/6/6/5cfebb6cbfea8.jpg'
    # bot.send_message(chat_id=249356603, text= f'[⁠]({photo})', parse_mode='markdown')

def main():
    bot = Bot(token= TG_TOKEN,)
    updater = Updater(bot=bot,)
    # Выводит сообщение "post" при перво подлючении пользователя, запуск функции do_start
    start_handler = CommandHandler("post", do_start)
    message_handler = MessageHandler(Filters.all, do_echo)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)
    # Запуск обновления
    updater.start_polling()
    # Не закрываться пока не обновится
    updater.idle()
    # sender()

if __name__ == '__main__':
    sender()
    main()


