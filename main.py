import telebot
from connections import bot_token
from telebot import types

user_data = {}

#start_markup
start_markup = types.InlineKeyboardMarkup()
start_markup.add(types.InlineKeyboardButton("🟨BNB🟨", callback_data="bnb"))
start_markup.add(types.InlineKeyboardButton("🛑TRX🛑", callback_data="trx"))
start_markup.add(types.InlineKeyboardButton("💜MATIC💜", callback_data="pol"))
start_markup.add(types.InlineKeyboardButton("♻️SOL♻️", callback_data="sol"))
start_markup.add(types.InlineKeyboardButton("🌐ETH🌐", callback_data="eth"))
start_markup.add(types.InlineKeyboardButton("💎SUI💎", callback_data="sui"))
start_markup.add(types.InlineKeyboardButton("⚫️APTOS⚫️", callback_data="aptos"))
start_markup.add(types.InlineKeyboardButton("Баланс👤", callback_data="balance"))

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт👋 Обери криптовалюту , яку хочеш купити або можеш перевірити свій баланс",reply_markup=start_markup)
        
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    chat_id = call.message.chat.id
    if call.data in ['bnb', 'trx', 'pol', 'sol', 'eth', 'sui', 'aptos']:
        bot.send_message(chat_id, f"Обрано {call.data}. Введіть кількість:")
        user_data[chat_id] = {'coin': call.data, 'status': 'quantity'}
    elif call.data == 'balance':
        pass

@bot.message_handler(func=lambda message: message.chat.id in user_data and user_data[message.chat.id]['status'] == 'quantity')
def handle_quantity(message):
    chat_id = message.chat.id
    quantity = message.text
    # Store quantity and ask for address
    user_data[chat_id]['quantity'] = quantity
    bot.send_message(chat_id, "Введіть адресу:")
    user_data[chat_id]['status'] = 'address'

@bot.message_handler(func=lambda message: message.chat.id in user_data and user_data[message.chat.id]['status'] == 'address')
def handle_address(message):
    chat_id = message.chat.id
    address = message.text
    # Store address and update status
    user_data[chat_id]['address'] = address
    user_data[chat_id]['status'] = 'pending_approval'
    
    # Send order information to the admin for confirmation
    order_info = f"Новий ордер:\nКористувач: {chat_id}\nМонета: {user_data[chat_id]['coin']}\nКількість: {user_data[chat_id]['quantity']}\nАдреса: {address}"
    bot.send_message(admin_chat_id, order_info)
    bot.send_message(chat_id, "Замовлення надіслано на розгляд адміністратору. Очікуйте підтвердження.")

@bot.message_handler(commands=['confirm'])
def confirm_order(message):
    if message.chat.id == admin_chat_id:
        # Get user_id from the command arguments
        try:
            user_id = int(message.text.split()[1])
            if user_id in user_data and user_data[user_id]['status'] == 'pending_approval':
                # Perform the transfer operation here
                # ...
                bot.send_message(user_id, "Ваше замовлення підтверджено та виконано.")
                del user_data[user_id]  # Clear user data after processing the order
            else:
                bot.send_message(admin_chat_id, "Неправильний користувач або статус замовлення.")
        except (IndexError, ValueError):
            bot.send_message(admin_chat_id, "Неправильний формат команди.")
    else:
        bot.send_message(message.chat.id, "Недостатні права.")

        
# RUN
bot.infinity_polling()