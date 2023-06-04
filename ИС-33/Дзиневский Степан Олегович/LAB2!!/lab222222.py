# Исходные данные:
import numpy as np
import re
import heapq

from typing import List

numbers = list(range(0, 1000000))  # список целых чисел
print("1.Cписок целых чисел от 0 до 999999:", numbers)

import random

num_1 = []
for i in range(99999):
    num_1.append(random.uniform(-1, 1))  # список вещественных чисел в диапазоне
print("2.Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]:", num_1)

birth_day = 12
birth_month = 4
r = birth_day / birth_month
num_2 = []  # итоговый список
birth_day = 12
birth_month = 4
r = birth_day / birth_month  # радиус окружности

import random
import math

for i in range(56000):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    hypotenuse = math.sqrt(x ** 2 + y ** 2)
    if hypotenuse <= r:
        num_2.append(complex(x, y))
    if len(num_2) == 42000:
        break
print("3.42000 разных точки комплексной плоскости, лежащие на окружности радиуса:", num_2, )

with open("2.txt", "r", encoding="utf8") as file:
    text = file.read()
    text = re.sub("[^a-zA-Zа-яА-Я]", " ", text)
    words = text.split()
print("4.Отрывок из книги:", words)


sortirovka = [6, 9, 10, 5]
print(sortirovka)


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


def binary_tree_sort(num_2):
    root = None
    for value in num_2:
        root = insert_node(root, value)
    sorted_list = []
    traverse_tree(root, sorted_list)
    return sorted_list


sorted_arr = binary_tree_sort(num_2)

print("Отсортированный массив по tree sort:", sorted_arr)


# 9 Heapsort, пирамидальная сортировка;

def heap_sort(words):
    heapq.heapify(words)
    sorted_words = []
    while words:
        sorted_words.append(heapq.heappop(words))
    return sorted_words


sorted_words = heap_sort(words)
print(":Heapsort, пирамидальная сортировка")
print(sorted_words)


# 10.Сортировка Quicksort
def quicksort(num_1):
    if len(num_1) <= 1:
        return num_1
    pivot = num_1[len(num_1) // 2]
    left = [x for x in num_1 if x < pivot]
    middle = [x for x in num_1 if x == pivot]
    right = [x for x in num_1 if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print("Отсортированный массив по Quicksort:", quicksort(num_1))


# 2 bubble sort, сортировка пузырьком;;

a = 5/5
ugli = np.linspace(0, 2*np.pi, 42, endpoint=False)
num3 = [np.cos(angle) + np.sin(angle)*1j for angle in ugli]

def bubbleSort(mas):
    n = len(mas)

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if mas[j] > mas[j + 1]:

                mas[j], mas[j + 1] = mas[j + 1], mas[j]

                swapped = True


        if not swapped:
            break

    return mas

sorted_num3 = bubbleSort(num3)
print("отсортированный список пузырьком:")
print(sorted_num3)









