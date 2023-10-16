from fractions import Fraction
from os import rmdir

print(float(10))
print(float(10.4))
print(float('10.6'))
print(float(2 / 7))
# print(float('2/7'))
a = Fraction('2/7')
print(float(a))

print(0.1)
print(format(0.1, '.15f'))
print(format(0.1, '.25f'))
print(0.125)
print(1 / 8)
print(format(0.125, '.25f'))

a = 0.1 + 0.1 + 0.1
print(format(a, '.25f'))
b = 0.3
print(format(b, '.25f'))
print(a == b)
