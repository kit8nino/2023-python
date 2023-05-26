import math
import random

BIRTH_DAY = 10
BIRTH_MONTH = 2


def point_to_number(point: tuple) -> float:
    x, y = point
    return (x * 10) + y


def get_random_point():
    angle = random.uniform(0, 2 * math.pi)
    return (
        (BIRTH_DAY / BIRTH_MONTH) * math.cos(angle),
        (BIRTH_DAY / BIRTH_MONTH) * math.sin(angle)
    )


def shell_sort(array: list) -> list:
    n = len(array)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and (
            point_to_number(array[j - interval]) if type(array[j - interval]) is tuple else array[j - interval]) > (
            point_to_number(temp) if type(temp) is tuple else temp):
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2 ** k - 1
    return array


def selection_sort(array: list) -> list:
    for i in range(len(array) - 1):
        min_idx = i
        for idx in range(i + 1, len(array) - 1):
            if (point_to_number(array[idx]) if type(array[idx]) is tuple else array[idx]) < (
            point_to_number(array[min_idx]) if type(array[min_idx]) is tuple else array[min_idx]):
                min_idx = idx
        array[i], array[min_idx] = array[min_idx], array[i]
    return array


def merge(lst1: list, lst2: list) -> list:
    lst = []
    i = 0
    j = 0
    while i <= len(lst1) - 1 and j <= len(lst2) - 1:
        if lst1[i] < lst2[j]:
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1
    if i > len(lst1) - 1:
        while j <= len(lst2) - 1:
            lst.append(lst2[j])
            j += 1
    else:
        while i <= len(lst1) - 1:
            lst.append(lst1[i])
            i += 1
    return lst


def merge_sort(array: list) -> list:
    if len(array) == 1:
        return array
    mid = (len(array) - 1) // 2
    lst1 = merge_sort(array[:mid + 1])
    lst2 = merge_sort(array[mid + 1:])
    result = merge(lst1, lst2)
    return result


def couting_sort(array: list) -> list:
    i_lower_bound, upper_bound = min(array), max(array)
    lower_bound = i_lower_bound
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        array = [item + lb for item in array]
        lower_bound, upper_bound = min(array), max(array)

    counter_items = [0] * (upper_bound - lower_bound + 1)
    for item in array:
        counter_items[item - lower_bound] += 1
    pos = 0
    for idx, item in enumerate(counter_items):
        num = idx + lower_bound
        for i in range(item):
            array[pos] = num
            pos += 1
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        array = [item - lb for item in array]
    return array


if __name__ == '__main__':
    # print(random.sample(range(1, 18), 4))

    # 5 - Shellsort, сортировка Шелла;
    # 8 - selection sort, сортировка выбором;
    # 11 - Merge sort, сортировка слиянием;
    # 12 - Counting sort, сортировка подсчетом;

    integer_rand_list = [random.randint(0, 999999) for _ in range(999999)]
    float_rand_list = [random.uniform(-1, 1) for _ in range(999999)]
    points_list = [get_random_point() for _ in range(42000)]
    book_words = open('book.txt', 'r', encoding='UTF-8').read().split(sep=' ')

    with open('shell_sort.txt', 'w', encoding='UTF-8') as f:
        f.write(str(shell_sort(book_words)))

    with open('selection_sort.txt', 'w', encoding='UTF-8') as f:
        f.write(str(selection_sort(points_list)))

    with open('couting_sort.txt', 'w', encoding='UTF-8') as f:
        f.write(str(couting_sort(integer_rand_list)))

    with open('merge_sort.txt', 'w', encoding='UTF-8') as f:
        f.write(str(merge_sort(float_rand_list)))
