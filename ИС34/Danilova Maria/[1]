import datetime
I = ("Данилова Мария Дмитриевна", 11, 5, 2004)
print(I)
attestat = {
'Рус': 4,
'Матем': 4,
'Литра': 4,
'Физика': 4,
'Биология':3,
'Общество': 4,
'Информатика': 5,
'География': 4,
'Родной язык': 4,
'Химия': 3,
'История': 4,
'Физра': 5,
'ОБЖ': 3,
'Английский': 3,

}
print('Аттестат ', attestat)
kiv = "Фрося"
print('Кива: ', kiv)

family = ['Мария', 'Анастасия', 'Ксения', 'Татьяна', 'Дмитрий', 'Юлия',
'Юлия', 'Екатерина', 'Галина', 'Мирон', 'Васелина', 'Надежда']
print('Семья:', family)


print("\n1)Средний балл:", sum(attestat.values()) / len(attestat.values()))


New_relat = family.copy()
New_relat.append("Фрося")
rel_u = set(New_relat)
print("\n2)Уникальные имена: ", rel_u)
print("\n2)Отсортированные родственники: ", sorted(rel_u))


long = ''
for elem in attestat.keys():
    long += elem
print("\n3) Длина названий предметов: ", (len(long)))


at_u = set(long)
at_u.remove(' ')
print("\n4)Уникальные буквы: ", sorted(at_u))


binar = ''.join(format(ord(x), '08b') for x in kiv)
print("\n5)бинарная кива: ", binar)


print("\n6)Отсотрированные родственники в обратном порядке: ", sorted(family)[::-1])


Today = datetime.datetime.now()
MyData = datetime.datetime(2004, 5, 11)
Time = Today - MyData
print("\n7)Я прожила: ", Time)


print("\n8) FIFO очередь (Закончить - stop)")
sort = sorted(family)
Atctecs = ['Tenoch','Acamapichtli','Huitzilihuitl','Chimalpopoca',"Xihuitl Temoc",
    'Itzcoatl','Moctezuma I','Atotoztli',
    'Axayacatl','Tizoc','Ahuitzotl','Moctezuma II','Cuitláhuac',
    'Cuauhtémoc','Tlacotzin','Motelchiuhtzin','Xochiquentzin','Huanitzin','Tehuetzquititzin',
    'Cecetzin','Cipac']
def zamena(i,A):
    number = (11 + 5 ** 2 + 2004) % 21 + 1
    A[i] = Atctecs[number]
    return print(" Результат: ", A)
att = [elem for elem in attestat.keys()]
print(att)
fifo_queue = []
command = "stop"
number = (9 + 12 ** 2 + 2003) % 21 + 1
while True:
    s = input()
    if s == command:
        for i in range(len(fifo_queue)):
            print(att[i])
        break
    fifo_queue.append(s)


print('\n9) Введите индекс имени родственника, чтобы заменить на имя ацтекского правителя (от 0 до 11): ')
i1 = int(input())
zamena(i1, sort)


dictat = {}
for i in range(len(sort) - 1):
    dictat[sort[i]] = sort[(i+1)]



slov = {}
for i in range(len(family)-1):
    slov[family[i]] = family[i+1]
print(slov)
print('\n11) Написать функцию-генератор: ')
numbervar = len("Данилова Мария Дмитриевна") * len(family) % 4
print('Номер моего варианта - ', numbervar)

def posledov(x, y):
    sum = 0
    if x == y:
      print(x)
    if x == 1:
      print(0)
      return 0
    else:
     for i in range(1, x):
        if x % i == 0:
            sum += i
            print(sum)
            return posledov(sum, x)
z = int(input("Введите число: "))
print("Аликвотная последовательность числа", z, ":")
posledov(z, z)

