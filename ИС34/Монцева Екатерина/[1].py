my_inform = tuple(("Монцева Екатерина Дмитриевна", "20", "02", "2004"))
my_marks = {
    'Русский язык': 5,
    'Математика': 5,
    'Физика': 5,
    'Литература': 5,
    'Биология': 5,
    'Информатика': 5,
    'Химия': 5,
    'Астрономиия': 5,
    'История': 5,
    'Обществознание': 5,
    'География': 5,
    'Физическая культура': 5,
    'Английский язык': 5,
    'Краеведение': 5,
    'Истрия России': 5,
    'Родной язык': 5,
    'Задачи в математике': 5}
name_family = ['Ирина', 'Дмитрий', 'Валентина',
               'Валентин', 'Юрий', 'Виктория', 'Оксана',
               'Андрей', 'Роман', 'Виктория', 'Евгения', 'Алексей',
               'Юрий', 'Роман', 'Антонина', 'Надежда', 'Людмила']
my_soft_kiva = "Симона"

all = 0
mid_mark = 0
for subject, mark in my_marks.items():
    all += mark
    mid_mark = all/len(my_marks)
print('1. Средняя оценка в аттестате:', mid_mark, '\n' )
mod_name_family = name_family.copy()
mod_name_family.append('Екатерина')
unique_name_family = []
for x in mod_name_family:
  if not x in unique_name_family:
      unique_name_family.append(x)
print('2. Уникальные имена в списке, включая своё:',unique_name_family,'\n' )
letters_coun = 0
letters = []
for key, value in my_marks.items():
    letters.append(key)
    for x in range(len(letters)-1):
        length = len(letters[x])
        letters_coun += length
        unique_letters = []
letter = []
for i in letters:
    letter.append(i.lower())
    for m in range(len(letter)-1):
        for t in letter[m]:
            if not t in unique_letters:
                unique_letters.append(t)

print('3. Общая длина всех названий предметов:', letters_coun, '\n')

print('4. Уникальные буквы в аттестате:', unique_letters, '\n')

bin_name = ''.join(format(ord(x), '08b') for x in my_soft_kiva)
print('5. Имя моей доамашней кивы в бинарном виде:', bin_name, '\n')

print ('6. Список родственников в обратном алфавитном порядке:', sorted(name_family, key=str.lower, reverse = True,),'\n')

from datetime import date
my_birthday = date(2004, 2, 20)
nowaday = date.today()
count_day = nowaday - my_birthday
print ('7. Кол-во дней от моего дня рождения до актуальной даты:', count_day, '\n')
print ('8. FIFO-очередь со стоп-словом "end":' )
FIFO_que = []
word = "end"
while True:
    list = input('Введите значение:')
    if list == word:
        for x in range(len(FIFO_que)):
            print(FIFO_que.pop(),end=" ")
        break
    FIFO_que.append(list)

name_atetecs = ['Теноч', 'Acamapichtli', 'Уицилиуитль', 'Чимальпопока', 'Сихуитль Темок',
                'Ицкоатль', 'Монтесума I', 'Атотоцтли', 'Аксайакатль', 'Тизок', 'Ауицотль',
                'Моктесума II', 'Cuitlahuac', 'Cuauhtemoc', 'Тлакотзин', 'Мотельчюхцин', 'Хочиквентзин']
def change(i,A):
    number = (20 + 2 ** 2 + 2004) % 21 + 1
    A[i] = name_atetecs[number]
    return print ("9. Результат:", A,'\n')


not_alfa_name_family = sorted(name_family, key=str.lower, reverse = True)
z = int(input('\n Введите индекс для замены имени от 0 до 15: '))
change(z, not_alfa_name_family)

unique_name_family1= sorted(unique_name_family, key=str.lower, reverse = True)

text = {}
for x in range(len(unique_name_family1)-1):
    text[unique_name_family1[x]] = unique_name_family1[x+1]
print('10. Новый словарь:', text, '\n')

variant = len("Монцева Екатерина Дмитриевна") * len(name_family) % 4
print('Мой номер варианта для 11 задания:', variant)
from math import sqrt

def Summa(m):
    sum = 0
    for x in range(1, int(sqrt(m)) + 1):
        if m % x == 0:
            if m // x == x:
                sum += x
            else:
                sum += x
                sum += m // x
    return sum - m

def printAliquot(m):
    print(m, end=" ")
    slog = set()
    slog.add(m)
    while m > 0:
        m = Summa(m)
        nextt = 0
        if m in slog:
            print("Повторите с:", m)
            break
        print(m, end=" ")
        slog.add(m)
if __name__ == "__main__":
    t = int(input('Введите число для аликвотной последовательности: '))
    print('11. Аликвотная последовательность: ', end="")
    printAliquot(t)
