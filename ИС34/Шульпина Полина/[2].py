import random
import math
#гномья сортировка
def gnomeSort(lot, size):
    i = 1
    while i < size:
        if (lot[i - 1] <= lot[i]):
            i += 1
        else:
            tmp = lot[i]
            lot[i] = lot[i - 1]
            lot[i - 1] = tmp
            i -= 1
            if (i == 0):
                i = 1
    return lot
#сортировка перемешиванием
def shakerSort(array):
    left = 1
    right = len(array)
    while left<right:
        for i in range(left, right):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
            if array[right-i] < array[right-i-1]:
                array[right-i], array[right-i-1] = array[right-i-1], array[right-i]
        left += 1; right -= 1
    return array
#сортировка слиянием
def mergeSort(A):
    if len(A) <= 1:
        return (A)
    L = mergeSort(A[:len(A) // 2])
    R = mergeSort(A[len(A) // 2:])
    B = []
    l = r = 0
    while l < len(L) and r < len(R):
        B.append(L[l] if L[l] <= R[r] else R[r])
        [l, r] = [l + 1, r] if L[l] <= R[r] else [l, r + 1]
    for l in range(l, len(L)):
        B.append(L[l])
    for r in range(r, len(R)):
        B.append(R[r])
    return B
#быстрая сортировка
def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)

#1-й список: гномья сортировка
numbers=[random.randint(0,999999) for i in range(999999)]
print(gnomeSort(numbers,len(numbers)))

#2-й список: сорировка слиянием
random_number=[round(random.uniform(-1, 1), 2) for x in range(999999)]
print(mergeSort(random_number))

#точки комплексной плоскости: быстрая сортировка
rad = 1.7
p = 2 * math.pi / 42000
points = []
for i in range (42000):
    x = rad * math.cos(i * p)
    y = rad * math.sin(i * p)
    points.append((x, y))
print(quicksort(points))

#текст: сортировка перемешиванием
with open('text', 'r', encoding = 'utf-8') as doc:
  book = doc.read().lower()
import re
s_without_p = re.sub(r'[^ А-я]', '', book)
words = s_without_p.split()
print(shakerSort(words))