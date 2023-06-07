from datetime import date
from collections import deque


def sum_str_list(mas):
    res = ""

    for string in mas:
        res += string

    return res


my_data = ("Боницкий", "Егор", "Дмитриевич", 21, 9, 2004)

subjects = {"Русский": 4, "алгебра": 4, "геометрия": 4,
            "физра": 5, "физика": 4, "информатика": 4,
            "астрономия": 5, "химия": 4, "история": 4,
            "обществознание": 4, "география": 4, "биология": 4,
            "обж": 5, "право": 4, "литра": 4}

family_names = ["Василий", "Татьяна", "Ярослав", "Карина",
                "Артём", "Нина", "Августина", 'Игорь',
                'Григорий', 'Данил', 'Егор', 'Артём',
                'Елена', 'Инна', 'Ростислав']

name_of_kiwi = "Комамура"

# 1
s = sum(subjects.values())
k = len(subjects)

print("Средня оценка в аттестате:", s / k)

# 2
my_name = my_data[1]
names = family_names + [my_name]
names_set = set(names)
sorted_names = sorted(names_set)

print("Различные имена родственников включая мое:", sorted_names)

# 3
length_list = [len(subject) for subject in subjects.keys()]
res = sum(length_list)

print("Общая длина всех названий предметов:", res)

# 4
all_letters_list = [subject.lower() for subject in subjects.keys()]
sum_letters = sum_str_list(all_letters_list)
set_letters = set(list(sum_letters))
sorted_letters = sorted(set_letters)

print("Уникальные буквы в названиях предметов:", sorted_letters)

# 5
res = name_of_kiwi.encode('utf-8')

print("Имя домашней пушистой киви в бинарном виде:", res)

# 6
sorted_reverse_key = True
sorted_names = sorted(family_names, reverse=sorted_reverse_key)

print("Отсортированный по алфавиту в обратном порядке список родственников:", sorted_names)

# 7
y = my_data[5]
m = my_data[4]
d = my_data[3]
my_date = date(y, m, d)
todaye_date = date.today()
res = (todaye_date - my_date).days

print("Кол-во дней от моей даты рождения до текущей:", res)

# 8
queue = deque()
subjects_list = list(subjects.keys())

for i in range(len(subjects_list)):
    print(i + 1, ". ", subjects_list[i], sep="")

print("0. Завершить ввод")
print("Введите индекс предмета или 0 для завершения: ")

index = -1

while index != 0:
    index = int(input("Выш выбор: "))
    if index != 0:
        queue.appendleft(subjects_list[index - 1])

print("Все элементы очереди:")
while len(queue) > 0:
    print(queue.pop())

# 9
y = my_data[5]
m = my_data[4]
d = my_data[3]

sorted_family_names = sorted(family_names)
names_Aztec_leaders = ["Tenoch", "Acamapichtli", "Huitzilihuitl", "Chimalpopoca", "Xihuitl Temoc", "Itzcoatl",
                       "Moctezuma I", "Atotoztli", "Axayacatl", "Tizoc", "Ahuitzotl", "Moctezuma II",
                       "Cuitláhuac", "Cuauhtémoc", "Tlacotzin", "Motelchiuhtzin", "Xochiquentzin", "Huanitzin",
                       "Tehuetzquititzin", "Cecetzin", "Cipac"]

for i in range(len(sorted_family_names)):
    print(i + 1, ". ", sorted_family_names[i], sep="")

index = int(input("Введите индекс для замены: "))
sorted_family_names[index - 1] = names_Aztec_leaders[(d + m ** 2 + y) % 21 + 1]

print("Измененный список имен:", sorted_family_names)

# 10
sorted_reverse_key = True
sorted_family_names = sorted(family_names, reverse=sorted_reverse_key)

family_names_linked_list = dict()

for i in range(len(sorted_family_names) - 1):
    family_names_linked_list[sorted_family_names[i]] = i + 1

family_names_linked_list[sorted_family_names[-1]] = None

print("Связанный список в виде словаря:", family_names_linked_list)


# 11 --- Вариант 2
def tribonacci():
    a, b, c = 0, 0, 1
    while True:
        yield a
        a, b, c = b, c, a + b + c


trib = tribonacci()
for i in range(10):
    print(next(trib))

