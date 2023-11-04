from telebot import types

start_markup = types.InlineKeyboardMarkup()
start_markup.add(types.InlineKeyboardButton("BNB", callback_data="bnb"))
start_markup.add(types.InlineKeyboardButton("TRX", callback_data="trx"))
start_markup.add(types.InlineKeyboardButton("MATIC", callback_data="pol"))
start_markup.add(types.InlineKeyboardButton("SOL", callback_data="sol"))
start_markup.add(types.InlineKeyboardButton("ETH", callback_data="eth"))
start_markup.add(types.InlineKeyboardButton("SUI", callback_data="sui"))
start_markup.add(types.InlineKeyboardButton("APTOS", callback_data="aptos"))
start_markup.add(types.InlineKeyboardButton("Баланс", callback_data="balance"))