me = ('Турков','Егор','Михайлович',24,6,2004)
lessons = {'Математика': 5, 'Биология': 5, 'Физика': 5, 'Химия': 5, 'География': 4, 'Литература': 4, 'Музыка': 5, 'ИЗО': 5, 'ОБЖ': 3, 'Физра': 5, 'История': 4, 'Экономика': 4, 'Право': 4, 'Экономика': 4, 'Информатика': 5}
relts = ['Ольга','Михаил','Егор','Евгений','Геннадий','Вера','Альбина','Роман','Мария','Дмитрий','Демьян','Мирон','Матвей']
pet_name = 'Августин'

#1
print (' №1')
mid_grades = round(sum(lessons.values())/len(lessons),1)
print (mid_grades)

#2
print (' №1')
for i in range(0, len(relts)):
  k = 0
  for n in range(0, i-1):
    if relts[i] == relts[n]:
        k= k+1
  if k==0:
      print(relts[i], ' ')

#3
print (' №3')
word = 0
for i in lessons:
   word = word + len(i)
print (word)

#4
print (' №4')
word = ' '
for i in lessons:
   word = word + i
print (word)
for a in range(len(word)):
  c = 0
  for b in range(a+1,len(word)):
    if word[a] == word[b]:
        c= c+1
  if c==0:
      print (word[a])

#5
print (' №5')
print (pet_name)
bin =' '.join(format(ord(x), 'b') for x in pet_name)
print (bin)

#6
print (' №6')
print (sorted(relts, reverse= True))

#7
print (' №7')
from datetime import date
now = date.today()
birth = date(me[5],me[4],me[3])
dif = now - birth
print(dif)

#8
print (' №8')
queue = ['Yi Sang', 'Faust', 'Don Quixote', 'Ryōshū', 'Meursault', 'Hong Lu', 'Heathcliff', 'Ishmael', 'Rodion', 'Sinclair', 'Outis', 'Gregor']
for i in range(len(queue)):
    print (queue[i], ': ', i)
FIFO = []
team = []
print ('Write index of sinner (you can get an index in tablet upward), what you want to appent in your team and write "-1" to stop appending.')
x = int
while x != -1:
        x = int(input("Write index: "))
        if x == -1:
            break
        else:
            team.append(queue[x])
print (team)

#9
print (' №9')
alt_relts_1 = sorted(relts, reverse= True)
number = (me[3] + me[4]**2 + me[5]) % 21 + 1;
print (number)
print ('The name of Aztec gov with this number:', number, ', is: Моктесума 1')
y = int(input("Write index of relative who you want to replace: "))
alt_relts_1[y] = 'Моктесума 1'
print (alt_relts_1)

#10
print (' №10')
dc_relts = {}
alt_relts_2 = sorted(relts, reverse= True)
for i in range(len(alt_relts_2)):
    dc_relts[alt_relts_2[i]] = alt_relts_2[(i+1) % len(alt_relts_2)]
print(dc_relts)

#11
print (' №11')
number = (len(me[0])+len(me[1])+len(me[2]))* len(relts) % 4
print (number)
print ('My variant is: ', number, ', an Aliquot Sequence')
x = int(input("Write first sequence member: "))
seq = []
seq.append(x)
import math
while x!= 0:
    sum = 0
    for i in range(1,x):
        if x%i == 0:
            sum = sum +i
    x = sum
    seq.append(sum)
print (seq)   
            
