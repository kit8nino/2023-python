from datetime import datetime

data = ("Кузнецов Никита Игоревич", 5, 6, 2004)
subject = {
"Англ. яз." : 5,
"Биология" : 5,
"География" : 4,
"ИП" : 5,
"Информатика" : 5,
"История" : 5,
"Литература" : 4,
"Математика" : 4,
"ОБЖ" : 5,
"Обществознание" : 4,
"Родной рус. язык" : 4,
"Русский язык" : 4,
"Физика" : 4,
"Физкультура" : 5,
"Химия" : 5,
}
relatives = ["Андрей", "Илья", "Яна", "Анастасия", "Илья"]
nickname = "Ральф"

def avarage():
    summ = 0
    for i in subject:
        summ += subject[i]
    summ /= len(subject)
    return summ

def unique_names():
    all_names = [data[0][9:16]]+relatives
    unique = set(all_names)
    return unique

def lenght():
    summ = 0
    for i in subject:
        summ += len(i)
    return summ

def unique_letters():
    unique = ""
    for i in subject:
        unique+=i
    unique_mas = set(unique)
    return unique_mas

def binar():
    binar = ' '.join(format(i, 'b') for i in bytearray(nickname, "utf-8"))
    return binar

def sort_relatives():
    relatives.sort(reverse = True)
    return relatives

def time():
    today = datetime.today()
    DR = datetime(data[3],data[2],data[1])
    return ((today - DR).days)

def FIFO():
    FIFO = []
    while(True):
        x=input()
        if (x == "Stop"):
            break
        FIFO.append(x)
    return FIFO

def replacement():
    x=int(input())
    relatives[x] = "Axayacatl"
    return relatives

def linked_list():
    linked_list = {}
    for i in range(len(relatives)):
        linked_list[relatives[i]] = relatives[(i+1)%len(relatives)]
    return linked_list

def aliquot_sequence(n):
        result = [n]
        while n > 1:
            divisors = [i for i in range(1, n) if n % i == 0]
            s = sum(divisors)
            result.append(s)
            n = s
        return result

number1 = (data[1] + data[2]**2 + data[3]) % 21 + 1
number2 = len("КузнецовНикитаИгоревич") * (len(relatives[0])+len(relatives[1])+len(relatives[2])+len(relatives[3])+len(relatives[4])) % 4

print("№1", avarage())
print("№2", unique_names())
print("№3", lenght())
print("№4", unique_letters())
print("№5", binar())
print("№6", sort_relatives())
print("№7", time())
print("№8", FIFO())
print("№9.1", "Номер, получаемый из нашей даты рождения: ", number1)
print("№9.2", replacement())
print("#10", linked_list())
print("№11.1", "Полученный номер моего варианта: ", number2)
print("Введите число для аликвотной последовательности: ")
num=int(input())
print("#11.2",aliquot_sequence(num))

