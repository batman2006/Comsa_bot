import telebot
from connections import bot_token
from markups import  start_markup

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт👋 Обери криптовалюту , яку хочеш купити або можеш перевірити свій баланс",reply_markup=start_markup)

"""@bot.message_handler(func=lambda message: chat_states.get(message.chat.id) == 'current_pass')
def check_current_password(message):
    user_password = redis_client.get(f"user_password:{message.chat.id}")
    if user_password == message.text:
        chat_states[message.chat.id] = 'new_password'
        bot.send_message(
            message.chat.id, "Введи новий код, який ти будеш використовувати для доступу до своїх паролей. Запам'ятай чи запиши його🛑")
        redis_client.set(f"temp_user_password:{message.chat.id}", "True")
    else:
        bot.reply_to(message, "Невірний код. Спробуйте ще раз.")


@bot.message_handler(func=lambda message: chat_states.get(message.chat.id) == 'new_password')
def set_new_password(message):
    redis_client.set(f"user_password:{message.chat.id}", message.text)
    chat_states[message.chat.id] = None
    bot.reply_to(
        message, "Дякую, твій новий код для доступу до своїх паролей успішно збережений! Тепер ви у головному меню", reply_markup=menu_markup)
    bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(func=lambda message: chat_states.get(message.chat.id) == 'my_password')
def my_checker(message):
    my_check_password(message)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "bot_pass":
        bot.send_message(
            call.message.chat.id, "Введи код, який ти будеш використовувати для доступу до своїх паролей. Запам'ятай чи запиши його🛑")
        chat_states[call.message.chat.id] = 'password_required'
        redis_client.set(f"temp_user_password:{call.message.chat.id}", "True")
    elif call.data == "new_pass":
        bot.send_message(
            call.message.chat.id, "Введи поточний код доступу")
        chat_states[call.message.chat.id] = 'current_pass'
    elif call.data == "gen_pass":
        bot.send_message(call.message.chat.id, "Виберіть параметри і натисність "
                                        "генерувати для створення надійних паролей🔑" , reply_markup=gen_markup)
    elif call.data in ["letters", "digits", "symbols"]:
        chat_id = call.message.chat.id
        if 'gen_markup_selections' not in chat_states:
            chat_states['gen_markup_selections'] = []
        chat_states['gen_markup_selections'].append(call.data)
    elif call.data == "generate_password":
        chat_id = call.message.chat.id
        if 'gen_markup_selections' in chat_states:
            selected_items = chat_states['gen_markup_selections']
            generated_passwords = generate_passwords(selected_items)
            password_text = "\n".join(generated_passwords)
            last_generated_password = password_text
            chat_states['last_generated_password'] = last_generated_password
            bot.send_message(
                chat_id, f"Згенерований пароль:\n  \n{password_text}",reply_markup=copy_markup)
    elif call.data == "main_menu":
        chat_id = call.message.chat.id
        bot.send_message(chat_id, "Тепер ви у головному меню",reply_markup=menu_markup)
        if 'gen_markup_selections' in chat_states:
            chat_states['gen_markup_selections'] = []
    elif call.data == "my_pass":
        bot.send_message(call.message.chat.id, "Введи поточний код доступу")
        chat_states[call.message.chat.id] = 'my_password'
    elif call.data == "save_pass":
        chat_id = call.message.chat.id
        bot.send_message(chat_id, "Введи логін до паролю, який ти хочеш зберегти👤")
        chat_states[chat_id] = {"state": "save_login", "login": None, "password": None}


@bot.message_handler(func=lambda message: chat_states.get(message.chat.id, {}).get("state") == "save_login")
def save_login(message):
    chat_id = message.chat.id
    chat_state = chat_states.get(chat_id, {})
    chat_state["login"] = message.text
    chat_state["state"] = "save_password"
    chat_states[chat_id] = chat_state
    bot.send_message(chat_id, "Введи пароль, який хочеш зберегти 🔐")


@bot.message_handler(func=lambda message: chat_states.get(message.chat.id, {}).get("state") == "save_password")
def save_password(message):
    chat_id = message.chat.id
    chat_state = chat_states.get(chat_id, {})
    chat_state["password"] = message.text

    login = chat_state["login"]
    password = chat_state["password"]

    save_to_database(chat_id, login, password)


    chat_state["state"] = None
    chat_state["login"] = None
    chat_state["password"] = None
    chat_states[chat_id] = chat_state

    bot.send_message(
        chat_id, "Логін та пароль збережено успішно!", reply_markup=menu_markup)

def save_to_database(user_id, login, password):
    data = {"user_id": user_id, "login": login, "password": password}
    collection.insert_one(data)

@bot.message_handler(func=lambda message: True)
def saver(message):
    save_password(message)"""
        
# RUN
bot.infinity_polling()