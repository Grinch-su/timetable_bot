__author__ = "Gregory Fedorov"
__copyright__ = "Copyright 2016, All rights reserved."
__version__ = "1.0.0"
__mail__= "grinchfedorov@gmail.com"
__status__ = "Production"
# from logging import DEBUG
import socket

from urllib.request import urlretrieve

import xlrd
import telebot
from telebot import types

import config

bot = telebot.TeleBot(config.token)

# debug logs
# logger = telebot.logger
# telebot.logger.setLevel(DEBUG)


txtHelp = """
Команды:
Меню - /menu
Помощь - /help
Новости - /news
Распиание - /timetable
Расписание 12 группы - /12
Расписание 16 группы - /16
Расписание 22 группы - /22
Расписание 26.1 группы - /26_1
Расписание 26.2 группы - /26_2
Расписание 32 группы - /32
Расписание 36 группы - /36
Расписание 37 группы - /37
Расписание 42 группы - /42
Расписание 46 группы - /46
Расписание 47 группы - /47
"""

# Обработчик команд '/start'.
@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_btn_start = types.KeyboardButton('Старт')
    markup.row(item_btn_start)
    bot.send_message(message.chat.id,text='Привет! Я бот.', reply_markup=markup)

@bot.message_handler(commands=["help"])
def send_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_btn_menu = types.KeyboardButton('Меню')
    markup.row(item_btn_menu)
    bot.send_message(message.chat.id, text=txtHelp, reply_markup=markup)

# Обработчик команд "/menu", "Меню" и "Старт"
@bot.message_handler(commands=["menu"])
@bot.message_handler(func=lambda message: message.text == 'Старт' or message.text == 'Меню')
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_btn_select = types.KeyboardButton('Расписание')
    item_btn_news = types.KeyboardButton('Новости')
    item_btn_settings = types.KeyboardButton('Настройки')
    markup.row(item_btn_select,item_btn_news)
    markup.row(item_btn_settings)
    bot.send_message(message.chat.id,text='Выберите категорию 👇', reply_markup=markup)

# Обработчик команды "Настройки"
@bot.message_handler(commands=["settings"])
@bot.message_handler(func=lambda message: message.text == 'Настройки')
def settings(message):
    gif = open('./img/gifdev.gif','rb')
    bot.send_document(message.chat.id,gif,caption='В разработке')

