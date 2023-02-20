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

r=relatives
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

while (True):
    ind=int(input())
    if ind >=0 and ind < len(r):
        r[ind]="Moctezuma II"
        break
print(r)
    
    

    



