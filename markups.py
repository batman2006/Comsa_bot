from telebot import types

start_markup = types.InlineKeyboardMarkup()
start_markup.add(types.InlineKeyboardButton("🟨BNB🟨", callback_data="BNB"))
start_markup.add(types.InlineKeyboardButton("🛑TRX🛑", callback_data="TRX"))
start_markup.add(types.InlineKeyboardButton("💜MATIC💜", callback_data="MATIC"))
start_markup.add(types.InlineKeyboardButton("♻️SOL♻️", callback_data="SOL"))
start_markup.add(types.InlineKeyboardButton("🌐ETH🌐", callback_data="ETH"))
start_markup.add(types.InlineKeyboardButton("💎SUI💎", callback_data="SUI"))
start_markup.add(types.InlineKeyboardButton("⚫️APTOS⚫️", callback_data="APTOS"))
start_markup.add(types.InlineKeyboardButton("Мій профіль👤", callback_data="profile"))

quantity_markup = types.InlineKeyboardMarkup()
quantity_markup.add(types.InlineKeyboardButton("Ввести суму в гривнях 🇺🇦", callback_data="grn"))
quantity_markup.add(types.InlineKeyboardButton("Ввести суму в доларах 🇺🇸", callback_data="usd"))
quantity_markup.add(types.InlineKeyboardButton("Повернутись назад ⬅️", callback_data="back"))

address_markup = types.InlineKeyboardMarkup()
address_markup.add(types.InlineKeyboardButton("Повернутись назад ⬅️", callback_data="back"))

profile_markup = types.InlineKeyboardMarkup()
profile_markup.add(types.InlineKeyboardButton("Реферальна система 👥", callback_data="refs"))
profile_markup.add(types.InlineKeyboardButton("Статистика обмінів 📊", callback_data="stats"))
profile_markup.add(types.InlineKeyboardButton("Повернутись назад ⬅️", callback_data="back"))