# Обработчик команд 'Расписание',"/timetable".
@bot.message_handler(commands=["timetable"])
@bot.message_handler(func=lambda message: message.text == 'Расписание')
def select_timetable(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_btn_42 = types.KeyboardButton('42');item_btn_46 = types.KeyboardButton('46');item_btn_47 = types.KeyboardButton('47')
    item_btn_32 = types.KeyboardButton('32');item_btn_36 = types.KeyboardButton('36');item_btn_37 = types.KeyboardButton('37')
    item_btn_22 = types.KeyboardButton('22');item_btn_26_1 = types.KeyboardButton('26.1');item_btn_26_2 = types.KeyboardButton('26.2')
    item_btn_12 = types.KeyboardButton('12');item_btn_16 = types.KeyboardButton('16')
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
    gif = open('./img/gifdev.gif','rb')
    bot.send_document(message.chat.id,gif,caption='В разработке')

# Обработчик команд "46", "/46"
@bot.message_handler(commands=["46"])
@bot.message_handler(func=lambda message: message.text == '46')
def get_table(message):
    timeout = 10
    socket.setdefaulttimeout(timeout)

    bot.send_message(message.chat.id, 'Загрузка файла с сервера 🔄')
    urlretrieve(config.url, config.file)
    open_xls = xlrd.open_workbook(config.source_xls, on_demand=True, formatting_info=True)
    open_sheet = open_xls.sheet_by_index(0)
    bot.send_message(message.chat.id, open_sheet.cell_value(0, 5))
    day = (open_sheet.col_values(colx=1, start_rowx=7, end_rowx=20))
    period = (open_sheet.col_values(colx=2, start_rowx=7, end_rowx=20))
    subject = open_sheet.col_values(colx=21, start_rowx=4, end_rowx=15)
    cabinet = open_sheet.col_values(colx = 22, start_rowx = 7, end_rowx = 15)
    cabinet = list(map(str,cabinet))
    lessons = []
    lessons.append(day)
    lessons.append(period)
    lessons.append(subject)
    lessons.append(cabinet)
    lessons = list(zip(*lessons))
    for row in lessons:
        if any(row):
            bot.send_message(message.chat.id,' '.join(row))

# Обработчик команд "47", "/47"
@bot.message_handler(commands=["47"])
@bot.message_handler(func=lambda message: message.text == '47')
def get_table(message):
    timeout = 10
    socket.setdefaulttimeout(timeout)

    bot.send_message(message.chat.id, 'Загрузка файла с сервера 🔄')
    urlretrieve(config.url, config.file)

    open_xls = xlrd.open_workbook(config.source_xls, on_demand=True, formatting_info=True)
    open_sheet = open_xls.sheet_by_index(0)
    bot.send_message(message.chat.id, open_sheet.cell_value(0, 5))
    day = (open_sheet.col_values(colx=1, start_rowx=7, end_rowx=20))
    period = (open_sheet.col_values(colx=2, start_rowx=7, end_rowx=20))
    subject = open_sheet.col_values(colx=23, start_rowx=7, end_rowx=15)
    cabinet = open_sheet.col_values(colx = 24, start_rowx = 7, end_rowx = 15)
    cabinet = list(map(str,cabinet))
    lessons = []
    lessons.append(day)
    lessons.append(period)
    lessons.append(subject)
    lessons.append(cabinet)
    lessons = list(zip(*lessons))
    for row in lessons:
        if any(row):
            bot.send_message(message.chat.id,' '.join(row))
# Обработчик команд "42", "/42"
@bot.message_handler(commands=["42"])
@bot.message_handler(func=lambda message: message.text == '42')
def get_table(message):
    timeout = 10
    socket.setdefaulttimeout(timeout)

    bot.send_message(message.chat.id, 'Загрузка файла с сервера 🔄')
    urlretrieve(config.url, config.file)
    open_xls = xlrd.open_workbook(config.source_xls, on_demand=True, formatting_info=True)
    open_sheet = open_xls.sheet_by_index(0)
    bot.send_message(message.chat.id, open_sheet.cell_value(0, 5))
    day = (open_sheet.col_values(colx=1, start_rowx=7, end_rowx=20))
    period = (open_sheet.col_values(colx=2, start_rowx=7, end_rowx=20))
    subject = open_sheet.col_values(colx=19, start_rowx=7, end_rowx=15)
    cabinet = open_sheet.col_values(colx = 20, start_rowx = 7, end_rowx = 15)
    cabinet = list(map(str,cabinet))
    lessons = []
    lessons.append(day)
    lessons.append(period)
    lessons.append(subject)
    lessons.append(cabinet)
    lessons = list(zip(*lessons))
    for row in lessons:
        if any(row):
            bot.send_message(message.chat.id,' '.join(row))

# Обработчик команд "36", "/36"
@bot.message_handler(commands=["36"])
@bot.message_handler(func=lambda message: message.text == '36')
def get_table(message):
    timeout = 10
    socket.setdefaulttimeout(timeout)

    bot.send_message(message.chat.id, 'Загрузка файла с сервера 🔄')
    urlretrieve(config.url, config.file)
    open_xls = xlrd.open_workbook(config.source_xls, on_demand=True,formatting_info=True)
    open_sheet = open_xls.sheet_by_index(0)
    bot.send_message(message.chat.id, open_sheet.cell_value(0, 5))
    day = (open_sheet.col_values(colx=1, start_rowx=7, end_rowx=20))
    period = (open_sheet.col_values(colx=2, start_rowx=7, end_rowx=20))
    subject = open_sheet.col_values(colx = 15,start_rowx = 7,end_rowx = 15)
    cabinet = open_sheet.col_values(colx = 16, start_rowx = 7, end_rowx = 15)
    cabinet = list(map(str,cabinet))
    lessons = []
    lessons.append(day)
    lessons.append(period)
    lessons.append(subject)
    lessons.append(cabinet)
    lessons = list(zip(*lessons))
    for row in lessons:
        if any(row):
            bot.send_message(message.chat.id,' '.join(row))

# Обработчик команд "37", "/37"
@bot.message_handler(commands=["37"])
@bot.message_handler(func=lambda message: message.text == '37')
def get_table(message):
    timeout = 10
    socket.setdefaulttimeout(timeout)

    bot.send_message(message.chat.id, 'Загрузка файла с сервера 🔄')
    urlretrieve(config.url, config.file)
    open_xls = xlrd.open_workbook(config.source_xls, on_demand=True, formatting_info=True)
    open_sheet = open_xls.sheet_by_index(0)
    bot.send_message(message.chat.id, open_sheet.cell_value(0, 5))
    day = (open_sheet.col_values(colx=1, start_rowx=7, end_rowx=20))
    period = (open_sheet.col_values(colx=2, start_rowx=7, end_rowx=20))
    subject = open_sheet.col_values(colx=17, start_rowx=7, end_rowx=15)
    cabinet = open_sheet.col_values(colx = 18, start_rowx = 7, end_rowx = 15)
    cabinet = list(map(str,cabinet))
    lessons = []
    lessons.append(day)
    lessons.append(period)
    lessons.append(subject)
    lessons.append(cabinet)
    lessons = list(zip(*lessons))
    for row in lessons:
        if any(row):
            bot.send_message(message.chat.id,' '.join(row))
# Обработчик команд "32", "/32"
@bot.message_handler(commands = ["32"])
@bot.message_handler(func=lambda message: message.text == '32')
def get_table(message):
    timeout = 10
    socket.setdefaulttimeout(timeout)

    bot.send_message(message.chat.id, 'Загрузка файла с сервера 🔄')
    urlretrieve(config.url, config.file)
    open_xls = xlrd.open_workbook(config.source_xls, on_demand=True, formatting_info=True)
    open_sheet = open_xls.sheet_by_index(0)
    bot.send_message(message.chat.id, open_sheet.cell_value(0, 5))
    day = (open_sheet.col_values(colx=1, start_rowx=7, end_rowx=20))
    period = (open_sheet.col_values(colx=2, start_rowx=7, end_rowx=20))
    subject = open_sheet.col_values(colx=13, start_rowx=7, end_rowx=15)
    cabinet = open_sheet.col_values(colx = 14, start_rowx = 7, end_rowx = 15)
    cabinet = list(map(str,cabinet))
    lessons = []
    lessons.append(day)
    lessons.append(period)
    lessons.append(subject)
    lessons.append(cabinet)
    lessons = list(zip(*lessons))
    for row in lessons:
        if any(row):
            bot.send_message(message.chat.id,' '.join(row))

# Обработчик команд "12", "/12"
@bot.message_handler(commands=["12"])
@bot.message_handler(func=lambda message: message.text == '12')
def get_table(message):
    timeout = 10
    socket.setdefaulttimeout(timeout)

    bot.send_message(message.chat.id, 'Загрузка файла с сервера 🔄')
    urlretrieve(config.url, config.file)
    open_xls = xlrd.open_workbook(config.source_xls, on_demand=True, formatting_info=True)
    open_sheet = open_xls.sheet_by_index(0)
    bot.send_message(message.chat.id, open_sheet.cell_value(0, 5))
    day = (open_sheet.col_values(colx=1, start_rowx=7, end_rowx=20))
    period = (open_sheet.col_values(colx=2, start_rowx=7, end_rowx=20))
    subject = open_sheet.col_values(colx=3, start_rowx=7, end_rowx=15)
    cabinet = open_sheet.col_values(colx = 4, start_rowx = 7, end_rowx = 15)
    cabinet = list(map(str,cabinet))
    lessons = []
    lessons.append(day)
    lessons.append(period)
    lessons.append(subject)
    lessons.append(cabinet)
    lessons = list(zip(*lessons))
    for row in lessons:
        if any(row):
            bot.send_message(message.chat.id,' '.join(row))

# Обработчик команд "16", "/16"
@bot.message_handler(commands=["16"])
@bot.message_handler(func=lambda message: message.text == '16')
def get_table(message):
    timeout = 10
    socket.setdefaulttimeout(timeout)

    bot.send_message(message.chat.id, 'Загрузка файла с сервера 🔄')
    urlretrieve(config.url, config.file)
    open_xls = xlrd.open_workbook(config.source_xls, on_demand=True, formatting_info=True)
    open_sheet = open_xls.sheet_by_index(0)
    bot.send_message(message.chat.id, open_sheet.cell_value(0, 5))
    day = (open_sheet.col_values(colx=1, start_rowx=7, end_rowx=20))
    period = (open_sheet.col_values(colx=2, start_rowx=7, end_rowx=20))
    subject = open_sheet.col_values(colx=5, start_rowx=7, end_rowx=15)
    cabinet = open_sheet.col_values(colx = 6, start_rowx = 7, end_rowx = 15)
    cabinet = list(map(str,cabinet))
    lessons = []
    lessons.append(day)
    lessons.append(period)
    lessons.append(subject)
    lessons.append(cabinet)
    lessons = list(zip(*lessons))
    for row in lessons:
        if any(row):
            bot.send_message(message.chat.id,' '.join(row))

# Обработчик команд "22", "/22"
@bot.message_handler(commands=["22"])
@bot.message_handler(func=lambda message: message.text == '22')
def get_table(message):
    timeout = 10
    socket.setdefaulttimeout(timeout)

    bot.send_message(message.chat.id, 'Загрузка файла с сервера 🔄')
    urlretrieve(config.url, config.file)
    open_xls = xlrd.open_workbook(config.source_xls, on_demand=True, formatting_info=True)
    open_sheet = open_xls.sheet_by_index(0)
    bot.send_message(message.chat.id, open_sheet.cell_value(0, 5))
    day = (open_sheet.col_values(colx=1, start_rowx=7, end_rowx=20))
    period = (open_sheet.col_values(colx=2, start_rowx=7, end_rowx=20))
    subject = open_sheet.col_values(colx=7, start_rowx=7, end_rowx=15)
    cabinet = open_sheet.col_values(colx = 8, start_rowx = 7, end_rowx = 15)
    cabinet = list(map(str,cabinet))
    lessons = []
    lessons.append(day)
    lessons.append(period)
    lessons.append(subject)
    lessons.append(cabinet)
    lessons = list(zip(*lessons))
    for row in lessons:
        if any(row):
            bot.send_message(message.chat.id,' '.join(row))

# Обработчик команд "26.1", "/26_1"
@bot.message_handler(commands=["26_1"])
@bot.message_handler(func=lambda message: message.text == '26.1')
def get_table(message):
    timeout = 10
    socket.setdefaulttimeout(timeout)

    bot.send_message(message.chat.id, 'Загрузка файла с сервера 🔄')
    urlretrieve(config.url, config.file)
    open_xls = xlrd.open_workbook(config.source_xls, on_demand=True, formatting_info=True)
    open_sheet = open_xls.sheet_by_index(0)
    bot.send_message(message.chat.id, open_sheet.cell_value(0, 5))
    day = (open_sheet.col_values(colx=1, start_rowx=7, end_rowx=20))
    period = (open_sheet.col_values(colx=2, start_rowx=7, end_rowx=20))
    subject = open_sheet.col_values(colx = 9, start_rowx = 7, end_rowx = 15)
    cabinet = open_sheet.col_values(colx = 10, start_rowx = 7, end_rowx = 15)
    cabinet = list(map(str,cabinet))
    lessons = []
    lessons.append(day)
    lessons.append(period)
    lessons.append(subject)
    lessons.append(cabinet)
    lessons = list(zip(*lessons))
    for row in lessons:
        if any(row):
            bot.send_message(message.chat.id,' '.join(row))

# Обработчик команд "26.2", "/26_2"
@bot.message_handler(commands=["26_2"])
@bot.message_handler(func=lambda message: message.text == '26.2')
def get_table(message):
    timeout = 10
    socket.setdefaulttimeout(timeout)

    bot.send_message(message.chat.id, 'Загрузка файла с сервера 🔄')
    urlretrieve(config.url, config.file)
    open_xls = xlrd.open_workbook(config.source_xls, on_demand = True, formatting_info = True)
    open_sheet = open_xls.sheet_by_index(0)
    bot.send_message(message.chat.id, open_sheet.cell_value(0, 5))
    day = (open_sheet.col_values(colx=1, start_rowx=7, end_rowx=20))
    period = (open_sheet.col_values(colx=2, start_rowx=7, end_rowx=20))
    subject = open_sheet.col_values(colx = 11, start_rowx = 7, end_rowx =20)
    cabinet = open_sheet.col_values(colx=12, start_rowx=7, end_rowx=20)
    cabinet = list(map(str,cabinet))
    lessons = []
    lessons.append(day)
    lessons.append(period)
    lessons.append(subject)
    lessons.append(cabinet)
    lessons = list(zip(*lessons))
    for row in lessons:
        if any(row):
            bot.send_message(message.chat.id,' '.join(row))

if __name__ == '__main__':
    bot.polling(none_stop = True)