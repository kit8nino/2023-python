# Исходные данные:
import re

from typing import List

numbers = list(range(0, 1000000))  # список целых чисел
print("1.Cписок целых чисел от 0 до 999999:", numbers)

import random

numbers_1 = []
for i in range(99999):
    numbers_1.append(random.uniform(-1, 1))  # список вещественных чисел в диапазоне
print("2.Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]:", numbers_1)

birth_day = 23
birth_month = 9
r = birth_day / birth_month
numbers_2 = []  # итоговый список
birth_day = 23
birth_month = 9
r = birth_day / birth_month  # радиус окружности

import random
import math

for i in range(56000):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    hypotenuse = math.sqrt(x ** 2 + y ** 2)
    if hypotenuse <= r:
        numbers_2.append(complex(x, y))
    if len(numbers_2) == 42000:
        break
print("3.42000 разных точки комплексной плоскости, лежащие на окружности радиуса:", numbers_2, )

with open("text.txt", "r", encoding="utf8") as file:
    text = file.read()
    text = re.sub("[^a-zA-Zа-яА-Я]", " ", text)
    words = text.split()
print("4.Отрывок из книги:", words)

# Моя сортировка
my_sort = [15, 10, 6, 2]
print(my_sort)


# 15.LSD (least significant digit)
def lsd_sort(numbers):
    max_num = max(numbers)  # определяем максимальное число в списке
    num_digits = len(str(max_num))  # определяем количество разрядов в максимальном числе
    buckets = [[] for _ in range(10)]  # создаем списки для каждого разряда
    for i in range(num_digits):  # сортируем числа по каждому разряду
        for num in numbers:  # распределяем числа по соответствующим спискам
            digit = (num // 10 ** i) % 10
            buckets[digit].append(num)
        numbers = []  # объединяем списки обратно в исходный список
        for bucket in buckets:
            numbers.extend(bucket)
            bucket.clear()
    return numbers


sorted_numbers = lsd_sort(numbers)


# 10.Сортировка Quicksort
def quicksort(numbers_1):
    if len(numbers_1) <= 1:
        return numbers_1
    pivot = numbers_1[len(numbers_1) // 2]
    left = [x for x in numbers_1 if x < pivot]
    middle = [x for x in numbers_1 if x == pivot]
    right = [x for x in numbers_1 if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# 6.Tree sort, сортировка деревом
def insert_node(root, value):
    if root is None:
        return {'value': value, 'left': None, 'right': None}
    if value.real < root['value'].real:
        root['left'] = insert_node(root['left'], value)
    else:
        root['right'] = insert_node(root['right'], value)
    return root


def traverse_tree(root, sorted_list):
    if root is None:
        return
    traverse_tree(root['left'], sorted_list)
    sorted_list.append(root['value'])
    traverse_tree(root['right'], sorted_list)


def binary_tree_sort(numbers_2):
    root = None  # звено
    for value in numbers_2:  # проходится по каждому элементу
        root = insert_node(root, value)
    sorted_list = []
    traverse_tree(root, sorted_list)
    return sorted_list


sorted_arr = binary_tree_sort(numbers_2)


# 2.Bubble sort, сортировка пузырьком;
def bubble_sort(words):
    n = len(words)
    for w in range(n):
        for j in range(n - w - 1):
            if words[j] > words[j + 1]:
                words[j], words[j + 1] = words[j + 1], words[j]  # Меняем элементы местами


bubble_sort(words)

print("Отсортированный массив по LSD:", sorted_numbers)
print("Отсортированный массив по Quicksort:", quicksort(numbers_1))
print("Отсортированный массив по tree sort:", sorted_arr)
print("Отсортированный массив по bubble sort:", ' '.join(words))
