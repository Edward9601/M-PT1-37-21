from datetime import datetime

minutes = {00: 'ровно', 1: 'одна минута', 2: 'две минуты', 3: 'три минуты', 4: 'четыре минуты', 5: 'пять минут',
           6: 'шесть минут',
           7: 'семь минут', 8: 'восеми минут', 9: 'девять минут', 10: 'десять минут', 11: 'одинадцать минут',
           12: 'двенадцать минут', 13: 'двенадцать минут', 14: 'четырнадцать минут', 15: 'пятнадцать минут',
           16: 'шестнадцать минут', 17: 'семнадцать минут', 18: 'восемнадцать минут', 19: 'девятнадцать минут',
           20: 'двадцать минут', 21: 'двадцать одна минута', 22: 'двадцать две минуты', 23: 'двадцать три минуты',
           24: 'двадцать четыре минуты', 25: 'двадцать пять минут', 26: 'двадцать шесть минут',
           27: 'двадцать семь минут',
           28: 'двадцать восемь минут', 29: 'двадцать девять минут', 30: 'половина', 31: 'тридцать одна минута',
           32: 'тридцать две минуты', 33: 'тридцать три минуты', 34: 'тридцать четыре минуты',
           35: 'тридцать пять минут',
           36: 'тридцать шесть минут', 37: 'тридцать семь минут', 38: 'тридцать восемь минут',
           39: 'тридаць девять минут'}

minutes2 = {40: 'без двадцати минут', 41: 'без девятнадцати минут', 42: 'без восемнадцати минут',
            43: 'без восемнадцати минут',
            44: 'без шестнадцати минут', 45: 'без пятнадцати минут', 46: 'без четырнадцати минут',
            47: 'без тренадцати минут',
            48: 'без двенадцати минут', 49: 'без одинадцати минут', 50: 'без десяти минут', 51: 'без девяти минут',
            52: 'без восьми минут', 53: 'без семи минут', 54: 'без шести минут', 55: 'без пяти минут',
            56: 'без четырёх минут',
            57: 'без трёх минут', 58: 'без двух минут', 59: 'без одной минуты'}

hours = {1: 'час ночи', 2: 'два часа ночи', 3: 'три часа ночи', 4: 'четыре часа ночи',
         5: 'пять утра', 6: ' шесть часов утра', 7: 'семь часов утра', 8: 'восемь часов утра', 9: 'девять часов утра',
         10: 'десять часов утра', 11: 'одинадцать часов утра', 12: 'двенадцать часов дня ', 13: 'час дня', 14: 'два',
         15: 'три часа дня', 16: 'четыре часа дня', 17: 'пять часов вечера', 18: 'шесть часов вечера',
         19: 'семь часов вечера',
         20: 'восемь часов вечера', 21: 'девять часов вечера', 22: 'десять часов ночи', 23: 'одинадцать часов ночи',
         00: 'двенадцать часов ночи'}
hours2 = {1: 'первого ночи', 2: 'второго ночи', 3: 'третьего ночи', 4: 'четвертого ночи', 5: 'пятого утра',
          6: 'шестого утра',
          7: 'седьмого утра', 8: 'восьмого утра', 9: 'девятого утра', 10: 'десятого утра', 11: 'одинадцатого утра',
          12: 'двенадцатого дня', 13: 'первого дня', 14: 'второго дня', 15: 'третьего дня', 16: 'четвертого дня',
          17: 'пятого вечера', 18: 'шестого вечера', 19: 'седьмого вечера', 20: 'восьмого вечера',
          21: 'девятого вечера',
          22: 'десятого ночи', 23: 'одинадцатого ночи', 00: 'двенадцатого ночи'}
hours3 = {1: 'час ночи', 2: 'два ночи', 3: 'три ночи', 4: 'четыре ночи', 5: 'пять утра', 6: ' шесть утра',
          7: 'семь утра',
          8: 'восемь утра', 9: 'девять утра', 10: 'десять утра', 11: 'одинадцать утра', 12: 'двенадцать дня',
          13: 'час дня',
          14: 'два дня', 15: 'три дня', 16: 'четыре дня', 17: 'пять вечера', 18: 'шесть вечера', 19: 'семь вечера',
          20: 'восемь вечера', 21: 'девять вечера',
          22: 'десять ночи', 23: 'одинадцатьэ ночи', 00: 'двенадцать ночи'}

# спрашивает у пльзователя ввести время.
input_h = int(input('Введите время в часах: '))
input_m = int(input('Введите время в минутах: '))

# ищет варианты в словаре и выводит время в терминал.
try:
    if input_m == 30:
        t_h = hours2[input_h]
        t_m = minutes[input_m]
        print('Введённое время: {0} {1}'.format(t_m, t_h))
    elif input_m == 00:
        t_h = hours[input_h]
        t_m = minutes[input_m]
        print('Введённое время: {0} {1}'.format(t_m, t_h))
    elif input_m <= 39 and input_m != 30:
        t_h = hours[input_h]
        t_m = minutes[input_m]
        print('Введённое время: {0} и {1}'.format(t_h, t_m))
    elif input_m <= 59 or input_m >= 40:
        t_h = hours3[input_h + 1]
        t_m = minutes2[input_m]
        print('Введённое время: {0} {1}'.format(t_m, t_h))
except KeyError:
    print('Извините,возникла ошибка,попробуйте перезапустить программу и ввести время в формате 24 часа.')

# переводит нынешнее времяв строку.
now = datetime.today()
dt_string = now.strftime("%H:%M")
dt_spl = dt_string.split(':')
fir_ind = int(dt_spl[0])
sec_ind = int(dt_spl[1])

# ищет подходящий вариант в словаре и выводит на экран
if sec_ind == 30:
    t_h = hours2[fir_ind]
    t_m = minutes[sec_ind]
    print('Введённое время: {0} {1}'.format(t_m, t_h))
elif sec_ind == 00:
    t_h = hours[fir_ind]
    t_m = minutes[sec_ind]
    print('Введённое время: {0} {1}'.format(t_m, t_h))
elif sec_ind <= 29 or sec_ind <= 39 and sec_ind != 30:
    t_h = hours[fir_ind]
    t_m = minutes[sec_ind]
    print('Введённое время: {0} и {1}'.format(t_h, t_m))
elif sec_ind <= 59 or sec_ind >= 40:
    t_h = hours3[fir_ind + 1]
    t_m = minutes2[sec_ind]
    print('Введённое время: {0} {1}'.format(t_m, t_h))