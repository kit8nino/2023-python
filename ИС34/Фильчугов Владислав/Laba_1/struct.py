import datetime
info = ('Фильчугов',  'Владислав', 'Евгеньевич', 10, 'Ноябрь', 2004)
Names = ('Оксана', 'Евгений', 'Анастасия', 'Любовь', 'Алик', 'Юрий', 'Марина', 'Людмила')
pet = 'mirage'
evaluations = [5, 4, 5, 3, 5, 4, 5, 5, 4, 3, 4, 5, 3, 5]
items = ['Алгебра', 'Физика', 'Русский', 'Геометрия', 'Астрономия', 'Литература', 'Физ-ра', 'Обществознание', 'История',
         'Английский язык', 'Химия', 'Биология', 'География', 'Родная литература']
for q, c in zip(items, evaluations):
    print(f'Предмет  {q} - Оценка {c}')
# 1
print('Среднее значение оценок в аттестате - ', sum(evaluations) / len(evaluations))
# 2
s = ['Владислав']
ni = list(Names) + s
print(set(ni))
# 3 - 4
s = ''.join(items)
print('Общая длина всех названий предметов - ', len(s))
print('Уникальные буквы в название предметов - ', list(set(s)))
# 5
binary = pet.encode('utf-8')
binary = ''.join(format(x,'b')for x in binary)
print('Имя домашней пушистой кивы в бинарном виде - ', binary)
# 6
Names = sorted(Names, reverse=True)
print('отсортированный по алфавиту (в обратном порядке) список родственников ', Names)
# 7
today = datetime.datetime.now().date()
born = datetime.date(2004, 10, 11)
days = today - born
print('С моего дня рождения прошло - ', days)
# 8
print('Задание 8 \n' 'Введите индекс\n' 'Для вывода всей очереди введите любое число > 13')
dq = []
x = 0
while x < len(items):
    x = int(input())
    if x < len(items):
        dq.append(items[x])
        print(dq)
if x >= len(items):
    print('Очередь - ', dq)
# 9
print('Задание 9 \n' 'Введите индекс имени\n')
index = int(input())
tlatoque = {}
tlatoque = Names
tlatoque[index] = 'Tlacotzin'
print(tlatoque)
# 10
years = (1960, 1980, 1962, 1959, 1985, 1978, 2008, 1962)
NY = [(s, i) for s, i in zip(years, Names)]
NY = sorted(NY)
dict_names = {}
for i, name in enumerate(NY):
    dict_names[name] = (i+1)
    if dict_names[name] == 0:
        dict_names[name] = len(Names)
print(dict_names)
# 11
FIO = ['ФильчуговВладсилавЕвгеньевич']
print('Номер варианта - ', len(FIO) * len(Names) % 4)
# Аликвотная последовательность
x = int(input('Введите число: '))
i = [x]
while i[-1] != 0 and i[-1] not in i[:-1]:
    summa = sum(j for j in range(1, i[-1]) if i[-1] % j == 0)
    i.append(summa)
print("Аликвотная последовательность для числа", {x}, ":", i)