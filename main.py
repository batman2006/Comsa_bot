import telebot
from connections import bot_token
from markups import  start_markup

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт👋 Обери криптовалюту , яку хочеш купити або можеш перевірити свій баланс",reply_markup=start_markup)
        
# RUN
bot.infinity_polling()