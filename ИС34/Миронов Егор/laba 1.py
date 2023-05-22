import datetime
# Мои данные
My=["Mironov Egor Sergeevich","20","9","2003"]
#Предметы и их оценки
predmet={"Русский язык":4, "Математика":5, "Литература":5, "Всеобщая история":4, "Информатика":5,"География":4,"Физра":5, "Обществознание":4,"Труды":5, "ИЗО":5,"Химия":4,"Биология":4,"Физика":4,"История России":4}
#Родственники
family=["Надежда","Егор","Сергей","Даниил","Володя","Таня","Михаил","Неля","Мария","Владислав","Олег","Катя"]
#Волосатое махнатое киви
GG="Kivinosets"

#Задача 1
a=0
b=0
for i in predmet:
    a+=int(predmet[i])
b=a/len(predmet)
print("1. Средний бал по предметам=",b)

#Уникальные Имена Задача 2
name_family = list(set(family))
print("2. Уникальные Имена Задача 2",name_family)

#Общаяя длина предметов Задача 3
c=0
for i in predmet:
    c+=len(i)
print("3. Длина всех предметов=",c)

#Уникум буквы в названиях предметов(Задача №4)
bucvs = list(predmet)
pusto=[]
i=0
while i<len(predmet):
  pusto +=list(bucvs[i].lower())
  i+=1
print("4. Уникум буквы в названиях предметов(Задача №4)=",list(set(pusto)))

#Имя киви в бинарном виде(Задача №5)
kivi="".join(format(ord(x),"08b")for x in GG)
print("5. Имя киви в бинарном виде=",kivi)

#Отсортированый список родственников только во обратном порядке (Задача №6)
jimmi=sorted(family, reverse=True)
print("6. Отсортированый список родственников только во обратном порядке",jimmi)

#Количество  дней от вашей даты рождения до текущей даты(Задание №7)
now=datetime.date.today()
DR=datetime.date(int(My[3]),int(My[2]),int(My[1]))
minus=now-DR
print("7.",minus)

#Fifo чередь в которую можно добавлять предметы по вводимому с клавиатуры индексу(до команды остановки), после введения вывести все.
#FIFO- обычная очередь, приходит один в конец, а первый уходит
#надо создать массив в бесконечном цикле

g=1
listic=list(predmet)
spisoc=[]
print("8. Добавьте предмет в список(выход=78)")
print("Предметы=",listic)
while g!=78:
    g=int(input("Введите индекст="))
    if g<=12:
        spisoc.append(listic[g])
    elif g==78:
        break
    else:
        print("Такого индекса нет.")
print("8.",spisoc,"\n")
#Меняю родствеников на Ацтекского правителя
g=(20+9**2+2003)%21+1
print("9. Индекс изменения=",g)
Gravity=jimmi
Gravity.pop(g)
Gravity.insert(g,"Tenoch")
print(Gravity,'\n')

#вернем список jimmi в начальное состояние
jimmi=sorted(family, reverse=True)
#Создать связный список(Словарь)
a=0
b=0
dd={family[a]:jimmi[b]}
b=-1
while a!=11:
    b=b+1
    if jimmi[a] == family[b]:
        dd[family[b]] = jimmi[a + 1]
        a=a+1
        b=-1
        continue
    elif b==12:
        b=-1
        continue
print("10. Конечный словарь=", dd,"\n")

#Функция Генератор(аликвотной последовательности)
number = (len(My[0]) * len(family) % 4)
print("11. Вариант",number)
h=int(input("Введите число="))
b=1
chisla=[]
aga=[h]
while h!=0:
    x = h // 2
    while x!=0:
        if h%x==0.0:
            chisla.append(x)
        x=x-1
    b=sum(chisla)
    chisla.clear()
    aga.append(b)
    h=b
print(aga)
