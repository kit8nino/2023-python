from datetime import date
import datetime

Data = ("Офицеров", "Егор", "Николаевич", 14, 3, 2004)

Certificate = {
    "Французский язык": 4,
    "Английский язык":  4,
    "Обществознание": 4,
    "Биология": 4,
    "Русский язык": 4,
    "Литература": 3,
    "ИЗО": 5,
    "Технология": 5,
    "Химия": 4,
    "Физика": 4,
    "Алгебра": 4,
    "Геометрия": 5,
    "Информатика": 4,
    "ОБЖ": 5,
    "Физическая культура": 4,
    "География": 5,
    "История ": 4,
    "Музыка": 5,
    }

relatives = ["Николай", "Ольга", "Татьяна", "Ульяна","Николай", "Ксения", "Нина", "Наталья", "Кирилл","Илья","Антон"]

kiwa = "Страшила"

print("Задание 1", sum(Certificate.values())/len(Certificate))

relatives.append(Data[1])
unique = list(set(relatives))
print("Задание 2", unique)
relatives.remove("Егор")

def length_of_items():
    summa = 0
    for i in Certificate:
        summa += len(i)
    return summa
print("Задание 3", length_of_items())

def unique_letters():
    unique = ""
    for i in Certificate:
        unique+=i
    unique_mas = set(unique)
    return unique_mas
print("Задание 4",unique_letters())


result_binary_kiwa = " ".join(format(ord(с), '08b') for с in kiwa)
print("Задание 5", result_binary_kiwa)

relatives.sort()
print("Задание 6", relatives[::-1])

date_of_birth = datetime.datetime(int(Data[5]), int(Data[4]), int(Data[3]),23,36)
current_date = datetime.datetime.now()
answer = current_date - date_of_birth
print("Задание 7", f"Я живу на это земле {answer}")

print("Задание 8 Для остановки введите 123")
items = list(Certificate)
FIFO = []
order = []
while ( id != 123 ):
    id = int(input())
    if id != 123:
        order.append(id)
for i in order:
    FIFO.append(items[i])
print(FIFO)

print("Задание 9")
number = ((int(Data[3]) + int(Data[4])**2 + int(Data[5])) % 21 + 1)
print("Номеру ",number,"соответствует правитель Куитлауак" )
print("Введите номер имени, которых хотите поменять на Куитлауак")
relat=relatives.copy()
while (True):
    number = int(input())
    if (number >= 0 and number < len(relat)):
        relat[int(number)] = "Куитлауак"
    break
print(relat)


dictionary = {}
for i in range(len(relatives)):
        dictionary[relatives[i]] = relatives[(i+1)%len(relatives)]
print("Задание 10",dictionary )

print("Задание №11  ")
number = len("ОфицеровЕгорНиколаевич ") * len(relatives) % 4
print("Вариант №",number,"- последовательность Сильвестера")

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
