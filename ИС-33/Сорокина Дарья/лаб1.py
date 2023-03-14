from datetime import date
import datetime

qq=("Сорокина", "Дарья", "Андреевна", 28, 10, 2004)

predmet={
    "Биология" : 3,
    "Русский язык" : 4,
    "Литература" : 3,
    "ИЗО" : 5,
    "Технология" : 5,
    "Химия" : 3,
    "Физика" : 4,
    "Алгебра" : 4,
    "Геометрия" : 5,
    "Информатика" : 4,
    "ОБЖ" : 5,
    "Физическая культура" : 4,
    "География" : 5,
    "История России" : 3,
    "История Всеобщая" : 4,
    }
relatives=["Елена", "Ирина", "Иван", "Александр", "Александр"]

kiwa="Димкарф"

def srb():
    summa=0
    for i in predmet:
        summa += predmet[i]
    summa /= len(predmet)
    return summa
print ("№1", srb())

relatives.append(qq[1])
uniq = list(set(relatives))
print("№2", uniq)
relatives.remove("Дарья")

def kol():
    summa = 0
    for i in predmet:
        summa += len(i)
    return summa
print("№3", kol())

b = " "
for i in predmet:
    b += i
mnb=[]
for i in b:
    n=0
    for j in b:
        if i==j:
            n += 1
    if n == 1:
       mnb += [i]
print ("№4", mnb)

binkiwa = ' '.join(format(ord(x), '08b') for x in kiwa)
print("№5", binkiwa)

r=relatives.copy()
r.sort(reverse=True)
print("№6", r)

dr=datetime.date(int(qq[5]), int(qq[4]), int(qq[3]))
td=datetime.date.today()
da=dr-td
rez=str(da)
print("№7", rez[1:].split()[0])

print("№8")
FIFO=[]
while (True):
    sl=input()
    if (sl=="стоп"):
        for i in range(len(FIFO)):
            print(FIFO.pop())
        break
    FIFO.append(sl)

print("№9")
number = ((int(qq[3]) + int(qq[4])**2 + int(qq[5])) % 21 +1)
print(number)
r1=r.copy()
while (True):
    ind=int(input())
    if ind >=0 and ind < len(r1):
        r1[ind]="Moctezuma II"
        break
print(r1)


list10 = {}
for i in range(len(r)):
        list10[r[i]] = r[(i+1)%len(r)]
print("№10", list10)

print("Задание №11 вариант: ")
number=len("СорокинаДарьяАндреевна")*(len(relatives[0])+len(relatives[1])+len(relatives[2])+len(relatives[3])+len(relatives[4]))%4
print(number)

def alikvotposl(x, x1):
    nx=0
    if x==x1:
        print(x)
    if x==1:
        print(0)
        return
    else:
        for i in range(1, x//2+1):
            if x%i==0:
                nx+=i
        print(nx)
        return alikvotposl(nx, x1)
print("Функция выведет аликвотную последовательность для введённых чисел: ")
A=int(input())
alikvotposl(A, A)

print("Всё!")
    
    
    

    



