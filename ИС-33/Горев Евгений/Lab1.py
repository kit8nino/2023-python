a = ("Горев Евгений Максимович", 12, 8, 2001)

b = {"ru_leng" : 4,
     "liter" : 4,
     "en_leng" : 5,
     "math" : 4,
     "chemistry" : 4,
     "geography" : 5,
     "history" : 5,
     "informatics" : 5,
     "biology" : 4,
     "physics" : 4,
     "drawing" : 5,
     "sport" : 5,
     "technology" : 5,
     "sociology" : 5,}

s = ["Данила", "Илья", "Анастасия", "Даша", "Данила"]

d = "Балдёж"


#zadanie_1___________________________________________________________________________________________
def srznach ():
     srznach = 0
     for i in b:
          srznach += b[i]
     srznach /= len(b)
     return srznach

print("№1 Средняя оценка в атестате: ", srznach())

#zadanie_2___________________________________________________________________________________________
def uniq_name ():
     uniq_name = list(set(s))
     uniq_name_and_me = uniq_name + [a[0][6:12]]
     return uniq_name_and_me

print("№2 Уникальные имена родственников + свое: ", uniq_name())

#zadanie_3___________________________________________________________________________________________
def length (b):
     total_length = 0
     for i in b:
          total_length += len(i)
     return total_length

print("№3 Общая длина всех названий предметов: ", length (b))

#zadanie_4___________________________________________________________________________________________
def uniq_letters ():
     result = []
     for i in b:
          result +=i
     un_letters = set(result)
     return un_letters

print("№4 Уникальные буквы в названиях предметов: ", uniq_letters())

#zadanie_5___________________________________________________________________________________________
def binar_name ():
     binar = ' '.join(format(i, 'b') for i in bytearray(d, "utf-8"))
     return binar

print("№5 Имя кивы в бинарном виде: ", binar_name())

#zadanie_6___________________________________________________________________________________________
def sortirovka_rodstvennikov ():
     global zz
     zz = sorted(s, reverse=True)
     return zz

print("№6 Отсортированный по алфавиту (в обратном порядке) список родственников: ", sortirovka_rodstvennikov())

#zadanie_7___________________________________________________________________________________________
import datetime
def raznica ():
     today = datetime.date.today()
     dr = datetime.date(int(a[3]),int(a[2]),int(a[1]))
     raznost = today - dr
     raznica = str(raznost)
     return raznica.split()[0]

print("№7 Количество дней от даты рождения до текущей даты: ", raznica())

#zadanie_8___________________________________________________________________________________________
def FIFO ():
     FIFO = []
     while(True):
          k = input()
          if (k == "Stop"):
               break
          FIFO.append(k)
     return FIFO

print ("№8 Введите слово, которое добавится в список: ")
print(FIFO())

#zadanie_9___________________________________________________________________________________________
print ("№9 Изменение в списке родственников: ")
def pravitel ():
     number = ((int(a[1])) + (int(a[2]))**2 + (int(a[3]))) % 21 + 1
     print("Номер правителя из списка: ", number)
     name_imperator = "Сипак"
     print("Имя императора: ", name_imperator)
     x = int(input())
     zz[x] = name_imperator
     return zz

print(pravitel())

#zadanie_10__________________________________________________________________________________________
def link_sp ():
     link = {s[i]: s[(i+1)%len(s)] for i in range(len(s))}
     return link

print ("№10 Связанный список: ")
print(link_sp())

#zadanie_11__________________________________________________________________________________________
number = len('ГоревЕвгенийМаксимович') * (len(s[0]) + len(s[1]) + len(s[2]) + len(s[3]) + len(s[4])) % 4
print('Вариант:', number)
#Нахождение чисел трибоначчи
def gen_tribonatti(n):
     if n == 0:
          return 0
     elif n == 1 or n == 2:
          return 1
     else:
          return gen_tribonatti(n - 1) + gen_tribonatti(n - 2) + gen_tribonatti(n - 3)

#Запись в массив последовательности чисел трибоначчи в зависимости от заданного значения
def tribonacci_sequence(n):
    sequence = []
    for i in range(n+1):
        sequence.append(gen_tribonatti(i))
    return sequence

print ("№11 Функция генератор: ")
print ('Введи количество выводимых чисел: ')
n = int(input())
print(tribonacci_sequence(n))