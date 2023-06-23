# исходные данные
import random

nums1 = list(range(1000000))

nums2 = [random.uniform(-1, 1) for i in range(99999)]

r = 14 / 6
points = []
for i in range(42000):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    point = complex(x, y)
    points.append(point)

points_sorted = sorted(points, key=abs)

with open('dvakapitana.txt', 'r', encoding='utf-8') as f:
    text = f.read()

words = text.split()
words = words[:10000]

for i in range(len(words)):
    words[i] = words[i].strip('.,?!:;-—\n')

words = [word for word in words if word.isalnum()]

#выбор 4 алгоритмов

# print(random.sample(range(1, 18), 4))
# [15, 7, 11, 17]

# 1
# сортировка least significant digit для первого списка

def lsd_sort(nums1):
    radix = 10
    max_len = False
    temp, placement = -1, 1

    while not max_len:
        max_len = True
        buckets = [list() for _ in range(radix)]

        for i in nums1:
            temp = i // placement
            buckets[temp % radix].append(i)
            if max_len and temp > 0:
                max_len = False

        a = 0
        for b in range(radix):
            buck = buckets[b]
            for i in buck:
                nums1[a] = i
                a += 1

        placement *= radix

    return nums1

sorted_nums1 = lsd_sort(nums1)

print("Zadanie 1:", sorted_nums1)

# 2
# Quicksort, быстрая сортировка для вторрго списка

def quickSort(nums2):
    if len(nums2) <= 1:
        return nums2
    else:
        pivot = nums2[0]
        less = []
        greater = []
        for i in range(1, len(nums2)):
            if nums2[i] < pivot:
                less.append(nums2[i])
            else:
                greater.append(nums2[i])
        return quickSort(less) + [pivot] + quickSort(greater)
    return arr

sorted_nums2 = quickSort(nums2)
print("Задание2:", sorted_nums2 )


# 3
# сортировка Gnome sort для третьего списка

def gnome_sort(arr):
    i = 0
    while i < len(arr):
        if i == 0 or abs(arr[i]) >= abs(arr[i-1]):
            i += 1
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
    return arr


sorted_points3 = gnome_sort(points_sorted)
print("Задание3:", sorted_points3)


#  4
# сортировка bitonic sort для четвертого списка

def bitonic_sort(arr):

    def bitonic_merge(arr, start, length, direction):
        if length > 1:
            mid = length // 2
            for i in range(start, start + mid):
                if direction == (arr[i] > arr[i + mid]):
                    arr[i], arr[i + mid] = arr[i + mid], arr[i]
            bitonic_merge(arr, start, mid, direction)
            bitonic_merge(arr, start + mid, mid, direction)

    def bitonic_sort_rec(arr, start, length, direction):
        if length > 1:
            mid = length // 2
            bitonic_sort_rec(arr, start, mid, True)
            bitonic_sort_rec(arr, start + mid, mid, False)
            bitonic_merge(arr, start, length, direction)


    bitonic_sort_rec(arr, 0, len(arr), True)
    return arr

sorted_words4 = bitonic_sort(words)
print("Zadanie 4 : ", sorted_words4)