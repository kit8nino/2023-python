import numpy as np
import random
import re
print(random.sample(range(1, 18), 4))
#5 13 2 4

lst1 = []
for i in range(1000000):
    lst1.append(i)

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
               arr[j] = arr[j - gap]
               j -= gap
            arr[j] = temp
        gap //= 2
    return arr

print("список 1 остосртированный методом Шелла", shell_sort(lst1))

lst2 = []
for i in range(100000):
    lst2.append(random.uniform(-1, 1))

def bucket_sort(arr):
    # Определяем диапазон значений и количество корзин
    min_val = round(min(arr))
    max_val = round(max(arr))
    bucket_size = 10
    bucket_count = (max_val - min_val) // bucket_size + 1

    # Инициализируем корзины
    buckets = [[] for _ in range(bucket_count)]

    # Распределяем значения по корзинам
    for val in arr:
        index = int((val - min_val) // bucket_size)
        buckets[index].append(val)

    # Сортируем каждую корзину
    for i in range(bucket_count):
        buckets[i].sort()

    # Собираем значения из корзин в отсортированный список
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr

print("список 2 остосртированный блочным методом", bucket_sort(lst2))

r = 19/3 #примерно 6
angles = np.linspace(0, 2*np.pi, 42000, endpoint=False)
lst3 = [np.cos(angle) + np.sin(angle)*6j for angle in angles]

def bubble_sort_complex(arr):
    n = 42000 #len(arr)
    # Проходим по всем элементам списка точек
    for i in range(n):
        # Последние i элементов уже отсортированы
        for j in range(0, n - i - 1):
            # Сравниваем расстояние от начала координат между точками
            if abs(arr[j]) > abs(arr[j + 1]):
                # Меняем местами элементы
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print("список 3 остосртированный пузырьковым методом", bubble_sort_complex(lst3))

lst4 = []
f = open("kniga.txt")
for line in f.readlines():
    line = re.sub("[^А-я]"," ", line)
    for word in line.split():
        lst4.append(word)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_word = arr[i]
        j = i - 1
        while j >= 0 and current_word < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = current_word
    return arr

print("список 4 остосртированный методом вставки", insertion_sort(lst4))