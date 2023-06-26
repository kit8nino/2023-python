import random
import math

#ВНИМАНИЕ! Сортировка пузырьком занимает очень много времени

# 1. Список целых чисел от 0 до 999999
list1 = [i for i in range(0, 1000000)]

# 2. Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
list2 = [random.uniform(-1, 1) for i in range(99999)]

# 3. 42000 разных точки комплексной плоскости, лежащие в пределах окружности радиуса
# r = birth_day / birth_month
# сортированные по модулю

list3 = []
birth_day=9
birth_month=4
r = birth_day / birth_month
for i in range (42000):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    l = math.sqrt(x**2 + y**2)
    if l <= r:
        list3.append(complex(x, y))

# Отрывок из книги Д. Дефо "Робинзон Крузо",
# разбитый на 12233 слова в список

with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    list4 = text.split()

# random.sample(range(1, 18), 4)
# Результат: [12, 2, 11, 8]
# 12. Counting sort, сортировка подсчетом
# 2. Bubble sort, сортировка пузырьком
# 11. Merge sort, сортировка слиянием
# 8. Selection sort, сортировка выбором

# 1. Counting sort, сортировка подсчетом

def counting_sort(func1):
    max_val = max(func1)

    count = [0] * (max_val + 1)

    for num in func1:
        count[num] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    result = [0] * len(func1)

    for num in func1:
        result[count[num] - 1] = num
        count[num] -= 1

    return result

# 2. Bubble sort, сортировка пузырьком

def bubble_sort(func2):
    n = len(func2)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if func2[j] > func2[j + 1]:
                func2[j], func2[j + 1] = func2[j + 1], func2[j]
    return func2

# 3. Merge sort, сортировка слиянием;

def merging(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if abs(a[i]) < abs(b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c

def merge_sort(func3):
    if len(func3) <= 1:
        return func3
    middle = len(func3)//2
    left = merge_sort(func3[:middle])
    right = merge_sort(func3[middle:])

    return merging(left, right)

# 4. Selection sort, сортировка выбором

def selection_sort(func4):
    n = len(func4)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if func4[j] < func4[min_index]:
                min_index = j
        func4[i], func4[min_index] = func4[min_index], func4[i]
    return func4

# Выполнение

while True:
    choise=input('Введите номер списка для сортировки (1 - 4): \n (для выхода введите "exit")')
    if choise=="1":
        print(counting_sort(list1),'\n')
        print("Сортировка первого списка методом Counting sort (сортировка подсчетом) выполнена.\n")
    elif choise=="2":
        print(bubble_sort(list2),'\n')
        print("Сортировка второго списка методом Bubble sort (сортировка пузырьком) выполнена.\n")
        #ВНИМАНИЕ! Сортировка пузырьком занимает очень много времени
    elif choise=="3":
        print(merge_sort(list3),'\n')
        print("Сортировка третьего списка методом Merge sort (сортировка слиянием) выполнена.\n")
    elif choise=="4":
        print(selection_sort(list4),'\n')
        print("Сортировка четвертого списка методом Selection sort (сортировка выбором) выполнена.\n")
    elif choise=="exit":
        print("Программа завершила работу.\n")
        break
    else:
        print("Введено неверное значение!\n")