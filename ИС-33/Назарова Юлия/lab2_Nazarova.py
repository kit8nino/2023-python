import random
import cmath
import math


f=open("book_list.txt", encoding='utf-8')
a=f.read()
a=a.replace('\n', ' ')
a=a.replace('.', ' ')
a=a.replace(',', ' ')
a=a.replace(':', ' ')
a=a.replace('"', ' ')
a=a.replace('-', ' ')
a=a.replace('!', ' ')
a=a.replace('?', ' ')
a=a.replace(';', ' ')
a=a.replace(')', ' ')
a=a.replace('(', ' ')
a=a.replace('«', ' ')
a=a.replace('»', ' ')
listnow=a.split()

masint=[]#массив целых чисел
mas=[]#массив вещественных чисел
for i in range(1_000_000):
    masint.append(random.randint(0, 999999))

for i in range(100_000):
    mas.append(random.uniform(-1, 1))
    
    
modulcom=[]
complexmas=[]
r=4/8
for i in range(42000):
    x=random.uniform(-r, r)
    y=random.uniform(-r, r)
    radius=math.sqrt(x**2 + y**2)
    if radius<=r:
        complexmas.append(complex(x, y))
        modulcom.append(math.sqrt(x**2 + y**2))
    if len(complexmas)==1000:
        break

def bubble_sort(mas):
    for i in range(len(mas) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if mas[j + 1] < mas[j]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]
                no_swap = False
        if no_swap:
            return


def insertion_sort(mas): 
    for i in range(1, len(mas)):  
        value = mas[i] 
        j = i - 1 
        while j >= 0 and value < mas[j]: 
            mas[j + 1] = mas[j] 
            j -= 1 
        mas[j + 1] = value 
    return


def comp_sort(A, B):
    step = len(A) - 1
    while step > 0:
        for i in range(0, len(A)-step):
            if (A[i] > A[i+step]):
                A[i], A[i+step] = A[i+step], A[i]
                B[i], B[i+step] = B[i+step], B[i]
        step = int(step//1.25)
    return


def gnome_sort(mas):
    i = 1
    while i < len(mas):
        if mas[i]<mas[i-1]:
            mas[i], mas[i-1] = mas[i-1], mas[i]
            i = i-1 if i > 1 else i+1
        else:
            i += 1
    return




print("Лабараторная работа №2. Алгоритмы сортировки")
print("--------------------------------------------------------------------------------------------------------------------------------------")
print("Задание 1. Не отсортированный список:", masint) 
insertion_sort(masint) 
print("Задание 1. (Сортировка вставками) Отсортированный список:", masint)
print("--------------------------------------------------------------------------------------------------------------------------------------")
print("")
print("Задание 2. Не отсортированный список:", mas) 
bubble_sort(mas)
print("Задание 2. (Сортировка пузырьком) Отсортированный список:", mas) 
print("--------------------------------------------------------------------------------------------------------------------------------------")
print("")
print("Задание 3. Не отсортированный список:", complexmas) 
comp_sort(modulcom, complexmas)
print("Задание 3. (Сортировка расческой ) Отсортированный список:", complexmas)
print("")
print("--------------------------------------------------------------------------------------------------------------------------------------")
print("Задание 4. Не отсортированный список:", listnow)
print("Это отрывок из романа Мастер и Маргарита. В данном отрывке", len(listnow), "слов.  ")
gnome_sort(listnow) 
print("Задание 4. (Гномья сортировка) Отсортированный список:", listnow)
print("--------------------------------------------------------------------------------------------------------------------------------------")