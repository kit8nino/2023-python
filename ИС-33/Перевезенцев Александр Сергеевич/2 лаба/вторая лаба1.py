import random
import math
import heapq
import re

# Исходные данные:

#1
first = list(range(999999 + 1))

#2
second = [random.uniform(-1, 1) for i in range(99999+1)]
#3
third = []
birth_day = 7  
birth_month = 11
r = birth_day / birth_month
third = []
for i in range (42000):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    l = math.sqrt(x**2 + y**2)
    if l <= r:
        third.append(complex(x, y))
#4
fourth = []
f = open('мастермагарита.txt')
for line in f.readlines():
    line = re.sub("[^А-я]"," ", line)
    for text in line.split():
        fourth.append(text)

# Моя сортировка:
# r = (random.sample(range(1, 18), 4))
moesortir = [12, 10, 6, 14]
print(moesortir)

# Counting sort
def twelfthsort(first):
    max_val = max(first)
    count_first = [0] * (max_val + 1)
    for x in first:
        count_first[x] += 1
    sort_first = []
    for x in range(len(count_first)):
        sort_first.extend([x] * count_first[x])
    return sort_first
first = twelfthsort(first)
print("Результат двенадцатой сортировки:")
print(first)

# Quicksort
def tenthsort(second):
    
    if len(second) <= 1:
        return second
    
    elem = second[0]
    left = list(filter( lambda x: x < elem, second))
    center = [i for i in second if i == elem]
    right = list(filter(lambda x: x > elem, second))

    return tenthsort(left) + center + tenthsort(right)

second = tenthsort(second)
print("Результат десятой сортировки:")
print(second)

# Tree sort
def insert_node(root, value):
    if root is None:
        return {'value': value, 'left': None, 'right': None}
    if value.real < root['value'].real:
        root['left'] = insert_node(root['left'], value)
    else:
        root['right'] = insert_node(root['right'], value)
    return root


def traverse_tree(root, sorted_list):
    if root is None:
        return
    traverse_tree(root['left'], sorted_list)
    sorted_list.append(root['value'])
    traverse_tree(root['right'], sorted_list)


def sixthsort(third):
    root = None  
    for value in third:  
        root = insert_node(root, value)
    sorted_list = []
    traverse_tree(root, sorted_list)
    return sorted_list


third = sixthsort(third)
print("Результат шестой сортировки:")
print(third)

# Radix sort
def fourteenthsort(fourth):
    max_length = len(max(fourth, key = len))
    for i in range(len(fourth)):
        fourth[i] = fourth[i].ljust(max_length)
    for i in range(max_length-1, -1, -1):
        fourth = sorted(fourth, key=lambda x: x[i])
    for i in range(len(fourth)):
        fourth[i] = fourth[i].strip()
    return fourth

fourth = fourteenthsort(fourth)
print("Результат четырнадцатой сортировки:")
print(fourth)