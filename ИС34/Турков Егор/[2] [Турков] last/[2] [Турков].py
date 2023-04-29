nl1 = []
nl2 = []
pl = []
wl = []
#1 - Bubble sort
#n = 100 - test
#n = 999999 - real
from random import randint
for i in range (0,n):
   nl1.append(randint(0,n))
for i in range(n-1):
    for j in range(n-i-1):
        if nl1[j] > nl1[j+1]:
            nl1[j], nl1[j+1] = nl1[j+1], nl1[j]
 
print(nl1)

#2 - Selection sort
#k = 100 - test
#k = 999999 - real
import random
for i in range (0,k):
   nl2.append(random.uniform(-1, 1))
for i in range(0,k-1):
    min = i
    for j in range(i+1,k):
        if nl2[j]< nl2[min]:
            min = j
    temp = nl2[i]
    nl2[i] = nl2[min]
    nl2[min] = temp
print (nl2)

#3 dwarf sort

#h = 100 - test
#h = 42000 - real
#r = 24/6 = 3
while len(pl)!=h:
    a = random.uniform(-3, 3)
    b = random.uniform(-3-a, 3-a)
    c = [a,b]
    if a**2+b**2 <=9:
        pl.append(c)
#print (pl)
g = len(pl)
i = 0
while i + 1 < g:
   if pl[i + 1][0]+pl[i + 1][1] >= pl[i][0]+pl[i][1]:
       i += 1
   else:
       pl[i], pl[i + 1] = pl[i + 1], pl[i]
       if i > 0:
           i-=1
       else:
           i+=1
print (pl)

#4 insertion sort
#f = open('4.txt') - test
#f = open('4_r.txt') - real
while True:
    line = f.readline()
    if not line:
        break
    wl = wl + line.split()
#print (wl)
    def insort(a):
        for i in range(1, len(a)):
            inst = a[i]
            k = len(a[i])
            j = i - 1
            while j >= 0 and len(a[j]) > k:
                a[j + 1] = a[j]
                j -= 1
                a[j + 1] = inst
insort(wl)
print (wl)
    