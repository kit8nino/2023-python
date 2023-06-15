# исходные данные

full_name = "Лядова Алиса Родионовна"
birthday = (19, 10, 2004)
subjects = ["Русский язык", "Литература", "Родной язык", "Родная литература", "Иностранный язык",
            "Математика", "Информатика", "История", "География", "Обществознание", "Физика",
            "Астрономия", "Химия", "Биология", "Физическая культура", "ОБЖ", "Индивидуальный проект"]
family_names = ["Елена", "Родион", "Марина", "Владимир", "Алина", "Глеб", "Юрий"]
pet_name = "Миса"

#1 ср оценка аттестата
average_score = round(sum([5, 5, 5, 5, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5])/len(subjects), 2)
print("Средняя оценка в аттестате: {}".format(average_score))

#2 уникальные имена родственников
unique_names = set([full_name.split()[0]]+family_names)
print("Уникальные имена родственников: {}".format(", ".join(unique_names)))

#3 общая длина названий всех предметов
total_len = sum([len(x) for x in subjects])
print("Общая длина названий предметов: {}".format(total_len))

#4 уникальные буквы в названиях предметов
unique_letters = len(set("".join(subjects)))
print("Уникальные буквы в названиях предметов: {}".format(unique_letters))

#5 имя кивы в бинарном виде
binary_pet_name = bin(int.from_bytes(pet_name.encode(), 'big'))
print("Имя домашней пушистой кивы в бинарном виде: {}".format(binary_pet_name))

#6 отсортированный список родственников
sorted_family_names = sorted(family_names, reverse=True)
print("Отсортированный в обратном алфавитном порядке список родственников: {}".format(sorted_family_names))

#7 кол-во дней от даты рождения до текущей даты
from datetime import datetime

current_date = datetime.now()
birthdate = datetime(year=birthday[2], month=birthday[1], day=birthday[0])
days_since_birth = (current_date-birthdate).days
print("Количество дней от даты рождения до текущей даты: {}".format(days_since_birth))

#8 FIFO очередь
import queue

q = queue.Queue()

while True:
    index = input("Введите номер предмета (или 'стоп' для завершения): ")
    if index.lower() == "стоп":
        break
    elif not index.isdigit() or int(index) > len(subjects):
        print("Неверный ввод")
    else:
        q.put(subjects[int(index)-1])

while not q.empty():
    print(q.get())

#9
names = ["Acamapichtli", "Huitzilihuitl", "Chimalpopoca", "Itzcoatl", "Moctezuma I", "Axayacatl", "Tizoc", "Ahuitzotl", "Moctezuma II", "Cuitlahuac", "Cuauhtemoc", "Tlacaelel", "Tezozomoc", "Maxtla", "Nezahualcoyotl", "Netzahualpilli", "Cacamatzin", "Moquihuix", "Totoquihuatzin", "Ixtlilxochitl", "Juan de Onate"]
number = (19 + 10**2 + 2004) % 21 + 1
new_name = names[number - 1]
sorted_family_names[number] = new_name
print('Отсортированный список родственников после замены:', sorted_family_names)

#10
family = dict(zip(sorted_family_names, range(len(sorted_family_names))))

for name in family:
    print("{} -> {}".format(name, sorted_family_names[family[name]]))

#11
def aliquot_sequence():
    n = 1
    while True:
        divisors_sum = sum([i for i in range(1,n) if n%i == 0])
        if divisors_sum == n:
            yield n
        n += 1

def sylvester_sequence():
    s = 1
    yield s
    for i in range(2, 20):
        s = s * i + 1
        yield s

def tribonacci_sequence():
    a, b, c = 0, 0, 1
    while True:
        yield c
        a, b, c = b, c, a + b + c

def leonardo_numbers():
    a, b = 1, 1
    yield a
    yield b
    while True:
        a, b = b, a + b + 1
        yield a

generator_number = len(full_name) * len(family_names) % 4

if generator_number == 0:
    gen = aliquot_sequence()
elif generator_number == 1:
    gen = sylvester_sequence()
elif generator_number == 2:
    gen = tribonacci_sequence()
else:
    gen = leonardo_numbers()

print("Первые 10 чисел из выбранной последовательности:")
for i in range(10):
    print(next(gen))