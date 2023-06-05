import random
import re
birth_day = 12
birth_month = 8

# var = random.sample(range(1, 18), 4)
# print(var)
# [14, 1, 8, 2]

#________________________________________________________________________________________________________
#список целых чисел от 0 до 999999;
arr1 = []
for i in range(1000000):
    arr1.append(i)

#(2)bubble sort
def bubble_sort(arr):
    l = len(arr)
    for i in range(l-1):
        b = False # флаг совершения обмена
        for j in range(l-i-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                b = True # обмен совершен
        if not b: # если не было обмена, значит список отсортирован
            break
    return arr
sorted_arr1 = bubble_sort(arr1)
print(sorted_arr1)

#________________________________________________________________________________________________________
#список из 99999 случайных вещественных чисел в диапазоне [-1, 1];
arr2 = []
for i in range(1000):
    arr2.append(random.uniform(-1, 1))

#(1)shaker sort
def cocktail_sort(arr):
    length = len(arr)
    swapped = True
    start_index = 0
    end_index = length - 1
    while swapped:
        swapped = False
        # проход слева направо
        for i in range(start_index, end_index):
            if arr[i] > arr[i+1]:
                # обмен элементов
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        # если не было обменов прерываем цикл
        if not swapped:
            break
        swapped = False
        end_index = end_index - 1
        # проход справа налево
        for i in range(end_index - 1, start_index - 1, -1):
            if arr[i] > arr[i + 1]:
                # обмен элементов
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start_index = start_index + 1
    return arr
sorted_arr2 = cocktail_sort(arr2)
print(sorted_arr2)

#________________________________________________________________________________________________________
#42000 разных точки комплексной плоскости, лежащие в пределах окружности радиуса r = birth_day / birth_month
# (можно случайных, можно равномерно распределённых), сортировать по модулю;
r = birth_day / birth_month
arr3 = []
for i in range(42001):
    # Рандомныеные координаты x и y
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    # Проверка наличия точек в пределах окружности радиуса
    if abs(complex(x, y)) <= r:
        arr3.append(complex(x, y))

#(8)selection sort
def selection_sort(arr):
    a = len(arr)
    for i in range(a):
        min = i
        for j in range(i + 1, a):
            if abs(arr[j]) < abs(arr[min]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr
sorted_arr3 = selection_sort(arr3)
print(sorted_arr3)

#________________________________________________________________________________________________________
#отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам.
arr4 = []
otrivok = open('text2lab.txt', encoding='utf-8')
for line in otrivok.readlines():
    line = re.sub("[^А-я]"," ", line)
    for word in line.split():
        arr4.append(word)

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
print(sorted_arr4)

#________________________________________________________________________________________________________
