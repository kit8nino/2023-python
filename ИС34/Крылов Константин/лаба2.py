import random
import math
import re
print((random.sample(range(1, 18), 4)))
# [16, 8, 6, 2]
intchisla=[random.randint(0,999999)for i in range(999999)]
real_numbers=[random.randint(-1,1)for i in range(999999)]

r=20/8
points=[]
for i in range(42000):
    h=random.uniform(0,2*math.pi)
    x=r*math.cos(h)
    y=r*math.sin(h)
    points.append((x,y))

with open('Война и мир.txt','r', encoding='utf-8')as f:
    text=f.read().lower()
texts=re.findall(r'\b\w+\b',text)
book=text.split()

#сортировка(8)

def choose_sort(arr):
    n=len(arr)
    for i in range(n):
        minindex=i
        for j in range(i+1,n):
            if arr[j]<arr[minindex]:
                minindex=j
        arr[i],arr[minindex]=arr[minindex],arr[i]
    return arr

real_number='Числа от -1 до 1.txt'
with open(real_number,'w')as f:
    f.write(','.join(map(str,choose_sort(real_numbers))))

#сортировка(16)
def digit(x,stepen):
    return int(x/10**(stepen-1))%10

def MSD(arr,low,high,degree):
    if (high-low)<2 or degree<1:
        return
    counts=[0]*10
    temp=[0]*(high-low)

    for i in range(low,high):
        dig=digit(arr[i],degree)
        counts[dig]+=1

    index=0
    for i,count in enumerate(counts):
        counts[i]=index
        index +=count

    for i in range(low,high):
        dig=digit(arr[i],degree)
        temp[counts[dig]]=arr[i]
        counts[dig]+=1

    for i in range(low,high):
        arr[i]=temp[i-low]

    counts.insert(0,0)
    for i in range(len(counts)-1):
        MSD(arr,low+counts[i],low+counts[i+1],degree-1)

def max(arr):
    m = arr[0]
    for i in range(1,len(arr)):
        if arr[i]>m:
            m=arr[i]
    return m

def sort(arr):
    maxim=max(arr)
    d=math.floor(math.log10(abs(maxim)))+1
    MSD(arr,0,len(arr),d)
    return arr
real_number='Числа от 0 до 999999.txt'
with open(real_number,'w')as f:
   f.write(','.join(map(str,sort(intchisla))))

#сортировка (6)

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,data):
    if root is None:
        root=Node(data)
    else:
        if data<=root.data:
            root.left=insert(root.left,data)
        else:
            root.right=insert(root.right,data)
    return root
def order(root,res):
    if root is not None:
        order(root.left,res)
        res.append(root.data)
        order(root.right,res)
def TreeSort(arr):
    root=None
    for data in arr:
        root=insert(root,data)
    res =[]
    order(root,res)
    return res

real_number='42000 разных точек комплексной плоскости.txt'
with open(real_number,'w')as f:
    f.write(','.join(map(str,TreeSort(points))))

#сортировка (2)
def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if len(arr[j])>len(arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

real_number = 'книга отсорт.txt'
with open(real_number,'w')as f:
    f.write(','.join(map(str,bubble(book))))