import random
import math

# Исходные данные

numbers = list(range(1000000))
print(numbers)

extended = []
for i in range(100000):
    extended.append(random.uniform(-1, 1))
print(extended)

r = 9 / 12
n = 42000
t = 2 * math.pi / n
points = []
for i in range(n):
    x = r * math.cos(i * t)
    y = r * math.sin(i * t)
    points.append((x, y))
print(points)

file = open('text.txt', encoding='utf-8')
reading = file.read()
text = reading.split()
print(text)

variants = ((random.sample(range(1, 18), 4))) #4,7,10,18
#print(variants)

# Гномья сортировка 7

def gnome_sort(lst, size):
    i = 1
    while i < size:
        if (lst[i - 1] <= lst[i]):
            i += 1
        else:
            tmp = lst[i]
            lst[i] = lst[i - 1]
            lst[i - 1] = tmp
            i -= 1
            if (i == 0):
                i = 1
    return lst
numbers_sort = gnome_sort(numbers, len(numbers))
print(numbers_sort)

# Сортировка вставками 4

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
extended_sort = insertion_sort(extended)
print(extended_sort)

#Гибридна сортировка 18

def insertion_sort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    for i in range(left + 1, right + 1):
        key_item = array[i]
        j = i - 1
        while j >= left and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array
points_sort = insertion_sort(points)
print(points_sort)

# Быстрая сортировка 10

def quick_sort(arr):
    if len(arr) > 1:
        pivot = arr.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in arr:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return (quick_sort(smlr_lst) + equal_lst + quick_sort(grtr_lst))
    else:
        return arr
text_sort = quick_sort(text)
print(text_sort)