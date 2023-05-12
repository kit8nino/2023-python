from datetime import datetime

FioDate = ("Кречин Александр Сергеевич", 3, 8, 2004)
Marks = {
    "Русский язык": 3,
    "Родной язык": 5,
    "Литература": 4,
    "Английский язык": 3,
    "История": 4,
    "Обществознание": 4,
    "География": 3,
    "Математика": 5,
    "Информатика": 5,
    "Физика": 5,
    "Астрономия": 5,
    "Биология": 5,
    "Химия": 3,
    "Физическая культура": 5
}
Relatives = ["Юлия", "Сергей", "Любовь", "Андрей", "Александр", "Ирина", "Света", "Маша", "Кристина", "Ульяна", "Лена", "Георгий"]
Kiva = "Шаверма"

# 1 Вывести среднюю оценку в аттестате

print("1) Средняя оценка в аттестате:", round(sum(Marks.values()) / len(Marks), 2))


# 2 вывести уникальные имена среди своих родственников включая свое

UniqueName = Relatives.copy()
UniqueName.append(FioDate[0].split(" ")[1])
print("2) Уникальные имена:", *set(UniqueName))

# 3 общая длина всех названий предметов
length = 0
Allletters = []
for i in Marks.keys():
    length += int(len(i))
    for z in i:
        if z != " ":
            Allletters.append(z.lower())
        continue
print("3) Длина всех названий предметов:", length)

# 4 уникальные буквы в названиях предметов
print("4) Уникальные буквы предметов:\n\t", *set(Allletters))

# 5 имя вашей домашней пушистой кивы в бинарном виде
print("5) Имя кивы:\n\t", ''.join(format(x,'08b') for x in bytearray(Kiva,'utf-8')))


# 6 отсортированный по алфавиту (в обратном порядке) список родственников
RelativesSort = Relatives.copy()
RelativesSort.sort(reverse=True)
print("6) Список родственников в обрат. алфавит порядке :\n\t", *RelativesSort)
# 7 количество дней от вашей даты рождения до текущей даты (должна быть всегда актуальной)
print('7) Кол-во дней от даты рождения: {}'.format((datetime.now() - datetime(day=int(FioDate[1]), month=int(FioDate[2]), year=int(FioDate[3]))).days))

# 8 FIFO очередь, в которую можно добавлять предметы по вводимому с клавиатуры индексу
# (до команды остановки), после введения - вывести все


valor = ["Omen", "Yoru", "Jet", "Sage", "Sova", "Phoenix", "Killjoy", "Astra", "Neon"]
FIFO = []
for valorIND in range(len(valor)):
    print(valor[valorIND], ':', (len(max(valor,key = len))  - len(valor[valorIND])) * " ", valorIND)
print("введите число того, что хотите добавить \n Чтобы прекратить -1")
valorPers = []
InputIND = int
while InputIND != -1:
    try:
        InputIND = int(input("Введите: "))
        if InputIND == -1:
            break
        if InputIND <= -1:
            raise IndexError
        valorPers.append(valor[InputIND])
    except ValueError:
        print("А всё, а я всё вижу")
    except IndexError:
           print("К моему большому сожалению таких у нас нет")
print("8) FIFO:", *valorPers)

# 9 по введеному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя
# под номером, получаемым из вашей даты рождения: number = (day + month**2 + year) % 21 + 1
AcNames = ("Tenoch", "Acamapichtli", "Huitzilihuitl", "Huitzilihuitl", "Xihuitl Temoc", "Itzcoatl", "Moctezuma I", "Atotoztli", "Axayacatl", "Tizoc", "Ahuitzotl", "Moctezuma II", "Cuitláhuac", "Cuauhtémoc", "Tlacotzin", "Motelchiuhtzin", "Xochiquentzin")
number = (FioDate[1] + FioDate[2]**2 + FioDate[3]) % 21 + 1
AcRelatives = RelativesSort.copy()
IndRel = 0
InputIndAc = 1
print("9)")
while IndRel <= (len(AcRelatives)) - 1:
    print(IndRel + 1, AcRelatives[IndRel])
    IndRel += 1
    if IndRel == len(AcRelatives):
        print("Какое имя хотите заменить?")
        try:
            InputIndAc = int(input())
            if InputIndAc not in range(1, len(AcRelatives) + 1):
                raise IndexError
            AcRelatives[InputIndAc - 1] = AcNames[number - 1]
        except ValueError:
            print("Нужны цифры")
        except IndexError:
            print("Таких не имеем")
        except:
            print("Что то пошло не так")

print(*AcRelatives)


'''
10) создать связный список, как словарь, где ключ - имя родственника,
 а значение - индекс следующего имени по исходному списку, 
 (к этому моменту, отсортированному в обратном алфавитном порядке)
 упорядоченному по их (родственников) годам рождения,
 исходный список при этом должен остаться неизменным
'''
dict = {}
for i in range(len(Relatives)):
        dict[Relatives[i]] = Relatives[(i+1)%len(Relatives)]
print("Задание 10",dict)
'''
#11 
 написать функцию-генератор:
    0)аликвотной последовательности;
    1)последовательности Сильвестра;
    2)числа трибоначчи;
    3)числа Леонардо. 
    Свой вариант определяется как number = len("ФИО") * len (family_names) % 4;
'''
I_am = ["КречинАлександрСергеевич"]
print ("11) ","My number: ", len(I_am) * len (Relatives) % 4)

def alikvotnposl(x, y):
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
    return alikvotnposl(sum, x)
z = int(input("Введите число: "))
print("Аликвотная последовательность числа", z, ":")
alikvotnposl(z, z)
