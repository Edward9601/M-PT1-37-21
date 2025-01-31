import random
from random import randint

k = int(input('Введите число - количество элементов списка: '))
d = int(input('Введите максимальное число k диапозона чисел (1, k): '))

def forming_list(n, max):
    s = []
    while n != 0:
        t = randint(1, max)
        if t not in s:
            s.append(t)
            n -= 1
        else:
            n = n
    return s

def sort(list_init):
    list_sort = sorted(list_init)
    return list_sort

def get_rangers(list_sorted):
    serie = []
    list_fin = []
    for i in range(len(list_sorted)-1):     
        if list_sorted[i] + 1 == list_sorted[i+1]:   
            serie.append(list_sorted[i])
            serie.append(list_sorted[i+1])
        else:
            if len(serie) > 0:
                list_fin.append(f'{serie[0]}-{serie[-1]}')
                serie = []
            else:
                list_fin.append(f'{list_sorted[i]}')
    if len(serie) > 1:
        list_fin.append(f'{serie[0]}-{serie[-1]}')
    elif len(serie) == 1:
        list_fin.append(f'{serie[0]}')
    else:
        list_fin.append(f"{list_sorted[-1]}")
    return list_fin

list0 = forming_list(k, d)
print(f'Список входной: {list0}')     

list1 = sort(list0) 
print(f'Сортированный список: {list1}')

list2 = get_rangers(list1)
print(f'Список из строк {list2}')

final = ', '.join(list2)
print(f'Строка серий {final}')