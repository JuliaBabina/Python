import telebot
from telebot import types 
import config
import random

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Сказать hi ")
    btn2 = types.KeyboardButton("👋 Цвет настроения? ")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)

color = ['Cиний', 'Все ок', 'В смысле?', 'Завтра будет лучше']
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Сказать hi"):
        bot.send_message(message.chat.id, text="Дратути)")
    else:
        bot.send_message(message.chat.id, random.choice(color))

print("server start")
bot.polling(none_stop=True)