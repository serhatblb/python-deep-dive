a = round(1.9)
print(a, type(a))

a = round(1.9, 0)
print(a, type(a))

# n > 0: round to n digits after the decimal point

print(round(1.8888, 3), round(1.8888, 2), round(1.8888, 1), round(1.8888, 0))
print("####")

# n < 0: round to n digits before the decimal point

print(round(888.88, 1), round(888.88, 0))
print(round(888.88, -1), round(888.88, -2), round(888.88, -3), round(888.88, -4))

print("example: ", round(9800, -4), "and: ", round(9800, -5))

# Ties

print(round(1.25, 1))
print(round(1.35, 1))
print(round(-1.25, 1))
print(round(-1.35, 1))
print(round(1.75, 1))
print(round(15, -1))


# +0.5 ekleme


def _round(x):
    from math import copysign

    return int(x + 0.5 * copysign(1, x))


print(round(1.5), _round(1.5))
print(round(2.5), _round(2.5))


print(round(-1.5), _round(-1.5))
print(round(-2.5), _round(-2.5))
