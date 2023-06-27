import random
import math

# список целых чисел от 0 до 999999
my_list = list(range(1000000))

# список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
list = [random.uniform(-1, 1) for _ in range(99999)]

# 42000 разных точки комплексной плоскости, лежащие на окружности радиуса r = 25 / 3
r = 25 / 3
complex_points = []
for i in range(42000):
    angle = random.uniform(0,2 * math.pi)
    complex_points.append((r * math.cos(angle*i), r * math.sin(angle*i)))

# отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам
with open('Книга.txt', encoding='utf-8') as book:
    txt = book.read().lower()
    words = txt.split()

#print(random.sample(range(1, 18), 4)) [10, 9, 5, 11]

#Быстрая сортировка (Quicksort):

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

#Пирамидальная сортировка (Heapsort):

def heapsort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

#Сортировка Шелла (Shellsort):

def shellsort(arr):
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

#Сортировка слиянием (Merge sort):

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        mergesort(left_half)
        mergesort(right_half)
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

while True:
    index = input("Введите номер списка для проверки сортировок (для завершения введите exit):")
    if index == "1":
        print(quicksort(my_list))
    elif index == "2":
        print(heapsort(list))
    elif index == "3":
        print(shellsort(complex_points))
    elif index == "4":
        print(mergesort(words))
    elif index == "exit":
        break
    else:
        print("Введено неверное значение!")