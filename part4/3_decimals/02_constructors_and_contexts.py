import decimal
from decimal import Decimal

# a = Decimal(10)
# print(a)

# b = Decimal('0.1')
# print(b)
# print(type(b))

# a = Decimal((1, (3, 1, 4, 1, 5), -4))
# print(a)

# decimal.getcontext().prec = 2

# a = Decimal('0.12345')
# b = Decimal('0.12345')
# c = a + b
# print(c)
# decimal.getcontext().prec = 4

# a = Decimal('0.12345')
# b = Decimal('0.12345')
# c = a + b
# print(c)

print("############# - CODE - #############")
############# - CODE - #############


print(Decimal('10'))
print(Decimal('-10'))
print(Decimal('-3.12345'))

t = (0, (3, 1, 4, 1, 5), -4)
print(Decimal(t))
print(Decimal((1, (3, 1, 4, 1, 5), -3)))

print("#" * 80)

print(format(0.1, '.25f'))
print(Decimal(0.1))
print(Decimal('0.1'))
print(Decimal('0.1') == Decimal(0.1))


a = Decimal('0.12345')
b = Decimal('0.12345')
print(a + b)
with decimal.localcontext() as ctx:
    ctx.prec = 2
    c = a + b
    print('c within local context: {0}'.format(c))
print('c within global context: {0}'.format(c))
