from datetime import datetime
from collections import deque

# Исходные данные
nameMe = ('Хонина', 'Екатерина', 'Владимировна', 28, 11, 2003)
school_certificate = {"Математика": 5, "Русский язык": 4, "Английский язык": 5, "История": 4, "География": 3, "Физика": 5, "Химия": 4, "Биология": 4, "Обществознание": 3, "Информатика": 5, "Физическая культура": 5, "ИЗО": 4, "Технология": 3, "Музыка": 4}
nameRel = ['Владимир', 'Наталья', 'София', 'Елена', 'Любовь', 'Людмила', 'Зинаида']
nameKiva = 'Йети'

day, month, year = nameMe[3], nameMe[4], nameMe[5]
number = (day + month**2 + year) % 21 + 1  # ищем номер по формуле
print("Номер:", number, "\n")

numberr = len(nameMe[0] + nameMe[1] + nameMe[2]) * len(nameRel) % 4
print("Номер 2:", numberr, "\n")

def AverMark(school_certificate):
    sum_marks = sum(school_certificate.values())  # суммируем значения оценок аттестата
    average_mark = sum_marks / len(school_certificate)  # делим сумму на количество
    return average_mark
average_mark = AverMark(school_certificate)
print("1. Вывод средней оценки в аттестате:", AverMark(school_certificate) , "\n")

all_names = nameMe[1] + ' '.join(nameRel)  # объединяем все имена в один список

def AllNames(all_names):
    unique_names = set(all_names)  # преобразуем список в множество для получения уникальных значений
    final_names = list(unique_names)  # преобразуем множество обратно в список
    return final_names

final_names = AllNames(all_names)
print("2. Вывод, исключив повторения, всех различных имен среди своих родственников (включая свое):", final_names, "\n")  # выводим список уникальных имен на экран

def LenKeys(school_certificates):
    keys_names = ""
    for names in school_certificates.keys():
        keys_names += names
    return len(keys_names.replace(" ", ""))

print("3. Общая длина всех названий предметов:", LenKeys(school_certificate), "\n")

def UniqLet(school_certificates):
    unique_letters = set(''.join(school_certificates.keys()))
    return unique_letters

unique_letters = UniqLet(school_certificate)
print("4. Уникальные буквы в названиях предметов:", unique_letters, "\n")

binary_name = ''.join(format(ord(i), '08b') for i in nameKiva)
print("5. Имя домашней пушистой кивы в бинарном виде:", binary_name, "\n")  # выводит строку в бинарном виде

sorted_reverse_rel = sorted(nameRel, reverse=True)
print("6. Вывод списка родственников отсортированный по алфавиту (в обратном порядке)", sorted_reverse_rel, "\n") # выводит список родственников отсортированный по алфавиту (в обратном порядке)

birthday = datetime(nameMe[5], nameMe[4], nameMe[3])  # дата рождения из кортежа
today = datetime.now()  # текущая дата и время

delta = today - birthday  # разница между текущей датой и днем рождения
days_since_birthday = delta.days  # извлекаем количество дней из объекта timedelta

print("7. Количество дней от даты рождения до текущей даты", days_since_birthday, "\n")  # выводит количество дней от дня рождения до текущей даты

queue = deque() # создаем пустую очередь

# заполняем очередь, пока пользователь не введет команду "stop"
while True:
    index = input("Введите индекс для добавления элемента в очередь (или stop для остановки ввода): ")
    if index == "stop":
        break
    queue.append(school_certificate[list(school_certificate.keys())[int(index)]])  # добавляем значение в очередь по индексу

# выводим элементы очереди
for element in queue:
    print("8. FIFO очередь, в которую можно добавлять предметы по вводимому с клавиатуры индексу (до команды остановки)", element, "\n")

def NameNew(nameMe, nameRel):
    rules = ["Tenoch", "Acamapichtli", "Huitzilihuitl", "Chimalpopoca", "Xihuitl Temoc", "Itzcoatl", "Moctezuma I",
             "Atotoztli", "Axayacatl", "Tizoc", "Ahuitzotl", "Moctezuma II", "Cuitláhuac", "Cuauhtémoc", "Tlacotzin",
             "Motelchiuhtzin", "Xochiquentzin", "Huanitzin", "Tehuetzquititzin"]
    SortRevReL = sorted_reverse_rel
    while 1:
        key = input(
            f"Введите индекс имени от 0 до {len(SortRevReL) - 1} для изменения его на имя ацтекского правителя {rules[number - 1]}:")
        try:
            if int(key) >= 0 and int(key) < len(rules):
                SortRevReL[int(key)] = rules[number - 1]
                return SortRevReL
            else:
                print("Введён не верный ключ!\n")
        except Exception:
            print("Введён не верный ключ!\n")

print("9. По введеному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя под номером, получаемым из вашей даты рождения", NameNew(nameMe, nameRel), "\n")

birthYear = [1983, 1984, 2010, 1958, 1976, 1965, 1950]

SortRevReL = sorted_reverse_rel
nameRel_dict = {}

for i in range(len(SortRevReL)):
    if i == len(SortRevReL):
        nameRel_dict[SortRevReL[i]] = None
    else:
        next_index = SortRevReL.index(SortRevReL[i])
        nameRel_dict[SortRevReL[i]] = SortRevReL.index(SortRevReL[next_index])

print("10. Cвязный список, как словарь, где ключ - имя родственника, а значение - индекс следующего имени по исходному списку", nameRel_dict, "\n")

print("11. Создать функцию-генератор", numberr, ", то есть аликвотной последовательности \n")

def aliquot_sequence(n):
    for i in range(1, n):
        if n % i == 0:
            yield i

n = int(input("Введите натуральное число: "))
print("Аликвотная последовательность для числа", n)
for aliquot in aliquot_sequence(n):
    print(aliquot, end=" ")