fio = ('Skvorcov', 'Danila', 'Vadimovich', 19, 3, 2004)
marks = {
    'matematika': 3,
    'angl yaz': 4,
    'rus yaz': 2,
    'fiz-ra': 6,
    'literatura': 3,
    'ritorika': 4,
     'biologiya': 4,
    'himia': 4,
    'fizika': 3,
    'astranomiya': 4,
    'informatika': 3,
    'vseobsh istoriya': 4,
    'istoriya Rossii': 5,
    'ekonomika': 3}
rodstvenniki = ['Vadim', 'Anna', 'Polina', 'Andrey', 'Kuzya', 'Vladimir']
name_of_kiwi = 'xuy' #китаец:/


#задние 1
def medium_mark():

    medium = 0
    for i in marks:
        medium += marks[i]
    medium /= len(marks)
    return medium
print ("задание 1", medium_mark())

#задание 2
rodstvenniki.append(fio[1])
unik = set(rodstvenniki)
print("задание 2",  unik)

#задание 3
def dlina_of_predmeti():
    summa = 0
    for i in marks:
        summa += len(i)
    return summa
print("задание 3", dlina_of_predmeti())

#задание 4
unikl = []
for i in marks:
    unikl += i
unikl_bukvi = set(unikl)
print("задание 4", unikl_bukvi)

#задание 5
bin_name__of_kiwi = " ".join(format(ord(i), "b") for i in name_of_kiwi)
print("задание 5", bin_name__of_kiwi)

#задание 6
r = rodstvenniki
r.sort(reverse = True)
print("задание 6", r)


#задание 7
import datetime
dr = datetime.date(int(fio[5]), int(fio[4]), int(fio[3]))
today = datetime.date.today()
q = today - dr
rezult = str(q)
print("задание 7", rezult.split()[0])


#задание 8
FIFO=[]
print("задание 8")
while (True):
    c=input("введите: ")
    if (c=="хватит"):
        for i in range(len(FIFO)):
            print(FIFO.pop())
        break
    FIFO.append(c)

#задание 9
number = ((int(fio[3]) + int(fio[4])**2 + int(fio[5])) % 21 + 1)
print("задание 9", number)
name_of_imp = 'Xochiquentzin'
x = int(input('Введите индекс'))
if (x > len(rodstvenniki)-1 or x < 0):
    print('введите другой индекс')
else:
    rodstvenniki[x] = name_of_imp
    print(rodstvenniki)

#задание 10
lst = []
for i in range(len(r)):
    ls = [r[i], i+1]
    lst.append(ls)
    ls = []
print(lst)

#задание 11
number = len(fio)*len(rodstvenniki)%4
print("задание 11 вариант", number)

def gen(n):
    a = 1
    current = 2
    hz = 1000000007

    c = 1
    while c <= n:
        yield current
        current = ((a % hz) * (current % hz)) % hz
        a = current
        current = (current + 1) % hz
        c += 1

print("задание 11 Сильвестр")
for i in gen(6):
    print(i, end = " ")
