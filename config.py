from urllib.parse import quote_plus
#krstc_bot TOKEN
# token = '224271945:AAEfyP6SPVABPWrinypP0xokd5RjIyxdY-g'

#krstcTest_bot Token
token = '244694359:AAH5ZEaFZUKVU5yKqAKT_zOLTQLqT_jOJfg'
source_xls = "Rechnaya.xls"
url = 'http://www.krstc.ru/site/www/raspis/{0}.xls'.format(quote_plus('Речная'))
file = 'Rechnaya.xls'


# BotFather
set_commands = """
menu - Меню
help - Помощь
news - Новости
timetable - Расписание
12 - Расписание 12 группы
16 - Расписание 16 группы
22 - Расписание 22 группы
26_1 - Расписание 26.1 группы
26_2 - Расписание 26.2 группы
32 - Расписание 32 группы
36 - Расписание 36 группы
37 - Расписание 37 группы
42 - Расписание 42 группы
46 - Расписание 46 группы
47 - Расписание 47 группы
"""