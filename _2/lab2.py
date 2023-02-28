# lab-2 from 2023-python


def foo(name, x=1, y='boo!', z=10):
    print(f'x: {x}, y: {y}, z: {z}')
    print(f'Hello, {name}!')
    return x * 2, y * 3, z * 4


def power_of(x, n=2, d=1):
    return x**(n/d)


def foo_func(foo, val):
    try:
        res = []
        for e in val:
            res.append(foo(e))
        print('try success')
        return res
    except:
        print('Exception!')
        return foo(val)


def f_of_func(val, foo=power_of):
    return foo(n=val)


def foo_fl(a, *names, **kwargs):
    print(f'a: {a}')
    if kwargs['mul']:
        for n in names:
            print(n)
    if kwargs['single']:
        print(*names)
