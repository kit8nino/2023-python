from datetime import date 
import datetime 
 
qq=("Цветков", "Андрей", "Сергеевич", 9, 4, 2004) 
 
predmet={  
    "Химия" : 3, 
    "Физика" : 4, 
    "Алгебра" : 4, 
    "Геометрия" : 5,
    "Биология" : 4, 
    "Русский язык" : 4, 
    "Литература" : 4, 
    "ИЗО" : 5, 
    "Технология" : 5,
    "Информатика" : 4, 
    "ОБЖ" : 5, 
    "Физическая культура" : 5, 
    "География" : 5, 
    "История России" : 3, 
    "История Всеобщая" : 4, 
    } 
relatives=["Наталия", "Сергей", "Людмила", "Владимир"] 
 
kiwa="Жужалица" 
 
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
relatives.remove("Андрей") 
 
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
        r1[ind]="Cecetzin" 
        break 
print(r1) 
 
 
list10 = {} 
for i in range(len(r)): 
        list10[r[i]] = r[(i+1)%len(r)] 
print("№10", list10) 
 
number = len("ЦветковАндрейСергеевич") * (len(relatives[0])+len(relatives[1])+len(relatives[2])+len(relatives[3]))%4
print("Задание №11, вариант: ",number)

def alikvotnayaposledovatelnost(t,firstt):
    newt=0
    if t==firstt:
        print(t)
    if t==1:
        print(0)
        return
    else:
        for i in range(1,t//2+1):
            if t%i==0:
                newt+=i
        print(newt)
        return alikvotnayaposledovatelnost(newt,firstt)
    
B=int(input("Функция выведет аликвотную последовательность для введённых чисел: "))
alikvotnayaposledovatelnost(B,B)
 
 
 
 
 
 
