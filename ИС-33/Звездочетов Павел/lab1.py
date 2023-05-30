# Данные:
self_data = (
    "Звездочетов",
    "Павел",
    "Алексеевич",
    28,
    10,
    2002,
)

last_name = 0
first_name = 1
patronymic = 2
day = 3
month = 4
year = 5

subjects = {
    "Алгебра": 5,
    "Геометрия": 4,
    "Русский": 2,
    "Английский": 5,
    "Немецкий": 3,
    "География": 4,
    "Обществознание": 4,
    "Информатика": 4,
    "Физра": 5,
    "МХК": 5,
    "Литература": 3,
    "Химия": 2,
    "Биология": 2,
    "Технология": 5,
}

relatives = [
    "Алексей", "Нина", "Виктория", "Роман",
    "Артём", "Татьяна", "Илона", 'Игорь',
    'Григорий', 'Данил', 'Дарья', 'Артём',
    'Елена', 'Игорь', 'Иван', 'Павел',
]

name_of_kiwi = "Пушок"

# ----------------------------------------------------------------------------------------------------------------------

# 1.
print("Средня оценка в аттестате:",
      sum(subjects.values()) / len(subjects))

# 2.
print("\nРазличные имена родственников (включая мое):",
      *sorted(set(relatives + [self_data[first_name]])))

# 3.
print("\nОбщая длина всех названий предметов:",
      sum([len(subject) for subject in subjects.keys()]))


# 4.
def sum_str(mas):
    res = ""

    for el in mas:
        res += el

    return res


print("\nУникальные буквы в названиях предметов:",
      *sorted(set(list(sum_str([subject.lower() for subject in subjects.keys()])))))

# 5.
print("\nИмя домашней пушистой киви в бинарном виде:",
      name_of_kiwi.encode('utf-8'))

# 6.
print("\nОтсортированный по алфавиту (в обратном порядке) список родственников:",
      *sorted(relatives, reverse=True))

# 7.
from datetime import date
from collections import deque

print("\nКол-во дней от моей даты рождения до текущей:",
      (date.today() - date(self_data[year], self_data[month], self_data[day])).days)

# 8.
queue = deque()
subjects_list = list(subjects.keys())

print()
for i in range(len(subjects_list)):
    print(i + 1, ". ", subjects_list[i], sep="")
print("0. Завершить ввод")
print("Введите индекс предмета или 0 для завершения: ")

while True:
    index = int(input(">>> "))

    if index == 0:
        break
    else:
        queue.appendleft(subjects_list[index - 1])

print("Все элементы очереди:")
while len(queue) > 0:
    print(queue.pop())

# 9.
sort_relatives = sorted(relatives)
names_Aztec_leaders = ["Tenoch", "Acamapichtli", "Huitzilihuitl",
                       "Chimalpopoca", "Xihuitl Temoc", "Itzcoatl",
                       "Moctezuma I", "Atotoztli", "Axayacatl",
                       "Tizoc", "Ahuitzotl", "Moctezuma II",
                       "Cuitláhuac", "Cuauhtémoc", "Tlacotzin",
                       "Motelchiuhtzin", "Xochiquentzin", "Huanitzin",
                       "Tehuetzquititzin", "Cecetzin", "Cipac"]

print()
for i in range(len(sort_relatives)):
    print(i + 1, ". ", sort_relatives[i], sep="")
print("Введите индекс для замены: ")

index = int(input(">>> "))
sort_relatives[index - 1] = names_Aztec_leaders[(self_data[day] + self_data[month] ** 2 + self_data[year]) % 21 + 1]

print("Измененный список имен:", *sort_relatives)

# 10.
sort_relatives = sorted(relatives, reverse=True)

relatives_linked_list = {sort_relatives[i]: i + 1 for i in range(len(sort_relatives) - 1)}
relatives_linked_list[sort_relatives[-1]] = None

print("Связанный список в виде словаря:", relatives_linked_list)


# 11. (Вариант 0)
def aliquot_sequence(n):
    current = n

    while True:
        divisors = []

        for i in range(1, int(current ** 0.5) + 1):
            if current % i == 0:
                divisors.append(i)
                if i != 1 and i != current // i:
                    divisors.append(current // i)

        if len(divisors) == 0:
            break

        sequence_sum = sum(divisors)

        yield sequence_sum

        if sequence_sum >= n:
            break
        elif sequence_sum == 1:
            yield 0
            break

        current = sequence_sum


number = int(input("\nВведите число: "))
print(f"Аликвотная последовательность числа {number}: ", end="")
for i in aliquot_sequence(number):
    print(i, end=" ")
