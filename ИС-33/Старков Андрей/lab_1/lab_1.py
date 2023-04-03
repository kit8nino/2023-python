import datetime

#Данные
dataPers=('Старков','Андрей','Владимирович',28,5,2004)
certSub={'Русский язык':4,'Математика':3,'Физика':4,'Биология':5,'Химия':1,'История':2,'Обществознание':5, 'Астрономия':3,'ОБЖ':4,'Литература':2,'Английский язык':5,'Физическая культура':1,'Чертение':5,'Краеведение':3}
namRel=['Владимир','Наталья','Павел','Екатерина','Анастасия','Ксения','Галина','Николай','Дмитрий','Анна','Зинаида','Виктор']
kivaName='Ватрушка'
number = len(dataPers[0]+dataPers[1]+dataPers[2])*len("".join(namRel))%4
#Первое задание
def first(certGrad):
    sum_ = 0;
    for value in certGrad.values():
        sum_ = sum_ + value
    return sum_/len(certGrad)

print("1. Средняя оценка в аттестате:", first(certSub),"\n")

#Второе задание
def second(person,relat):
    uniq_names = []
    uniq_names.append(person[1])
    for i in range(len(relat)):
        uniq_names.append(relat[i])
    return list(set(uniq_names))

print("2. Уникальные имена родственников(включая своё):", second(dataPers,namRel),"\n")

#Третье задание
def third(certNames):
    namesSub = ""
    for names in certNames.keys():
        namesSub+=names
    return len(namesSub.replace(" ", ""))

print("3. Общая длина всех названий предметов:", third(certSub),"\n")

#Четвёртое задание
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

#Пятое задание
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

#Шестое задание
def sixth(namRel):
    sortNamesRev = namRel
    sortNamesRev.sort(reverse=True)
    return sortNamesRev

print("6. Отсортированный список родственниов по алфавиту в обратном порядке:", sixth(namRel),"\n")

#Седьмое задание
def seventh(dataPers):
    brDate = datetime.datetime(dataPers[5],dataPers[4],dataPers[3])
    nowDate = datetime.datetime.now()
    return (nowDate - brDate).days

print("7. Дней от дня рождения до текущей даты:", seventh(dataPers),"\n")

#Восьмое задание
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
        
#Девятое задание
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

#Десятое задание
def tenth():#Данная функция не является универсальной и используется в частном порядке!
    svList={"Павел":3,"Николай":7,"Наталья":6,"Ксения":11,"Зинаида":1,"Екатерина":0,"Дмитрий":5,"Галина":10,"Владимир":2,"Виктор":4,"Анна":8,"Анастасия":9}
    return svList

print("10. Связный циклический список:",tenth(),"\n")

#Одинадцатое задание
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

