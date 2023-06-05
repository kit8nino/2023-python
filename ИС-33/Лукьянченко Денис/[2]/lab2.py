"""
import random
print(random.sample(range(1, 18), 4))
#[2, 10, 14, 11]

2.Bubble sort, сортировка пузырьком;
10.Quicksort, быстрая сортировка;
14.Radix sort, поразрядная сортировка;
11.Merge sort, сортировка слиянием;
"""
import random
import re

# Импорт и генерация списков
# Генерация значений списка целых чисел от 0 до 999.999
One_Million_Numbers = [x for x in range(1000000)]

# Генерация списка из 99.999 вещественных чисел в диапозоне [-1; 1]
real_numbers = []
for i in range(99999):
    real_numbers.append(random.uniform(-1, 1))

# Генерация значений списка из 42.000 разных точек комплексной плоскости, лежащие в пределах окружности радиуса r
r = int(15 / 3)
comNumL = []
while True:
    comNum = complex(random.randint(-r, r) / random.random(), random.randint(-r, r) / random.random())
    if len(comNumL) == 42000:
        break
    if comNum.real ** 2 + comNum.imag ** 2 <= r ** 2:
        comNumL.append(comNum)

# Импорт значений списка из слов отрывка книги Робинзон Крузо (полная книга с 96 тыс. слов)
text = []
with open("Robinzon_Kruzo.txt", encoding="utf-8", mode="r") as arr:
    for line in arr:
        line = re.sub(r'[^ А-я]', '', line)
        for i in line.split():
            text.append(i)


# Алгоритмы сортировки
# Реализация сортировки 2 - сортировка пузырьком, для списка целых чисел от 0 до 999999
def Bubble_Sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Реализация сортировки 10 - быстрая сортировка, для списка из 99.999 вещественных чисел в диапозоне [-1; 1]
def Quick_Sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return Quick_Sort(left) + middle + Quick_Sort(right)


# Реализация сортировки 14 - поразрядная сортировка для списка состоящего из слов отрывка книги Робинзон Крузо
def Radix_Sort(words):
    max_length = len(max(words, key=len))
    for i in range(len(words)):
        words[i] = words[i].ljust(max_length)
    for i in range(max_length - 1, -1, -1):
        words = sorted(words, key=lambda x: x[i])
    for i in range(len(words)):
        words[i] = words[i].strip()
    return words


# Реализация сортировки 11 - сортировка слиянием для списка целых чисел от 0 до 999999
def Merge_Sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        Merge_Sort(left_half)
        Merge_Sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


# Вывод результата
print("Рандомайзер выдал мне [2, 10, 14, 11]")
print(Bubble_Sort(real_numbers))
print(Quick_Sort(real_numbers))
print(Merge_Sort(One_Million_Numbers))
print(Radix_Sort(text))
