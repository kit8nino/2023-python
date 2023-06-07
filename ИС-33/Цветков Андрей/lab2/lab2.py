import random
import math
import heapq

perv = list(range(1000000))
vtor = [random.uniform(-1, 1) for i in range(99999)]

tri = []
r = 9/4
for i in range(42000):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    c = math.sqrt(x**2 + y**2)
    if c <= r:
        tri.append(complex(x, y))

with open('text.txt', 'r', encoding='utf-8') as f:
    book_lst = f.read().split()

# print(random.sample(range(1, 18), 4))
# [12, 10, 11, 1]

print("Сортировка подсчетом(countingsort)")
def counting_sort(per):
    max_val = max(per)
    count_per = [0] * (max_val+1)

    for num in per:
        count_per[num] += 1

    sorted_per = []
    for i in range(len(count_per)):
        sorted_per.extend([i]*count_per[i])

    return sorted_per

per_int_counting = counting_sort(perv)

print("Сортировка подсчетом(countingsort)")
print("Result")
print(per_int_counting)


print("Быстрая сортировка(quicksort)")


def quick_sort(vtor2):
    if len(vtor2) <= 1:
        return vtor2
    elem = vtor2[0]
    left = list(filter(lambda x: x < elem, vtor2))
    center = [i for i in vtor2 if i == elem]
    right = list(filter(lambda x: x > elem, vtor2))
    return quick_sort(left) + center + quick_sort(right)


vtor22 = quick_sort(vtor)

assert vtor22 == sorted(vtor)
print("Быстрая сортировка(quicksort)")
print("Result")
print(vtor22)

print("Сортировка слиянием(mergesort)")


def merge_two_list(a, b):
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


def merge_sort(tri3):
    if len(tri3) <= 1:
        return tri3
    middle = len(tri3) // 2
    left = merge_sort(tri3[:middle])
    right = merge_sort(tri3[middle:])

    return merge_two_list(left, right)


comp = merge_sort(tri)
print("Result")
print(comp)

print("Сортировка перемешиванием(shakersort)")

def shaker_sort(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        for i in range(left, right):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        right -= 1

        for i in range(right, left, -1):
            if lst[i-1] > lst[i]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
        left += 1
    return lst

with open('text.txt', 'r', encoding='utf-8') as f:
    book_lst = f.read().split()

sorted_lst = shaker_sort(book_lst)
print("Result")
print(sorted_lst)

#with open('sorttext.txt', 'w') as f:
    #f.write(' '.join(sorted_lst))