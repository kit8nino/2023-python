import random
import math
import heapq

odin = list(range(1000000))
dva = [random.uniform(-1, 1) for i in range(99999)]

tri = []
r = 28/10
for i in range (42000):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    l = math.sqrt(x**2 + y**2)
    if l <= r:
        tri.append(complex(x, y))


chetire=[]
f = open('2.txt', 'r')
for line in f.readlines():
    for word in line.split():
        chetire.append(word)




#print(random.sample(range(1, 18), 4))
#[5, 10, 11, 9]

print("Первая сортировка Шелла")
def shell_sort(odin11):
    gap = len(odin11) // 2
    while gap>0:
        for value in range(gap, len(odin11)):
            current_value =odin11[value]
            position = value
            while position >= gap and odin[position-gap] > current_value:
                odin11[position] = odin11 [position - gap]
                position -= gap
                odin11[position] = current_value
        gap//=2
    return odin
odin1 = shell_sort(odin)
print("Result")
print(odin1)

print("Вторая сортировка, Быстрая сортировка")

def quick_sort(dva2):

    if len(dva2) <= 1:
        return dva2

    elem = dva2[0]
    left = list(filter( lambda x: x<elem, dva2))
    center = [i for i in dva2 if i == elem]
    right = list(filter(lambda x: x>elem, dva2))

    return quick_sort(left) + center + quick_sort(right)

dva22 = quick_sort(dva)
print("Result")
print(dva22)

print("Третья сортировка слиянием")
print("Result")

def merge_two_list(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if abs(a[i]) < abs(b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


def merge_sort(tri3):
    if len(tri3) <= 1:
        return tri3
    middle = len(tri3)//2
    left = merge_sort(tri3[:middle])
    right = merge_sort(tri3[middle:])

    return merge_two_list(left, right)

comp = merge_sort(tri)
print(comp)

print("Четвёртая: Heapsort, пирамидальная сортировка")
print("Result")

def heap_sort(words):
    heapq.heapify(words)
    sorted_words = []
    while words:
        sorted_words.append(heapq.heappop(words))
    return sorted_words


sorted_words = heap_sort(chetire)
print(sorted_words)


