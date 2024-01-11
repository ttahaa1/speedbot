from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Hello! I am your Telegram Bot.')

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    updater = Updater(token='YOUR_NEW_BOT_TOKEN', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
