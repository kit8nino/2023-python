import datetime

info=("Мокеичева","Екатерина","Васильевна",25,3,2004)

studies={
    "Русский язык":4,
    "Литература":5,
    "Родной язык":4,
    "Родная литература":5,
    "Иностранный язык":5,
    "Математика":4,
    "Информатика":5,
    "МОИ":5,
    "История":5,
    "Обществознание":5,
    "Право":5,
    "География":4,
    "Биология":4,
    "Физика":3,
    "Химия":4,
    "Физическая культура":5,
    "ОБЖ":5,
    "Экономика":5,
    "Культурология":5,}

name=["Марина","Виктор","Татьяна","Анастасия","Елизавета","Василий","Александра","Алексей","Денис","Степан",
      "Дарья","Ксения","Мария","Ирина","Дмитрий","Мария"]

#пусть будет не kiwa, а kiwi, тип птичка
kiwi="Готэм"

def avg():
    summa=0
    for i in studies:
        summa += studies[i]
    summa /= len(studies)
    return summa
print(f"Average value of the list with procision upto 2 demical value: {avg():.2f}")


temp=[]
for x in name:
    if x not in temp:
        temp.append(x)
name=temp
name.append("Екатерина")
print(f"Updated List after removing duplicates = {temp}")

def dlina():
    summa=0
    for i in studies:
        summa += len(i)
    return summa
print("Total length of all item names",dlina())

ggg=""
for h in studies:
    ggg+=h
new=[]
for h in ggg:
    m=0
    for n in ggg:
        if h==n:
            m+=1
    if m==1:
        new+=[h]
print("Unique letters",new)

bin_result=''.join(format(ord(x),'08b') for x in kiwi)
print("Binary kiwi",bin_result)

name.sort(reverse=True)
print("Reverse list",name)

from datetime import date
today_data=date.today()
date_of_birth_date=datetime.date(info[5],info[4],info[3])
delta=today_data-date_of_birth_date
print("Amount of days",delta)

fifo=[]
while(True):
    s=input()
    if (s=="стоп") or (s=="Стоп") or (s=="СТОП") or (s=="stop") or (s=="Stop") or (s=="STOP"):
        for i in range(len(fifo)):
            print(fifo.pop())
        break
    fifo.append(s)

num=((int(info[3])+int(info[4])**2+int(info[5]))%21+1)
print("Ruler number",num)
kq=name.copy()
while(True):
    ff=int(input())
    if ff>=0 and ff<len(kq):
        kq[ff]="Acamapichtli"
        break
print("List with ruler",kq)

name_sort=sorted(name,reverse=True)
new_spisok={}
for i in range(len(name_sort)-1):
    new_spisok[name_sort[i]]=name_sort[i+1]
print("Spisok",new_spisok)


variantik=len("Мокеичева Екатерина Васильевна")*len(name)%4
print("Variantik",variantik)

def alikvotni(x,y):
    s=0
    if x==y:
        print(x)
    if x==1:
        print(0)
        return 0
    else:
        for i in range(1,x):
            if x%i==0:
                s+=i
        print(s)
        return alikvotni(s,x)
G=int(input())
print("Alikvotni posledovat")
alikvotni(G,G)
