import datetime
my_data = tuple(('Шестых Денис Олегович', '14', '5', '2003'))
relat = ['Денис', 'Саша', 'Олег', 'Саша', 'Таня', 'Юля', 'Даша', 'Коля', 'Паша', 'Сергей', 'Юля', 'Максим', 'Федор', 'Катя', 'Валя', 'Кристина', 'Ульяна', 'Женя', 'Платон']
data_name = {'Денис':2003, 'Саша':1983, 'Олег':1982, 'Саша':1969, 'Таня':1972, 'Юля':1999, 'Паша':1980, 'Сергей':1983, 'Юля':1982, 'Максим':2004, 'Федор':2009, 'Катя':2006, 'Валя':1981, 'Кристина':1987, 'Ульяна':2019, 'Женя':1984, 'Платон':2018}
atestat = {'Литература': 3, 'Русский язык': 3, 'Английский': 4, 'Алгебра': 4, 'Музыка': 4, 'Геометрия': 4, 'Информатика': 5, 'История России': 4, 'Всеобщяя История': 4, 'Обществознание': 4, 'География': 4, 'Биология': 4, 'Химия': 3, 'Физика': 4, 'Астрономия': 4, 'Физра': 4, 'ОБЖ': 4, 'Фак. Рус.Яз': 3, 'Фак. Литра': 4, 'Фак. Матем.': 4, 'Фак. История': 4, 'Фак. Обществ.': 5, 'Фак. Биология': 4, 'Чуловек и его здоровье': 4}
kiva_name = "Чмоня"

#1 Средняя оценка аттестата
avg_grade = sum(atestat.values()) / len(atestat)
print ("#1-Средняя оценка в аттестате:", avg_grade)

#2 Уникальное имя
unique_names = set(relat)
print("#2-", unique_names)

#3 Общяя длина названий предметов в аттестате
total_lenght = 0
for subject in atestat:
    total_lenght += len(atestat)
print("#3-", total_lenght)

#4 Уникальные буквы в названиях предметов
unique_lett = set()
for subject in atestat:
    for letter in subject:
        #убрал из уникальных букв пробел и точку
        if letter.isalpha():
         unique_lett.add(letter)
print("#4-", unique_lett)

#5 Имя Кивы в виде бинарного кода
binar_name = ""
for char in kiva_name:
    binar_name += bin(ord(char))[2:].zfill(8)
print("#5-", binar_name)

#6 Список родствеников отсортированны по алфавиту(в обратном порядке)
name_rev = sorted(relat,reverse=True)
print("#6-", name_rev)
#я думал этот шаг будет довольно сложным, а тут просто есть reverse

#7 Количество дней сколько я живу
br_day = datetime.date(2003, 5, 14)
today = datetime.date.today()
days = today - br_day
print("#7-", days)

#8 FIFO очередь, в которую можно добавлять предметы по вводимому с клавиатуры индексу
#Сейчас бы быстро понять что такое FIFO
queue = []
while True:
    index = input("Введите предмет для добавления его в очередь (stop для остановки)")
    if index == 'stop':
        break
    queue.append(index)
print("#8-Очередь:", queue)

#9 Замена имени родственника на имя ацтекского правителя
index = int(input("Введите номер фамилии которую хатите заменить(начиная с нуля):"))
day = int(input("Введите день рождения"))
month = int(input("Введите месяц рождения:"))
year = int(input("Введите год рождения"))
number = (day + month**2 + year)%21 + 1
aztec_name = ["Tenoch", "Acamapichtli", "Huitzilihuitl", "Chimalpopoca", "Xihuitl Temoc", "Itzcoatl", "Moctezuma I", "Atotoztli", "Axayacatl", "Tizoc", "Ahuitzotl", "Moctezuma II", "Cuitláhuac", "Cuauhtémoc", "Tlacotzin", "Motelchiuhtzin", "Xochiquentzin", "Huanitzin", "Tehuetzquititzin", "Cecetzin", "Cipac"]
name_sort = sorted(relat)
if 0 <= index < len(relat):
    relat[index] = aztec_name[number-1]
    print("#9-", relat)
else:
    print("#9-Такого правителя нет")

#10 Создать связный список, как словарь, где ключ - имя родственника, а значение - индекс следующего имени по исходному списку
name_sp = {}
for i in range(len(name_rev)):
    name_sp[name_rev[i]] = [i % len(name_rev)]
print("#10-", name_sp)
#Я не понял как сделать тоже самое еще и с сортировкой по годам. Я криво, но сделал отдельно сортировку по годам рождения
def sort_data(person):
    return person["year"]

data_name2 = [
    {"name": "Денис", "year": 2003},
    {"name": "Вера", "year": 1983},
    {"name": "Олег", "year": 1982},
    {"name": "Саша", "year": 1969},
    {"name": "Таня", "year": 1972},
    {"name": "Юля", "year": 1999},
    {"name": "Паша", "year": 1980},
    {"name": "Сергей", "year": 1983},
    {"name": "Юля", "year": 1982},
    {"name": "Максим", "year": 2004},
    {"name": "Федор", "year": 2009},
    {"name": "Катя", "year": 2005},
    {"name": "Валя", "year": 1981},
    {"name": "Кристина", "year": 1987},
    {"name": "Ульяна", "year": 2019},
    {"name": "Женя", "year": 1984},
    {"name": "Платон", "year": 2018},
]

name_rev2 = sorted(data_name2, key=sort_data)
print("#10(по годам)-", name_rev2)

#11 Функция-генератор
var = len("Шестых Денис Олегович") * len (relat) % 4
print("Вариант для 11 задачи:", var)
#Чисал Леонардо это ряд чисел начинающихся с вдух единиц. Каждое последующее число это сумма двух предыдущих
def leonard_num(n):
    num = [1, 1]
    for i in range(2, n):
        num.append(num[i - 1] + num[i-2])
    return num
#Допусти нам надо 15 чисел, в leonard_num нужно написать 15
print("#11-", leonard_num(15))

#В итоге data_name в начале мне даже не пригодилься. Даже не знаю почему я его не удалил