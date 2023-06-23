from datetime import date
#исходные данные
dannye_tuple = ("Марганова Александра Сергеевна","14.06.2004")
attestat = {"Математика": 5, "Русский язык": 5, "Биология": 5, "География": 5, "Литература": 5, "Экономика": 5, "Право": 5, "Физика": 5, "Информатика": 5, "История": 5, "Обществознание": 5, "Химия": 5, "Экология": 5, "Физическая культура": 5}
family_names = ["Ирина", "Сергей", "Нина", "Вероника", "Светлана", "Артём", "Александра"]
koshka = "Sima"

#1
summa = sum(attestat.values())
srvalue = summa/(len(attestat))
print("Srednya ocenka v attestate:", srvalue)

#2
print("Imena(unique) rodstvennikov:", set(family_names))

#3
dlinaslov = 0
for i in attestat:
    for j in i:
        if (not j.isdigit()):
            dlinaslov +=1
print("Dlina nazv predmetov:", dlinaslov)

#4
uniquebukvi = []
for i in attestat:
    for j in i:
        uniquebukvi.append(j)
print("Unique bukvi v nazv predmetov: ", set(uniquebukvi))

#5
koshka_bin = ""
for i in koshka:
    koshka_bin = ''.join(format(ord(i), '08b'))
print("Binarnaya koshka: ", koshka_bin)

#7
today_date = date.today()
second_date = date(2004, 6, 14)
delta = today_date - second_date
print("Since birthday:", delta)

#6

print("Sorted family names: ", sorted(family_names, reverse = True))

#8
import queue
ochered = queue.Queue()
while ochered.empty():
    ochered.put(input())
print("FIFO:", ochered.get())

#9
name_pravitelya = number = (14 + 6**2 + 2004) % 21 + 1
print("Variant: ", name_pravitelya, "Huanitzin")

index = queue.Queue()
print("Vvedite index:")
while index.empty():
    index.put(int(input()))
family_names[index.get()] =  "Huanitzin"
print("New family names:", family_names)

#10

svyazny_spisok = {}
for i in range(len(family_names)):
    svyazny_spisok[family_names[i]] = family_names[(i+1) % len(family_names)]
print("Svyazny spisok:", svyazny_spisok)

#11
number = len("Марганова Александра Сергеевна") * len(family_names) % 4
print("Variant:", number)

def trib(n):
    a, b, c = 0, 0, 1
    for i in range(n):
        yield a
        a, b, c = b, c, a+b+c
print("Tribonachi:", list(trib(10)))

