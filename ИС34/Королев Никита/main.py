import datetime
# боже упаси написать это, и понять
# данные обо мне, кортеж
me = ['Королев Никита Дмитриевич','6','3','2004']
tuple_me = tuple(me)

# тут словарь
lessons = {'Русский':5,'Математика':4,'Английский':2,'Литература':4,'Алгебра':5,'Геометрия':5,'Физика':4,'ИЗО':5,'Обществознание':3,'Биология':1,'Астрономия':4,'Химия':4,'История':5,'Физкультура':5,'Музыка':5,}

# имена родственников
names = ['Светлана','Игорь','Андрей','Надежда','Екатерина','Виктор','Дмитрий','Иван','Богдан','Роман','Лия','Арина','Рената','Альбина','Виктор']
names2 =[]
DateName = {'Светлана':1982,'Игорь':1979,'Андрей':1984,'Надежда':1982,'Екатерина':1964,'Виктор':1962,'Дмитрий':2002,'Иван':2011,'Богдан':2004,'Роман':2000,'Лия':2002,'Арина':2000,'Рената':1998,'Альбина':2003,'Виктор':2012}

# Строка с именем Кивы
Kiva = "Чуханчик"

# 1 Среднее значение оценок по аттестату
x=0
a=0
for i in lessons:
    x=x+int(lessons[i])
a=x/len(lessons)
print('Ответ на 1 вопрос: ',a)

# 2 Уникальное имя, если больше такого не встречается в списке
k=0
for i in names:
    if i not in names2:
        names2.append(i)
    else:
        continue
print('Ответ на 2 вопрос: Уникальные имена членов моей семьи: ',names2)
names2=[]

# 3 Общая длина всех названий предметов
k=0
for i in lessons:
    k+=len(i)
print('Ответ на 3 вопрос: Общая длина всех названий предметов: ',k)

# 4 Уникальные буквы в названии предметов
DiffWord=[]
BadWord=[]
for i in lessons:
    for y in i:
        DiffWord.append(y.lower())
for i in DiffWord:
        if i not in BadWord:
            BadWord.append(i)
print('Ответ на 4 вопрос: Уникальные буквы в слове: ',BadWord)

# 5 Имя домащней кивы в бинарном виде
Kiva2=' '.join(format(ord(x),'b')for x in Kiva)
print('Ответ на 5 вопрос: Имя кивы в бинарном виде:',Kiva2)

# 6 отсортированный по алфавиту (в обратном порядке) список родственников
print('Ответ на 6 вопрос: Отсортированый в обратном порядке список родственников',sorted(names,reverse=True))

# 7 определение колличества дней с момента моего рождения
Birth=datetime.date(int(tuple_me[3]),int(tuple_me[2]),int(tuple_me[1]))
Now=datetime.date.today()
delta=Now - Birth
print('Ответ на 7 вопрос: Количество дней, прошедших со дня моего рождения:',delta.days)

# 8 FIFO очередь, в которую можно добавлять предметы по вводимому с клавиатуры индексу (до команды остановки)
k=1
Ocher=[]
while k==1:
    print('Хотите внести элемент в очередь? 1-да 0-нет')
    k=int(input())
    if k==1:
        print('Введите предмет:')
        a=input()
        Ocher.append(a)
        a=0
    else:
        print('Ответ на 8 вопрос: Выводимая FIFO очередь',Ocher)

# 9 по введеному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя под номером, получаемым из вашей даты рождения: number = (day + month**2 + year) % 21 + 1
print('Отсортированный список родственников: ',sorted(names))
names3=sorted(names)
print('Введите порядковый номер имени, который хотите поменять на Ацтекское')
d=datetime.date(int(tuple_me[3]),int(tuple_me[2]),int(tuple_me[1]))
number=(((d.day+(d.month**2)+d.year)%21)+1)
a=int(input())
print('Имя поменялось на правителя под номером: ',number)
NameAztec=['Tenoch','Acamapichtli','Huitzilihuitl','Chimalpopoca','Xihuitl Temoc','Itzcoatl','Moctezuma I','Atotoztli','Axayacatl','Tizoc','Ahuitzotl','Moctezuma II','Cuitláhuac','Cuauhtémoc','Tlacotzin','Motelchiuhtzin','Xochiquentzin','Huanitzin','Tehuetzquititzin','Cecetzin','Cipac']
names3.insert(a-1,NameAztec[number-1])
names3.pop(a)
print('Ответ на 9 вопрос: Измененный список:',names3)

# 10 создать связанный список, как словарь, где ключ - имя родственника, а значение - индекс слудеющего имени по исходному списку,упорядоченному по их годам рождения, исходный список должен остаться неизменным
DateNameDiff={}
DateNameDiff=sorted(DateName.items(),key=lambda x: x[1])
IskSp={}
for i in range(len(DateNameDiff)-1):
    IskSp[DateNameDiff[i]]=i+1
print(IskSp)

# 11 сделать генератор аликвотной последовательности
var=(len(me[0])*len(names))%4
print('Номер варианта:'+str(var))

print('Напишите 3 первых числа последовательности трибоначчи, поочередно')
n=int(input())
k=int(input())
z=int(input())
number=[n,k,z]
for i in range (0,10):
    l=number[len(number)-1]+number[len(number)-2]+number[len(number)-3]
    print(l)
    number.append(l)