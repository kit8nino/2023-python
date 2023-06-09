import datetime
import queue
my_info=tuple(('Крылов', 'Константин','Дмитриевич',20,8,2004))
print(my_info)
disc={'алгебра':4,'англ': 5,'астрономия':5,'Биология':4,'география':4,'геометрия':4,'информатика':5,'история':4,'краеведение':5,'литература':4,'обществознание':4,'ОБЖ':5,'русский':4,'физика':4,'физра':5}
relat=['Игорь','Леша','Люда','Зоя','Дима','Гена','Антон','Дима']
zver='Валенсия'

#Task 1

n=len(disc.values())
summ_mark = 0
for value in disc.values():
    summ_mark += value
mean_mark=summ_mark/n
print('средняя оценка в аттестате: ',mean_mark)

#task2

relat.append(my_info[1])
rel_unique=list(set(relat))
print('ответ на 2 задание' ,rel_unique)
relat.remove('Константин')

#task3

che=''
for elem in disc.keys():
    che+=elem
print('Ответ на 3 задание',len(che))

#Task4

dt=list(disc)
b=0
newD=[]
while b<len(disc):
    newD+=list(dt[b].lower())
    b+=1
print('Ответ на 4 задание: ',(set(newD)))

#Task 5

zverBIN=(''.join(format(ord(c),'b')for c in zver))
print('ответ на 5 задание: ',zverBIN)

#task6

sorted_relat= sorted(relat,reverse=1)
print('ответ на 6 задание',sorted_relat)

#task 7

today=datetime.datetime.now()
birthday=datetime.datetime(int(my_info[5]),int(my_info[4]),int(my_info[3]))
proshlo=today-birthday
print('Ответ на 7 вопрос : я живу уже',proshlo)

#task8

print('Вопрос 8. Вводите индекты предметов, которые хотите вывести на экран(для продолжения введите 23)')
disc1=list(disc)
FIFO=[]
index=[]
s=0
while (s!=23 and s<=len(disc)):
    s=int(input())
    if s !=23:
        index.append(s)
for o in index:
    FIFO.append(disc1[o])
print(FIFO)

#task9

digit=((int(my_info[3])+int(my_info[4])**2+int(my_info[5]))%21+1)
print('номер правителя: ',digit)
print('Введите индекс, чье имя вы хотите заменить на правителя: ')
relat1=relat.copy()
while(True):
    number = int(input())
    if (number>=0 and number<len(relat1)):
        relat1[int(number)]= 'Tizoc'
        break
    else: print('неправильный индекс')
print('Ответ на 9 вопрос: ', relat1)

#task 10

dictionary={}
for i in range(len(relat)):
    dictionary[relat[i]]=relat[(i+1)%len(relat)]
print('task 10; ',dictionary)

#task 11

my_fio=len('КрыловКонстантинДмитриевич')*len(relat)%4
print('Вопрос 11: Вариант: ', my_fio,' - аликвотной последовательности')

def alikvotnost(x,y):
    sum=0
    if x==y:
        print(x)
    if x == 1:
        print(0)
        return 0
    else:
        for i in range(1,x):
            if x%i==0:
                sum+=i
    print(sum)
    return alikvotnost(sum,x)
g=int(input('Введите число: '))
print('аликвотная последовательность числа ',g,': ')
alikvotnost(g,g)
#чтобы прога не закрывалась
h=int(input())