import random
import math
import heapq


spisok1=list(range(0,10))

spisok2=[random.uniform(-1,1) for i in range(99)]

spisok3=[]
r=25/3
for i in range(42000):
    x=random.uniform(-r,r)
    y=random.uniform(-r,r)
    z=math.sqrt(x**2+y**2)
    if z<=r:
        spisok3.append(complex(x,y))

book=[]
b = open('2.txt')
for line in b.readlines():
    for word in line.split():
        book.append(word)

#print(random.sample(range(1,18),4))
#[2, 1, 11, 8]

print('Первая сортировка пузырьком') #по убыванию
for i in range(len(spisok1)):
    flag=0
    for j in range(len(spisok1)-1):
        if spisok1[j] < spisok1[j+1]:
            spisok1[j], spisok1[j+1] = spisok1[j+1], spisok1[j]
            flag=1
        if flag==0:
            break
print('Результат',spisok1)

print('Вторая сортировка перемешиванием')
def mySort1(array):
    left=1
    right=len(array)
    while left<right:
        for i in range(left,right):
            if array[i] < array[i-1]:
                array[i], array[i-1] = array[i-1], array[i]
            if array[right-i] < array[right-i-1]:
                array[right-i], array[right-i-1] = array[right-i-1], array[right-i]
        left +=1; right -=1
    return array
print('Результат',mySort1(spisok2))

print('Третья сортировка слиянием')
def merge_list(a,b):
    c=[]
    i=j=0
    while i<len(a) and j<len(b):
        if abs(a[i]) < abs(b[j]):
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    if i<len(a):
        c+=a[i::]
    if j<len(b):
        c+=b[j::]
    return c

def merge_sort(spisok3_3):
    if len(spisok3_3) <= 1:
        return spisok3_3
    middle=len(spisok3_3)//2
    left=merge_sort(spisok3_3[:middle])
    right=merge_sort(spisok3_3[middle:])

    return merge_list(left, right)
rez=merge_sort(spisok3)
print('Результат',rez)

print('Четвертая сортировка выбором')
for i in range(len(book)):
    min=i
    for j in range(i+1,len(book)):
        if book[j]<book[min]:
            min=j
    if i != min:
        book[i], book[min] = book[min], book[i]

print('Результат', *book)



