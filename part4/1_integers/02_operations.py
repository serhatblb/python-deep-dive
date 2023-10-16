from math import floor, trunc

print(155 / 4)
print(155 // 4)
print(155 % 4)
print(floor(3.14))
print(floor(-3.99))
print(floor(-3.1))

# positive numbers
a = 135
b = 4

c = b * (a // b) + a % b

print("a//b: ", a // b)
print("a%b: ", a % b)
if a == c:
    print("islem dogru")

# negative numbers

a = -135
b = 4

c = b * (a // b) + a % b

print("a//b: ", a // b)
print("a%b: ", a % b)
if a == c:
    print("islem dogru")

# other negative numbers
a = 135
b = -4

c = b * (a // b) + a % b

print("a//b: ", a // b)
print("a%b: ", a % b)
if a == c:
    print("islem dogru")

# two negative numbers
a = -135
b = -4

c = b * (a // b) + a % b

print("a//b: ", a // b)
print("a%b: ", a % b)
if a == c:
    print("islem dogru")

# code

print(type(1 + 2))
print(type(1 * 2))
print(type(4 - 10))
print(type(4**2))
print(type(2 / 3))
print(type(10 / 2))
print(type(3 // 2))
#
print(floor(3.14))
print(floor(-3.0000))
print(floor(-3.14))
print(floor(-3.00000001))
print(floor(-3.00000000000000000001))  # 15 sıfırdan sonra 1  = olarak degerlendiriliyor

print("##############################################################")

a = 33
b = 16

print(a / b)
print(a // b)
print(floor(a / b))
print("##############################################################")

a = -33
b = 16

print(a / b)
print(a // b)
print(floor(a / b))
print(trunc(a / b))

print("##############################################################")

a = b * (a // b) + (a % b)

a = 13
b = 4

print('{} / {} = {}'.format(a, b, a / b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} % {} = {}'.format(a, b, a % b))
print(a == b * (a // b) + (a % b))

print("##############################################################")

a = b * (a // b) + (a % b)

a = -13
b = 4

print('{} / {} = {}'.format(a, b, a / b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} % {} = {}'.format(a, b, a % b))
print(a == b * (a // b) + (a % b))

print("##############################################################")

a = b * (a // b) + (a % b)

a = 13
b = -4

print('{} / {} = {}'.format(a, b, a / b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} % {} = {}'.format(a, b, a % b))
print(a == b * (a // b) + (a % b))

print("##############################################################")

a = b * (a // b) + (a % b)

a = -13
b = -4

print('{} / {} = {}'.format(a, b, a / b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} % {} = {}'.format(a, b, a % b))
print(a == b * (a // b) + (a % b))
