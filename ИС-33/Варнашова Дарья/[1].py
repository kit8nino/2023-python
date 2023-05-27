import datetime

#Данные
dataPers=('Варнашова','Дарья','Александровна',4,2,2004)
certSub={'Русский язык':4,'Математика':4,'Физика':4,'Биология':5,'Химия':4,'История':5,'Обществознание':4, 'Астрономия':4,'ОБЖ':5,'Литература':5,'Английский язык':4,'Физическая культура':5,'Чертение':5,'Краеведение':4}
namRel=['Дарья','Александр','Евгения','Иван','Лидия','Валентина','Анастасия','Пётр','Сергей','Мария']
kivaName='Ники'
number = len(dataPers[0]+dataPers[1]+dataPers[2])*len("".join(namRel))%4
#1 задание
def first(certGrad):
    sum_ = 0;
    for value in certGrad.values():
        sum_ = sum_ + value
    return sum_/len(certGrad)

print("1. Средняя оценка в аттестате:", first(certSub),"\n")

#2 задание
def second(person,relat):
    uniq_names = []
    uniq_names.append(person[1])
    for i in range(len(relat)):
        uniq_names.append(relat[i])
    return list(set(uniq_names))

print("2. Уникальные имена родственников(включая своё):", second(dataPers,namRel),"\n")

#3 задание
def third(certNames):
    namesSub = ""
    for names in certNames.keys():
        namesSub+=names
    return len(namesSub.replace(" ", ""))

print("3. Общая длина всех названий предметов:", third(certSub),"\n")

#4 задание
def fourth(certNames):
    uniqLetters = []
    for names in certNames.keys():
        name = ""
        nameLower=""
        list_ = []
        nameLower = names.lower()
        for i in range(len(names)):
            if nameLower[i]==" ":
                continue
            else:
                list_.append(nameLower[i])
        name = ", ".join(set(list_))
        uniqLetters.append(name)
    return uniqLetters

print("4. Уникальные буквы в названиях предметов:", fourth(certSub),"\n")

#5 задание
print("5. ")
def fifth(kivaName):
    while 1:
       key = input("Выберите кодировку, которой будет соответствовать бинарный код: 'un' - Unicode; 'ut' - UTF-8:")
       if key == "un":
            return ' '.join(format(ord(c), 'b') for c in kivaName)
       elif key == "ut":
            return ' '.join(format(c, 'b') for c in bytearray(kivaName, "utf-8"))
       else:
            print("Неверный ключ! Попробуйте снова.\n")
            continue

print("Имя домашней пушистой кивы в бинарном виде:", fifth(kivaName),"\n")

#6 задание
def sixth(namRel):
    sortNamesRev = namRel
    sortNamesRev.sort(reverse=True)
    return sortNamesRev

print("6. Отсортированный список родственниов по алфавиту в обратном порядке:", sixth(namRel),"\n")

#7 задание
def seventh(dataPers):
    brDate = datetime.datetime(dataPers[5],dataPers[4],dataPers[3])
    nowDate = datetime.datetime.now()
    return (nowDate - brDate).days

print("7. Дней от дня рождения до текущей даты:", seventh(dataPers),"\n")

#8 задание
print("8. ")
def eighth(certSub):
    subs = [ x for x in certSub.keys()]
    listSub = []
    while 1:
        key = input(f"Введите индекс предмета от 0 до {len(subs)-1} для добавления в очередь(стоп ключ 'exit'):")
        try:
            if key == "exit":
                return listSub
            elif int(key)>=0 and int(key)<len(subs):
                listSub.append(subs[int(key)])
                print(f"Добавлен элемент с индексом [{key}]: {subs[int(key)]}\n")
            else:
                print("Введён не верный ключ!\n")
        except Exception:
            print("Введён не верный ключ!\n")

print("Ваш список предметов:", eighth(certSub),"\n")

#9 задание
print("9. ")
def ninth(dataPers, namRel):
    number = (dataPers[3] + dataPers[4]**2 + dataPers[5]) % 21 + 1
    rules = ["Tenoch","Acamapichtli","Huitzilihuitl","Chimalpopoca","Xihuitl Temoc","Itzcoatl","Moctezuma I","Atotoztli","Axayacatl","Tizoc","Ahuitzotl","Moctezuma II","Cuitláhuac","Cuauhtémoc","Tlacotzin","Motelchiuhtzin","Xochiquentzin","Huanitzin","Tehuetzquititzin","Cecetzin","Cipac"]
    sortListRel = sixth(namRel)
    while 1:
        key = input(f"Введите индекс имени от 0 до {len(sortListRel)-1} для изменения его на имя ацтекского правителя {rules[number - 1]}:")
        try:
            if int(key)>=0 and int(key)<len(rules):
                sortListRel[int(key)] = rules[number - 1]
                return sortListRel
            else:
                print("Введён не верный ключ!\n")
        except Exception:
            print("Введён не верный ключ!\n")

print("Новый список:",ninth(dataPers, namRel),"\n")

#10 задание
def tenth():#Данная функция не является универсальной и используется в частном порядке!
    svList={"Сергей":9,"Пётр":8,"Мария":0,"Лидия":5,"Иван":4,"Евгения":3,"Дарья":1,"Валентина":6,"Анастасия":7,"Александр":2}
    return svList

print("10. Связный циклический список:",tenth(),"\n")

#11 задание
print("11. По формуле было получено число", number, ", что соответствует последовательности Сильвестера.\n")
def eleventh():#Данная функция не является универсальной и используется в частном порядке!
    k=int(input("Введите индекс последовательности:"))
    def sylvester(n):
        product = 1
        for k in range(n):
            product *= sylvester(k)
        return product + 1
    for n in range(k+1):
        yield sylvester(n)

print([count for count in eleventh()])
