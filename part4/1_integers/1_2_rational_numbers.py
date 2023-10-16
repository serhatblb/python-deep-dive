import math
from fractions import Fraction

a = Fraction(10, 3)
print(a)
b = Fraction(2, -3)
print(b)

print(a, b, a + b, a - b, a * b, a / b)

c = Fraction(0.75) == Fraction(3, 4)
print(c)
print(Fraction(1.375))
print(Fraction(0.3))

############### RATIONAL NUMBERS - CODING ##################

print(Fraction(1, 3))
print(Fraction(denominator=3, numerator=1))
a = Fraction(0.125)
print(Fraction(a))

print(Fraction('0.125'))
print(Fraction(1, 8))

print("#############################################")

x = Fraction(2, 3)
y = Fraction(3, 4)
print(Fraction(x + y))
print(x * y)
print(Fraction(8, 16))
print(Fraction(1, -4))

print(x.numerator)
print(x.denominator)


x = Fraction(math.pi)
print(x)
print(float(x))

y = Fraction(math.sqrt(2))
print(y)
print(float(y))


a = 0.125
print(a)
print(Fraction(a))

b = 0.3
print(b)
print(Fraction(b))

print(format(b, '0.5f'))
print(format(b, '0.15f'))
print(format(b, '0.25f'))

x = Fraction(0.3)
x.limit_denominator(10)
print(x.limit_denominator(10))

x = Fraction(math.pi)
print(float(x))
print(x.limit_denominator(10))
print(x.limit_denominator(100))
print(311 / 99)
