import datetime


name=('Пилкина','Алиса','Денисовна',27,9,2004)
SchSub= {'Математика':4, 'Физика':5, 'Химия':5,'Астрономия':5, 'Литература':4, 'История':2, 'География':2, 'ОБЖ':4, 'ФК':5,'Немецкий язык':4, 'Черчение':5, 'Экспериментальная физика':4, 'Биология':5, 'Английский':4, 'Русский':4}
nameR=['Денис', 'Наталья','Никита','Анастасия','Елена','Алексей','Матвей','Светлана','Алекса','Александр']
nameK='Дастер'
opt= len(name[0]+name[1]+name[2])*len("".join(nameR))%4

#1
a = sum(SchSub.values())/len(SchSub)
print("1) Средняя оценка в аттестате:", a,"\n")

#2
def s(person,nam):
    names = []
    names.append(person[1])
    for i in range(len(nam)):
        names.append(nam[i])
    return list(set(names))

print("2) Уникальные имена родственников и свое:", *s(name,nameR), sep=',' )
print("")
#3

def Leng():
    summa=0
    for i in SchSub:
        summa += len(i)
    return summa
print("3) Общая длина всех названий предметов: ",Leng(),"\n")

#4

def unique(g):
    uni = set()
    for f in g:
        for letter in f:
            uni.add(letter)
    return uni
print("4) Уникальные букви: ",unique(SchSub),"\n")

#5

def dvoich(word):
    binar = []
    for letter in word:
        binary = bin(ord(letter))[2:]  # Преобразуем символ в его двоичное представление
        binar.append(binary)
    return binar
rez="".join(dvoich(nameK))
print("5) Имя в двоич. представлении: ",rez,"\n")

#6

def sortirovochka(nameR):
    sortNames = nameR
    sortNames.sort(reverse=True)
    return sortNames

print("6) Сортировка в обратном порядке:", sortirovochka(nameR),"\n")

#7

def dni(name):
    LastDate = datetime.datetime(name[5],name[4],name[3])
    NowDate = datetime.datetime.now()
    return (NowDate - LastDate).days

print("7) Прошло", dni(name),"дней. ","\n")

#8

queue = []

while True:
    print("Список предметов:")
    for index, subject in enumerate(SchSub.keys()):
        print(f"{index}: {subject}")

    item = input("Введите стоп для остановки или что-то другое чтобы открыть список предметов): ")

    if item.lower() == "стоп":
        break

    index = int(input("Введите индекс : "))
    subject = list(SchSub.keys())[index]
    queue.append(subject)
print("8) Очередь ", (queue),  "\n")

#9

num=((int(name[3])+int(name[4])**2+int(name[5]))%21+1)
print("Выберите индекс родственника:D от 0 до ",num)
izmen=sortirovochka(nameR).copy()
while(True):
    nomer=int(input())
    if nomer>=0 and nomer<len(izmen):
        izmen[nomer]="Huitzilihuitl"
        break
print("9) Измененный список",izmen)

#10

def cheto():
    sspisok ={"Матвей":2, "Наталья":0, "Светлана":7, "Алексей":5, "Денис":6, "Анастасия":4, "Елена":9, "Алекса":1, "Никита":8, "Александр":3}
    return sspisok
print("10) список :",cheto(),"\n")

#11!!!

print("мой вариантик = ", opt,"(аликвотная последовательность)")

def aliquot_sequence(n):
    yield n
    while n != 1:
        n = sum(i for i in range(1, n) if n % i == 0)
        yield n
for num in aliquot_sequence(10):
    print("11) последовательность : ", num)