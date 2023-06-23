# Исходные данные
fio = ('Коротаев', 'Александр', 'Павлович', 24, 11, 2003)
attestat = {
    'Математика': 4,
    'Русский язык': 4,
    'Английский язык': 5,
    'Геометрия': 4,
    'Физкультура': 5,
    'Физика': 3,
    'Химия': 5,
    'Информатика': 4,
    'История': 5,
    'Обществознание': 4,
    'Биология': 5,
    'География': 4,
    'Литература': 4,
    'ОБЖ': 5,
    'Технология': 5
}
rodstvenniki = ['Людмила', 'Павел', 'Александр', 'Валентина', 'Александр']
kiviname = 'Локи'

#1
avg_attestat = sum(attestat.values()) / len(attestat)
print(f"1.Средняя оценка в аттестате: {avg_attestat}")
#2
unique_names = list(set(rodstvenniki))
print(f"2.Уникальные имена родственников: {unique_names}")
#3
subject_names = list(attestat.keys())
total_length = sum(len(name) for name in subject_names)
print(f"3.Общая длина всех названий предметов: {total_length}")
#4
unique_letters = set(''.join(subject_names))
print(f"4.Уникальные буквы в названиях предметов: {unique_letters}")
#5
binarykiviname = ' '.join(format(ord(letter), 'b') for letter in kiviname)
print(f"5.Имя домашней пушистой кивы в бинарном виде: {binarykiviname}")
#6
sorted_unique_names = sorted(unique_names, reverse=True)
print(f"6.Отсортированный по алфавиту (в обратном порядке) список родственников: {sorted_unique_names}")
#7
import datetime

birthday = datetime.date(2003, 11, 24)
today = datetime.date.today()
delta = today - birthday
print(f"7.Количество дней от даты рождения до текущей даты: {delta.days}")
#8
FIFO=[]
print("8.")
while (True):
    c=input("Введите индекс предмета (или \"стоп\" для остановки): ")
    if (c=="стоп"):
        for i in range(len(FIFO)):
            print(FIFO.pop())
        break
    FIFO.append(c)
#9
y = fio[5]
m = fio[4]
d = fio[3]
sorted_rodstvenniki = sorted(rodstvenniki)
names_Aztec_leaders = ["Tenoch", "Acamapichtli", "Huitzilihuitl", "Chimalpopoca", "Xihuitl Temoc", "Itzcoatl",
                       "Moctezuma I", "Atotoztli", "Axayacatl", "Tizoc", "Ahuitzotl", "Moctezuma II",
                       "Cuitláhuac", "Cuauhtémoc", "Tlacotzin", "Motelchiuhtzin", "Xochiquentzin", "Huanitzin",
                       "Tehuetzquititzin", "Cecetzin", "Cipac"]
print("9.")
for i in range(len(sorted_rodstvenniki)):
    print(i + 1, ". ", sorted_rodstvenniki[i], sep="")

index = int(input("Введите индекс для замены: "))
sorted_rodstvenniki[index - 1] = names_Aztec_leaders[(d + m ** 2 + y) % 21 + 1]

print("Измененный список имен:", sorted_rodstvenniki)
#10
rodstvenniki_new_list = {}
for i in range(len(rodstvenniki)):
    rodstvenniki_new_list[rodstvenniki[i]] = rodstvenniki[(i+1) % len(rodstvenniki)]
print("10.Создание списка:", rodstvenniki_new_list)
#11
number = len(fio)*len(rodstvenniki)%4
print("11. Вариант ", number)

def tribonacci():
    a, b, c = 0, 0, 1
    while True:
        yield a
        a, b, c = b, c, a + b + c
trib = tribonacci()
for i in range(10):
    print(next(trib))
