# ИСХОДНЫЕ ДАННЫЕ
import datetime

Data = ('Taimarov Dmitry Alekseevich','2004,9,15')
Attestat = {'Russianlanguage':4,'Literature':5,'Nativelanguage':4,'Englsihlanguage':4,'History':4,'Socialscience':4,'Math':4,'IT':5,'Biology':4,'Chemistry':4,'Physic':4,'Astronomy':4,'PhysicalCulture':4,'OBZH':4,'Geography':5}
Names = ['Alexey','Olga','Vladislav','Anna','Danil','Lyudmila','Aleksandr','Igor','Vitalyi','Aleksandr','Danil','Timur','Andrey','Dmitry']
Kiva = "omarchik"
print("ИСХОДНЫЕ ДАННЫЕ:\n Моё ФИО и ДР: %s\n Аттестат: %s\n Родственники: %szn")

# №1
length = len(Attestat.values())
meanA = 0
for key in Attestat.keys():
    meanA += Attestat[key]
print("№1: \n",meanA/length, sep='')

# №2 и №6
sortedfamily = sorted(set(Names), reverse=True)
print("№2 и №6: \n",sortedfamily,sep='')

# №3
LessonsLength = ''
for key in Attestat.keys():
    LessonsLength += key
print("№3: \n",LessonsLength,sep='')

# №4
uniqueletter = set(LessonsLength)
res = ''
for x in uniqueletter:
    if LessonsLength.count(x) == 1:
        res +=x
print("№4: \n",res,sep='')

# №5
ascii_kiva = []
for letter in Kiva:
    ascii_kiva.append(ord(letter))
i = 0
print("№5:",sep='')
for value in ascii_kiva:
    v = ascii_kiva[i]
    n = ''
    while v > 0:
        n = str(v%2)+n
        v = v//2
    print(n,end=' ')
    i = i+1

# №7
currentdate = datetime.datetime.now()
birth = datetime.datetime(2004,9,15)
period = currentdate - birth
print("\n№7: \n",period,sep='')

# №8
fifo = []
lessons = [elem for elem in Attestat]
print("№8: ")
while True:
    vvod = input('введите ключ(стоп-слово (-1)): ',)
    if vvod == "-1":
        for i in range(len(fifo)):
            print(lessons[i])
        break
    fifo.append(vvod)

# №9
number = ((15+9**2+2004)%21 + 1)
Aztecs = ['Tenoch','Acamapichtli','Huitzilihuitl','Chimalpopoca','Xihuitl Temoc','Itzcoatl','Moctezuma I','Atotoztli','Axayacatl','Tizoc','Ahuitzotl','Moctezuma II','Cuitláhuac','Cuauhtémoc','Tlacotzin','Motelchiuhtzin','Xochiquentzin','Huanitzin','Tehuetzquititzin','Cecetzin','Cipac']
vvod2 = int(input('№9: \nВведите ключ (от 0 до 11): '))
def Aztekinfamily(a,A):
    A[a] = Aztecs[number]
    return (print(A))
azteksortedfamily = sortedfamily.copy()
Aztekinfamily(vvod2,azteksortedfamily)

# №10
linkedlist = {}
for i in range(len(sortedfamily)-1):
    linkedlist[sortedfamily[i]] = sortedfamily[i+1]
print("№10: \n",linkedlist,sep='')

# №11
number2 = len(Data[0])*len(Names) %4
print("№11:\nМой вариант: ",number2)
def Tribonacci(n):
    i = 0
    a, b, c, d = 0, 0, 1, 0
    while i < n:
        d = a+b+c
        print(d, end =' ')
        a = b
        b = c
        c = d
        i += 1
Tribonvalue = int(input("Введите, сколько хотите вывести чисел трибоначчи: "))
Tribonacci(Tribonvalue)