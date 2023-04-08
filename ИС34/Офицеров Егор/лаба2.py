import random
import math

# список целых чисел от 0 до 999999
integers = []
for i in range(1000000):
    integers.append(i)

# список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
numbers = []
while (len(numbers) < 99999):
    numbers.append(round(random.uniform(-1, 1),2))

# 42000 разных точки комплексной плоскости, лежащие на окружности радиуса r = 14 / 3
r = 14 / 3
complex_points = []
for i in range(42000):
    angle = random.uniform(0,2 * math.pi)
    complex_points.append((r * math.cos(angle*i), r * math.sin(angle*i)))

# отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам
with open('Книга.txt', encoding='utf-8') as book:
    txt = book.read().lower()
    words = txt.split()

#print(random.sample(range(1, 18), 4)) [11, 5, 8, 2]

#11-cортировка слиянием
def merge_sort(array):
    if len(array) > 1:
        mid = len(array)//2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
merge_sort(integers )

#5-cортировка Шелла
def Shellsort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k -1
    return array

#8-сортировка выбором
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

#2-сортировка пузырьком
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if len(array[j]) > len(array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

while True:
    index = input("Введите номер списка для проверки сортировок (для завершения введите exit):")
    if index == "1":
        print(integers)
    elif index == "2":
        print(Shellsort(numbers))
    elif index == "3":
        print(selection_sort(complex_points))
    elif index == "4":
        print(bubble_sort(words))
    elif index == "exit":
        break
    else:
        print("Введено неверное значение!")