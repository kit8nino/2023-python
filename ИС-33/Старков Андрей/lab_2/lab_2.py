"""
import random

print(random.sample(range(1, 18), 4))

#[2, 10, 1, 4]
1. Сортировка перемешиванием(Shaker sort);
2. Сортировка пузырьком(Bubble sort);
4. Сортировка вставкой(Insertion sort);
10. Быстрая сортировка(Quicksort).
"""
import random
import cmath
import re
#Импорт и генерация списков

#Генерация значений списка целых чисел от 0 до 999999 
list1=[x for x in range(1000000)]

#Импорт значений списка из 99999 случайных вещественных чисел в диапазоне [-1, 1]
list2=[]
with open("2_2.csv", "r") as file2:
    for line in file2:
        list2.append([float(x.replace(",",".")) for x in line.split()])

#Генерация значений списка из 42000 разных точек комплексной плоскости, лежащие в пределах окружности радиуса r
r = int(28/5)
comNumL=[]
while True:
    comNum=complex(random.randint(-r,r)/random.random(),random.randint(-r,r)/random.random())
    if len(comNumL)==42000:
        break
    if comNum.real**2+comNum.imag**2<=r**2:
        comNumL.append(comNum)

#Импорт значений списка из слов отрывка книги
text=[]
with open("2_4.txt",encoding="utf-8",mode="r") as data:
    for line in data:
        line = re.sub(r'[^ А-я]', '', line)
        for i in line.split():
            text.append(i)

#Алгоритмы
#Реализация сортировки 2 - сортировка пузырьком, для списка целых чисел от 0 до 999999 
def bubbleSort(data):
    for i in range(len(data)-1):
        stop=0
        for j in range(len(data)-1-i): 
            if(data[j]>data[j+1]): 
                data[j], data[j+1] = data[j+1], data[j]
                stop=1
                print("Replace")
            print("Skip",i)
        if stop ==0:
            break
    return data

#Реализация сортировки 10 - быстрой сортировки, для второго списка из 99999 случайных вещественных чисел в диапазоне [-1, 1]
def quickSort(data):
   if len(data) <= 1:
       return data
   else:
       supPoint = random.choice(data)
       smNums = [x for x in data if x < supPoint]
       medNums = [x for x in data if x == supPoint]
       bigNums = [x for x in data if x > supPoint]
       return quickSort(smNums) + medNums + quickSort(bigNums)

#Реализация сортировки 1 - сортировки перемешиванием, для третьего списка из 42000 разных точек комплексной плоскости, лежащие в пределах окружности радиуса r
def shakerSort(data):
    left = 0
    right = len(data)-1
    while left<right:
        for i in range(left,right):
            if (data[i].real**2+data[i].imag**2)**0.5 > (data[i+1].real**2+data[i+1].imag**2)**0.5:
                data[i], data[i+1] = data[i+1], data[i]
                k = i
        right = k
        
        for i in range(right, left,-1):
            if (data[i].real**2+data[i].imag**2)**0.5 < (data[i-1].real**2+data[i-1].imag**2)**0.5:
                data[i], data[i-1] = data[i-1], data[i]
                k = i
        left = k
    return data

#Реализация сортировки 4 - сортировка вставками, для четвёртого списка из слов отрывка книги
def insertionSort(data):
	for i in range(len(data)):
		j = i - 1 
		buff = data[i]
		while data[j] > buff and j >= 0:
			data[j + 1] = data[j]
			j -= 1
		data[j + 1] = buff
	return data

#Оболочка
print("Рандомайзер выдал мне такой список значений [2, 10, 1, 4]:\n2. Сортировка пузырьком(Bubble sort);\n10. Быстрая сортировка(Quicksort);\n1. Сортировка перемешиванием(Shaker sort);\n4. Сортировка вставкой(Insertion sort).")
while True:
    wrLn=input("Введите номер списка для проверки(для завершения введите 'ex'):")
    if wrLn=="1":
        print(bubbleSort(list1))
    elif wrLn=="2":
        print(quickSort(list2))
    elif wrLn=="3":
        print(shakerSort(comNumL))
    elif wrLn=="4":
        print(insertionSort(text))
    elif wrLn=="ex":
        break
    else:
        print("Введено неверное значение!")
