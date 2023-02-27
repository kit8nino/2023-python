from datetime import date
import datetime


dannie = ("Котов", "Дмитрий", "Владимирович", 16,6,2004)
ocenki={
    "Алгебра": 5,
    "Геометрия": 4,
    "Русский язык": 4,
    "Литература": 4,
    "История": 4,
    "Английский язык": 5,
    "физика": 4,
    "Информатика": 5,
    "ИЗО": 5,
    "География": 5,
    "Физическая культура": 5,
    "Химия": 5,
    "Музыка": 5,
    "Экономика": 4,

}

rodstvenniki = ["Людмила","Татьяна","Лев","Светлана"]

imyakiva = "Мира"

def main():

    sredniu = 0
    for i in ocenki:
        sredniu+=ocenki[i]
    sredniu/=len(ocenki)
    return sredniu
print ("Nomer 1", main())


rodstvenniki.append(dannie[1])
ynikalnoe = list(set(rodstvenniki))
print("Nomer 2",  ynikalnoe)

def dlina():
    summa = 0
    for i in ocenki:
        summa+=len(i)
    return summa
print("Nomer 3", dlina())


uniqal = []
for i in ocenki:
    uniqal +=i
uniqal_bukvi = set(uniqal)
print("Nomer 4", uniqal_bukvi)



binimyakiva= " ".join(format(ord(i), "b") for i in imyakiva)
print("Nomer 5", binimyakiva)

r=rodstvenniki
r.sort(reverse=True)
print("Nomer 6", r)

datarojdeniya=datetime.date(int(dannie[5]), int(dannie[4]), int(dannie[3]))
tekushyadata=datetime.date.today()
qw=datarojdeniya-tekushyadata
rez=str(qw)
print("Nomer 7", rez[1:].split()[0])

FIFO=[]
print("Nomer 8")
while (True):
    c=input()
    if (c=="стоп"):
        for i in range(len(FIFO)):
            print(FIFO.pop())
        break
    FIFO.append(c)

    
number = ((int(dannie[3]) + int(dannie[4])**2 + int(dannie[5])) % 21 + 1)
print("Nomer 9", number)

while (True):
    index=int(input())
    if index>=0 and index < len(r):
        r[int(index)]="Cecetzin"
    break
print(r)









    



