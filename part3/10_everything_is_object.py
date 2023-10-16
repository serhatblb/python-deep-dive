import re

a = 10
print(type(a))

b = int(10)
print(type(b))

c = int()
c = int('1010', base=2)
print(c)


def square(x):
    return x**2


print(type(square))

f = square

print(id(square))

print(id(f))

print(f is square)
print(square(2))
print(f(2))


def kup(a):
    return a**3


def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return kup


f = select_function(1)

print(f is square)
print(f(2))

f = select_function(2)
print(f is kup)
print(f(2))


print(select_function(2)(3))  # 3 un kupunu calıstırıyor. fonksiyona once 2 girdigi icin kupu seciyor


def exec_function(fn, n):
    return fn(n)


print(exec_function(kup, 3))
print(exec_function(square, 3))
