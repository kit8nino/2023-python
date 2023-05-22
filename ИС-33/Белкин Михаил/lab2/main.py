import random
import math
zadan1 = list(range(1000000)) #список целых чисел от 0 до 999999

random99999 = [random.uniform(-1, 1) for _ in range(99999)] #список из 99999 случайных вещественных чисел в диапазоне [-1, 1]

points = []
for i in range(42000):
    r = 3 / 11
    theta = random.uniform(0, 2 * math.pi)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    point = complex(x, y)
    points.append(point)                      #42000 разных точки комплексной плоскости, лежащие в пределах окружности

    with open('kniga.txt', 'r') as f:   #отрывок из книги
        content = f.read()



#сортировка Шелла
print("сортировка Шелла \n")
def Shell(zadan1):
    gap = len(zadan1) // 2
    while gap > 0:
        for i in range(gap, len(zadan1)):
            temp = zadan1[i]
            j = i
            while j >= gap and zadan1[j - gap] > temp:
                zadan1[j] = zadan1[j - gap]
                j -= gap
            zadan1[j] = temp
        gap //= 2
    return zadan1

sorted = Shell(zadan1)
print(sorted, "\n")

#гномья сортировка
print("гномья сортировка \n")
def gnome(random99999):
    i, size = 1, len(random99999)

    while i < size:
        if i == 0 or random99999[i - 1] <= random99999[i]:
            i += 1
        else:
            random99999[i], random99999[i - 1] = random99999[i - 1], random99999[i]
            i -= 1

    return random99999

sorted_arr = gnome(random99999)
print(sorted_arr, "\n")



#сортировка вставкой
print("сортировка вставкой \n")


for i in range(1, len(points)):
    temp = points[i]
    j = i - 1
    while j >= 0 and abs(temp) < abs(points[j]):
        points[j + 1] = points[j]
        j -= 1
    points[j + 1] = temp
for point in points:
    print(point)

#сортировка блочная (карманная)
print("сортировка блочная (карманная) \n")

# разбиение содержимого на слова и добавление в список
words = content.split()

# функция для слияния двух списков в отсортированный список
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

# функция для блочной сортировки списка слов
def block_sort(words):
    if len(words) <= 1:
        return words
    else:
        mid = len(words) // 2
        left = block_sort(words[:mid])
        right = block_sort(words[mid:])
        return merge(left, right)

# вызов функции блочной сортировки и вывод отсортированного списка слов
sorted_words = block_sort(words)
print(sorted_words)




print("[5, 7, 4, 13]")