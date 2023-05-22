imya = ('Rylova Ekaterina Dmitrievna' , 13, 5, 2004) # Say my name
predmeti = {'русский': 5, 
            'литература': 5, 
            'математика': 4, # Алгебра и геометрия, да-да 
            'история': 5, 
            'физика': 5, 
            'обществознание': 4, 
            'информатика': 5, 
            'география': 5, 
            'ОБЖ': 5, 
            'английский': 4, 
            'немецкий': 5, 
            'родной язык': 5, 
            'родная литература': 5, 
            'физ-ра': 5} # At school hated history and english teacher
rodstvenniki = ['Dima', 'Nadya', 'Matvei', 'Diana', 'Ivan', 'Elena', 'Slava', 'Kostya', 'Vadim', 'Tanya', 'Elena'] # I love them <3
kiva = 'limon' # Have you seen that "kiwa hirsuta"(wiki name)? God, she's scary don't scare me much more

# 1 # 1 # 1 # 1 # 1 # 1 # 1 # 1 # 1 # 1
my_best_diplom = (sum(predmeti.values())) / len(predmeti)
print('\nСредняя оценка аттестата: ',  my_best_diplom)


# 2 # 2 # 2 # 2 # 2 # 2 # 2 # 2 # 2 # 2 
a = rodstvenniki.copy()
a.append('Katya')
a_unique = set(a)
print('\nУникальные имена: ', a_unique)


# 3 # 3 # 3 # 3 # 3 # 3 # 3 # 3 # 3 # 3 
predmeti_bez_chifer = list(predmeti) 
long = 0
for i in predmeti_bez_chifer:
    long = long + len(i) 
print('\nДлинна названий предметов: ', long+6) # Из-за скоращения физкультуры, их на 6 меньше, просто добавим


# 4 # 4 # 4 # 4 # 4 # 4 # 4 # 4 # 4 # 4
aga = ''
for bykva in predmeti_bez_chifer: # Преобразуем список в строку 
    aga = aga + bykva

unique = list(set(aga)) # Достаём уникальные символы из строки
print('\nУникальные буквы: ', unique)


# 5 # 5 # 5 # 5 # 5 # 5 # 5 # 5 # 5 # 5 https://pythonpip.ru/examples/stroka-v-dvoichnyy-kod-v-python
vbit = ''.join(format(x,'08b') for x in bytearray(kiva,'utf-8'))
print('\nИмя кивы в 1001: ', vbit)


# 6 # 6 # 6 # 6 # 6 # 6 # 6 # 6 # 6 # 6
obratno = rodstvenniki.copy()
obratno.sort(reverse=True)
print('\nZ->A список родственников: ', obratno)


# 7 # 7 # 7 # 7 # 7 # 7 # 7 # 7 # 7 # 7 https://stackoverflow.com/questions/151199/how-to-calculate-number-of-days-between-two-given-dates
import datetime  

den_rojdeniya = datetime.datetime(imya[3],imya[2],imya[1])
period = datetime.datetime.today() - den_rojdeniya
print('\nЯ родилась: ', period.days, ' дней назад.')


# 8 # 8 # 8 # 8 # 8 # 8 # 8 # 8 # 8 # 8
# Создаём список, каждому элементу придаём индекс.
# Вводим индекс с клавиатуры, как завершим ввод, то выводим наши индексы (предметы списка).
# Мысли вслух.

spisok = ['Жмурки - КлоуКома', 'Красота - OM.', 'Космос - Алекша Нович', 'Bless My Blues - Ilya Fisherman']
FIFO = list(spisok)
index = []
print('\nВведите индекс от 1 до 4. Чтобы закончить и вывести FIFO, пишите stop.\nCписок: ', spisok)
while True:
    yo = input()
    if yo == 'stop':
        break
    index.append(yo)

for i in index:
    print('Ваш FIFO: ', FIFO[int(i)-1]) # int != str !!!!!!!!!!!!!!! 

# 9 # 9 # 9 # 9 # 9 # 9 # 9 # 9 # 9 # 9
achtek = ['Tenoch', 'Acamapichtli', 'Huitzilihuitl', 'Chimalpopoca', 'Xihuitl Temoc', 'Xihuitl Temoc', 'Moctezuma I', 'Atotoztli', 'Atotoztli', 'Tizoc', 'Ahuitzotl', 'Moctezuma II', 'Cuitláhuac', 'Cuauhtémoc', 'Cuauhtémoc', 'Tlacotzin', 'Tlacotzin', 'Xochiquentzin', 'Huanitzin', 'Tehuetzquititzin', 'Tehuetzquititzin', 'Tehuetzquititzin']
num = (imya[1] + imya[2]**2 + imya[3])%21+1
achtek_rod = obratno.copy()
while True:
    index_num= int(input('\nВведите номер имени в списке(список имён выше): ')) - 1
    if index_num >= 0:
        achtek_rod[int(index_num)] = achtek[int(num)]
    break
print('Списочек с правителем: ', achtek_rod)

# 10 # 10 # 10 # 10 # 10 # 10 # 10 # 10 # 10
obratno_da =[['Vadim', 1977], ['Tanya', 1994], ['Slava', 2007], ['Nadya', 1985], ['Matvei', 2014], ['Kostya', 1974], ['Ivan', 1969], ['Elena', 1994], ['Elena', 1982], ['Dima', 1999], ['Diana', 2001]]
# Не понятно задание. "словарь, где ключ - имя родственника, а значение - индекс следующего имени по исходному списку"??????
# Отсортирую по годам, не знаю больше =(

def sorting(obratno_da):
    return obratno_da[1]
obratno_da.sort(key=sorting)
print('\nСписок людей с датой рождения по возрастанию: ', obratno_da)


# 11 # 11 # 11 # 11 # 11 # 11 # 11 # 11 # 11
new_num = len(imya)*len(rodstvenniki)%4 # 0


print('\nМой вариант:', new_num, '- аликвотная последовательность')
chisl = int(input("Введите число для alik последовательности: "))
def alik(a, b): 
    s = 0
    if a == b:
        print(a)
    if a == 1:
        print(0)
        return 0
    else:
        for i in range(1, a-1):
            if a % i==0:
                s += i
    print(s)
    return alik(s, a)

print("Аликвотная последовательность числа", chisl, ":")
alik(chisl, chisl)