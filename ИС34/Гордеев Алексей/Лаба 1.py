import datetime
import queue
FIO = ("Гордеев", "Алексей", "Александрович", 2004 ,7 ,15)
Eval = {"Русский": 5 ,"Математика": 4 ,"Литература": 5 ,"История": 5 ,
        "Информатика": 5 ,"География": 4 ,"Физра": 5 ,"Обществознание": 4 ,
        "Труды": 5 ,"ИЗО": 5 ,"Физика": 4 ,"Краевединение": 5 ,"Химия": 4 ,"Биология": 5}
Relat = ["Александр", "Ольга", "Иван", "Иван", "Семен", "Михаил", "Сергей","Лидия","Николай", "Алиса", "Макар","Алексей"]
Kiwi = "Барбос"

# Task 1
sumEval = sum(Eval.values()) 
l = len(Eval)
print("Task 1 ", "Answer: ", round(sumEval / l, 2))

# Task 2
p = len(set(Relat))
print("Task 2 ", "Answer: " , p)

#Task 3
d = list(Eval)
long = 0
for i in d:
    long += len(i)
print("Task 3 ","Answer: ", long) 

#Task 4

d = list(Eval)
b = 0
list1 = []
while b < len(Eval):
    list1 += list(d[b].lower())
    b += 1
print("Task 4 ", "Answer: ", (set(list1)))

#Task 5

bin_result = (' '.join(format(ord(c), 'b') for c in Kiwi))
print("Task 5 ","Answer: ", bin_result)

#Task 6
Sort_Relat = sorted(Relat, reverse = True)
print("Task 6", "Answer: ", Sort_Relat)

#Task 7

a = input('Сегодняшняя дата (гггг-мм-дд): ')
a = a.split('-')
today_date = datetime.date(int(a[0]),int(a[1]),int(a[2]))
my_birthday = datetime.date(int(FIO[3]),int(FIO[4]),int(FIO[5]))
passed = today_date - my_birthday
print("Task 7 ", "Answer: " , passed)

#Task 8

print("Task 8 ", "Вводите индекс (Если вы захотите вывести всё, введите 666) :")
Eval1 = list(Eval)
queue = []
indexes = []
while (b != 666 and b <= len(Eval)):
    b = int(input())
    if b != 666:
        indexes.append(b)
for i in indexes:
    queue.append(Eval1[i])
print(queue)

#Task 9

num = ((int(FIO[3]) + int(FIO[4])**2 + int(FIO[5])) % 21 + 1)
print("Task 9  Номер правителя: ", num)
print("Введите индекс, чье имя вы хотите заменить на имя правителя: ")

while (True):
    number = int(input())
    if (number >= 0 and number < len(Relat)):
        Relat[int(number)] = "Ahuitzotl"
    break
print("Answer: ", Relat)

#Task 10 

dictionary = {}
for i in range(len(Sort_Relat) - 1):
    dictionary[Sort_Relat[i]] = Sort_Relat[(i + 1)]
print("Task 10","Answer: " , dictionary)

#Task 11

My_FIO = ["ГордеевАлексейАлександрович"]
print ("Task 11 ","My number: ", len(My_FIO) * len (Relat) % 4)

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