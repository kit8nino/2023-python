from datetime import date

data = ('Олейник Даниил Олегович', 9, 4, 2005)

day = data[1]

month = data[2]

year = data[3]

subjects = {
    "Математика": 4,
    "Русский язык": 3,
    "Литература": 5,
    "Иностранный язык": 5,
    "Физика": 2,
    "Химия": 4,
    "Биология": 3,
    "История": 4,
    "Обществознание": 3,
    "География": 4,
    "Информатика": 2,
    "Технология": 3,
    "Физическая культура": 5,
    "ОБЖ": 4
}

relatives = ['Маша', 'Евгений', 'Людмила', 'Анатолий', 'Надежда', 'Дмитрий', 'Егор']

kiva = 'Milo'

#1

print('1. Средняя оценка в аттестате:', round(sum(subjects.values())/len(subjects), 1))

#2

relatives2 = set(relatives + [data[0]])

result2 = ', '.join(str(element) for element in relatives2)

print('2. Имена родственников без повторений: ', result2)

#3

dict_length = 0

for key in subjects.keys():
    if isinstance(key, str):
        dict_length += len(key)

print("3. Общая длина всех названий предметов:", dict_length)

#4

unique = set()

for key in subjects.keys():
    if isinstance(key, str):
        unique.update(set(key.lower()))

unique_str = ''.join(unique)

print("4. Уникальные буквы в названиях предметов:", unique_str)

#5

kiva_str = ''.join(bin(ord(char))[2:].zfill(8) for char in kiva)

print("5. Имя домешней пушистой кивы в бинарном виде:", kiva_str)

#6

relatives.sort(reverse=True)

print("6. Родственники в обратном алфавитном порядке", relatives)

#7

birthday = date(year, month, day)

current_date = date.today()

date_dif = (current_date - birthday).days

print("7. Количество дней от моей даты рождения до текущей даты: ", date_dif)

#8

print("8. Вводите индекс предмета. Чтобы вывести всё, введите 99) :")
subjects_list = list(subjects)
index = 0
queue = []
index_list = []
while (index != 99 and index <= len(subjects)):
    index = int(input())
    if index != 99:
        index_list.append(index)
for i in index_list:
    queue.append(subjects_list[i])
print(queue)

#9

copied_list = relatives[:]
number = (day + month**2 + year) % 21 + 1
print('9. Номер ацтекского правителя: ' + str(number))
ruler = 'Tlacotzin'
n = int(input('введите индекс родственника для замены: '))
copied_list[n] = ruler

print(copied_list)

#10

linked_list = {}
for i in range(len(relatives)):
    linked_list[relatives[i]] = relatives[(i+1)%len(relatives)]
print(linked_list)

#11

#Номер варианта

summa = 0
for i in range(len(relatives)):
    summa = summa + len(relatives[i])
number = len("Олейник Даниил Олегович") * summa % 4
print("Мой вариант:", number)

#Создание послеодвательности

numba = 10
devider = []
alikvot = [10]
while numba >= 1:
    for i in range(1, numba):
        if numba == 1:
            alikvot.append(0)
        elif numba % i == 0:
            devider.append(i)
    asum = sum(devider)
    alikvot.append(asum)
    numba = asum
    devider = []
print("11.Аликвотная последовательность:", alikvot)