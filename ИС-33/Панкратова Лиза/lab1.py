from datetime import datetime

myinfo = ("Панкратова Елизавета Дмитриевна", 27, 2, 2004)
subject = {
"Англ. яз." : 5,
"Биология" : 5,
"География" : 5,
"ИП" : 5,
"Информатика" : 5,
"История" : 5,
"Литература" : 5,
"Математика" : 5,
"ОБЖ" : 5,
"Обществознание" : 5,
"Родной рус. язык" : 5,
"Русский язык" : 5,
"Физика" : 5,
"Физкультура" : 5,
"Химия" : 5,
"История Нижегородского края" : 5,
}
brother = ["Алексей", "Николай", "Денис", "Максим", "Тимофей"]
name = "Жора"

def sred():
    print(sum(subject.values()) / len(subject))
sred()

def names():
    names = [myinfo[0][11:20]]+brother
    rod = set(names)
    print(rod)
names()

def dlin():
  total_subjects_length = sum(len(subject) for subject in subject.keys())
  print("Общая длина названий предметов:", total_subjects_length)
dlin()

def sym():
    unique_letters = set()
    for predmet in subject.keys():
        unique_letters.update(set(predmet.lower()))
    print("Уникальные буквы в названиях предметов:", unique_letters)
sym()

def kiwi():
    binary_name = "".join(format(ord(char), 'b') for char in name)
    print("Имя питомца в бинарном виде:", binary_name)
kiwi()

def sort_brother():
    brother.sort(reverse = True)
    print("Список родственников в обратном алфавитном порядке:",brother)
sort_brother()

def birth():
    today = datetime.today()
    birthday = datetime(myinfo[3], myinfo[2], myinfo[1])
    print((today - birthday).days)
birth()

def FIFO():
    FIFO = []
    while(True):
        x=input()
        if (x == "Stop"):
            break
        FIFO.append(x)
    print(FIFO)
FIFO()

def replace():
    x=int(input())
    brother[x] = "Huanitzin"
    print(brother)
replace()

def linked():
    linked_list = {}
    for i in range(len(brother)):
        linked_list[brother[i]] = brother[(i+1)%len(brother)]
    print(linked_list)
linked()

def aliquot(n):
    yield n
    while True:
        divisors = [i for i in range(1, n) if n % i == 0]
        next_num = sum(divisors)
        if next_num == n:
            break
        yield next_num
        n = next_num
print("Введите число для аликвотной последовательности: ")
num=int(input())
for i in aliquot(num):
    print(i)