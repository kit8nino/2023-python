from datetime import datetime
ya = ("Семенов Андрей Александрович", 14, 9, 2004)
attestat = {'Русский язык': 4,
            'Математика': 4,
            'Английский язык': 4,
            'Чувашский язык': 5,
            'География': 5,
            'История': 4,
            'Физическая культура': 5,
            'Обществознание': 4,
            'Индивидуальный проект': 5,
            'Химия': 4,
            'Технология': 5,
            'Информатика': 5,
            'Литература': 4,
            'Физика': 4}
rodstv = ['Юлиана', 'Илья', 'Анна', 'Владимир', 'Дмитрий', 'Даниил', 'Михаил', 'Анна', 'Елизавета', 'Мария', 'Семен', 'Андрей']
kiwy = "Исай"
print("Я:", ya)
print("Аттестат:", attestat)
print("Имена родственников:", rodstv)
print("Имя кивы:", kiwy)
#1
print("1.Cредний балл:", sum(attestat.values())/len(attestat.values()))
#2
rod = rodstv
rod = list(set(rod))
print("2.Имена без повторений:", rod)
#3
d = list(attestat)
dl = 0
for i in d:
    dl += len(i)
print("3.Общая длина:", dl)
#4
unique_letters = set()
for key in attestat:
    for letter in key:
        unique_letters.add(letter)
print(unique_letters)
#5
word = kiwy
encoded = word.encode('utf-8')
binar = ''.join(format(b, '08b') for b in encoded)
print("5.Имя кивы в бинарном коде:", binar)
#6
sortrodstv = sorted(rodstv, reverse=False)
print("6.Отсортированный по алфавиту список:", sortrodstv)
#7
my_data = datetime(2004, 9, 14)
today = datetime.today()
remains = (today-my_data).days
print("7.Количество дней от моей даты рождения:", remains)
#8
fifo = []
while True:
    index = input("8.Введите индекс(для остановки введите 'stop'): ")
    if index == 'stop':
        break
    fifo.append(index)
print(fifo)
#9
pravit = 'Cipac'
number = (14 + 9**2 + 2004 % 21 + 1)
print("9.Номер правителя: ", number)
index = int(input("Введите индекс: "))
if index < 0 or index >= len(sortrodstv):
    print("Индекс не подходящий.")
else:
    sortrodstv[index] = pravit
    print("Измененный список: ", sortrodstv)
#10
srodstv = sorted(rodstv)
spisok = {}
for i in range(len(srodstv)-1):
    spisok[srodstv[i]] = srodstv[i+1]
print("10.Связаный список: ", spisok)
#11
num = len("Семенов Андрей Александрович") * len(rodstv) % 4
print("11.Мой вариант: ", num)
def alikposl(x, y):
    z = 0
    if x == y:
        print(x)
    if x == 1:
        print(0)
        return 0
    else:
        for i in range(1, x):
            if x % i == 0:
                z += i
    print(z)
    return alikposl(z, x)
q = int(input("Введите число: "))
print("Аликвотная последовательность:", q, ":")
alikposl(q, q)