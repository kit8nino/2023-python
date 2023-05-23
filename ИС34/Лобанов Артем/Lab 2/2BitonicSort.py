def bitonic_sort(arr, direction=True, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = bitonic_sort(arr[:mid], True, key=key)
        right = bitonic_sort(arr[mid:], False, key=key)
        return merge(left + right, direction, key=key)

def merge(arr, direction,key=lambda x: x):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        for i in range(mid):
            if (key(arr[i]) > key(arr[i + mid])) == direction:
                # меняем местами
                arr[i], arr[i + mid] = arr[i + mid], arr[i]
        # зачем? Это не описать словами...
        left = merge(arr[:mid], direction, key=key)
        right = merge(arr[mid:], direction, key=key)
        # крутые и сортированные перцы теперь вместе
        return left + right

from generation import read_file
import math
# надо докрутить количество элементов в массиве до степени двойки, поскольку только с такими массивами дано работать битону
def add_to2_power(arr):
    return arr+(2**math.ceil(math.log2(len(arr)))-len(arr))*([float('inf')] if arr and type(arr[0])!=str else ['\U0010ffff'])
# ну и убрать лишнего, что конечно окажется в конце, ведь бесконечности нет равных (или последнему символу Unicode)
def bitonic_sort_for_everyone(arr,key=lambda x: x):
    return bitonic_sort(add_to2_power(arr),key=key)[:len(arr)]

# Список целых чисел от 0 до 999999
arr = read_file("integers.txt",int)
sorted_arr = bitonic_sort_for_everyone(arr)
print(sorted_arr==arr, len(arr))

# Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
arr = read_file("floats.txt",float)
sorted_arr = bitonic_sort_for_everyone(arr)
print(sorted_arr==sorted(arr), len(arr))

# 42000 разных точки комплексной плоскости, лежащие в пределах окружности радиуса r = birth_day / birth_month
arr = read_file("points.txt",complex)
sorted_arr = bitonic_sort_for_everyone(arr, key=lambda x: abs(x))
print(sorted_arr==sorted(arr, key=lambda x: abs(x)), len(arr))

# Отрывок из книги не менее 10000 слов, разбитый в список по словам
from words import words
arr = words.split()
sorted_arr = bitonic_sort_for_everyone(arr)
print(sorted_arr==sorted(arr), len(arr))
