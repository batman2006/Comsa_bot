from telebot import types

start_markup = types.InlineKeyboardMarkup()
start_markup.add(
    types.InlineKeyboardButton("Встановити код бота", callback_data="bot_pass"))

menu_markup = types.InlineKeyboardMarkup(row_width=1)
menu_markup.add(
    types.InlineKeyboardButton("Мої паролі", callback_data="my_pass"),
    types.InlineKeyboardButton("Зберегти пароль", callback_data="save_pass"),
    types.InlineKeyboardButton("Генератор паролей", callback_data="gen_pass"),
    types.InlineKeyboardButton("Змінити код доступу бота", callback_data="new_pass"))

gen_markup = types.InlineKeyboardMarkup(row_width=1)
gen_markup.add(
    types.InlineKeyboardButton(text="Літери", callback_data="letters"),
    types.InlineKeyboardButton(text="Цифри", callback_data="digits"),
    types.InlineKeyboardButton(text="Символи", callback_data="symbols"),
    types.InlineKeyboardButton(text="Згенерувати", callback_data="generate_password"))

copy_markup = types.InlineKeyboardMarkup(row_width=1)
copy_markup.add(
    types.InlineKeyboardButton(text="Згенерувати ще раз", callback_data="generate_password"),
    types.InlineKeyboardButton(text="Головне меню",callback_data="main_menu"))