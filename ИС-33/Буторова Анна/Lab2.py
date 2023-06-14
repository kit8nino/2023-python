import random
import re
import heapq
import math

numbers = list(range(0, 1000000))  # список целых чисел
print("1.Cписок целых чисел от 0 до 999999:", numbers)


num_1 = []
for i in range(99999):
    num_1.append(random.uniform(-1, 1))  # список вещественных чисел в диапазоне
print("2.Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]:", num_1)

birth_day = 29
birth_month = 6
r = birth_day / birth_month
num_2 = []  # итоговый список
birth_day = 29
birth_month = 6

for i in range(56000):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    hypotenuse = math.sqrt(x ** 2 + y ** 2)
    if hypotenuse <= r:
        num_2.append(complex(x, y))
    if len(num_2) == 42000:
        break
print("3.42000 разных точки комплексной плоскости, лежащие на окружности радиуса:", num_2, )

arr4 = []
otrivok = open('2.txt', encoding='utf-8')
for line in otrivok.readlines():
    line = re.sub("[^А-я]"," ", line)
    for words in line.split():
        arr4.append(words)



sortirovka = [6, 9, 10, 14]
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

print("Первая сортировка: tree sort, сортировка деревом")
print("Отсортированный массив по tree sort:", sorted_arr)


# 9 Heapsort, пирамидальная сортировка;

def heap_sort(words):
    heapq.heapify(words)
    sorted_words = []
    while words:
        sorted_words.append(heapq.heappop(words))
    return sorted_words

sorted_words = heap_sort(list(words))

print("Вторая сортировка: Heapsort, пирамидальная сортировка")
print("Результат второй сортировки:")
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

print("Третья сортировка: quick sort, быстрая сортировка")
print("Отсортированный массив по Quicksort:", quicksort(num_1))



#(14)radix sort
def radix_sort(arr):
    # определяем максимальную длину слова в списке
    max_length = len(max(arr, key=len))
    # заполняем слова пробелами до максимальной длины
    for i in range(len(arr)):
        arr[i] = arr[i].ljust(max_length)
    # сортируем слова посимвольно, начиная с конца
    for i in range(max_length - 1, -1, -1):
        words = sorted(arr, key=lambda x: x[i])
    # удаляем пробелы из отсортированных слов
    for i in range(len(words)):
        words[i] = words[i].strip()
    return words
sorted_arr4 = radix_sort(arr4)

print("Четвертая сортировка: radix sort, поразрядная сортировка")
print("Результат четвертой сортировки:")
print(sorted_arr4)


