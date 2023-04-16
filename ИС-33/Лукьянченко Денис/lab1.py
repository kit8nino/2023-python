import datetime
import os

# Мои данные:
My_data = ('Лукьянченко', 'Денис', 'Дмитриевич', 15, 3, 2004)
Subjects_in_certificate = {'Астрономия': 5, 'Биология': 4, 'География': 4, 'Иностранный язык': 4, 'Информатика': 5,
                           'История': 5, 'Обществознание': 4, 'Химия': 4, 'ОБЖ': 5, 'Литература': 5,
                           'Математика': 4, 'Физическая культура': 5, 'Экология': 5, 'Русский язык': 4}

names_of_my_relatives = ['Марина', 'Дмитрий', 'Юлия', 'Александр', 'Любовь', 'Надежда', 'Шура', 'Алеся', 'Сергей', 'Маша']
Kiva_Name = 'Булочка'


# Задание № 1
def first_task(certificate_grades):
    sum_of_grades = 0
    for value in certificate_grades.values():
        sum_of_grades = sum_of_grades + value
    return sum_of_grades / len(certificate_grades)
print("1. Моя средняя оценка в аттестате:", first_task(Subjects_in_certificate), "\n")


# Задание № 2
def second_task(person, relative):
    unique_names = []
    unique_names.append(person[1])
    for i in range(len(relative)):
        unique_names.append(relative[i])
    return list(set(unique_names))
print("2. Уникальные имена родственников (включая моё имя):", second_task(My_data, names_of_my_relatives), "\n")


# Задание № 3
def third_task(certificate_names):
    name_subject = ""
    for names in certificate_names.keys():
        name_subject += names
    return len(name_subject.replace(" ", ""))
print("3. Общая длина всех названий предметов из аттеста:", third_task(Subjects_in_certificate), "\n")


# Задание № 4
def fourth_task(certificate_names):
    unique_letters = []
    for names in certificate_names.keys():
        subject_letter = ""
        subject_name = ""
        list_ = []
        subject_name = names.lower()
        for i in range(len(names)):
            if subject_name[i] == " ":
                continue
            else:
                list_.append(subject_name[i])
        subject_letter = ", ".join(set(list_))
        unique_letters.append(subject_letter)
    return unique_letters
print("4. Уникальные буквы в названиях предметов:", fourth_task(Subjects_in_certificate), "\n")


# Задание № 5
def fifth_task(Kiva_Name):
    return ' '.join(format(ord(c), 'b') for c in Kiva_Name)
print("5. Имя моей домашней пушистой кивы в бинарном виде:", fifth_task(Kiva_Name), "\n")


# Задание № 6
def sixth_task(names_of_my_relatives):
    names_of_my_relatives.sort(reverse=True)
    return names_of_my_relatives
print("6. Отсортированный список родственниов по алфавиту в обратном порядке:", sixth_task(names_of_my_relatives), "\n")


# Задание № 7
def seventh_task(My_data):
    my_birthday_date = datetime.datetime(My_data[5], My_data[4], My_data[3])
    current_date = datetime.datetime.now()
    return (current_date - my_birthday_date).days
print("7. От дня моего рождения до текущей даты:", seventh_task(My_data), "дней", "\n")


# Задание № 8
def eighth_task(Subjects_in_certificate):
    subjects = [x for x in Subjects_in_certificate.keys()]
    list_of_subject = []
    while 1:
        key = input(f"8. Введите индекс предмета от 0 до {len(subjects) - 1} для добавления в очередь (чтобы выйти, введите 'exit'):")
        if key == "exit":
            return list_of_subject
        elif int(key) >= 0 and int(key) < len(subjects):
            list_of_subject.append(subjects[int(key)])
            print(f"Добавлен элемент с индексом [{key}]: {subjects[int(key)]}\n")
        else:
            print("Введён не верный ключ!\n")
print("Ваш список предметов:", eighth_task(Subjects_in_certificate), "\n")


# Задание № 9
def ninth(My_data, names_of_my_relatives):
    number = (My_data[3] + My_data[4] ** 2 + My_data[5]) % 21 + 1
    names_of_Aztec_rulers = ["Tenoch", "Acamapichtli", "Huitzilihuitl", "Chimalpopoca", "Xihuitl Temoc", "Itzcoatl", "Moctezuma I",
             "Atotoztli", "Axayacatl", "Tizoc", "Ahuitzotl", "Moctezuma II", "Cuitláhuac", "Cuauhtémoc", "Tlacotzin",
             "Motelchiuhtzin", "Xochiquentzin", "Huanitzin", "Tehuetzquititzin", "Cecetzin", "Cipac"]
    sort_list_of_relatives = sixth_task(names_of_my_relatives)
    while 1:
        key = input(f"9. Введите индекс имени от 0 до {len(sort_list_of_relatives) - 1},для изменения его на имя ацтекского правителя {names_of_Aztec_rulers[number - 1]}:")
        if int(key) >= 0 and int(key) < len(names_of_Aztec_rulers):
            sort_list_of_relatives[int(key)] = names_of_Aztec_rulers[number - 1]
            return sort_list_of_relatives
        else:
            print("Введён не верный ключ!\n")
print("Новый список:", ninth(My_data, names_of_my_relatives), "\n")


# Задание № 10
def tenth_task():
    linked_list = { 'Марина':1, 'Дмитрий':0, 'Юлия':4, 'Александр':7, 'Любовь':2, 'Надежда':8, 'Шура':3, 'Алеся':9, 'Сергей':6,
                         'Маша':5}
    return linked_list
print("10. Связный циклический список:", tenth_task(), "\n")


# Задание № 11
number = len(My_data[0] + My_data[1] + My_data[2]) * len("".join(names_of_my_relatives)) % 4
print("11. По формуле было получено число -", number, ", что соответствует Аликвотной последовательности.\n")
def eleventh_task(x, x1):
    new_x = 0
    if x == x1 and x >= 0:
        print(x)
    if x == 1:
        print(0)
        return 0
    if x == 6:
        print('6 - совершенное число!')
        return 0
    if x == 220:
        print('220 имеет повторяющуюся аликвотную последовательность с периодом 2.')
        return 0
    elif x <= 0:
        print('Аликвотная последовательность начинающаяся с некоторого положительного целого числа')
    else:
        for i in range(1, x // 2 + 1):
            if x % i == 0:
                new_x += i
        print(new_x)
        return eleventh_task(new_x, x1)
number_aliquot_sequence = int(input('Введите неотрицательное число: '))
eleventh_task(number_aliquot_sequence, number_aliquot_sequence)
os.system('pause')