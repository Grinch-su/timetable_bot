import socket
from urllib.request import urlretrieve

import xlrd

import config
from main import bot


def getTable(message, dcx=int, pcx=int, scx=int, ccx=int):
    timeout = 10
    socket.setdefaulttimeout(timeout)
    bot.send_message(message.chat.id, 'Загрузка файла 🔄')
    urlretrieve(config.URL, config.FILE)
    open_xls = xlrd.open_workbook(config.SOURCE_XLS, on_demand=True, formatting_info=True)
    open_sheet = open_xls.sheet_by_index(0)
    bot.send_message(message.chat.id, open_sheet.cell_value(0, 5))
    day = open_sheet.col_values(colx=dcx, start_rowx=7, end_rowx=20)
    period = open_sheet.col_values(colx=pcx, start_rowx=7, end_rowx=20)
    subject = open_sheet.col_values(colx=scx, start_rowx=7, end_rowx=20)
    cabinet = open_sheet.col_values(colx=ccx, start_rowx=7, end_rowx=20)
    cabinet = list(map(str, cabinet))
    lessons = [day, period, subject, cabinet]
    lessons = list(zip(*lessons))
    for row in lessons:
        if any(row):bot.send_message(message.chat.id, '\n'.join(row))
