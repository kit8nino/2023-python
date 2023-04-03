# Исходные данные
name = ('Иванов', 'Иван', 'Иванович', 10, 5, 2000)
birth_date = (2000, 10, 5)
attestat = {
    'Математика': 5,
    'Русский язык': 4,
    'Английский язык': 5,
    'Физика': 4,
    'Химия': 4,
    'Информатика': 5,
    'История': 4,
    'Обществознание': 4,
    'Биология': 4,
    'География': 4,
    'Литература': 4,
    'Иностранный язык (второй)': 5,
    'ОБЖ': 5,
    'Технология': 5
}
relatives = ['Мама', 'Папа', 'Брат', 'Сестра']
pet_name = 'Бакс'

# 1. Средняя оценка в аттестате
avg_mark = sum(attestat.values()) / len(attestat)
print(f'1.Средняя оценка в аттестате: {avg_mark:.2f}')

# 2. Различные имена родственников
unique_relatives = list(set(relatives))
print(f'2.Различные имена родственников: {unique_relatives}')

# 3. Общая длина всех названий предметов
total_len = sum(len(subject) for subject in attestat)
print(f'3.Общая длина названий предметов: {total_len}')

# 4. Уникальные буквы в названиях предметов
unique_letters = set(''.join(attestat.keys()))
print(f'4.Уникальные буквы в названиях предметов: {unique_letters}')

# 5. Имя домашней кивы в бинарном виде
binary_pet_name = ' '.join(format(ord(letter), 'b') for letter in pet_name)
print(f'5.Имя домашней кивы в бинарном виде: {binary_pet_name}')

# 6. Отсортированный список родственников
sorted_relatives = sorted(relatives, reverse=True)
print(f'6.Отсортированный список родственников: {sorted_relatives}')

# 7. Количество дней от даты рождения до текущей даты
from datetime import datetime
current_date = datetime.now()
birth_datetime = datetime(*birth_date)
days_since_birth = (current_date - birth_datetime).days
print(f'7.Количество дней от даты рождения до текущей даты: {days_since_birth}')

# 8. FIFO очередь
queue = []
while True:
    index = input("Введите индекс предмета (или \"стоп\" для остановки): ")
    if index == "стоп":
        break
    queue.append(list(attestat.keys())[int(index)])
print(queue)

# 9 поменять имя в списке родственников на имя ацтекского правителя
number = (name[3] + name[4]**2 + name[5]) % 21 + 1
tlatoque = ["Acamapichtli", "Huitzilihuitl", "Chimalpopoca", "Itzcoatl", 
            "Moctezuma I", "Axayacatl", "Tizoc", "Ahuitzotl", "Moctezuma II", 
            "Cuitlahuac", "Cuauhtemoc", "Tlacaelel", "Tezozomoc", "Maxtla", 
            "Nezahualcoyotl", "Netzahualpilli", "Cacamatzin", "Moquihuix", 
            "Totoquihuatzin", "Ixtlilxochitl", "Juan de Oñate"]
relatives_sorted = sorted(relatives, reverse=True)
zad9 = number % 4
relatives_sorted[zad9] = tlatoque[number]
print("9.Отредактированный список родственников:", relatives_sorted)

# 10 zad10
zad10 = {}
for i in range(len(relatives)):
        zad10[relatives[i]] = relatives[(i+1)%len(relatives)]
print("10.", zad10)
# 11 функция генетратор

my_name = ["ДзиневскийСиепанОлегович"]
print ("My number: ", len(my_name) * len (relatives) % 4)

def zad11(x, y):
    sum = 0
    if x == y:
        print(x)
    if x == 1:
        print(0)
        return 0
    else:
        for i in range(1, x):
            if x % i==0:
                sum += i
    print(sum)
    return zad11(sum, x)
z = int(input("Введите число: "))
print("Аликвотная последовательность числа", z, ":")
zad11(z, z)
