import random

spisok_cel_chisl = [ random.randint(0, 999999) for i in range(999999)]

spisok_randfom = [ random.uniform(-1, 1) for i in range(99999)]

import math

r = 10
n = 42000
theta = 2 * math.pi / n
points = []
for i in range(n):
    x = r * math.cos(i * theta)
    y = r * math.sin(i * theta)
    points.append((x, y))

#print(points)

import re

with open('mertvye-dushi.txt', 'r', encoding = 'utf-8') as f:
    text = f.read().lower()
words = re.findall(r'\b\w+\b', text)
words = [word.lower() for word in words]

#print(words)

#print(random.sample(range(1, 18), 4))

#сортировки вставкой    расчестка
#Сортировка выбором    сортировка подсчетом

#сортировка расчесткой

def comb_sort(arr):
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap/shrink)
        if gap <= 1:
            gap = 1
            sorted = True
        for i in range(0, n-gap):
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                sorted = False
    return arr

#print(comb_sort(spisok_cel_chisl))

#сортировка вставкой

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

#print(insertion_sort(spisok_randfom))

#сортировка выбором

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

#print(selection_sort(points))

#Сортировка подсчетом

def counting_sort(arr):
    max_value = max(arr, key=len)
    counts = [0] * (len(max_value) + 1)
    for string in arr:
        counts[len(string)] += 1
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    output = [0] * len(arr)
    for string in arr:
        output[counts[len(string)] - 1] = string
        counts[len(string)] -= 1
    return output

#print(counting_sort(words))
