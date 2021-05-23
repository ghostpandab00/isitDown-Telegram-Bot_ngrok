import constants as keys
from telegram.ext import * 
import responses as r

def start(update, context):
    user_name = update.message.from_user
    update.message.reply_text('Yo {} 👊 \n\nWelcome ta 𝖎𝖘𝖎𝖙𝖉𝖔𝖜𝖓 𝕭𝖔𝖙 🤖\n/help fo" help'.format(user_name['username']))

def help(update, context):
    update.message.reply_text('Type da website name. Eg: google.𝘤𝘰𝘮')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = r.status_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",help))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()









