import math
def msd_sort(array, key=lambda x: x):
    arr = array.copy()
    max_num = key(max(arr, key=key))
    # Количество разрядов у максимального числа
    num_digits = int(math.log10(max_num))
    # Начиная с num_digits пойдем делать дела 
    digits(arr, num_digits, 0, len(arr), key)
    # arr уже не тот что прежде - передадим его знания миру
    return arr

def digits(arr, num_digits, left, right, key):
    if left >= right or num_digits<0:
        # здесь все файналли закончится
        return
    # По корзине на цифору
    buckets = [[] for _ in range(10)]
    # Разряд num_digits 
    for i in range(left, right):
        digit = int(key(arr[i]) // (10 ** num_digits)) % 10
        buckets[digit].append(arr[i])
    # Пройдемся по корзинам которые уже в порядке возрастания
    for bucket in buckets:
        # Cортируем корзины по предыдущему разряду
        digits(bucket, num_digits-1, 0, len(bucket), key)
        # Теперь bucket не тот что прежде - его знания нужно слить в общину
        for j in range(len(bucket)):
            arr[left] = bucket[j]
            left += 1


def msd_sort_for_everyone(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    # находим самое дальнее античисло что бы прибавить его ко всем
    min_num = key(min(arr, key=key)) 
    min_num = -min_num if min_num<0 else 0
    max_digits_after_dot = key(max(arr, key=lambda x: len(str(key(x)+min_num).split('.')[1]) if type(key(x)+min_num)==float else 0))
    max_digits_after_dot = len(str(max_digits_after_dot).split('.')[1]) if type(max_digits_after_dot)==float else 0
    return msd_sort(arr,key=lambda x: (key(x)+min_num)*10**max_digits_after_dot)
    # мсд сорт + типа 😎

from generation import read_file

# Список целых чисел от 0 до 999999
arr = read_file("integers.txt",int)
sorted_arr = msd_sort(arr)
print(sorted_arr==sorted(arr), len(arr))

# Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
arr = read_file("floats.txt",float)
sorted_arr = msd_sort_for_everyone(arr)
print(sorted_arr==sorted(arr), len(arr))

# 42000 разных точки комплексной плоскости, лежащие в пределах окружности радиуса r = birth_day / birth_month
arr = read_file("points.txt",complex)
sorted_arr = msd_sort_for_everyone(arr, key=lambda x: abs(x))
print(sorted_arr==sorted(arr, key=lambda x: abs(x)), len(arr))

#Внимание внимание это просто прикольно, я не хочу добавлять отдельно сортировку для строк
# будем короче сравнивать строки
# Пусть u(x0) это порядковый номер символа x0 в алфавите из n символов
# а u(x0x1x2x3...xl) это уникальное число строки x0x1x2x3...xl соотносящееся с другими числами как соответствующие им строки
# так же максимальная длинна строки равна l
# тогда u(x0x1x2x3...xl) = u(x0)*(n+1)^l + u(x1)*(n+1)^(l-1) + ... + u(xl)
# если же в строке меньше l символов, то u считаем равным нулю для пустых позиций
# это все правда потому что я придумал формулу: 1*(n+1)^l - 1 = n*(n+1)^(l-1) + n*(n+1)^(l-2) + ... + n

# w+ в generation это что то такое
symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyzЁАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяё'
# почему буква ё открывает и закрывает русский?
def u(x):
    return symbols.index(x)+1 # u('0')!=0, u('0')==1 ведь количество символов имеет значение
def string_price(string,n,l):
    return sum(u(string[i])*(n+1)**(l-i) for i in range(len(string)))

# Отрывок из книги не менее 10000 слов, разбитый в список по словам
from words import words
arr = words.split()[:10000] # можно и подождать в целом: True 131658
word_max_length = len(max(arr,key=lambda x: len(x)))
sorted_arr = msd_sort(arr,key=lambda x: string_price(x,len(symbols),word_max_length))
print(sorted(arr)==sorted_arr, len(arr))
