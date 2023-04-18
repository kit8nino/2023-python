from datetime import date
import datetime


FIOdata = ("Перевезенцев", "Александр", "Сергеевич", 7, 11, 2004)
o = {
    "Алгебра": 5,
    "Биология": 4,
    "Геометрия": 4,
    "Русский язык": 4,
    "Литература": 4,
    "История": 4,
    "Английский язык": 5,
    "Физика": 4,
    "Информатика": 5,
    "ИЗО": 5,
    "География": 5,
    "Физическая культура": 5,
    "Химия": 5,
    "Музыка": 5,
    "Экономика": 4,

}

rodnie = ["Светлана","Сергей","Дмитрий","Светлана","Степан"]

Mykiva = "Лолик"

# 1 task
def main():
    s = 0
    for i in o:
        s = s + o[i]
    s = s / len(o)
    return s
print ("Number 1:", main())

# 2 task
rodnie.append(FIOdata[1])
unik1 = list(set(rodnie))
print("Number 2:",  unik1)

# 3 task
def d():
    sum = 0
    for i in o:
        sum = sum + len(i)
    return sum
print("Number 3:", d())

# 4 task
unik = " "
for i in o:
     unik += i
unik_bukvi = []
for i in unik:
    n = 0
    for j in unik:
        if i == j:
            n += 1
    if n == 1:
        unik_bukvi += [i]
print("Number 4:", unik_bukvi)


# 5 task
mykivi= " ".join(format(ord(i), "b") for i in Mykiva)
print("Number 5:", mykivi)

# 6 task
r = rodnie
r.sort(reverse = True)
print("Number 6:", r)

# 7 task
datarojdeniya = datetime.date(int(FIOdata[5]), int(FIOdata[4]), int(FIOdata[3]))
dataseychas = datetime.date.today()
q = datarojdeniya - dataseychas
rezult = str(q)
print("Number 7:", rezult[1:].split()[0])

# 8 task
FIFO = []
print("Number 8:")
while (True):
    c = input()
    if (c == "Стоп"):
        for i in range(len(FIFO)):
            print(FIFO.pop())
        break
    FIFO.append(c)

# 9 task    
number = ((int(FIOdata[3]) + int(FIOdata[4])**2 + int(FIOdata[5])) % 21 + 1)
print("Number 9:", number)

# 10 task
while (True):
    index = int(input())
    if index >= 0 and index < len(r):
        r[int(index)] = "Itzcoatl"
    break
print(r)

slovar = {}
for i in range(len(rodnie)):
        slovar[rodnie[i]] = rodnie[(i + 1) % len(rodnie)]
print("Number 10:", slovar)

# 11 task
number = len("ПеревезенцевАлександрСергеевич") * (len(rodnie[0])+len(rodnie[1])+len(rodnie[2])+len(rodnie[3]))%4
print("Number 11:"," Мой Вариант  = ",number)

def alposled(n):
    yield n
    while True:
        divisors = [i for i in range(1, n) if n % i == 0]
        next_num = sum(divisors)
        if next_num == n:
            break
        yield next_num
        n = next_num
    
num = int(input("Введите число, последовательность: "))
for i in alposled(num):
    print(i)








    



