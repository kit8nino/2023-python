#Исходные данные
int_numbers = list(range(1000000))

import random
rand_numbers = [random.uniform(-1, 1) for i in range(99999)]

import  math
r = 14/9
points = []
for i in range(42000):
    z = random.uniform(0, 2*math.pi)
    x = r * math.cos(z)
    y = r * math.sin(z)
    points.append(complex(x, y))

with open("text.txt", "r") as textfile:
    text = textfile.read().lower()
textwords = text.split()
#print(random.sample(range(1, 18), 4)) [1, 10, 3, 5]

#1.Shaker sort, сортировка перемешиванием.
def shaker_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = shaker_sort(left)
    right = shaker_sort(right)
    return sort1(left, right)

def sort1(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

print(shaker_sort(int_numbers))

#10.Quicksort, быстрая сортировка.
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        lesser = [x for x in arr[1:] if x < pivot]
        greater = [x for x in arr[1:] if x >= pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)

#print(quicksort(rand_numbers))

##3.Comp sort, сортировка расческой.
def comp_sort(arr):
    gap = len(arr)
    shrink = 1.3
    swapped = True
    while gap > 1 or swapped:
        gap = max(1, int(gap / shrink))
        swapped = False
        i = 0
        while i + gap < len(arr):
            if abs(arr[i]) > abs(arr[i + gap]):
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
            i += 1
    return arr

#print(comp_sort(points))

##5.Shellsort, сортировка Шелла.
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and str(arr[j - gap]) > str(temp):
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr
#print(shell_sort(textwords))