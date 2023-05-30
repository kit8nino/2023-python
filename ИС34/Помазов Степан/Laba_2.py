import random
import math
from random import uniform as unif
from random import choice
#print(random.sample(range(1, 18), 4))
#вывело [2, 10, 13, 9] - это bubble sort,Quicksort,Heapsort,Bucket sort

def BubbleSort(A):
    print('Началась сортировка BubbleSort!!!')
    N = len(A)
    for i in range(N-1):
       for j in range(N-2, i-1 ,-1):
          if A[j+1] < A[j]:
             A[j], A[j+1] = A[j+1], A[j]
    return A

def QuickSort(A):
    if len(A) <= 1: return A
    X = choice(A)
    B1 = [b for b in A if b < X]
    BX = [b for b in A if b == X]
    B2 = [b for b in A if b > X]
    return QuickSort(B1) + BX + QuickSort(B2)

def HeapSort(A):
    print('Началась сортировка HeapSort!!!')
    N = len(A)
    for i in range(N-1):
        nMin = i
        for j in range(i + 1, N):
            if A[j] < A[nMin]:
                nMin = j
            if i != nMin:
                A[i], A[nMin] = A[nMin], A[i]
    return A
def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var


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

#### ИСХОДНЫЕ_ДАННЫЕ ######
num_list = [random.randint(0,999999) for i in range(1000000)]
rand_float_list = [unif(-1,1) for i in range(100000)] # 99999 случайных вещественных чисел в диапазоне от -1 до 1
birth_day = 10
birth_month = 9
r = birth_day / birth_month
c_points = []
for i in range(42000):
    ugol = random.uniform(0, 2 * math.pi)
    x = r * math.cos(ugol * i)
    y = r * math.sin(ugol * i)
    point = complex(x, y) # создание комплексной точки из координат (x, y)
    c_points.append(point.real)
with open("text.txt",encoding='utf-8') as textfile:
    text = textfile.read().lower()
textwords = text.split()
print('Началась сортировка QuickSort!!!')
print(QuickSort(num_list))
print(HeapSort(rand_float_list))
print(bucket_sort(c_points))
print(BubbleSort(textwords))

