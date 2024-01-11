import os
from telegram.ext import Updater, CommandHandler

def main():
    # استخدام os.environ للوصول إلى متغير التكوين
    updater = Updater(token=os.environ.get('TELEGRAM_TOKEN'), use_context=True)

    # باقي الكود...

if __name__ == '__main__':
    main()
