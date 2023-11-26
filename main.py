import telebot
from connections import bot_token
from markups import start_markup, quantity_markup, address_markup, profile_markup , grn_markup , usd_markup , sure_markup

user_data = {}
form_status = None
currency_status = None

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт👋 Обери криптовалюту , яку хочеш купити або можеш перевірити свій баланс", reply_markup=start_markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    global form_status , chosen_coin
    chat_id = call.message.chat.id

    if call.data == 'back':
        if form_status == 'quantity':
            bot.send_message(chat_id, "Обери криптовалюту, яку хочеш купити або можеш перевірити свій баланс🤝", reply_markup=start_markup)
            form_status = None
        elif form_status == 'address':
            chosen_coin = user_data[chat_id]['coin']
            bot.send_message(chat_id, f"Обрано {chosen_coin}. Введіть потрібну кількість 🔢", reply_markup=quantity_markup)
            form_status = 'quantity'
        elif form_status == 'profile':
            bot.send_message(chat_id, "Обери криптовалюту, яку хочеш купити або можеш перевірити свій баланс🤝", reply_markup=start_markup)
            form_status = None
        elif 'markup' in form_status:  # assuming the status contains "markup"
            bot.send_message(chat_id, f"Обрано {chosen_coin}. Введіть потрібну кількість 🔢", reply_markup=quantity_markup)
            form_status = 'quantity'
    elif call.data in ['BNB', 'TRX', 'MATIC', 'SOL', 'ETH', 'SUI', 'APTOS']:
        bot.send_message(chat_id, f"Обрано {call.data}. Введіть потрібну кількість 🔢", reply_markup=quantity_markup)
        user_data[chat_id] = {'coin': call.data, 'status': 'filling'}
        form_status = "quantity"
    elif call.data in ['grn', 'usd']:
        chosen_coin = user_data[chat_id]['coin']  # Retrieve the chosen coin from user_data
        if call.data == 'grn':
            bot.send_message(chat_id, f"Обрано гривні. Введіть вартість потрібної вам кількості в гривнях", reply_markup=quantity_markup)
        elif call.data == 'usd':
            bot.send_message(chat_id, f"Обрано долари. Введіть вартість потрібної вам кількості в доларах", reply_markup=quantity_markup)
        user_data[chat_id] = {'coin': chosen_coin, 'status': 'filling'}
        form_status = "markup"  # Change form_status to 'markup'
    elif call.data in ['profile']:
        bot.send_message(chat_id, "Переглянь свою статистику або скористайся реферальною системою🤝", reply_markup=profile_markup)

@bot.message_handler(func=lambda message: message.chat.id in user_data and form_status == "quantity")
def handle_quantity(message):
    global form_status
    chat_id = message.chat.id
    text = message.text.lower()
    chosen_coin = user_data[chat_id]['coin']

    if text == 'back':
        bot.send_message(chat_id, f"Обрано {chosen_coin}. Введіть потрібну кількість 🔢", reply_markup=quantity_markup)
        form_status = 'quantity'
    else:
        quantity = message.text
        user_data[chat_id]['quantity'] = quantity
        bot.send_message(chat_id, f"Введіть вашу адресу для отримання {chosen_coin} 💌", reply_markup=address_markup)
        form_status = "address"

@bot.message_handler(func=lambda message: message.chat.id in user_data and form_status == 'address')
def handle_address(message):
    global form_status
    chat_id = message.chat.id
    address = message.text
    user_data[chat_id]['address'] = address
    user_data[chat_id]['status'] = 'complete'
    bot.send_message(chat_id, "◾️ Я впевнений в покупці криптовалюти.                                         ◾️ Я оплачую з своєї банківської карти.", reply_markup=sure_markup)
    form_status = "sure"


# RUN
bot.infinity_polling()