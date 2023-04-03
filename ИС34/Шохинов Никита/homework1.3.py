my_data = ("Шохинов", "Никита", "Сергеевич","10", "1", "2004")
my_rating = {"Русский": 4,"Математика": 5,"Литература": 4,"История": 5,
             "Информатика": 5,"Обществознание": 4,"Биология": 5,"География": 5,
             "Английский": 4,"ОБЖ": 5,"Физкультура": 5,"Физика": 5,
             "Химия": 5,"Изо": 5,}
my_family = ["Оля","Сергей","Варя","Лиза","Женя","Андрей","Оля","Сергей","Савелий",
             "Леша","Валя","Нина","Коля","Костя"]
my_pet = "Буся"

from datetime import datetime # Библиотека для 7 задания

# №1

Average_rating = (sum(my_rating.values()))/(len(my_rating))
print("№ 1\n", "Средняя оценка: ",Average_rating)

# №2

Unique_name_family = list(set(my_family))
print("№ 2\n", Unique_name_family)

# №3

size_dictionary = 0
list_my_rating = list(my_rating)
for i in list_my_rating:
    size_dictionary += len(i)
print("№ 3\n", size_dictionary)

# №4

list_my_rating = list(my_rating)
letter = []
for i in range(14):
    letter += list(list_my_rating[i].lower())
Unique_letter = set(letter)
print("№ 4\n", Unique_letter)

# №5

bin_name_of_pet = " ".join(map(bin, bytearray(my_pet, "utf-8")))
print("№ 5\n", bin_name_of_pet)

# №6

sorted_my_family = sorted(my_family, reverse=True)
print("№ 6\n", sorted_my_family)

# №7

print("№ 7\n", "Вы прожили: {} дней".format((datetime.now() - datetime(day=int(my_data[3]), month=int(my_data[4]), year=int(my_data[5]))).days))

# №8
print("№ 8\n", "Введите индексы до 14, что бы остановить ввод напишите \"Stop\": ")
Filter = None
index_array = []
while True:
    Filter = input()
    if Filter == "Stop":
        break
    index_array.append(Filter)
for i in index_array:
    print(list_my_rating[int(i)-1])

# №9 надо раскоментировать #6

number_9 = (10 + 1**2 + 2004) % 21 + 1
print("№ 9\n","Вариант: ",number_9)
print("Введите индекс: ")
index_9 = int(input())-1
sorted_my_family[index_9] = "Cipac"
print(sorted_my_family)

# №10 надо раскоментировать #6

linked_list = {}
for i in range(len(sorted_my_family)-1):
    linked_list[sorted_my_family[i]] = sorted_my_family[i+1]
print("№ 10\n", linked_list)

# №11

number_11 = len("Шохинов Никита Сергеевич") * len(my_family) % 4
print("№ 11\n",number_11,"\nВведите число:")
# 0

def gener_alik(number):
    print(number)
    sum_of_dividers = 0
    for i in range(number - 1, 0, -1):
        if (number % i == 0):
            sum_of_dividers += i
    number = sum_of_dividers
    if number == 0:
        return "Done"
    return gener_alik(number)
print(gener_alik(int(input())))
