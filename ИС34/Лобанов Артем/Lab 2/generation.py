#------- Чтение списка
def read_file(filename, data_type):
    with open(filename, 'r', errors='ignore') as f:
        return list(map(data_type, f.read().split()))
#------- Запись списка
def write_file(filename, arr):
    with open(filename, 'w') as f:
        for i in arr:
            f.write(str(i) + ' ')

# Список целых чисел от 0 до 999999
write_file('integers.txt',[i for i in range(100000)])

# Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
import random
write_file('floats.txt',[random.uniform(-1,1) for i in range(99999)])

# 42000 сортированных по модулю разных точки комплексной плоскости, лежащие в пределах окружности радиуса r = birth_day / birth_month
birth_day = 28
birth_month = 4
r = birth_day / birth_month
write_file("points.txt",\
        [complex(a, random.uniform(-(r**2-a**2)**0.5, (r**2-a**2)**0.5)) 
        for z in range(42000) 
        for a in [random.uniform(-r, r)]])

# Отрывок из книги не менее 10000 слов, разбитый в список по словам
from KORAN import koran
import re
#некие проблемс с чтением файлов, поэтому так
words = re.findall(r'\w+', koran)
with open('words.py', 'w', encoding='utf-8') as f:
    f.write("words = '''\n")
    for word in words:
        f.write(word + '\n')
    f.write("\n'''")
