from math import isclose

x = 0.1

print(format(x, '.25f'))

print(x)

x = 0.125

print(format(x, '.25f'))

x = 0.125 + 0.125 + 0.125
y = 0.375

print(x == y)

x = 0.1 + 0.1 + 0.1
y = 0.3

print(x == y)

print(format(x, '.25f'))
print(format(y, '.25f'))
print(round(x, 3))
print(round(y, 3))
print(round(x, 3) == round(y, 3))  # round yuvarlama yapiyor

x = 10000.01
y = 10000.02

print(y / x)
print(round(x, 1) == round(y, 1))

x = 0.01
y = 0.02

print(y / x)
print(round(x, 1) == round(y, 1))

######### isclose() #########
print("\n######### isclose() #########")

x = 0.1 + 0.1 + 0.1
y = 0.3
print(x == y)
print(isclose(x, y))

x = 0.01
y = 0.02
print(isclose(x, y, rel_tol=0.01))

x = 123456789.01
y = 123456789.02

print(isclose(x, y, rel_tol=0.01))


x = 0.0000001
y = 0.0000002

print(isclose(x, y, rel_tol=0.01))
print(isclose(x, y, rel_tol=0.01, abs_tol=0.01))


x = 0.0000001
y = 0.0000002

a = 123456789.01
b = 123456789.02

print('x = y:', isclose(x, y, abs_tol=0.0001, rel_tol=0.01))
print('a = b:', isclose(a, b, abs_tol=0.0001, rel_tol=0.01))
