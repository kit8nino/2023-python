from datetime import datetime
data = ("Глушенков Андрей Владимирович", 25, 8, 2004)
predmeti = {
"Алгебра" : 4,
"Биология" : 4,
"География" : 4,
"Геометрия" : 4,
"Ин.яз (англ.)" : 4,
"Информатика" : 4,
"История России": 4,
"Литература" : 4,
"ОБЖ": 5,
"Обществознание" : 4,
"Русский язык" : 4,
"Физ.культура" : 5
}
rodstveniki = ["Светлана", "Владимир", "Екатерина", "Анастасия", "Юлия", "Алексей", "Александр", "Владимир", "Валентина", "Дмитрий"]
nickname = "Рафаэль"
n1 = (data[1] + data[2]**2 + data[3]) % 21 + 1
summ=0
for i in range(len(rodstveniki)):
    summ+=len(rodstveniki[i])
n2 = len("ГлушенковАндрейВладимирович") * summ % 4
def sred():
    summ = 0
    for i in predmeti:
        summ += predmeti[i]
    summ /= len(predmeti)
    return summ
print(sred())
def unicalnie_name():
    all_names = [data[0][10:16]]+rodstveniki
    unique = set(all_names)
    return unique
print(unicalnie_name())
def dlina():
    summ = 0
    for i in predmeti:
        summ += len(i)
    return summ
print(dlina())
def unicalnie_bykvi():
    unique = ""
    for i in predmeti:
        unique+=i
    unique_mas = set(unique)
    return unique_mas
print(unicalnie_bykvi())
def binar():
    binar = ' '.join(format(i, 'b') for i in bytearray(nickname, "utf-8"))
    return binar
print(binar())
def sort_rodstveniki():
    rodstveniki.sort(reverse = True)
    return rodstveniki
print(sort_rodstveniki())
def time():
    today = datetime.today()
    DR = datetime(data[3],data[2],data[1])
    return ((today - DR).days)
print(time())
def FIFO():
    FIFO = []
    while(True):
        x=input()
        if (x == "Стоп"):
            break
        FIFO.append(x)
    return FIFO
print("Команда остановки - Стоп")
print(FIFO())
def replacement():
    x=int(input())
    rodstveniki[x] = "Tlacotzin"
    return rodstveniki
print("Ответ : ",replacement())
def linked_list():
    linked_list = {}
    for i in range(len(rodstveniki)):
        linked_list[rodstveniki[i]] = rodstveniki[(i+1)%len(rodstveniki)]
    return linked_list
print(linked_list())
def tribonacci(n):
    a, b, c = 0, 1, 1
    count = 0
    while count < n:
        yield a
        a, b, c = b, c, a + b + c
        count += 1
n = int(input("Введите количество чисел последовательности трибоначчи: "))
for x in tribonacci(n):
    print(x)







