from cmath import pi
from functools import reduce

l = [5, 8, 6, 10, 9]
print(min(l))
print(max(l))
print(sum(l))
print(any(l))
print(all(l))

l = [0, '', None, 100]
result = bool(0) or bool('') or bool(None) or bool(100)
print(bool(0))
print(bool(0) or bool(''))
print(bool(0) or bool('') or bool(None))
print(bool(0) or bool('') or bool(None) or bool(100))

s = [1, 3, 5, 6]

reduce = lambda x, y: x * y, s
print(reduce)

print('\n')
print('################################# CODE #################################')
print('\n')

l = [5, 8, 6, 10, 9]

_max = lambda x, y: x if x > y else y
print(_max(3, 4))
print(_max(10, 2))


def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result


print(max_sequence(l))


_min = lambda x, y: x if x < y else y


def min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result


print(min_sequence(l))

_add = lambda x, y: x + y


def add_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _add(result, x)
    return result


print(add_sequence(l))


def _reduce(function, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = function(result, x)
    return result


print(_reduce(_max, l))
print(_reduce(_min, l))
print(_reduce(_add, l))


# print(reduce(_max, {1, 2, 3, 4, 5}))
print('\n')

print(min(l))
print(min({1, 2, 3, 4, 5}))
print(max(l))
print(sum(l))
print(sum({1, 2, 3, 4, 5}))

print('\n')

s = {True, 1, 0, None}
print(all(s))
s2 = {True, 1, 's'}
print(all(s2))

print(bool(True) and bool(1) and bool('s'))
print(bool(True) and bool(1) and bool(0) and bool(None))

print(any(s))
print(any(s2))

s3 = {False, 0, '', None}
print(any(s3))

# reduce(lambda a, b: bool(a) and bool(b), s)

# reduce(lambda a, b: bool(a) and bool(b), s2)

l = [5, 8, 6, 10, 9]
# 5 * 8 * 6 * 10 * 9

# print(reduce(lambda a, b: a * b, l))


def fact(n):
    return 1 if n < 2 else n * fact(n - 1)


print(fact(5))
