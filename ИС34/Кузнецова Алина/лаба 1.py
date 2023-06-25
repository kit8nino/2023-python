
# Исходные данные
name = "Кузнецова Алина Александровна"
birthday = (25, 3, 2004)
attestat = {"Математика": 5, "Русский язык": 4, "Английский язык": 4, "Физика": 4, "Химия": 4, "Биология": 5, "История": 5, "Обществознание": 5, "География": 4, "Информатика": 5, "Физическая культура": 5, "Общественное здоровье и безопасность жизнедеятельности": 5, "Экология": 5, "Экономика": 4, "Право": 4, "Астрономия": 5}
relatives = ["Юлия", "Александр", "Валентина", "Владимир", "Валентин", "Галина", "Лариса", "Вероника", "Наталия", "Людмила", "Раиса"]
pet_name = "Бусинка"

# 1. Средняя оценка в аттестате
average_mark = sum(attestat.values()) / len(attestat)
print("Средняя оценка в аттестате:", average_mark)

# 2. Различные имена родственников
unique_relatives = list(set(relatives + [name.split()[0]]))
print("Различные имена родственников:", unique_relatives)

# 3. Общая длина названий предметов
subject_lengths = [len(subject) for subject in attestat.keys()]
total_subject_length = sum(subject_lengths)
print("Общая длина названий предметов:", total_subject_length)

# 4. Уникальные буквы в названиях предметов
unique_letters = set("".join(attestat.keys()))
print("Уникальные буквы в названиях предметов:", unique_letters)

# 5. Имя домашнего питомца в бинарном виде
binary_pet_name = "".join([format(ord(letter), "08b") for letter in pet_name])
print("Имя домашнего питомца в бинарном виде:", binary_pet_name)

# 6. Отсортированный по алфавиту (в обратном порядке) список родственников
sorted_relatives = sorted(relatives, reverse=True)
print("Отсортированный список родственников:", sorted_relatives)

# 7. Количество дней от даты рождения до текущей даты
from datetime import date
today = date.today()
days_since_birthday = (today - date(birthday[2], birthday[1], birthday[0])).days
print("Количество дней от даты рождения до текущей даты:", days_since_birthday)

# 8. FIFO очередь предметов
queue = []
while True:
    index = input("Введите индекс предмета (или 'стоп' для завершения): ")
    if index == "стоп":
        break
    subject = list(attestat.keys())[int(index)]
    queue.append(subject)
print("Очередь предметов:", queue)

# 9. Изменение имени в списке родственников
number = (birthday[0] + birthday[1]**2 + birthday[2]) % 21 + 1
new_name = "Moctezuma II"
sorted_relatives[number] = new_name
print("Измененный список родственников:", sorted_relatives)

# 10. Связный список родственников
sorted_relatives = sorted(relatives, reverse=True)
birth_years = [1980, 1975, 1955, 1960, 1965, 1945, 1950, 1990, 1985, 1970, 1968]
relative_dict = {}
for i in range(len(sorted_relatives)-1):
    relative_dict[sorted_relatives[i]] = sorted_relatives.index(sorted_relatives[i+1])
relative_dict[sorted_relatives[-1]] = None
print("Связный список родственников:", relative_dict)

# 11. Функция-генератор
family_names = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", "Новиков", "Морозов", "Волков", "Лебедев", "Козлов"]
number = len(name) * len(family_names) % 4

def aliquot_sequence(start, step):
    current = start
    while True:
        yield current
        current += step
        if current <= 0:
            break

def sylvester_sequence():
    yield 2
    start = 2
    for i in range(2, number+1):
        sequence = list(aliquot_sequence(start, i))
        start = sequence[-1] + 1
        for num in sequence:
            yield num

def tribonacci_sequence():
    a, b, c = 0, 0, 1
    yield a
    yield b
    yield c
    for i in range(3, number):
        d = a + b + c
        yield d
        a, b, c = b, c, d

def leonardo_sequence():
    a, b = 1, 1
    yield a
    yield b
    for i in range(2, number):
        c = a + b + 1
        yield c
        a, b = b, c

if number == 0:
    sequence = aliquot_sequence(1, 1)
elif number == 1:
    sequence = sylvester_sequence()
elif number == 2:
    sequence = tribonacci_sequence()
else:
    sequence = leonardo_sequence()

print("Последовательность:", list(sequence))