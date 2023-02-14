from math import factorial

print('hi!')

fact = {1}
N = 50
temp = 1
for i in range(1, N):
    temp *= i
    fact.add(temp)

# print(sorted(fact))

fact_right_version = [factorial(x) for x in range(N)]
# комментировать так
"""
или так
если надо несколько строк сразу
"""
# print(fact_right_version)

# fact_div2 = [fact_r_v[i]/2 for i in range(len(fact_r_v))]
fact_div2 = [x / 2 for x in fact_right_version]

N = int(input('Enter factorials counter: '))
print(N)

v = [int(x) for x in input('count to 20: ').split(', ')]
print(v)

for i in v:
    print('Element ', i, ' is good')

print(*v) # <- распакованный список, просто значения, разделенные пробелами
