import random
#[2,10,8,12]

N1 = list(range(1000000))
N2 = [random.uniform(-1, 1) for x in range(1000000)]
N3 = []
birth_day=5
birth_month=6
r = birth_day / birth_month
while len(N3) < 42000:
    x = random.uniform(-r,r)
    y = random.uniform(-r,r)
    z = complex(x,y)
    distance = abs(z)
    if distance <= r:
        N3.append(z)
N4 = open('prest.txt', encoding = 'UTF-8')
word_list = N4.read().split()
N4.close()

def sort2(array):
    a=len(array)
    for i in range(a-1):
        for j in range(a-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

def sort10(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return sort10(left) + middle + sort10(right)

def sort8(arr):
    a = len(arr)
    for i in range(a):
        min = i
        for j in range(i+1, a):
            if abs(arr[j]) < abs(arr[min]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

def sort12(arr):
    max_val = max(arr)
    count_arr = [0] * (max_val + 1)
    for i in arr:
        count_arr[i] += 1
    sort_arr = []
    for i in range(len(count_arr)):
        sort_arr.extend([i] * count_arr[i])
    return sort_arr

print(sort2(word_list))
print(sort10(N2))
print(sort8(N3))
print(sort12(N1))