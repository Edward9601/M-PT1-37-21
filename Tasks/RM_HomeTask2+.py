# Вывод текстом времени

from datetime import datetime
now = datetime.now()

print(f'Текущее время: \n {now.strftime("%H:%M")}')

# Словари значений

d_pol = {(1, 13): 'второго', 
         (2, 14): 'третьего', 
         (3, 15): 'четвертого', 
         (4, 16): 'пятого', 
         (5, 17): 'шестого', 
         (6, 18): 'седьмого', 
         (7, 19): 'восьмого', 
         (8, 20): 'девятого', 
         (9, 21): 'десятого', 
         (10, 22): 'одиннадцатого', 
         (11, 23): 'двенадцатого', 
         (0, 12): 'первого'}

dict_hour = {1: 'один', 
             2: 'два', 
             3: 'три', 
             4: 'четыре', 
             5: 'пять', 
             6: 'шесть', 
             7: 'семь', 
             8: 'восемь', 
             9: 'девять', 
             10: 'десять', 
             11: 'одиннадцать',
             12: 'двеннадцать', 
             13: 'тринадцать', 
             14: 'четырнадцать', 
             15: 'пятнадцать', 
             16: 'шестнадцать', 
             17: 'семнадцать', 
             18: 'восемнадцать',
             19: 'девятнадцать', 
             20: 'двадцать', 
             21: 'двадцать один', 
             22: 'двадцать два', 
             23: 'двадцать три', 
             0: 'ноль '}

dict_min = {0: 'ноль', 
            1: 'одна', 
            2: 'две', 
            3: 'три', 
            4: 'четыре', 
            5: 'пять', 
            6: 'шесть', 
            7: 'семь', 
            8: 'восемь', 
            9: 'девять', 
            10: 'десять',
            11: 'одиннадцать', 
            12: 'двеннадцать', 
            13: 'тринадцать', 
            14: 'четырнадцать', 
            15: 'пятнадцать', 
            16: 'шестнадцать', 
            17: 'семнадцать',
            18: 'восемнадцать', 
            19: 'девятнадцать',
            20: 'двадцать'}

d_0 = {2: 'двадцать', 
       3: 'тридцать', 
       4: 'сорок', 
       5: 'пятьдесят'}

d_bez = {30: 'половина', 
         40: 'без двадцати', 
         45: 'без пятнадцати', 
         50: 'без десяти', 
         55: 'без пяти'}

d_h = {(1, 21): 'час',  
       (2, 3, 4, 22, 23): 'часа', 
       (0,) : 'часов', 
       tuple (i for i in range(5,21)): 'часов'}

d_m = {(1,): 'минута', 
       (2, 3, 4,): 'минуты', 
       tuple (i for i in range(5,21)): 'минут',
       (0,): 'минут'}

l_bez = [30, 40, 45, 50, 55]                          # Список исключений



def time_to_word(time_var):
    t3 = time_var.replace(' ', '').split(':')

    h1 = t3[0]                                        # часы в строке
    m1 = t3[1]                                        # минуты в строке
    h1_0 = int(h1[0])                                 # 1-я цифра в часах
    h1_1 = int(h1[1])                                 # 2-я цифра в часах
    m1_0 = int(m1[0])                                 # 1-я цифра в минутах
    m1_1 = int(m1[1])                                 # 2-я цифра в минутах

    
    if int(m1) in l_bez:                              # Случаи 30-55 минут
        polov = str(d_bez.get(int(m1)))
        if int(m1) == 30:                             # 30 минут
            if h1_0 > 0:                              # Двузначное число часов
                h = int(h1)
            else:                                     # Однозначное число часов
                h = int(h1[1:])
            for key in d_pol.keys():
                if h in key:
                    h_ = str(d_pol.get(key))

        else:                                         # 40, 45, 50, 55 минут
            if h1_0 > 0 and int(h1) < 13:             # Двузначное число часов
                h = int(h1) + 1
            elif int(h1) > 12:
                h = int(h1) - 11
            else:                                     # Однозначное число часов
                h = int(h1[1:])+1

            dict_hour[1] = 'час'                      # Замена в словаре в случае 00 часов
            h_ = str(dict_hour.get(int(h)))
            
        out = f'{polov} {h_}'
        return out

    else: 
        if h1_0 > 0:                                  # Двузначное число часов
            h = int(h1)
        else:                                         # Однозначное число часов
            h = int(h1[1:])
                                                
        for key in d_h.keys():                        # Вывод слова "часов" 
            if h in key:
                hours = d_h.get(key)

        h_ = str(dict_hour.get(int(h)))

        if m1_1 > 0 and m1_0 in range(2,6):           # Проверка 2-х цифр в минутах
            m_dec = d_0.get(m1_0)
            m_one = dict_min.get(m1_1)
            m_ = f'{m_dec} {m_one}'
            for key in d_m.keys():                    # Вывод слова "минут"
                if m1_1 in key:
                    mins = d_m.get(key)

        else:
            m_ = dict_min.get(int(m1))
            for key in d_m.keys():                    # Вывод слова "минут"
                if int(m1) in key:
                    mins = d_m.get(key)
                                                
        out = f'{h_} {hours} {m_} {mins}'
        return out
    

print(f'Текущее время: {time_to_word(now.strftime("%H:%M"))}')

time_man = input('Введите время в формате ЧЧ:ММ, например 05:26 \n ')

while True:
    if int(time_man.replace(' ', '').split(':')[0]) >= 0 and int(time_man.replace(' ', '').split(':')[0]) < 24:
        if int(time_man.replace(' ', '').split(':')[1]) >= 0 and int(time_man.replace(' ', '').split(':')[1]) < 60:
            print(f'Введенное время: {time_to_word(time_man)}')
            break
        else:
            time_man = input('Введите правильный формат времени (часы - от 0 до 23, минуты - от 0 до 59) \n ')
    else:
        time_man = input('Введите правильный формат времени (часы - от 0 до 23, минуты - от 0 до 59) \n ')
        

