from datetime import datetime

FioDate = ("Амерханов Линар Андреевич", 17, 2, 2005)
MarkSchool = {
    "Русский язык": 5,
    "Родной язык": 5,
    "Литература": 5,
    "Английский язык": 4,
    "История": 5,
    "Обществознание": 5,
    "География": 5,
    "Математика": 5,
    "Информатика": 5,
    "Физика": 5,
    "Астрономия": 5,
    "Биология": 5,
    "Химия": 5,
    "Физическая культура": 5
}
Relatives = ["Фания", "Сергей", "Ляйсян", "Андрей", "Камиль", "Румия", "Рамиль"]
KivaName = "Шмоня"

# 1 Вывести среднюю оценку в аттестате

print("1) Средняя оценка в аттестате:", round(sum(MarkSchool.values()) / len(MarkSchool), 2))


# 2 вывести уникальные имена среди своих родственников включая свое

UniqueRelativesMyName = Relatives.copy()
UniqueRelativesMyName.append(FioDate[0].split(" ")[1])
print("2) Уникальные имена:", *set(UniqueRelativesMyName))

# 3 общая длина всех названий предметов
length = 0
Allcharacters = []
for i in MarkSchool.keys():
    length += int(len(i))
    for z in i:
        if z != " ":
            Allcharacters.append(z.lower())
        continue
print("3) Длина всех названий предметов:", length)

# 4 уникальные буквы в названиях предметов
print("4) Уникальные букавки:", *set(Allcharacters))

# 5 имя вашей домашней пушистой кивы в бинарном виде
print("5) Имя кивы:\n\t", ''.join(format(x,'08b') for x in bytearray(KivaName,'utf-8')))
#https://pythonpip.ru/examples/stroka-v-dvoichnyy-kod-v-python

# 6 отсортированный по алфавиту (в обратном порядке) список родственников
RelativesSORT = Relatives.copy()
RelativesSORT.sort(reverse=True)
print("6) Список родственников в обрат. алфавит порядке :\n\t", *RelativesSORT)
# 7 количество дней от вашей даты рождения до текущей даты (должна быть всегда актуальной)

print('7) Кол-во дней от даты рождения: {}'.format((datetime.now() - datetime(day=int(FioDate[1]), month=int(FioDate[2]), year=int(FioDate[2]))).days))
# https://www.cyberforum.ru/python-tasks/thread3016562.html

# 8 FIFO очередь, в которую можно добавлять предметы по вводимому с клавиатуры индексу
# (до команды остановки), после введения - вывести все


Alk = ["Виски", "Водка", "Абсент", "Бренди", "Пиво", "Сидр", "Чача", "Текила", "Шнапс", "Ром"]
FIFO = []
for AlkIND in range(len(Alk)):
    print(Alk[AlkIND], ':', (len(max(Alk,key = len))  - len(Alk[AlkIND])) * " ", AlkIND)
print("Введите индекс, того что хотите добавить в очередь \n Чтобы остановиться введите -1")
AlkPers = []
InputIND = int
while InputIND != -1:
    try:
        InputIND = int(input("Введите: "))
        if InputIND == -1:
            break
        if InputIND <= -1:
            raise IndexError
        AlkPers.append(Alk[InputIND])
    except ValueError:
        print("Циферки вводи!")
    except IndexError:
           print("Нет такого ¯\_(ツ)_/¯")
print("8) FIFO:", *AlkPers)


# 9 по введеному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя
# (Wiki Badge) под номером, получаемым из вашей даты рождения: number = (day + month**2 + year) % 21 + 1
AcNames = ("Tenoch", "Acamapichtli", "Huitzilihuitl", "Huitzilihuitl", "Xihuitl Temoc", "Itzcoatl", "Moctezuma I", "Atotoztli", "Axayacatl", "Tizoc", "Ahuitzotl", "Moctezuma II", "Cuitláhuac", "Cuauhtémoc", "Tlacotzin", "Motelchiuhtzin", "Xochiquentzin")
number = (FioDate[1] + FioDate[2]**2 + FioDate[3]) % 21 + 1
AcRelatives = RelativesSORT.copy()
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
            print("Циферки вводить надо было!")
        except IndexError:
            print("Нет такого ¯\_(ツ)_/¯, уходим, ребята")
        except:
            print("Ты что-то сделал не так(")

print(*AcRelatives)


'''
10) создать связный список, как словарь, где ключ - имя родственника,
 а значение - индекс следующего имени по исходному списку, 
 (к этому моменту, отсортированному в обратном алфавитном порядке)
 упорядоченному по их (родственников) годам рождения,
 исходный список при этом должен остаться неизменным
'''
Rel10 = {} #ХЗ ЧЕ ТУТ ДЕЛАТЬ, НАВЕРНОЕ ТАК
for i in range(len(RelativesSORT)):
        Rel10[RelativesSORT[i]] = RelativesSORT[(i+1) % len(RelativesSORT)]

print("10)", Rel10)


'''
#11 
 написать функцию-генератор:

    1)аликвотной последовательности;
    2)последовательности Сильвестра;
    3)числа трибоначчи;
    4)числа Леонардо. Свой вариант определяется как number = len("ФИО") * len (family_names) % 4;
первое, второе и третье числа Трибоначчи равны единице;
каждое следующее число Трибоначчи равно сумме трёх предыдущих.
'''
def Tribon(n):
    TribonMass = [1, 1, 1]
    for TribonI in range(n - 3):
        TribonMass.append(sum(TribonMass[-3:]))
    print(*TribonMass)

print("Функция-генератор номер", len(FioDate[0]) * len(Relatives) % 4, "\n\t Числа трибоначчи")
try:
    Tribon(int(input("Введите до какого числа n последовательности выводить числа: ")))
except:
    print("Ну нет так нет")


