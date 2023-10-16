# mesela 3 parametresei olan bir fonksiypnu 2 parametre ile cagormaya calısıyor

from functools import partial


def my_func(a, b, c):
    print(a, b, c)


my_func(10, 20, 30)


def f(x, y):
    return my_func(10, x, y)


f(20, 30)
f(200, 300)

f = lambda x, y: my_func(10, x, y)
f(200, 300)

print('\n')

f = partial(my_func, 10)
f(20, 30)

f = partial(my_func, 10, 20)
f(30)

print('\n')


def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)


my_func(10, 20, 100, 200, k1='a', k2='b', k3=1000, k4=2000)

# fonksiyonun parametrelerini degistirme
def f(x, *vars, kw, **kwvars):
    return my_func(10, x, *vars, k1='a', k2=kw, **kwvars)


f(20, 100, 200, kw='b', k3=1000, k4=2000)

# fonksiyonun parametrelerini degistirme partial ile
f = partial(my_func, 10, k1='a')
f(20, 100, 200, k2='b', k3=1000, k4=2000)


print('\n')


def pow(base, exponant):
    return base**exponant


sq = partial(pow, 2)
print(sq(10))
print(sq(5))


def my_func(a, b):
    print(a, b)


a = [1, 2]
f = partial(my_func, a)
print(f(100))
a.append(3)
print(f(100))

print('\n')

origin = (0, 0)

l = [(1, 1), (0, 2), (-3, 2), (0, 0), (10, 10)]

dist2 = lambda p1, p2: (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

print(dist2((1, 1), origin))

print(sorted(l, key=lambda p: dist2(origin, p)))
