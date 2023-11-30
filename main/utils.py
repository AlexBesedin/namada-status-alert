import telebot

from constants import TELEGRAM_TOKEN, CHAT_ID


def send_to_telegram(message):
    try:
        bot = telebot.TeleBot(TELEGRAM_TOKEN)
        bot.send_message(CHAT_ID, message)
    except Exception as e:
        print(f'Error: {e}')