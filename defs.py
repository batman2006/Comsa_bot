import telebot
from connections import bot_token, redis_client, db_password
from markups import menu_markup
from telebot import types
from pymongo import MongoClient
from urllib.parse import quote_plus

encoded_password = quote_plus(db_password)
bot = telebot.TeleBot(bot_token)
cluster = MongoClient(
    f"mongodb+srv://nazarworker17:{encoded_password}@cluster0.momxsd3.mongodb.net/?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]

def save_password(message):
    if redis_client.exists(f"bot_pass_request:{message.chat.id}"):
        redis_client.set(f"user_password:{message.chat.id}", message.text)
        redis_client.delete(f"bot_pass_request:{message.chat.id}")
        bot.reply_to(message, f"Дякую, твій код для доступу до своїх паролей успішно збережений!")
        bot.delete_message(message.chat.id, message.message_id)

def check_new_password(message):
    user_password = redis_client.get(f"user_password:{message.chat.id}")
    if user_password == message.text:
        bot.reply_to(message, "Тепер ви у головному меню",
                     reply_markup=menu_markup)
        bot.delete_message(message.chat.id, message.message_id)
    else:
        bot.reply_to(message, "Невірний код. Спробуйте ще раз.")


def my_check_password(message):
    user_password = redis_client.get(f"user_password:{message.chat.id}")
    if user_password == message.text:
        bot.reply_to(message, "Ваші паролі🔒")
        bot.delete_message(message.chat.id, message.message_id)

        passwords_collection = db["test"]  
        passwords = passwords_collection.find({"user_id": message.chat.id})

        markup = types.ReplyKeyboardMarkup(row_width=1)
        for password_data in passwords:
            password = password_data["password"]
            button = types.KeyboardButton(text=password)
            markup.add(button)

        bot.send_message(message.chat.id, "Оберіть пароль:",
                         reply_markup=markup)
    else:
        bot.reply_to(message, "Невірний код. Спробуйте ще раз.")
