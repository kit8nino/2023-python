from datetime import date
import datetime

myna = ("Ульдяков Андрей Романович", 4,10,2004)
attestat = {
    'Алгебра': 4,
    'Физика': 5,
    'Обществознание': 4,
    'Информатика': 5,
    'Музыка': 5,
    'Английский язык': 4,
    'Русский язык': 4,
    'Литература': 5,
    'История': 5,
    'Химия': 4,
    'Геометрия': 4,
    'Физическая культура': 5,
    'География': 5,
    'Биология': 4
}
kiwa_name = "Фарш"
relatives = ['Анна', 'Валя', 'Валя', 'Рома', 'Люда', 'Андрей', 'Лина', 'Саша', 'Таня']
mod_relatives = relatives.copy()
mod_relatives.append('Андрей')

# Определяем средний балл аттестата

print("1. Средний балл аттестата", round(sum(attestat.values()) / len(attestat), 2))

# Уникальные имена

UniqueName =relatives.copy()
UniqueName.append(myna[0].split(" ")[1])
print("2. Уникальные имена", *set(UniqueName))

# общая длина названий
length = 0
Allsubjects = []
for i in attestat.keys():
    length += int(len(i))
    for z in i:
        if z != " ":
            Allsubjects.append(z.lower())
        continue
print("3. Длина всех названий предметов:", length)

# уникальные буквы в названиях предметов
print("4. Уникальные буквы в названиях предметов:", *set(Allsubjects))

# имя пушистой кивы(?) в бинарном коде
print("5. кива:\n\t", ''.join(format(x, '08b') for x in bytearray(kiwa_name, 'utf-8')))

# отсортированный по алфавиту список родственников
relatives_sort = relatives.copy()
relatives_sort.sort(reverse=True)
print("6. Список родственников по алфавиту наоборот:\n\t", *relatives_sort)


date_of_birth = datetime.datetime(int(myna[3]), int(myna[2]), int(myna[1]),23,36)
current_date = datetime.datetime.now()
answer = current_date - date_of_birth
print("Задание 7", f"Я живу на это земле {answer}")

# FIFO очередь, в которую можно добавлять предметы по вводимому с клавиатуры индексу

valor = ["sanich", "tailssich", "knock", "amy", "jet", "shadiw", "big"]
FIFO = []
for valorIND in range(len(valor)):
    print(valor[valorIND], ':', (len(max(valor, key = len)) - len(valor[valorIND])) * " ", valorIND)
print("введите число того, что хотите добавить \n Чтобы прекратить -1")
valorPers = []
InputIND = int
while InputIND !=-1:
    try:
        InputIND = int(input("Введите: "))
        if InputIND == -1:
            break
        if InputIND <= -1:
            raise IndexError
        valorPers.append(valor[InputIND])
    except ValueError:
        print("Что-то не так")
    except IndexError:
        print("Что-то не так")
print("8. FIFO:", *valorPers)

# по введеному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя (Wiki Badge) под номером, получаемым из вашей даты рождения: number = (day + month**2 + year) % 21 + 1;

acst_name = ("Acamapichtli", "Xihuitl Temoc", "Tizoc", "Moctezuma I", "Itzcoatl", "Huitzilihuitl", "Tenoch")
ac_relatives = relatives_sort.copy()
IndRel = 0
InputIndAc = 1
print("Задание 9")
number = ((int(myna[1]) + int(myna[2])**2 + int(myna[3])) % 21 + 1)
print("Номеру ",number,"соответствует правитель Тисосик" )
print("Введите номер имени, которых хотите поменять на Тисосик")
relat=relatives.copy()
while (True):
    number = int(input())
    if (number >= 0 and number < len(relat)):
        relat[int(number)] = "Тисосик"
    break
print(relat)

print(*ac_relatives)

# создать связный список, как словарь, где ключ - имя родственника, а значение - индекс следующего имени по исходному списку, упорядоченному по их (родственников) годам рождения, исходный список при этом должен остаться неизменным

Rel10 = {}
for i in range(len(relatives_sort)):
    Rel10[relatives_sort[i]] = relatives_sort[(i+1) % len(relatives_sort)]

print("10.", Rel10)

# написать функцию-генератор:
# последовательности сильвестра;
# Свой вариант определяется как number = len("ФИО") * len (family_names) % 4;
print("Функция_генератор номер", len(myna[0]) * len(relatives) % 4)
# количество дней от вашей даты рождения до сейчас
def eleventh():
    k = int(input("Введите индекс последовательности:"))

    def syl(n):
        product = 1
        for k in range(n):
            product *= syl(k)
        return product + 1

    for n in range(k + 1):
        yield syl(n)

print([count for count in eleventh()])
