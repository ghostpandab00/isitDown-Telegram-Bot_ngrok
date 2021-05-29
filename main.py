import os
import re
import telegram
from telegram.ext import *
import constants as keys
import responses as r


global bot
bot = telegram.Bot(token=keys.API_KEY)

PORT = int(os.environ.get('PORT', 8443))

def start(update, context):
    user_name = update.message.from_user
    update.message.reply_text('Hey! {}  This Bot Help You To Check The Status Of Website As Well As Server, Check /help For Input Syntax'.format(user_name['username']))

def help(update, context):
    update.message.reply_text('Type Your Website Name Like example.com OR IP Server Address Like 127.0.0.1')

def textcheck(update, context):
    user_text = str(update.message.text)
    parts = user_text.split(".")

    if len(parts) == 4 or user_text.isnumeric() == True:
        handle_messageip(update, context)

    else:
        handle_messagehost(update, context)

def handle_messagehost(update, context):
    user_text = str(update.message.text)
    text = str(user_text).lower()
    response = r.sitestatus_responses(text)
    update.message.reply_text(response)

def handle_messageip(update, context):
    user_text = update.message.text
    responseIP = r.ipstatus_chceck(user_text)
    update.message.reply_text(responseIP)

def error(update, context):
    print(f"update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",help))

    dp.add_handler(MessageHandler(Filters.text, textcheck))
    dp.add_handler(MessageHandler(Filters.text, handle_messagehost))
    dp.add_handler(MessageHandler(Filters.text, handle_messageip))

    dp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0",
                       port=int(PORT),
                       url_path=keys.API_KEY,
                       webhook_url='https://isitdown-telegram-bot.herokuapp.com/' + keys.API_KEY)

    updater.idle()

main()
