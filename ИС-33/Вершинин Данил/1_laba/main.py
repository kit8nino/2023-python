#Исходные данные
my_prs = ("Вершинин", "Данил", "Александрович", 1, 10, 2004)
attestat = {"Математика": 5,
            "Русский язык": 4,
            "Физика": 4,
            "История": 5,
            "Химия": 4,
            "Английский язык": 5,
            "Биология": 4,
            "География": 4,
            "Обществознание": 5,
            "Литература": 4,
            "Информатика": 5,
            "Физкультура": 5,
            "МХК": 4,
            "ДВСР": 5,
            "ОБЖ": 5,
            "Индивидуальный проект": 5,
            "Астрономия": 4}
fam_name = ["Светлана", "Александр", "Лидия", "Олег", "Александр", "Любовь", "Юля", "Борис", "Александр", "Евгения"]
pet_name = "Ося"

print(my_prs)
print(attestat)
print(fam_name)
print(pet_name)

#Задание 1
avg_grade = sum(attestat.values()) / len(attestat)
print("1) Средняя оценка в аттестате:", avg_grade)

#Задание 2
my_name = "Данил"
fam_name.append(my_name)
unique_names = set(fam_name)
print("2) Все различные имена:", unique_names)

#Задание 3
total_length = sum([len(subject) for subject in attestat])
print("3) Общая длина всех названий предметов:", total_length)

#Задание 4
empt = ""
for i in attestat:
    empt += i
    unique_letters = set(empt)
print("4) Уникальные буквы в названиях предметов:", unique_letters)

#Задание 5
binar_petname = ""
for i in pet_name:
    binar_petname += bin(ord(i))[2:] + " "
print("5) Имя питомца в бинарном виде:", pet_name, "-", binar_petname)

#Задание 6
print("6) Отсортированный список:", sorted(fam_name, reverse=True))

#Задание 7
from datetime import datetime
today = datetime.today()
my_dr = datetime(2004, 1, 10)
num_days = (today - my_dr).days
print("7) Количество дней от моего др до сегодняшней даты", num_days)

#Задание 8
print("Введите ниже элементы списка('Stop' для остановки):")
FIFO = []
while(True):
    x = input()
    if x == "Stop":
        break
    FIFO.append(x)
print("8) FIFO очередь:", FIFO)

#Задание 9
pravitel = (1+10**2 + 2004) % 21 + 1
print("Введите индекс для замены:")
x = int(input())
print("Правитель под номером", pravitel, "-", "Ицкоуатль")
fam_name[x] = "Ицкоуатль"
print("9) Новый список по введенному индексу:", fam_name)

#Задание 10
slovarb = {}
for i in range(len(fam_name)):
    slovarb[fam_name[i]] = fam_name[(i+1) % len(fam_name)]
print("10) Связаный список:", slovarb)

#Задание 11
len_fam = 0
for i in range(len(fam_name)):
    len_fam = len_fam + len(fam_name[i])
number = len("ВершининДанилАлексадрович") * len_fam % 4
print("11) Вариант -", number)

def aliquot_sequence(z):
    yield z
    while True:
        deliteli = [i for i in range(1, z) if z % i == 0]
        numb = sum(deliteli)
        if numb == z:
            break
        yield numb
        z = numb

print("Введите число для последовательности: ")
num2 = int(input())
for i in aliquot_sequence(num2):
    print(i)