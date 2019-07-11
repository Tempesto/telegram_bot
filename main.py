from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from send_msg import sender
from config import TG_TOKEN

def do_start(bot: Bot, update: Update):
    print('chat_id = ', update.message.chat_id)
    bot.send_message(
        chat_id=update.message.chat_id,
        # text = update.message.chat_id,
    )

def do_echo(bot: Bot, update: Update):
    print('chat_id = ', update.message.chat_id)
    text = update.message.chat_id
    bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
    )

def main():
    bot = Bot(token= TG_TOKEN,)
    updater = Updater(bot=bot,)
    # Выводит сообщение "post" при перво подлючении пользователя, запуск функции do_start
    start_handler = CommandHandler("post", do_start)
    message_handler = MessageHandler(Filters.text, do_echo)
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


