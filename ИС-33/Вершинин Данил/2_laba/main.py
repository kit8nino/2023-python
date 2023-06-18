import random
import heapq

#print(random.sample(range(1, 18), 4)) # вернет список из 4 случайных значений в заданном диапазоне, сделать один раз
#[12, 9, 10, 11]

#12 - Counting sort, сортировка подсчетом;
#9 - Heapsort, пирамидальная сортировка;
#10 - Quicksort, быстрая сортировка;
#11 - Merge sort, сортировка слиянием;

integer_list = [i for i in range(1000000)]

veshb_list = [random.uniform(-1, 1) for i in range(1000000)]

zxc = []
birth_day= 1
birth_month= 10
r = birth_day / birth_month
while len(zxc) < 42000:
    x = random.uniform(-r,r)
    y = random.uniform(-r,r)
    z = complex(x,y)
    distance = abs(z)
    if distance <= r:
        zxc.append(z)

sorted_points = sorted(zxc, key=abs)

op = open('lab2_text.txt', encoding = 'UTF-8')
word_list = op.read().split()
op.close()

#12
def Countingsort(arr):
    max_val = max(arr)
    count_arr = [0] * (max_val + 1)
    for i in arr:
        count_arr[i] += 1
    sort_arr = []
    for i in range(len(count_arr)):
        sort_arr.extend([i] * count_arr[i])
    return sort_arr

#9
def Heapsort(qwe):
    heapq.heapify(qwe)
    sorted_words = []
    while qwe:
        sorted_words.append(heapq.heappop(qwe))
    return sorted_words

#10
def Quicksort(num):
   if len(num) <= 1:
       return num
   else:
       q = random.choice(num)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in num:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return Quicksort(s_nums) + e_nums + Quicksort(m_nums)

#11
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if abs(left[i]) < abs(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

#print('Целые числа:', Countingsort(integer_list))
#print('Слова из книги:', Heapsort(word_list))
#print('Вещественные числа:', Quicksort(veshb_list))
print('Точки комплексной плоскости:', merge_sort(sorted_points))