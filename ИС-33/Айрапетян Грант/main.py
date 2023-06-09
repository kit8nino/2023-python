#Исходные данные:

my_tuple = ("Грант Айрапетян Сергеевич", 23, 9, 2004)

my_dictionary = {"Русский язык": 4,
                 "Литература": 4,
                 "Родной язык": 4,
                 "Иностранный язык": 5,
                 "Математика": 4,
                 "Информатика": 5,
                 "История": 4,
                 "Обществознание": 4,
                 "География": 5,
                 "Биология": 4,
                 "Физика": 4,
                 "Астрономия": 5,
                 "Химия": 5,
                 "Физическая культура": 5,
                 "ОБЖ": 5,
                 "Финансовая грамотность": 4,
                 "Индивидуальный проект": 5}

my_list = ["Самсон", "Диана", "Давид", "Наира", "Сергей", "Марк", "Софи", "Джулия", "Арам", "Ксения", "Овик", "Лия",
           "Белла", "Наира", "Марк"]

my_line = "Милана"

print("Кортеж:", my_tuple)
print("Словарь:", my_dictionary)
print("Список:", my_list)
print("Строка:", my_line)

#Действия:
print("Действия:")

#Задание1
s = 0
k = 0
for i in my_dictionary:
    s = s + my_dictionary[i]
    k += 1
print("1.Средняя оценка в аттестате:", s/k)

#Задание2
def get_unique_words(my_list):
    list_of_unique_words = [] #пустой список, который будет включать все уникальные имена
    list_of_unique_words.append("Grant")
    unique_words = set(my_list) #используется set для получения уникальных имен из списка
    for word in unique_words:
        list_of_unique_words.append(word)
    return list_of_unique_words
print("2.Уникальные имена среди родственников:", get_unique_words(my_list))

#Задание3
total_length = 0
for key in my_dictionary:
    total_length += len(key)
print("3.Общая длина всех названий предметов:", total_length)

#Задание4
unique_letters = ""
for letter in my_dictionary:
    unique_letters += letter
    unique_letters_new = set(unique_letters)
print("4.Уникальные буквы в названиях предметов:", unique_letters_new)

#Задание5
word = my_line
binary_word = ""
for letter in word:
    binary_word += bin(ord(letter))[2:] + " "
print("5.Имя домашней пушистой кивы в бинарном виде:", word, ":", binary_word)

#Задание6
print("6.Отсортированный список:", sorted(my_list, reverse=True))

#Задание7
import datetime
now = datetime.datetime.today()
DR = datetime.datetime(2004, 9, 23)
d = now - DR
print('7.Я прожил: {} дней.'.format(d.days))

#Задание8
print("Введите ниже элементы списка:")
FIFO = []
while(True):
    sos = input()
    if sos == "stop":
        break
    FIFO.append(sos)
print("8.Задание с FIF0:", FIFO)

#Задание9(1)
print("Введите индекс для замены:")
pop = int(input())
my_list[pop] = "Ахаякатль"
print("9.Новый список по введенному индексу:", my_list)

#Задание9(2)
n = (my_tuple[1] + my_tuple[2]**2 + my_tuple[3]) % 21 + 1 #номер правителя
print("Номер ацтекского правителя:", n, "- Ахаякатль")

#Задание10
my_new_list = {}
for i in range(len(my_list)):
    my_new_list[my_list[i]] = my_list[(i+1) % len(my_list)]
print("10.Создание списка:", my_new_list)

#Задание11
#Номер варианта
summa = 0
for i in range(len(my_list)):
    summa = summa + len(my_list[i])
number = len("АйрапетянГрантСергеевич") * summa % 4
print("Мой вариант:", number)

#Аликвотная последовательность
numb = 10
delitel = []
alikvot_pos = [10]
while numb >= 1:
    for i in range(1, numb):
        if numb == 1:
            alikvot_pos.append(0)
        elif numb % i == 0:
            delitel.append(i)
    summa3 = sum(delitel)
    alikvot_pos.append(summa3)
    numb = summa3
    delitel = []
print("11.Создание аликвотная последовательности:", alikvot_pos)



