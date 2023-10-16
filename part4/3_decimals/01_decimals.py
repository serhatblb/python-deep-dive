import decimal
from decimal import Decimal

print("-->", decimal.getcontext())

print(decimal.getcontext().prec)
decimal.getcontext().prec = 6
print(decimal.getcontext().prec)

g_ctx = decimal.getcontext()

print(type(g_ctx))
g_ctx.rounding = decimal.ROUND_HALF_UP
print(decimal.ROUND_HALF_UP)

print("-->", decimal.getcontext())

g_ctx.prec = 28
g_ctx.rounding = decimal.ROUND_HALF_EVEN

print("-->", decimal.getcontext())

print("#" * 80)

print(type(decimal.localcontext()))
print(type(decimal.getcontext()))

with decimal.localcontext() as ctx:
    print(type(ctx))
    print("-->", ctx)


with decimal.localcontext() as ctx:
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    print("-->", ctx)
    print("-->", decimal.getcontext())
    print(id(ctx) == id(decimal.getcontext()))

print("#" * 80)

x = Decimal('1.25')
y = Decimal('1.35')

with decimal.localcontext() as ctx:
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    print(round(x, 1))
    print(round(y, 1))
print(round(x, 1))
print(round(y, 1))


print("#" * 80)

print(Decimal((0, (3, 1, 4, 1, 5), -4)))
print(type(Decimal((0, (3, 1, 4, 1, 5), -4))))
