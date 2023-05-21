import random
import math
# a = []
# a = random.sample(range(1,18),4)
# print(a)
# Выпали [12, 8, 15, 13] Counting sort, Selection sort, Least significant digit, Bucket sort

#Создание целочисленного списка чисел
quantityIL = 1000000
integerlist = [random.randint(0,quantityIL-1) for i in range(quantityIL)]

#Создание вещественного списка чисел
floatlist = [random.uniform(-1,1) for i in range(100000)]

#Создание текстового списка слов
with open("First.txt",encoding='utf-8') as text:
    text1 = text.read()
booksfragment = text1.split()

#Создание точек комплексных чисел
birth_day = 15
birth_month = 9
r = birth_day/birth_month
complex_points = []
for i in range(42000):
     angle = random.uniform(0, 2 * math.pi)
     x = r * math.cos(angle * i)
     y = r * math.sin(angle * i)
     points = complex(x, y) # создание комплексной точки из координат (x, y)
     complex_points.append(points.real)

#Counting sort
def counting_sort(arr):
    count = [0]*len(arr)
    print('counting cort:')
    for i in arr:
        count[i] = count[i]+1
    for i in range(len(arr)):
        print((str(i)+' ')*count[i],end = '')

#Selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        minvalue = i
        for j in range(i,len(arr)):
            if arr[minvalue]>arr[j]:
                minvalue = j
        arr[i],arr[minvalue]=arr[minvalue],arr[i]
    print('selection sort:\n',arr)

#Least significant digit
def least_significant_digit(arr):
    maximum = max(arr)
    discharge = len(str(maximum))
    pass_list = [[] for _ in range(10)]
    for i in range(discharge):
        for j in arr:
            digit = (j//10**i)%10
            pass_list[digit].append(j)
        arr = []
        for k in pass_list:
            arr.extend(k)
            k.clear()
    print('least significant digit:\n', arr)

#Bucket sort
def bucket_sort(arr):
    bucket = []
    for i in range(len(arr)):
        bucket.append([])
    for j in arr:
        index_b = int(j)
        bucket[index_b].append(j)
    for k in range(len(arr)):
        bucket[k] = sorted(bucket[k])
    d = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[d] = bucket[i][j]
            d += 1
    print('bucket sort:\n',arr)

counting_sort(integerlist)
print('\n')
selection_sort(complex_points)
selection_sort(booksfragment)
least_significant_digit(integerlist)
bucket_sort(floatlist)