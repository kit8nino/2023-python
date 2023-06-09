import random
import re


def counting_sort(lst):
    counts = [0] * 1000000
    sorted_lst = [None] * len(lst)
    for num in lst:
        counts[num] += 1
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    for num in lst:
        sorted_lst[counts[num] - 1] = num
        counts[num] -= 1
    return sorted_lst


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = random.choice(lst)
    left, mid, right = [], [], []
    for num in lst:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            mid.append(num)
        else:
            right.append(num)
    return quick_sort(left) + mid + quick_sort(right)


def shell_sort(lst):
    gap = len(lst) // 2
    while gap > 0:
        for i in range(gap, len(lst)):
            temp = lst[i]
            j = i
            while abs(j) >= abs(gap) and abs(lst[j - gap]) > abs(temp):
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    l, rr = 0, 0
    while l < len(left) and rr < len(right):
        if left[l] <= right[rr]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[rr])
            rr += 1
    result += left[l:]
    result += right[rr:]
    return result


# Список целых чисел от 0 до 999999
lst1 = list(range(1000000))
random.shuffle(lst1)
sorted_lst1 = counting_sort(lst1)

# Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
lst2 = [random.uniform(-1, 1) for _ in range(99999)]
sorted_lst2 = quick_sort(lst2)

# Список из 42000 точек комплексной плоскости
r = 11 / 5  # birth_day = 11, birth_month = 5
lst3 = [complex(random.uniform(-r, r), random.uniform(-r, r)) for _ in range(42000)]
sorted_lst3 = shell_sort(lst3)

# Отрывок из книги не менее 10000 слов, разбитый в список по словам
with open('book.txt') as f:
    lst4 = (re.sub(r'[^A-Za-zА-Яа-я]', ' ', f.read())).split()
sorted_lst4 = merge_sort(lst4)
print("Сортированный список целых чисел от 0 до 999999: ", sorted_lst1)
print("Сортированный список из 99999 случайных вещественных чисел в диапазоне [-1, 1]: ", sorted_lst2)
print("Сортированный список из 42000 точек комплексной плоскости: ", sorted_lst3)
print("Сортированный Отрывок из книги не менее 10000 слов, разбитый в список по словам: ", sorted_lst4)
