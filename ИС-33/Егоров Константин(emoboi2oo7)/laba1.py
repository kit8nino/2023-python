

fio = ('Egorov', 'Konstantin', 'Aleksandrovich', 5, 5, 2004)
marks = {
    'matematika': 4,
    'angl yaz': 3,
    'rus yaz': 5,
    'fiz-ra': 3,
    'literatura': 5,
    'ritorika': 5,
     'biologiya': 6,
    'himia': 6,
    'fizika': 3,
    'astranomiya': 4,
    'informatika': 4,
    'vseobsh istoriya': 4,
    'istoriya Rossii': 5,
    'ekonomika': 3}
rodstvenniki = ['Elena', 'Aleksandr', 'Andrey', 'Sergey', 'Vladimir', 'Vladimir']
name_of_kiwi = 'Balbes'


#zadanie 1
def medium_mark():

    medium = 0
    for i in marks:
        medium += marks[i]
    medium /= len(marks)
    return medium
print ("zadanie 1", medium_mark())

#zadanie 2
rodstvenniki.append(fio[1])
unik = set(rodstvenniki)
print("zadanie 2",  unik)

#zadanie 3
def dlina_of_predmeti():
    summa = 0
    for i in marks:
        summa += len(i)
    return summa
print("zadanie 3", dlina_of_predmeti())

#zadanie 4
unikl = []
for i in marks:
    unikl += i
unikl_bukvi = set(unikl)
print("zadanie 4", unikl_bukvi)

#zadanie 5
bin_name__of_kiwi = " ".join(format(ord(i), "b") for i in name_of_kiwi)
print("zadanie 5", bin_name__of_kiwi)

#zadanie 6
r = rodstvenniki
r.sort(reverse = True)
print("zadanie 6", r)


#zadanie 7
import datetime
dr = datetime.date(int(fio[5]), int(fio[4]), int(fio[3]))
today = datetime.date.today()
q = today - dr
rezult = str(q)
print("zadanie 7", rezult.split()[0])


#zadanie 8
FIFO=[]
print("zadanie 8")
while (True):
    c=input("vvedite: ")
    if (c=="stop"):
        for i in range(len(FIFO)):
            print(FIFO.pop())
        break
    FIFO.append(c)

#zadanie 9
number = ((int(fio[3]) + int(fio[4])**2 + int(fio[5])) % 21 + 1)
print("zadanie 9", number)
name_of_imp = 'Tehuetzquititzin'
x = int(input('Vvedite indeks'))
if (x > len(rodstvenniki)-1 or x < 0):
    print('etot indeks nekorrekten')
else:
    rodstvenniki[x] = name_of_imp
    print(rodstvenniki)

#zadanie 10
lst = []
for i in range(len(r)):
    ls = [r[i], i+1]
    lst.append(ls)
    ls = []
print(lst)

#zadanie 11
number = len(fio)*len(rodstvenniki)%4
print("zadanie 11 variant", number)

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

print("zadanie 11 Silvestr")
for i in gen(6):
    print(i, end = " ")





























































