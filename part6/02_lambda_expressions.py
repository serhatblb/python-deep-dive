# def my_func(x):
#     return x**2

# ustteki fonksiyonu lambda ile yazdık

my_func = lambda x: x**2

lambda x, y: x + y

print(my_func(6))


def apply_func(x, func):
    return func(x)


print(apply_func(5, lambda x: x**2))

print('\n')
print('######################## CODE ########################')
print('\n')


def square(x):
    return x**2


print(type(square))

print(square)

print(lambda x: x**2)
print(type(lambda x: x**2))
print(lambda x, y: x + y)
print(type(lambda x, y: x + y))

f = square
print(id(f), id(square))
print(f(5), square(5))

print(f)

f = lambda x: x**2
print(f)
print(f(5))

g = lambda x, y=10: x + y
print(g)
print(g(1, 2))
print(g(1))

f = lambda x, *args, y, **kwargs: (x, args, y, kwargs)
print(f(1, 'a', 'b', y=100, a=10, b=20))

print('\n')


def apply_func(x, fn):
    return fn(x)


print(apply_func(5, square))

print(apply_func(5, lambda x: x**2))

print(apply_func(5, lambda x: x**3))

print('\n')


def apply_func(fn, *args, **kwargs):
    return fn(*args, **kwargs)


print(apply_func(square, 4))
print(apply_func(lambda x: x**2, 4))
print(apply_func(lambda x, y: x + y, 1, 2))
print(apply_func(lambda x, *, y: x + y, 1, y=20))
print(apply_func(lambda *args: sum(args), 1, 2, 3, 4, 5))
print(apply_func(sum, (1, 2, 3, 4, 5)))
print(sum((1, 2, 3, 4, 5)))
