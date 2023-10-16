from audioop import add
from time import perf_counter


def outer():
    x = 'python'

    def inner():
        print(x)

    return inner


fn = outer()

print(fn.__code__.co_freevars)
print(fn.__closure__)

print('\n')


def outer():
    x = [1, 2, 3]
    print('outer:', hex(id(x)))

    def inner():
        print('inner:', hex(id(x)))
        print(x)

    return inner


fn = outer()
print(fn.__closure__)
fn()  # ic ve dıs aynı adresi gösteriyor.

print('\n')

# sayac
def counter():
    count = 0  # local degisken

    def inc():
        nonlocal count
        count += 1
        return count

    return inc


c = counter()
print(c())
print(c())
print(c())

print('\n')


def outer():
    count = 0

    def inc1():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count += 1
        return count

    return inc1, inc2  #  iki kapanış arasında paylaşılan serbest bir değişkenimiz var.


fn1, fn2 = outer()
print(fn1.__closure__, fn2.__closure__)

print(fn1())
print(fn2())
print(fn1())
print(fn2())

print('\n')
# Multiple Instances of Closures
print('\n')


def func():
    x = perf_counter()
    print('x:', x, 'id: ', id(x))


func()

print('\n', '*' * 50, '\n')


def pow(n):
    # n is local to pow
    def inner(x):
        # x is local to inner
        return x**n

    return inner


square = pow(2)
print(square(5))

cube = pow(3)
print(cube(5))

print(square.__closure__)
print(cube.__closure__)
print(id(square), id(cube))

print('\n', '*' * 50, '\n')


def adder(n):
    def inner(x):
        return x + n

    return inner


add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)
add_4 = adder(4)

print(add_1(10), add_2(10), add_3(10), add_4(10))

print('\n', '*' * 50, '\n')


def create_adders():
    adders = []
    for n in range(1, 5):
        adders.append(lambda x, step=n: x + step)
    return adders


adders = create_adders()

print(adders[0].__closure__)
print(adders[0].__code__.co_freevars)
print(adders[0](10))
print(adders[1](10))
print(adders[2](10))
print(adders[3](10))


print('\n', '*' * 30, "Nested Closures", '*' * 30, '\n')


def incrementer(n):
    def inner(start):
        current = start

        def inc():
            a = 10  # local var
            nonlocal current
            current += n
            return current

        return inc

    return inner


fn = incrementer(2)
print(fn)
print(fn.__code__.co_freevars)
print(fn.__closure__)

inc_2 = fn(100)
print(inc_2)
print(inc_2.__code__.co_freevars)
print(inc_2())
print(inc_2())

inc_3 = incrementer(3)(200)

print(inc_3())
print(inc_3())
