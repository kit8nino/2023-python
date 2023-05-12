"""
import random

print(random.sample(range(1, 18), 4))

#[2, 10, 1, 4]
1. Сортировка перемешиванием
2. Сортировка пузырьком
4. Сортировка вставкой
10. Быстрая сортировка
"""
import random
import cmath
import re


list1 = [x for x in range(1000000)]

list2 = [random.uniform(-1, 1) for x in range(1000000)]


r = int(28 / 5)
comNumL = []
while True:
    comNum = complex(random.randint(-r, r) / random.random(), random.randint(-r, r) / random.random())
    if len(comNumL) == 42000:
        break
    if comNum.real ** 2 + comNum.imag ** 2 <= r ** 2:
        comNumL.append(comNum)


text = []
with open("text.txt", encoding="utf-8", mode="r") as data:
    for line in data:
        line = re.sub(r'[^ А-я]', '', line)
        for i in line.split():
            text.append(i)



def Sortic(data):
    for i in range(len(data) - 1):
        stop = 0
        for j in range(len(data) - 1 - i):
            if (data[j] > data[j + 1]):
                data[j], data[j + 1] = data[j + 1], data[j]
                stop = 1
                print("Replace")
            print("Skip", i)
        if stop == 0:
            break
    return data



def Sorts(data):
    if len(data) <= 1:
        return data
    else:
        supPoint = random.choice(data)
        smNums = [x for x in data if x < supPoint]
        medNums = [x for x in data if x == supPoint]
        bigNums = [x for x in data if x > supPoint]
        return Sorts(smNums) + medNums + Sorts(bigNums)



def Sort_1(data):
    left = 0
    right = len(data) - 1
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


def Sort_2(data):
    for i in range(len(data)):
        j = i - 1
        buff = data[i]
        while data[j] > buff and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = buff
    return data



print(
    "Рандомайзер выдал мне такой список значений [2, 10, 1, 4]:\n2. Сортировка пузырьком(Bubble sort);\n10. Быстрая сортировка(Quicksort);\n1. Сортировка перемешиванием(Shaker sort);\n4. Сортировка вставкой(Insertion sort).")
while True:
    wrLn = input("Введи номер списка для проверки (для завершения введи 'ex'):")
    if wrLn == "1":
        print(Sortic(list1))
    elif wrLn == "2":
        print(Sorts(list2))
    elif wrLn == "3":
        print(Sort_1(comNumL))
    elif wrLn == "4":
        print(Sort_2(text))
    elif wrLn == "ex":
        break
    else:
        print("Введено неправильное значение!")