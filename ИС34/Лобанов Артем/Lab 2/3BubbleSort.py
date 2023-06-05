def bubble_sort(array, key=lambda x: x):
    arr=array.copy()
    n = len(arr)
    for i in range(n):
        swap = False
        for j in range(0, n-i-1):
            if key(arr[j]) > key(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap: break # уже готовенький (только поэтому первый и отсортировался)
    return arr

from generation import read_file

# Список целых чисел от 0 до 999999
arr = read_file("integers.txt",int)
sorted_arr = bubble_sort(arr)
print(sorted_arr==sorted(arr), len(arr))

# я не буду это комментировать!
# бабл сорт безнадежен
'''
# Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
arr = read_file("floats.txt",float)
sorted_arr = bubble_sort(arr)
print(sorted_arr==sorted(arr))

# 42000 разных точки комплексной плоскости, лежащие в пределах окружности радиуса r = birth_day / birth_month
arr = read_file("points.txt",complex)
sorted_arr = bubble_sort(arr,key=lambda x: abs(x))
print(sorted_arr)

# Отрывок из книги не менее 10000 слов, разбитый в список по словам
from words import words
arr = words.split()
sorted_arr = bubble_sort(arr)
print(sorted_arr==sorted(arr), len(arr))
'''
