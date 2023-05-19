import random
import math


# print(random.sample(range(1, 18), 4))
# [5, 11, 8, 4]
a = []
birth_day = 4
birth_month = 10
for i in range(0, 1000000):  # Шелла
    a.append(i)
b = []
o = 0
while o < 99999:  # сортировка слиянием
    r = random.uniform(-1, 1)
    b.append(r)
    o += 1
o = 0
tochka = []
r = birth_day / birth_month

while o < 42000:  # сортировка выбором
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    u = [x, y]
    tochka.append(u)
    o += 1

n = open('1text1.txt', 'r')  # сортировка вставками
n = (n.read().split())


def sort_1(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2 ** k - 1
    return array


def sort_2(m):
    if len(m) > 1:
        mid = len(m) // 2
        left = m[:mid]
        right = m[mid:]
        sort_2(left)
        sort_2(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                m[k] = left[i]
                i += 1
            else:
                m[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            m[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            m[k] = right[j]
            j += 1
            k += 1
    return b

def sort_3(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def sort_4(z):
    for i in range(len(z)):
        j = i - 1
        buff = z[i]
        while z[j] > buff and j >= 0:
            z[j + 1] = z[j]
            j -= 1
        z[j + 1] = buff
    return z

#def write_to_file(output, file_path):
 #   with open(file_path, 'w') as file:
  #      file.write(output)

#write_to_file(sort_1(a), 'output.txt')

with open('output.txt', 'w') as f:
    f.write(','.join(map(str, sort_1(a))))
    f.write(','.join(map(str, sort_2(b))))
    f.write(','.join(map(str, sort_3(tochka))))
    f.write(','.join(map(str, sort_4(n))))