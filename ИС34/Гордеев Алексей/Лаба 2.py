from random import randint
import random
import math
import re

# список целых чисел от 0 до 999999
numbers = []
for i in range(999999):
    numbers.append(randint(0, 999999))

# список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
numbers_ve = []
while (len(numbers_ve) < 99999):
    numbers_ve.append(round(random.uniform(-1, 1), 3))

# 42000 разных точки комплексной плоскости, лежащие на окружности радиуса r = 15 / 7
r = 15 / 7
complex_numbers = []
for i in range(42000):
    p = random.uniform(0, 2 * math.pi)
    x = r * math.cos(p)
    y = r * math.sin(p)
    complex_numbers.append(complex(x, y).real)

# отрывки из книги
with open('Отрывки из рассказов.txt', 'r', encoding = 'utf-8') as f:
    txt = f.read().lower()
without_symbols_text = re.findall(r'\b\w+\b', txt)
book_by_words = txt.split()




#print(random.sample(range(1, 18), 4)) (13, 8, 7, 2)


#блочная сортировка
def bucket_sorting(array):
    max_val = max(array)
    min_val = min(array)
    bucket_size = 5  
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]
    for n in array:
        index = (n - min_val) // bucket_size
        buckets[index].append(n)
    res = []
    for bucket in buckets:
        sorted_bucket = sorted(bucket)
        res.extend(sorted_bucket)
    return res
# print(bucket_sorting(numbers))


#сортировка выбором
def selection_sorting(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array
# print(selection_sorting(numbers_ve))


# gnome
def gnome_sorting(array):
    index = 1
    while index < len(array):
        if index == 0:
            index = 1
        if array[index] >= array[index - 1]:
            index += 1
        else:
            array[index], array[index - 1] = array[index - 1], array[index]
            index -= 1
    return array
# print(gnome_sorting(complex_numbers))


#сортировка пузырьком
def bubble_sorting(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if len(array[j]) > len(array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
# print(bubble_sorting(book_by_words))