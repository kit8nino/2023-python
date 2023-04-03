import datetime
I = ("Редькин Максим Денисович", 9, 12, 2003)
print('я: ', I)
at = {
    'Математика': 5,
    'Русский язык': 4,
    'Литература': 4,
    'Физика': 4,
    'Обществознание': 3,
    'Информатика': 5,
    'Родной язык': 4,
    'История России': 4,
    'Физическая культура': 5,
    'История': 3,
    'Английский язык': 3,
    'Индивидуальный проект': 5
}
print('Аттестат ', at)
kivy_name = "Роман"
print('Имя кивы: ', kivy_name)

relatives = ['Денис', 'Дарья', 'Денис', 'Дарья', 'Елена', 'Сергей',
             'Ольга', 'Ольга', 'Нина', 'Борис', 'Алексей', 'Татьяна']
print('Родственники:', relatives)

#1
print("\n1)Средний балл:", sum(at.values()) / len(at.values()))

#2
New_relat = relatives.copy()
New_relat.append("Максим")
rel_u = set(New_relat)
print("\n2)Уникальные имена: ", rel_u)
print("\n2)Отсортированные родственники: ", sorted(rel_u))

#3
long = ''
for elem in at.keys():
    long += elem
print("\n3)Общая длина названий предметов: ", (len(long)))

#4
at_u = set(long)
at_u.remove(' ')
print("\n4)Уникальные буквы: ", sorted(at_u))

#5
binar = ''.join(format(ord(x), '08b') for x in kivy_name)
print("\n5)бинарная кива: ", binar)

#6
print("\n6)Отсотрированные в обратном порядке: ", sorted(relatives)[::-1])

#7
Today = datetime.datetime.now()
MyData = datetime.datetime(2003, 12, 9)
Time = Today - MyData
print("\n7)Время прошло: ", Time)

#8,9
print("\n8) FIFO очередь (Стоп слово - stop)")
sort = sorted(relatives)
Atctecs = ['Tenoch','Acamapichtli','Huitzilihuitl','Chimalpopoca',"Xihuitl Temoc",
                         'Itzcoatl','Moctezuma I','Atotoztli',
                         'Axayacatl','Tizoc','Ahuitzotl','Moctezuma II','Cuitláhuac',
                         'Cuauhtémoc','Tlacotzin','Motelchiuhtzin','Xochiquentzin','Huanitzin','Tehuetzquititzin',
                         'Cecetzin','Cipac']
def zamena(i,A):
    number = (9 + 12 ** 2 + 2003) % 21 + 1
    A[i] = Atctecs[number]
    return print(" Результат: ", A)
att = [elem for elem in at.keys()]
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

print('\n9) Введите индекс имени родственника, чтобы заменить на имя ацтекского правителя (от 0 до 12): ')
i1 = int(input())
zamena(i1, sort)

#10
dictionary = {}
for i in range(len(sort) - 1):
    dictionary[sort[i]] = sort[(i + 1)]
print("\n10)Диктаторы: ", dictionary)

#11
slov = {}
for i in range(len(relatives)-1):
    slov[relatives[i]] = relatives[i+1]
print(slov)
print('\n11) Написать функцию-генератор: ')
numbervar = len("Редькин Максим Денисович") * len(relatives) % 4
print('Номер моего варианта - ', numbervar)

def al_pos(x, y):
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
    return al_pos(sum, x)
z = int(input("Введите число: "))
print("Аликвотная последовательность числа", z, ":")
al_pos(z, z)
