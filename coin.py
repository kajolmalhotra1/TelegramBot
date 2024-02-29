import os
import telebot
from dotenv import load_dotenv
from telebot.apihelper import ApiTelegramException
load_dotenv()

API_KEY = os.environ['TELEGRAM_KEY']

bot = telebot.TeleBot(API_KEY)

#passing the 'hello' command to the bot
@bot.message_handler(commands=['hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello!")

#looking out for messages
try:
  bot.polling()
except ApiTelegramException as e:
  print(e)
