import datetime


dannyje = ("Emily Crow", 5, 12, 2001)
attestat = {
    "Алгебра": 4,
    "Геометрия": 4,
    "Литература": 4,
    "Русский язык": 2,
    "История России": 3,
    "Английский язык": 5,
    "Физика": 4,
    "Информатика": 5,
    "ИЗО": 5,
    "Музыка": 5,
    "Физическая культура": 4,
    "География": 4,
    "Труд": 5,
    "Экономика": 4
}
rodstvenniki = ["Emma", "Polina", "Elena", "Anna", "Anna", "Maria"]

imjaKivy = "Miša"

def main():
    #                                       #
    #   Выводим средний балл аттестата :)   #
    #                                       #
    print("Ex. 1")
    print("-------------------------------------------------------")
    sr = 0
    for i in attestat:
        sr += attestat[i]
    sr /= len(attestat)
    print(round(sr, 2))

    #                                       #
    #   Выводим имена            #
    #   родственников без повторов :)                    #
    #                                       #
    print("\nEx. 2")
    print("-------------------------------------------------------")

    r2 = rodstvenniki + [dannyje[0][0:5]]
    endR = []

    for i in range(len(r2)):
        if r2[i] not in endR:
            endR += [r2[i]]
    print(endR)

    #                                       #
    #   Общая длина всех                    #
    #   названий предметов                  #
    #                                       #
    print("\nEx. 3")
    print("-------------------------------------------------------")
    summa = 0
    for i in attestat:
        summa += len(i)
    print(summa)

    #                                       #
    #   Уникальные буквы                    #
    #   в названиях предметов               #
    #                                       #
    print("\nEx. 4")
    print("-------------------------------------------------------")
    b2 = ""
    for i in attestat:
        b2 += i
    endB = []
    for i in b2:
        if i not in endB:
            endB += [i]
            
    print(endB)

    #                                       #
    #   Имя пушистой кивы                   #
    #   в бинароном виде                    #
    #                                       #
    print("\nEx. 5")
    print("-------------------------------------------------------")
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
    print("\nEx. 6")
    print("-------------------------------------------------------")
    r2 = rodstvenniki
    r2.sort(reverse=True)
    print(r2)

    #                                       #
    #   Количество дней от даты рождения    #
    #                                       #
    print("\nEx. 7")
    print("-------------------------------------------------------")
    now = datetime.datetime.today()
    MD = datetime.datetime(dannyje[3], dannyje[2], dannyje[1])
    print((now - MD).days, "дней")

    #                                       #
    #   FIFO очередь                        #
    #                                       #
    print("\nEx. 8")
    print("-------------------------------------------------------")
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
    print("\nEx. 9")
    print("-------------------------------------------------------")
    print(r2)
    while (True):
        a = input()
        if (int(a) and int(a) >= 0 and int(a) < len(r2)):
            r2[int(a)] = "Axayacatl"
            break
    print(r2)







if __name__=="\x5f\x5f\x6d\x61\x69\x6e\x5f\x5f":import os;main()if os.path.basename(__file__)=="\x4c\x61\x62\x2e\x20\x31\x20\x2d\x20\x45\x72\x6f\x77\x2e\x70\x79" else 0;

input()