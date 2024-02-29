import os
import environs
import telebot
from dotenv import load_dotenv
from pycoingecko import CoinGeckoAPI

load_dotenv()
token = os.getenv("Api_Token")


#getting the key
# BOT_TOKEN = env('5316743985:AAFGa4LLX_AObGVtX3U2li1a7iCEX3ZadBw')

#creating the bot
bot = telebot.TeleBot('token')
coin_client = CoinGeckoAPI()

# print(coin_client.get_price(ids='bitcoin',vs_currencies='usd')['bitcoin']['usd'])

#passing the 'text' command to the bot

#getting the bot to output "text"s
@bot.message_handler(func=lambda message: True, content_types=['text'])
def help(message):
 def crypto_price_message_handler(message):
  crypto_id = message.text
price_response = coin_client.get_price(ids='crypto_id',vs_currencies='usd')['crypto_id']['usd']

if price_response:
    price = price_response[crypto_id]['usd']
    bot.send_message(chat_id= message.chat.id, text={"Price of {crypto_id}:{price}"})
else:
    bot.send_message(chat_id=message.chat.id, text={"Crypto {crypto_id} was not found"})

#looking out of messages
bot.pulling(none_stop=True)




