import random
import math
import re

numbers2 = []
for i in range(1_000_000):
    numbers2.append(random.randint(0, 999999))

numbers = []
for i in range(99999):
    numbers.append(random.uniform(-1, 1))

modulcom=[]
complexmas=[]
r=27/9
for i in range(42000):
    x=random.uniform(-r, r)
    y=random.uniform(-r, r)
    radius=math.sqrt(x**2 + y**2)
    if radius<=r:
        complexmas.append(complex(x, y))
        modulcom.append(math.sqrt(x**2 + y**2))
    if len(complexmas)==1000:
        break

text = []
with open("2_1.txt", encoding="utf-8", mode="r") as arr:
    for line in arr:
        line = re.sub(r'[^ А-я]', '', line)
        for i in line.split():
            text.append(i)


#print(random.sample(range(1,18),4))
#[9, 16, 4, 8]

#selection sort, сортировка выбором (9)
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

#insertion sort, сортировка вставкой(4)
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

#Heapsort, пирамидальная сортировка (9)
def heapify(lst, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and lst[left] > lst[largest]:
        largest = left

    if right < n and lst[right] > lst[largest]:
        largest = right

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)
def heap_sort(lst):
    n = len(lst)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)

    return lst


#most significant digit (16)

def msd_sort(lst):
    if len(lst) <= 1:
        return lst
    max_length = max(len(str(x)) for x in lst)
    return msd_sort_recursive(lst, 0, len(lst), max_length)


def msd_sort(lst):
    if len(lst) <= 1:
        return lst
    max_length = max(len(word) for word in lst)
    return msd_sort_recursive(lst, 0, len(lst), 0, max_length)
def msd_sort_recursive(lst, start, end, digit_pos, max_length):
    if start >= end or digit_pos >= max_length:
        return lst
    bins = [[] for _ in range(33)]

    for i in range(start, end):
        word = lst[i]
        if digit_pos < len(word):
            letter = ord(word[digit_pos])
        else:
            letter = 0
        bins[letter].append(word)

    for i in range(33):
        bins[i] = msd_sort_recursive(bins[i], 0, len(bins[i]), digit_pos + 1, max_length)

    merged = []
    for i in range(33):
        merged.extend(bins[i])

    return merged


selection_sort(numbers2)
print("Задание 1. :", numbers2)
insertion_sort(numbers)
print("Задание 2. :", numbers)
heap_sort(modulcom)
print("Задание 3. :", modulcom)
msd_sort(text)
print("Задание 4. :", text)









































