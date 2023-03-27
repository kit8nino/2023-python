data = tuple('Шульпина Полина Олеговна')
birthday=(2004,10,17)
subjects = {
'русский':5,
'литература':5,
'алгебра':5,
'физика':5,
'история':4,
'география':5,
'физкультура':5,
'химия':4,
'ОБЖ':5,
'обществознание':5,
'краеведение':5,
'биология':4,
'черчение':5,
'геометрия':5,
'астрономия':5,
'икт':5,
}
relatives=['Света','Олег','Артем','Валя','Паша','Коля','Люся','Маша','Женя']
cat=('Asya')
n=len(subjects.values())
mean_mark=0
for value in subjects.values():
    mean_mark +=value
average=mean_mark/len(subjects)
print('1.среднее значение:',average)
relatives.append('Полина')
not_repeat=[]
for elem in relatives:
    if not elem in not_repeat:
        not_repeat.append(elem)
print('2.различные имена родственников',not_repeat)
relatives.sort()
sum=''
for elem in subjects.keys():
    sum+=elem
    unletters = []
    letter = []
    for i in sum:
        letter.append(i.lower())
        for n in range(len(letter) - 1):
            for t in letter[n]:
                if not t in unletters:
                    unletters.append(t)
print('3.общая длина всех названий предметов:',len(sum)-1)
print('4.уникальные буквы в названиях предметов',unletters)
bin_result = ''.join(format(x,'08b') for x in bytearray(cat,'utf-8'))
print('5.имя кивы в бинарном виде:',bin_result)
print('6.отсортированный в обратном порядке список родственников:',relatives[::-1])
from datetime import date
birth = date(2004,10,17)
today=date.today()
difference_days=today-birth
print('7.Количество дней от вашей даты рождения до текущей даты:',difference_days)
rulers=['Теноч','Acamapichtli','Уицилиуитль','Чимальпопока',
    'Сихуитль Темок','Ицкоатль','Монтесума I','Атотоцтли','Аксайакатль','Тизок',
    'Ауицотль','Моктесума II','Cuitláhuac','Cuauhtémoc','Тлакотзин','Мотельчюхцин',
    'Сочиквентзин','Хуаницин','Теуэцквитицин','Чечетцин','Cipac']


number=(17+17**2+2004)%21+1
print('введите индекс от 0 до 9')
i=int(input())
relatives[i]=rulers[number]
print('9.Итог:',relatives[i])





