################## CONSTRUCTORS AND BASES - LECTURE ##################


import encodings
import fractions
from email.mime import base
from math import trunc
from string import digits
from unicodedata import digit

a = int(1.99)
print(int(3.99))
b = True
c = False
print(int(b))
print(int(c))

print(int("123"))
a = int("1010", 2)
print(a)

x = int("222")
print(x)
print(type(x))

print(int("A12F", 16))
print(int("534", 8))
print(int("A", 11))
# reverse process bin()

print(bin(10))
print(oct(10))
print(hex(10))

a = 0b1010
print(int(a))
print(int("232", 4))

print("#############################################")

# base change algorithm


def base_change(number, base):
    if base < 2:
        raise ValueError('Base b must be >= 2')
    if number < 0:
        raise ValueError('Number n must be >= 0')
    if number == 0:
        return [0]

    digits = []
    while number > 0:
        m = number % base
        number = number // base
        digits.insert(0, m)
    return digits


print(base_change(232, 5))
print(base_change(1485, 16))
print("#############################################")
################## CONSTRUCTORS AND BASES - CODING ##################
print("#############################################")
# help(int)
print(int(10))
print(int(10.9))
print(int(-10.9))


a = fractions.Fraction(10, 3)
print(a)
print(float(a))
print(int(a))

print(int("12345"))
print(int("101", 2))
print(int("FF", 16))
print(int("ff", 16))
# print(int("B", 11)) # hata veriyor, 2 tabanına degeri girmek gibi
print(bin(10))
print(oct(10))
print(hex(10))
print("#############################################")
a = int("101", 2)
print(a)
b = 0b101
print(b)
print("#############################################")


def from_base10(n, b):
    if b < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError('Number n must be >= 0')
    if n == 0:
        return [0]

    digits = []
    while n > 0:
        # m = n % b
        # n = n // b
        # m, n = n % b, n // b
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits


a = from_base10(10, 2)
print(a)

a = from_base10(255, 16)
print(a)


print("#############################################")


def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError('digit_map is not large enough to encode the digits')
    encoding = ''
    for d in digits:
        encoding += digit_map[d]
    return encoding


print(encode([15, 13], '0123456789ABCDEF'))
print("#############################################")


def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError('Base b must be between 2 and 36')
    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding


e = rebase_from10(4315, 16)
print(e)
print(int(e, base=16))

f = rebase_from10(10, 2)
print(f)
print(int(f, base=2))

n = rebase_from10(-314, 2)
print(n)
print(int(n, base=2))

n = rebase_from10(314, 2)
print(n)
print(int(n, base=2))
