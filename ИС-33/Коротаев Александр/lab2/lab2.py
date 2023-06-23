# Исходные данные:
import re
import random
import math
from typing import List

spisok_c = list(range(0, 1000000))  # список целых чисел
print("1.Cписок целых чисел от 0 до 999999:", spisok_c)



spisok_v = []
for i in range(99999):
    spisok_v.append(random.uniform(-1, 1))  # список вещественных чисел в диапазоне
print("2.Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]:", spisok_v)

birth_day = 24
birth_month = 11
r = birth_day / birth_month
spisok = []  # итоговый список
birth_day = 24
birth_month = 11
r = birth_day / birth_month  # радиус окружности



for i in range(56000):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    hypotenuse = math.sqrt(x ** 2 + y ** 2)
    if hypotenuse <= r:
        spisok.append(complex(x, y))
    if len(spisok) == 42000:
        break
print("3.42000 разных точки комплексной плоскости, лежащие на окружности радиуса:", spisok)

with open("text.txt", "r", encoding="utf8") as file:
    text = file.read()
    text = re.sub("[^a-zA-Zа-яА-Я]", " ", text)
    words = text.split()
print("4.Отрывок из книги:", words)


sortirovka = [4, 10, 8, 2]
print(sortirovka)

#4.Сортировка insertion sort
def insertionSort(spisok_c):
    for i in range(len(spisok_c)):
        current_value=spisok_c[i]
        position=i
        while position > 0 and spisok_c[position-1] > current_value:
            spisok_c[position]=spisok_c[position - 1]
            position -=1
            spisok_c[position]=current_value
    return spisok_c

result=insertionSort(spisok_c)


# 10.Сортировка Quicksort
def quicksort(spisok_v):
    if len(spisok_v) <= 1:
        return spisok_v
    pivot = spisok_v[len(spisok_v) // 2]
    left = [x for x in spisok_v if x < pivot]
    middle = [x for x in spisok_v if x == pivot]
    right = [x for x in spisok_v if x > pivot]
    return quicksort(left) + middle + quicksort(right)

#8. Сортировка selection sort

def selectionSort(arr):
    a = len(arr)
    for i in range(a):
        min = i
        for j in range(i+1, a):
            if abs(arr[j]) < abs(arr[min]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

# 2.Сортировка bubble sort
def bubble_sort(words):
    n = len(words)
    for w in range(n):
        for j in range(n - w - 1):
            if words[j] > words[j + 1]:
                words[j], words[j + 1] = words[j + 1], words[j]  # Меняем элементы местами
                
bubble_sort(words)











print("Отсортированный массив по insertionsort: ", result)
print("Отсортированный массив по Quicksort:", quicksort(spisok_v))
print("Отсортированный массив по selection sort:", selectionSort(spisok))
print("Отсортированный массив по bubble sort:", ' '.join(words))


