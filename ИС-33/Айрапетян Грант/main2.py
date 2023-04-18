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
class Tree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value.real < self.value.real:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.insert(value)


def tree_sort(numbers_2):
    if len(numbers_2) == 0:
        return numbers_2

    root = Tree(numbers_2[0])
    for i in range(1, len(numbers_2)):
        root.insert(numbers_2[i])
    sorted_lst = []

    def in_order_traversal(node):
        if node is not None:
            in_order_traversal(node.left)
            sorted_lst.append(node.value)
            in_order_traversal(node.right)

    in_order_traversal(root)

    return sorted_lst


sorted_lst = tree_sort(numbers_2)


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
print("Отсортированный массив по tree sort:", sorted_lst)
print("Отсортированный массив по bubble sort:", ' '.join(words))
