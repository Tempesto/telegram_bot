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
    )

def do_echo(bot: Bot, update: Update):
    print('chat_id = ', update.message.chat_id)

def main():
    bot = Bot(token= TG_TOKEN,)
    updater = Updater(bot=bot,)
    start_handler = CommandHandler("post", do_start)
    message_handler = MessageHandler(Filters.all, do_echo)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    sender()
    main()


