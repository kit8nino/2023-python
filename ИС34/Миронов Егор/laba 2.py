#Числа от 0 до 999999
chisla=list(range(0,1000000))
#список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
import random
rondom=[]
for i in range(99999):
    a=random.uniform(-1,1)
    rondom.append(a)

#42000 разных точки комплексной плоскости, лежащие в пределах окружности радиуса r = birth_day / birth_month (можно случайных, можно равномерно распределённых), сортировать по модулю;
r=20/9
import math
i=0
completh=[]
for i in range(42000):
    j=random.uniform(0,2 *math.pi)
    x=r*math.cos(j)
    y=r*math.sin(j)
    completh.append(complex(x,y).real)

#Книга отрывок
with open("Сталкер.txt", "r", encoding = "utf-8") as slova:
    txt=slova.read().lower()
    words=txt.split()

#Сортировка
a=random.sample(range(1, 18), 4) # вернет список из 4 случайных значений в заданном диапазоне, сделать один раз
#1,11,7,13


#1.Сортировка перемешиванием(shaker sort)
random.shuffle(chisla)#перемешаю масив чтоб проверить работу сортировки(проверил на списке из 10000 чисел)
i=0
b=0
c=len(chisla)-1
while b!=c:
    i=0
    while i != c:
        if chisla[i] > chisla[i + 1]:
            chisla[i], chisla[i + 1] = chisla[i + 1], chisla[i]
        i += 1
    while i != 0:
        if chisla[i] < chisla[i - 1]:
            chisla[i], chisla[i - 1] = chisla[i - 1], chisla[i]
        i -= 1
    b=0
    while i!=c:
        if chisla[i] < chisla[i + 1]:
            i+=1
            b+=1
        else:
            i+=1
            b=0
print("1.",chisla)
#11.Merge sort, сортировка слиянием;
def Sliv(sort):
    if len(sort)>1:
        mid = len(sort)//2
        lef_Sliv = sort[:mid]
        right_Sliv = sort[mid:]
        Sliv(lef_Sliv)
        Sliv(right_Sliv)
        i=0
        b=0
        c=0
        while i<len(lef_Sliv) and b<len(right_Sliv):
            if lef_Sliv[i]<right_Sliv[b]:
                sort[c]=lef_Sliv[i]
                i+=1
            else:
                sort[c]=right_Sliv[b]
                b+=1
            c+=1
        while i<len(lef_Sliv):
            sort[c]=right_Sliv[i]
            i+=1
            c+=1
        while b<len(right_Sliv):
            sort[c]=right_Sliv[b]
            b+=1
            c+=1
Sliv(rondom)
print("2.",rondom)

#7.Gnome sort, гномья сортировка;
i=0
c=len(completh)
while i!=c:
    if completh[i] > completh[i - 1] or completh[i] == completh[0]:
        i += 1
        continue
    elif completh[i] < completh[i - 1]:
        completh[i], completh[i - 1] = completh[i - 1], completh[i]
        i -= 1
        continue
print("3.",completh)

#13.Bucket sort, блочная (карманная) сортировка;
def Bucket(tekst):
    r = max(tekst)
    c = len(tekst)
    b = r / c
    bloky = []
    for j in range(c):
        bloky.append([])
    for i in range(c):
        a =int(tekst[i] / r)
        if a != c:
            bloky[a].append(tekst[i])
        else:
            bloky[c - 1].append(tekst[i])
    for g in range(c):
        for i in range(1, len(bloky[g])):
            vnutry=bloky[g]
            h=vnutry[i]
            j=i-1
            while(j>=0 and h<vnutry[j]):
                vnutry[j+1]=vnutry[j]
                j=j-1
            vnutry[j+1]=h
    the_end = []
    for i in range(c):
        the_end = the_end + bloky[i]
    return (the_end)
chisla_words=[len(i) for i in words] #преобразуем слова в числа
print("4.",Bucket(chisla_words))