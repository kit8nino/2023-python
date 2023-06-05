"""
import random

print(random.sample(range(1, 18), 4))


#[4, 10, 1, 2]
#1.shaker sort, сортировка перемешиванием;
#2.bubble sort, сортировка пузырьком;
#4.insertion sort, сортировка вставкой;
#14.least significant digit;
"""
import random
import cmath
import re

spisok_1=[x for x in range(1000000)]
print("1.Cписок целых чисел от 0 до 999999:", spisok_1)

spisok_2 = []
for i in range(99999):
    spisok_2.append(random.uniform(-1, 1))  # список вещественных чисел в диапазоне
print("2.Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]:", spisok_2)


#Генерация значений списка из 42000 разных точек комплексной плоскости, лежащие в пределах окружности радиуса r
r = int(16/6)
comSpisok=[]
while True:
    comchisla=complex(random.randint(-r,r)/random.random(),random.randint(-r,r)/random.random())
    if len(comSpisok)==42000:
        break
    if comchisla.real**2+comchisla.imag**2<=r**2:
        comSpisok.append(comchisla)
print("3.42000 разных точки комплексной плоскости, лежащие на окружности радиуса:", comSpisok, )
#Импорт значений списка из слов отрывка книги
with open("textlab_2.txt", "r", encoding="utf8") as file:
    text = file.read()
    text = re.sub("[^a-zA-Zа-яА-Я]", " ", text)
    words = text.split()
print("4.Отрывок из книги:", words)

#insertion sort, для 1 списка
def insertionSort(spisok_1):
    for i in range(len(spisok_1)):
        current_value=spisok_1[i]
        position=i
        while position > 0 and spisok_1[position-1] > current_value:
            spisok_1[position]=spisok[position - 1]
            position -=1
            spisok_1[position]=current_value
    return spisok_1

result=insertionSort(spisok_1)
                

#Quicksort, для 2 списка
def quicksort(spisok_2):
    if len(spisok_2) <= 1:
        return spisok_2
    a = spisok_2[len(spisok_2) // 2]
    sleva = [x for x in spisok_2 if x < a]
    seredina = [x for x in spisok_2 if x == a]
    pravo = [x for x in spisok_2 if x > a]
    return quicksort(sleva) + seredina + quicksort(pravo)

#shaker sort, для 3 списка
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


#Bubble sort, для 4 списка
def bubble_sort(words):
    n = len(words)
    for b in range(n):
        for j in range(n - b - 1):
            if words[j] > words[j + 1]:
                words[j], words[j + 1] = words[j + 1], words[j]# Меняем элементы местами

bubble_sort(words)


print("Отсортированный массив по insertionsort: ", result)
print("Отсортированный массив по Quicksort: ", quicksort(spisok_2))
print("Отсортированный масиив по bubble sort: ",  ' '.join(words))
print("Отсортированный масиив по shakersort: ", shakerSort(comSpisok))
                







