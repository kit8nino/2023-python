import random
import math
#print(random.sample(range(1,18),4))
#выдало 1-сортировка перемешиванием, 12-сортировка подсчетом, 13-блочная (карманная) сортировка, 15-least significant digit

#список целых чисел от 0 до 999999
numbers = list(range(1000000))

#список из 99999 случайных вещественных чисел в диапазоне [-1, 1]
random_number = [random.uniform(-1, 1) for _ in range(99999)]

#42000 разных точки комплексной плоскости, лежащие в пределах окружности
r = 14 / 5
cir_point = []
for i in range(42000):
    angle = random.uniform(0, 2 * math.pi)
    x = r * math.cos(angle * i)
    y = r * math.sin(angle * i)
    cir_point.append(complex(x, y))

#отрывок из книги не менее 10000 слов
with open("Text.txt", encoding='utf-8') as textfile:
    text = textfile.read()
bookword = text.split()

#Сортировка подсчетом
def count_sort(arr):
    #Создадим словарь для подсчета количества каждого элемента
    count_dict = {}
    for i in arr:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    #Сотировка этого словаря
    sort_list = []
    for key, value in sorted(count_dict.items()):
     sort_list += [key] * value

    return sort_list
sort_list = count_sort(bookword)
print(sort_list)

#Сортировка перемешиванием
def check_dist(point):
    dist = abs(point.real) + abs(point.imag)
    return dist <= r
sorted_list = sorted(cir_point, key=lambda point: not check_dist(point))
print(sorted_list)
#Я что-то написал что работает и даже не знаю как проверить что оно работает правильно, так что буду молиться богу что все в порядке

#least significant digit
def lsd_sort(nums):
    #Определяем количество разрядов
    max_num = max(nums)
    num_dig = len(str(int(max_num))) if max_num > 0 else 1
    for i in range(num_dig):
        num_bucket = 10
        buckets = [[] for _ in range(num_bucket)]
        for num in nums:
            dig = (int(num // 10**i) % 10)
            buckets[dig].append(num)
        nums = [num for bucket in buckets for num in bucket]
    return nums
lsd_sorted = lsd_sort(random_number)
print(lsd_sorted)

#Блочная (карманная) сортировка
def bucket_sort(nums):
    #Определяем количество корзие
    num_bucket = 15
    max_dig = len(str(max(nums)))
    buckets = [[] for _ in range(num_bucket)]
    for dig in range(1, max_dig+1):
        for num in nums:
            bucket_index = (num // 10**(dig - 1)) % 10
            buckets[bucket_index].append(num)
        nums = []
        for bucket in buckets:
            nums.extend(bucket)
            bucket.clear()
        return nums
buck_sort = bucket_sort(numbers)
print(buck_sort)

#Молюсь всем богам чтоб все было правельно. Prayge
