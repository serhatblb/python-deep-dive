import imp
import math
from math import sqrt

s = [1, 2, 3]

print(len(s))


print(sqrt(4))


print(math.pi)
print(math.exp(1))

##################################################


def function_1():
    print('running function_1')


print(type(function_1))
print(function_1)
print(function_1())


def function_2(a=int, b=int):
    return a * b


print(function_2(2, 3))
print(function_2('a', 3))  # char
print(function_2([1, 2], 3))  # list

##################################################


def function_3():
    return function_4()


def function_4():
    return 'running function_4'


print(function_3())

my_func = function_4
print(my_func())

# lambda

lambda x: x**2

fn1 = lambda x: x**2
print(fn1(2))
