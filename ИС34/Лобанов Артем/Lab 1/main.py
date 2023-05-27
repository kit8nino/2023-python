import random, datetime
"""
Исходные данные:
    свои ФИО, число, месяц, год рождения в виде кортежа;
    предметы в школьном аттестате (не меньше 14), как словарь из названия и оценки (можно мокать);
    имена (только) ближайших (до двоюродных включительно) родственников в списке;
    имя, которое вы бы дали своей домашней пушистой киве (строка).
"""
FIO_date = ("Лобанов Артем Сергеевич", 28, 4, 2004)
SchoolMarks = {
        "Русский язык": random.randint(2,5),
        "Литература": random.randint(2,5),
        "Английский язык": random.randint(2,5),
        "История": random.randint(2,5),
        "Обществознание": random.randint(2,5),
        "География": random.randint(2,5),
        "Математика": random.randint(2,5),
        "Информатика": random.randint(2,5),
        "Физика": random.randint(2,5),
        "Астрономия": random.randint(2,5),
        "Биология": random.randint(2,5),
        "Химия": random.randint(2,5),
        "Физическая культура": random.randint(2,5)
        } #я правда не знаю где мой аттестат и что там написано

Fml = ["Наталья","Сергей","Людмила","Василий","Михаил","Галина","Элла","Александр"]
Kiva = "Попугай"

#вывести среднюю оценку в аттестате;
print("средняя оценка ", sum(SchoolMarks.values())/len(SchoolMarks))

#вывести, исключив повторения, все различные имена среди своих родственников (включая свое);
print("различные имена ", *set(Fml+[FIO_date[0].split()[1]]))

#общая длина всех названий предметов;
print("общая длинна названий ", sum(len(sub) for sub in SchoolMarks.keys()))   

#уникальные буквы в названиях предметов;
print("уникальные буквы названий ", *set(letter for sub in SchoolMarks.keys() for letter in sub))

#имя вашей домашней пушистой кивы в бинарном виде;
print("бинарная кива ", ''.join(bin(letter_number)[2:] for letter_number in Kiva.encode('utf-8')))    

#отсортированный по алфавиту (в обратном порядке) список родственников;
print("икинневтсдор ", *sorted(Fml, reverse=True))

#количество дней от вашей даты рождения до текущей даты (должна быть всегда актуальной
print("Количество дней c днюхи меня ", (datetime.date.today()-datetime.date(FIO_date[3],FIO_date[2],FIO_date[1])).days,\

#FIFO очередь, в которую можно добавлять предметы по вводимому с клавиатуры индексу 
#(до команды остановки), после введения - вывести все
"\n Введите индекс предмета (от 0 до 4) или stop для остановки\n")
print("Очередь предметов ", *[["Лена","Вика","Вероника","Таня","Даня"][int(i)] for i in iter(input, 'stop') if i.isdigit() and int(i) in range(5)])

'''я сдаюсь'''
#по введеному индексу, поменять имя в отсортированном списке родственников на имя ацтекского правителя
#под номером, получаемым из вашей даты рождения: number = (day + month**2 + year) % 21 + 1;
ruler = ['Itzcoatl', 'Moctezuma I', 'Axayacatl', 'Tizoc', 'Ahuitzotl', 'Moctezuma II', 'Cuitláhuac', 'Cuauhtémoc', 'Acamapichtli', 'Huitzilihuitl', 'Chimalpopoca', 'Itzcoatl II', 'Ahuizotl', 'Totoquihuatzin', 'Moctezuma Xocoyotzin', 'Tlacaelel', 'Nezahualcoyotl', 'Maxtla', 'Tlacopan Tlayacan', 'Cacamatzin', 'Tezozomoc', 'Tlacateotl'][(FIO_date[1]+FIO_date[2]**2+FIO_date[3])%21+1] #-1?
while index:=input(f"введите индекс для замены (от 0 до {len(Fml)-1})\n"):
    if index.isdigit() and int(index) in range(len(Fml)):
        Fml[int(index)]=ruler
        break
    print("дурак?")
print("новая семья " ,*Fml)

#создать связный список, как словарь, где ключ - имя родственника, а значение - индекс следующего имени по исходному списку (к этому моменту, отсортированному в обратном алфавитном порядке), упорядоченному по их (родственников) годам рождения (года или создать отдельным списком, или просто держите их в уме при составлении связного -- оба варианта валидны), исходный список при этом должен остаться неизменным
'''хотя не так уж я и плох'''
births = [1970, 1980, 1965, 1975, 1978, 1955, 1963, 1983]
print("тот самый список ",\
{Fml[index]: index+1 if index != len(Fml)-1 else 0 for index, date in sorted(enumerate(births), key=lambda x: x[1])})

#написать функцию-генератор (cвой вариант определяется как number = len("ФИО") * len (family_names) % 4):
print("вариант ", len(FIO_date[0])*len(Fml)%4) #0

#аликвотной последовательности;
def alik(n: int):
    if type(n)!=int or n<=0:
        raise ValueError("тайлер дерден?")
    elif n!=1:
        yield n
        while (a:=[k for k in range(2,round(n**(1/2))+1) if n%k==0]) and (s:=sum(a+[n//k for k in a if n//k!=k])+1) and s!=n: 
            yield s
            n=s
    yield from (1,0)
print(*[i for i in alik(666)])
