import datetime
def Silvestr_sequence(n):
    a = 1
    ans = 2
    N = 1000000007
    i = 1
    while i <= n:
        print(ans, end=" ")
        ans = ((a % N) * (ans % N)) % N
        a = ans
        ans = (ans + 1) % N
        i = i + 1
aboutme = ("Помазов Степан Павлович", 10,9,2004)
attestat = {
    'Математика' : 5,
    'Русский язык' : 5,
    'Литература' : 5,
    'Физика' : 5,
    'Обществознание' : 5,
    'Информатика' : 5,
    'Родной язык' : 5,
    'История России' : 5,
    'Физическая культура' : 5,
    'История' : 5,
    'Английский язык' : 5,
    'Индивидуальный проект' : 5,
    'Химия' : 5,
    'География' : 5,
    'Биология' : 5
}
kivy_name = "Ласка"
relatives = ['Артём', 'Екатерина', 'Павел', 'Валентина', 'Людмила',
             'Эльвира', 'Александр','Анастасия','Семён','Богдан','Анна', 'Сергей','Наталья','Александр','Татьяна']
mod_relatives = relatives.copy()
mod_relatives.append('Степан')
sr_mark = 0
s = 0
for subject, mark in attestat.items():
    s += mark
sr_mark = s/len(attestat)

count_letters_of_lessons = 0
# отбираю названия предметов
keys = []
for key, value in attestat.items():
    keys.append(key)
for i in range(len(keys)-1):
    length = len(keys[i])
    count_letters_of_lessons+=length
unique_letters_in_keys = []
# Перевожу все буквы предметов в нижний регистр
keys1 = []
for item in keys:
    keys1.append(item.lower())
for i in range(len(keys1)-1):
    for j in keys1[i]:
        if j in unique_letters_in_keys:
            continue
        elif j == ' ':
            continue
        else:
            unique_letters_in_keys.append(j)
unique_relatives_names = set(mod_relatives) #неповторяющиеся имена
kivy_bin_name = ''.join(format(ord(x), '08b') for x in kivy_name)

now = datetime.datetime.now()
my_birth_date = datetime.datetime(2004,9,10)
period = now - my_birth_date

list_of_names_atctecs = ['Tenoch','Acamapichtli','Huitzilihuitl','Chimalpopoca',"Xihuitl Temoc",
                         'Itzcoatl','Moctezuma I','Atotoztli',
                         'Axayacatl','Tizoc','Ahuitzotl','Moctezuma II','Cuitláhuac',
                         'Cuauhtémoc','Tlacotzin','Motelchiuhtzin','Xochiquentzin','Huanitzin','Tehuetzquititzin',
                         'Cecetzin','Cipac']
def zamena(i,A):
    number = (10 + 9 ** 2 + 2004) % 21 + 1
    A[i] = list_of_names_atctecs[number]
    return print("Результат: ", A)

sortrelatives = sorted(relatives, reverse=True)

print("1) Средний балл аттестата: ",sr_mark,sep='')
print("2) Уникальные имена родственников, включая моё имя: ",unique_relatives_names,sep='')
print('3) Общая длина всех названий предметов: ',count_letters_of_lessons,sep='')
print('4) Уникальные буквы в названиях предметов: ',unique_letters_in_keys,sep='')
print("5) Имя пушистой кивы в бинарном виде: ", kivy_bin_name,sep='')
print("6) Отсортированные имена родственников в обратном порядке: ", sorted(relatives, reverse=True),sep='')
print("7) С момента моего рождения прошло: ", period.days," дней",sep='')
print('8) FIFO - очередь, введенная с клавиатуры (остановка словом stop): ')
fifo_queue = []
command = "stop"
number = (10 + 9 ** 2 + 2004) % 21 + 1
while True:
    s = input()
    if s == command:
        for i in range(len(fifo_queue)):
            print(fifo_queue.pop(),end=" ")
        break
    fifo_queue.append(s)
print('\n9) Введите индекс имени родственника, чтобы заменить на имя ацтекского правителя (от 0 до 15): ')
i1 = int(input())
zamena(i1,sortrelatives)
print('10) ')
slov = {}
for i in range(len(relatives)-1):
    slov[relatives[i]] = relatives[i+1]
print(slov)
print('11) Написать функцию-генератор: ')
numbervar = len("Помазов Степан Павлович") * len(relatives) % 4
print('Номер моего варианта - ', numbervar)
print('Мне нужно написать функцию последовательности Сильвестра')
n = int(input("Сколько чисел последовательности вывести? (целое число) "))
Silvestr_sequence(n)


