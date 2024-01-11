import os
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your bot.")

def main():
    # استخدام os.environ للوصول إلى متغير التكوين
    updater = Updater(token=os.environ.get('TELEGRAM_BOT_TOKEN'), use_context=True)

    
    # اضف الأمر الذي تريد تخصيصه
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    # بدء التحديث
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
