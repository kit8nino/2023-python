import math
import random
import re
from random import randint

'''
print(random.sample(range(1, 18), 4)) # 
'''

# Сортировка расчёской - что-то типа сортировки пузырьком. Мы используем шаг прохода > 1. 
# Рассматриваем пары элементов, находящихся на максимальном расстоянии друг от друга. 
# После каждого прохода void уменьшается. 
def hairbrush(mass):
    void = len(mass)
    swaps = True
    while void > 1 or swaps:
        void = max(1, int(void / 1.25))  
        swaps = False
        for i in range(len(mass) - void):
            j = i + void
            if mass[i] > mass[j]:
                mass[i], mass[j] = mass[j], mass[i]
                swaps = True
    return mass

# Крайне глупая сортировка. При нахождении неотсортированной пары соседей происходит обмен
# и возврат на шаг назад
def gnome(mass):
	i, size = 1, len(mass)
	while i < size:
		if mass[i - 1] <= mass[i]:
			i += 1
		else:
			mass[i - 1], mass[i] = mass[i], mass[i - 1]
			if i > 1:
				i -= 1
	return mass


def counting_sort(mass):
   itog = [0] * len(mass)
   low = min(mass)
   high = max(mass)
   count_array = [0 for i in range(low, high+1)]
   for i in mass:
      count_array[i-low] += 1
   for j in range(1, len(count_array)):
      count_array[j] += count_array[j-1]
   for k in reversed(mass):
      itog[count_array[k-low] - 1] = k
      count_array[k-low] -= 1
   return itog

# Большее толкаем вверх
def BubbleSort(mass):
    sh = len(mass)
    for i in range(sh-1):
       for j in range(sh-2, i-1 ,-1):
          if mass[j+1] < mass[j]:
             mass[j], mass[j+1] = mass[j+1], mass[j]
    return mass


# Список из чисел 0 -- 9,99999 * 10^5
list_one = []
for i in range(999999): 
    list_one.append(randint(0, 9))

list_one_sorted = counting_sort(list_one)
print("Первое задание, список случайных чисел, сортировокой подсчёта: \n", list_one_sorted)


# Cписок из 99999 случайных вещественных чисел в диапазоне [-1, 1]
list_two = []
while (len(list_two) < 99999):
    list_two.append(round(random.uniform(-1, 1),5)) #5 знаков

list_two_sorted = hairbrush(list_two)
print("Второе задание, список случайных чисел [-1; 1], сортировокой расчёски: \n", list_two_sorted)

# 42000 разных точки комплексной плоскости, лежащие в пределах окружности радиуса r
list_three = []
birth_day = 13
birth_month = 5
r = birth_day / birth_month
for i in range(42000):
    p = random.uniform(0, 2 * math.pi)
    x = r * math.cos(p)
    y = r * math.sin(p)
    list_three.append(complex(x, y).real)

list_three_sorted = gnome(list_three)
print("Третье задание, точки комплексной плоскости в пределах окружности: \n", list_three_sorted)

# Отрывок из книги (любой, на свой выбор) не менее 10000 слов, разбитый в список по словам.
with open('lez.txt', 'r', encoding = 'utf-8') as f:
    txt = f.read().lower() # Достаём текст
no_sym_text = re.findall(r'\b\w+\b', txt) # Убираем из текста символы
list_four = txt.split() # Создаём строку со всеми словами

list_four_sorted = BubbleSort(list_four)
print("Четвертое задание, отрывок из кники, список по словам: \n", list_four_sorted)

