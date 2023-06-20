
#[4, 10, 1, 9]
#4.Insertion sort, сортировка вставкой;
#10.Quicksort, быстрая сортировка;
#1.Shaker sort, сортировка перемешиванием;
#9.Heap sort, пирамидная сортировка

import random
import re
import heapq
spisok_1 = [x for x in range(1000000)]
print("1.Cписок целых чисел от 0 до 999999:", spisok_1)

spisok_2 = []
for i in range(99999):
    spisok_2.append(random.uniform(-1, 1))
print("2.Список из 99999 случайных вещественных чисел в диапазоне [-1, 1]:", spisok_2)

# 42000 разных точек комплексной плоскости, лежащие в пределах окружности радиуса r = birth_day / birth_month
r = int(19/10)
comSpisok = []
while True:
    comchisla = complex(random.randint(-r, r) / random.random(), random.randint(-r, r) / random.random())
    if len(comSpisok) == 42000:
        break
    if comchisla.real ** 2 + comchisla.imag ** 2 <= r ** 2:
        comSpisok.append(comchisla)
print("3.42000 разных точки комплексной плоскости, лежащие на окружности радиуса:", comSpisok, )
# импорт значений списка из слов отрывка книги
with open("войнаимир1.txt", "r", encoding="utf8") as file:
    text = file.read()
    text = re.sub("[^a-zA-Zа-яА-Я]", " ", text)
    words = text.split()
print("4.Отрывок из книги:", words)


# вставкой, 1 список
def insertionSort(spisok_1):
    for i in range(len(spisok_1)):
        current_value = spisok_1[i]
        position = i
        while position > 0 and spisok_1[position - 1] > current_value:
            spisok_1[position] = spisok_1[position - 1]
            position -= 1
            spisok_1[position] = current_value
    return spisok_1


result = insertionSort(spisok_1)


# быстрая, 2 список
def quicksort(spisok_2):
    if len(spisok_2) <= 1:
        return spisok_2
    a = spisok_2[len(spisok_2) // 2]
    levo = [x for x in spisok_2 if x < a]
    seredina = [x for x in spisok_2 if x == a]
    pravo = [x for x in spisok_2 if x > a]
    return quicksort(levo) + seredina + quicksort(pravo)


# перемешивание , 3 список
def shaker_sort(data):
    left = 0
    right = len(data) - 1
    k=0
    while left < right:
        for i in range(left, right):
            if (data[i].real ** 2 + data[i].imag ** 2) ** 0.5 > (data[i + 1].real ** 2 + data[i + 1].imag ** 2) ** 0.5:
                data[i], data[i + 1] = data[i + 1], data[i]
                k = i
        right = k

        for i in range(right, left, -1):
            if (data[i].real ** 2 + data[i].imag ** 2) ** 0.5 < (data[i - 1].real ** 2 + data[i - 1].imag ** 2) ** 0.5:
                data[i], data[i - 1] = data[i - 1], data[i]
                k = i
        left = k
    return data


# пирамидная, для 4 списка
def heap_sort(words):
    heapq.heapify(words)
    sorted_words = []
    while words:
        sorted_words.append(heapq.heappop(words))
    return sorted_words


print("Отсортированный массив по сортировке вставкой: ", result)
print("Отсортированный массив по быстрой сортировке: ", quicksort(spisok_2))
print("Отсортированный масcив по  сортиворке перемешиванием: ", shaker_sort(comSpisok))
print("Отсортированный масcив по пирамидной сортировке : ", heap_sort(words))