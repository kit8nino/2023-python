import datetime


dannyje = ("Emily Crow", 5, 12, 2001)
attestat = {
    "Олгебра": 4,
    "Гиомитрия": 4,
    "Летиротура": 4,
    "Рускый йазык": 2,
    "Исторея расии": 3,
    "Инглишь лангуаге": 5,
    "Физека": 4,
    "ыНФОРМАТЕКА": 5,
    "Изаброзитильное искуства": 5,
    "Мюзыка": 5,
    "Физичискоя кюльтюра": 4,
    "Гиогрофия": 4,
    "ТРУД": 5,
    "Икан0мека": 4
}
rodstvenniki = ["Emma", "Polina", "Elena", "Anna", "Anna", "Maria"]

imjaKivy = "Miša"

def main():
    #                                       #
    #   Выводим средний балл аттестата :)   #
    #                                       #
    print("Ex. 1")
    sr = 0
    for i in attestat:
        sr += attestat[i]
    sr /= len(attestat)
    print(round(sr, 2))

    #                                       #
    #   Выводим уникальные имена            #
    #   родственников :)                    #
    #                                       #
    print("Ex. 2")
    r2 = rodstvenniki + [dannyje[0][0:5]]
    endR = []
    for i in r2:
        clock = 0
        for j in r2:
            if (i == j):
                clock += 1
        if (clock == 1):
            endR += [i]
    print(endR)

    #                                       #
    #   Общая длина всех                    #
    #   названий предметов                  #
    #                                       #
    print("Ex. 3")
    summa = 0
    for i in attestat:
        summa += len(i)
    print(summa)

    #                                       #
    #   Уникальные буквы                    #
    #   в названиях предметов               #
    #                                       #
    print("Ex. 4")
    b2 = ""
    for i in attestat:
        b2 += i
    endB = []
    for i in b2:
        clock = 0
        for j in b2:
            if (i == j):
                clock += 1
        if (clock == 1):
            endB += [i]
    print(endB)

    #                                       #
    #   Имя пушистой кивы                   #
    #   в бинароном виде                    #
    #                                       #
    print("Ex. 5")
    bin = []
    dec = []
    for i in imjaKivy:
        dec += [int(i.encode("utf-8").hex(), 16)]
    for i in dec:
        b = []
        while True:
            if i < 1:
                break
            b += str(i % 2)
            i //= 2
        bin += ['']
        for j in range(len(b)):
            bin[len(bin)-1] += b[len(b)-j-1]
    print(bin)
    
    #                                       #
    #   Сортировка списка родственников     #
    #                                       #
    print("Ex. 6")
    r2 = rodstvenniki
    r2.sort(reverse=True)
    print(r2)

    #                                       #
    #   Количество дней от даты рождения    #
    #                                       #
    print("Ex. 7")
    now = datetime.datetime.today()
    MD = datetime.datetime(dannyje[3], dannyje[2], dannyje[1])
    print((now - MD).days, "дней")

    #                                       #
    #   FIFO очередь                        #
    #                                       #
    print("Ex. 8")
    FIFO = []
    while (True):
        a = input()
        if (a == "stop"):
            for i in range(len(FIFO)):
                print(FIFO.pop())
            break
        FIFO.append(a)

    #                                       #
    #   Ацтеки                              #
    #                                       #
    print("Ex. 9")
    print(r2)
    while (True):
        a = input()
        if (int(a) and int(a) >= 0 and int(a) < len(r2)):
            r2[int(a)] = "Axayacatl"
            break
    print(r2)







if __name__=="\x5f\x5f\x6d\x61\x69\x6e\x5f\x5f":import os;main()if os.path.basename(__file__)=="\x4c\x61\x62\x2e\x20\x31\x20\x2d\x20\x45\x72\x6f\x77\x2e\x70\x79" else 0;

input()
