import random
import math
from random import uniform as unif
from random import choice

# Исходные данные:
birth_day = 3
birth_month = 8
num_list = [random.randint(0, 999999) for i in range(1000000)]

num_float_list = [unif(-1, 1) for o in range(100000)]
r = birth_day / birth_month
tochka = []
# 42000 разных точки комплексной плоскости, лежащие в пределах окружности радиуса
# r = birth_day / birth_month (можно случайных, можно равномерно распределённых), сортировать по модулю:
for i in range(42000):
    ugol = random.uniform(0, 2 * math.pi)
    x = r * math.cos(ugol * i)
    y = r * math.sin(ugol * i)
    point = complex(x, y)
    tochka.append(point.real)
# Чтение файла
h = open("kniga.txt")
kniga = (h.read()).split()
e1=0
#
def HeapSort(A, e1):
    print('Началась сортировка HeapSort!!!')
    N = len(A)
    for i in range(N-1):
        e1 = e1 + 1
        print(e1)
        nMin = i
        for j in range(i + 1, N):
            if A[j] < A[nMin]:
                nMin = j
            if i != nMin:
                A[i], A[nMin] = A[nMin], A[i]
            if (e1 == 10000):
                h = A
                zap1 = open("HeapSort.txt", "w")
                zap1.write(str(h))
                return h

# Сортировка пузырьком
def BubbleSort(A):
    print('Началась сортировка BubbleSort!!!')
    N = len(A)
    for i in range(N-1):
       for j in range(N-2, i-1 ,-1):
          if A[j+1] < A[j]:
             A[j], A[j+1] = A[j+1], A[j]

    return A
# Сортировка
def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var
#
def bucket_sort(input_list):
    print('Началась сортировка BucketSort!!!')
    max_value = max(input_list)
    size = max_value / len(input_list)
    buckets_list = []
    for x in range(len(input_list)):
        buckets_list.append([])
    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])
    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])
    final_output = []
    for x in range(len(input_list)):
        final_output = final_output + buckets_list[x]

    return final_output
#

def QuickSort(A, e1):
    print("Сортировка QuickSort, пожалуйста ждите...")
    if len(A) <= 1: return A
    X = random.choice(A)
    B1 = []
    BX = []
    B2 = []
    for i in A:
        if i < X:
            B1.append(i)
        elif i > X:
            BX.append(i)
        else:
            B2.append(i)

    n = QuickSort(B1, e1) + B2 + QuickSort(BX, e1)
    zap1 = open("QuickSort.txt", "w")
    zap1.write(str(n))
    return n

# Сортировка исходных данных

print(QuickSort(num_list, e1))
print(HeapSort(num_float_list, e1))
print(bucket_sort(tochka))
print(BubbleSort(kniga))