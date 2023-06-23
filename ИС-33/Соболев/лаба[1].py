from datetime import datetime

data = ("Соболев Дмитрий Сергеевич", 19, 6, 2004)                                        
atestat = {
"Русский язык" : 4,
"Математика" : 5,
"Литература" : 5,
"Информатика" : 4,
"Физика" : 4,
"История" : 4,
"Английский язык" : 4,
"Индивидуальный проект" : 5,
"Черчение" : 4,
"Физическая культура" : 5
}
rodstveniki = ["Альбина", "Евгений", "Даниил", "Марина", "Кирилл"]
nick_Kivi = "Варя"


def atestat1():
    sum1 = 0
    for i in atestat:
        sum1 += atestat[i]
    sum1 /= len(atestat)
    return sum1
print("1:", atestat1())

def imena():
    imena1 = [data[0][9:16]]+rodstveniki
    unique = set(imena1)
    return unique
print("2:", imena())

def lenght():
    sum2 = 0
    for i in atestat:
        sum2 += len(i)
    return sum2
print("3:", lenght())

def unique_letters():
    unique = ""
    for i in atestat:
        unique+=i
    unique_mas = set(unique)
    return unique_mas
print("4:", unique_letters())

def Kiva():
    Kiva = ' '.join(format(i, 'b') for i in bytearray(nick_Kivi, "utf-8"))
    return Kiva
print("5:", Kiva())

def sort_rodstveniki():
    rodstveniki.sort(reverse = True)
    return rodstveniki
print("6:", sort_rodstveniki())

def time():
    today = datetime.today()
    DR = datetime(data[3],data[2],data[1])
    return ((today - DR).days)
print("8:", time())

print("Введите список:")
FIFO = []
while(True):
    sos = input()
    if sos == "stop":
        break
    FIFO.append(sos)
print("8:", FIFO)


print("Введите индекс для замены:")
pop = int(input())
list1[pop] = "Itzcoatl"
print("9.1:", list1)

n = (my_tuple[1] + my_tuple[2]**2 + my_tuple[3]) % 21 + 1 
print("9.2", n, "Itzcoatl")


list2 = {}
for i in range(len(list1)):
    list2[my_list[i]] = list2[(i+1) % len(list2)]
print("10:", list2)


sum3 = 0
for i in range(len(list1)):
    sum3 = sum3 + len(list1[i])
number = len("СоболевДмитрийСергеевич") * sum3 % 4
print("Варинат ", number)


num = 10
delitel = []
alikvot_pos = [10]
while num >= 1:
    for i in range(1, num):
        if num == 1:
            alikvot_pos.append(0)
        elif num % i == 0:
            delitel.append(i)
    sum4 = sum(delitel)
    alikvot_pos.append(sum4)
    num = sum4
    delitel = []
print("11:", alikvot_pos)
