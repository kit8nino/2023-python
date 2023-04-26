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

def sum_3_4(x, three=3, four=4):
    return x + three + four

print(sum_3_4(5), sum_3_4(6, three=7), sum_3_4(7, four=2, three=1))

fib_list = [1]


def get_fibb(fib_index):
    global N, v, fib_list
    fib_one = 1
    fib_two = 1
    print('N is ', N)
    for i in range(fib_index-1):
        fib_one, fib_two = fib_two, fib_two + fib_one
        yield fib_two


fib_number = int(input('Enter index (fibbonacci): '))
for e in get_fibb(fib_number):
    print(e)

while fib_number != -1:
    fib_number = int(input('Enter index (fibbonacci): '))
    print(f'Fib {fib_number} is {get_fibb(fib_number)}')
