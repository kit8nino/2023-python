# это будет интересно

# список из... 20 чисел

import random
from random import randint
prosto=[]
for i in range(20):
    prosto.append(randint(0,999999))

# список из 99999 вещественных чисел от -1 до 1
import random
vesh=[]
for i in range(99999):
    vesh.append(random.uniform(-1,1))

# 42000 разных точки комплексной плоскости, лежащие в пределах окружности радиуса r = birth_day / birth_month (можно случайных, можно равномерно распределённых), сортировать по модулю;
import math

r=6/3

point=[]
for i in range(42000):
    ugol = random.uniform(0,r*math.pi)
    x=r*math.cos(ugol)
    y=r*math.sin(ugol)
    poit = (x,y)
    point.append(poit)

# отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам.
import re
slova = []
with open('knig.txt', 'r') as f:
    text = f.read().lower()
slova = re.findall(r'\b\w+\b', text)
slova = [word.lower() for word in slova]
f.close
#определяем числа, прогу выведу, здесь 4 моих числа: 3 10 1 2
#print(random.sample(range(1, 18), 4))

#сортировка расческой для списка из 20 чисел
k = int(len(prosto)//1.247)
#print("Изн список",prosto)
for l in reversed(range(k)):
    x = 0
    y = l - 1
    while (y < len(prosto) and x<y):
        if prosto[x] > prosto[y]:
            prosto[x], prosto[y] = prosto[y], prosto[x]
            x += 1
            y += 1
            l -= 1
        else:
            x += 1
            y += 1
            l -= 1
#print("Отсортированный список",prosto)

#быстрая сортировка вещественных чисел
def quicksort(x):
    if len(x)<=1:
        return x
    else:
        q=random.choice(x)
        f_nums = []
        s_nums = []
        l_nums = []
        for n in x:
            if n<q:
                f_nums.append(n)
            elif n>q:
                l_nums.append(n)
            else:
                s_nums.append(n)
        return quicksort(f_nums)+s_nums+quicksort(l_nums)
#print(vesh)
#print(quicksort(vesh))

# шейкерная сортировка
def shaker_sort(array):
    length = len(array)
    swapped = True
    start_index = 0
    end_index = length - 1

    while (swapped == True):

        swapped = False

        # проход слева направо
        for i in range(start_index, end_index):
            if (array[i] > array[i + 1]):
                # обмен элементов
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        # если не было обменов прерываем цикл
        if (not (swapped)):
            break

        swapped = False

        end_index = end_index - 1

        # проход справа налево
        for i in range(end_index - 1, start_index - 1, -1):
            if (array[i] > array[i + 1]):
                # обмен элементов
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        start_index = start_index + 1


#shaker_sort(point)
#print(point)


#сортировка выбором
def bubble(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if len(array[j]) > len(array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
key = ['арбуз','проза','мир','огурец']
#print(bubble_sorting(key))
print(bubble(slova))