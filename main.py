from telebot import types, TeleBot

import config
import timetable

bot = TeleBot(config.TOKEN)


# debug logs
# logger = telebot.logger
# telebot.logger.setLevel()

# Обработчик команд '/start'.
@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_btn_start = types.KeyboardButton('Старт')
    markup.row(item_btn_start)
    bot.send_message(message.chat.id, text='Привет! Я бот.', reply_markup=markup)


@bot.message_handler(commands=["help"])
def send_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_btn_menu = types.KeyboardButton('Меню')
    markup.row(item_btn_menu)
    bot.send_message(message.chat.id, text=config.TxtHelp, reply_markup=markup)


# Обработчик команд "/menu", "Меню" и "Старт"
@bot.message_handler(commands=["menu"])
@bot.message_handler(func=lambda message: message.text == 'Старт' or message.text == 'Меню')
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_btn_select = types.KeyboardButton('Расписание')
    item_btn_news = types.KeyboardButton('Новости')
    item_btn_settings = types.KeyboardButton('Настройки')
    markup.row(item_btn_select, item_btn_news)
    markup.row(item_btn_settings)
    bot.send_message(message.chat.id, text='Выберите категорию 👇', reply_markup=markup)


# Обработчик команды "Настройки"
@bot.message_handler(commands=["settings"])
@bot.message_handler(func=lambda message: message.text == 'Настройки')
def settings(message):
    gif = open('./img/gifdev.gif', 'rb')
    bot.send_document(message.chat.id, gif, caption='В разработке')


# Обработчик команд 'Расписание',"/timetable".
@bot.message_handler(commands=["timetable"])
@bot.message_handler(func=lambda message: message.text == 'Расписание')
def select_timetable(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_btn_42 = types.KeyboardButton('42')
    item_btn_46 = types.KeyboardButton('46')
    item_btn_47 = types.KeyboardButton('47')
    item_btn_32 = types.KeyboardButton('32')
    item_btn_36 = types.KeyboardButton('36')
    item_btn_37 = types.KeyboardButton('37')
    item_btn_22 = types.KeyboardButton('22')
    item_btn_26_1 = types.KeyboardButton('26.1')
    item_btn_26_2 = types.KeyboardButton('26.2')
    item_btn_12 = types.KeyboardButton('12')
    item_btn_16 = types.KeyboardButton('16')
    item_btn_menu = types.KeyboardButton('Меню')
    markup.row(item_btn_42, item_btn_46, item_btn_47)
    markup.row(item_btn_32, item_btn_36, item_btn_37)
    markup.row(item_btn_22, item_btn_26_1, item_btn_26_2)
    markup.row(item_btn_12, item_btn_16)
    markup.row(item_btn_menu)
    bot.send_message(message.chat.id, text='Выберите группу 👇', reply_markup=markup)


# Обработчик команд "Новости", "/news"
@bot.message_handler(commands=["news"])
@bot.message_handler(func=lambda message: message.text == 'Новости')
def news(message):
    gif = open('./img/gifdev.gif', 'rb')
    bot.send_document(message.chat.id, gif, caption='В разработке')


# Обработчик команд "46", "/46"
@bot.message_handler(commands=["46"])
@bot.message_handler(func=lambda message: message.text == '46')
def get_table(message):
    return timetable.getTable(message, dcx=1, pcx=2, scx=21, ccx=22)


# Обработчик команд "47", "/47"
@bot.message_handler(commands=["47"])
@bot.message_handler(func=lambda message: message.text == '47')
def get_table(message):
    return timetable.getTable(message, dcx=1, pcx=2, scx=23, ccx=24)


# Обработчик команд "42", "/42"
@bot.message_handler(commands=["42"])
@bot.message_handler(func=lambda message: message.text == '42')
def get_table(message):
    return timetable.getTable(message, dcx=1, pcx=2, scx=19, ccx=20)


# Обработчик команд "36", "/36"
@bot.message_handler(commands=["36"])
@bot.message_handler(func=lambda message: message.text == '36')
def get_table(message):
    return timetable.getTable(message, dcx=1, pcx=2, scx=15, ccx=16)


# Обработчик команд "37", "/37"
@bot.message_handler(commands=["37"])
@bot.message_handler(func=lambda message: message.text == '37')
def get_table(message):
    return timetable.getTable(message, dcx=1, pcx=2, scx=17, ccx=18)


# Обработчик команд "32", "/32"
@bot.message_handler(commands=["32"])
@bot.message_handler(func=lambda message: message.text == '32')
def get_table(message):
    return timetable.getTable(message, dcx=1, pcx=2, scx=13, ccx=14)


# Обработчик команд "12", "/12"
@bot.message_handler(commands=["12"])
@bot.message_handler(func=lambda message: message.text == '12')
def get_table(message):
    return timetable.getTable(message, dcx=1, pcx=2, scx=3, ccx=4)


# Обработчик команд "16", "/16"
@bot.message_handler(commands=["16"])
@bot.message_handler(func=lambda message: message.text == '16')
def get_table(message):
    return timetable.getTable(message, dcx=1, pcx=2, scx=5, ccx=6)


# Обработчик команд "22", "/22"
@bot.message_handler(commands=["22"])
@bot.message_handler(func=lambda message: message.text == '22')
def get_table(message):
    return timetable.getTable(message, dcx=1, pcx=2, scx=7, ccx=8)


# Обработчик команд "26.1", "/26_1"
@bot.message_handler(commands=["26_1"])
@bot.message_handler(func=lambda message: message.text == '26.1')
def get_table(message):
    return timetable.getTable(message, dcx=1, pcx=2, scx=9, ccx=10)


# Обработчик команд "26.2", "/26_2"
@bot.message_handler(commands=["26_2"])
@bot.message_handler(func=lambda message: message.text == '26.2')
def get_table(message):
    return timetable.getTable(message, dcx=1, pcx=2, scx=11, ccx=12)

if __name__ == '__main__':
    bot.polling(none_stop=True)
