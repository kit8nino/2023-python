import random
print((random.sample(range(1, 18), 4)))
# [2, 14, 7, 13]

# 1 Radix sort
s = [random.randint(0, 100000) for i in range(999999)]
max_r = len(str(max(s)))
for i in range(max_r):
    boxs = [[] for _ in range(10)]
    for num in s:
        find_out = (num // 10 ** i) % 10
        boxs[find_out].append(num)
    s = []
    for box in boxs:
        s.extend(box)

# 2 Bucket sort
List = [random.uniform(-1, 1) for _ in range(99999)]
k = len(List) // 3
if len(List) % k != 0:
    k += 1
buckets = [[] for _ in range(k)]
for num in List:
    index = hash(num) % k
    buckets[index].append(num)
for i in range(k):
    buckets[i].sort()
result = []
for i in range(k):
    result += buckets[i]
result.sort()

# 3 insertion sort
complex_num = []
for i in range(42000):
    x = random.uniform(-10/11, 10/11)
    y = random.uniform(-10/11, 10/11)
    z = complex(x, y).real
    complex_num.append(z)
for i in range(1, len(complex_num)):
    start = complex_num[i]
    abs_i = abs(complex_num[i])
    while i > 0 and abs(complex_num[i - 1]) > abs_i:
        complex_num[i] = complex_num[i - 1]
        i -= 1
    complex_num[i] = start
# 4 Bubble sort
with open('fragment.txt', 'r', encoding='utf-8') as f:
    words = []
    text = f.read()
    text = text.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "").replace("—", "").replace(
        "( )", "").replace(";", "")
    words = text.split()
    n = (len(words))
    for repeat in range(n - 1):
        for i in range(n - 1):
            if words[i] > words[i + 1]:
                words[i], words[i + 1] = words[i + 1], words[i]
