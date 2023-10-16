a = 10


def my_func(n):
    c = n**2
    return c


def my_func(n):
    print('global:', a)
    c = a**n
    return c


print(my_func(2))


def my_func(n):
    a = 2
    c = a**2
    return c


print(a)
print(my_func(3))
print(a)  # global degiskenin degeri


def my_func(n):
    global a  # global degiskenin degerini degistirir
    a = 2
    c = a**2
    return c


print(a)
print(my_func(3))
print(a)  # degismis global degiskenin degeri

print('\n')


def my_func(n):
    global var
    var = 'hello world'
    return n**2


print(my_func(2))
print(var)

print('\n')

a = 10
b = 100


def my_func():
    print('a:', a)
    print('b:', b)


my_func()

print('\n')

a = 10
b = 100


def my_func():
    print(a)
    print(b)
    # b = 1000  # global degisken daha once tanitilmis oldugu icin hata verir


my_func()


print('\n', '*' * 50, '\n')

print = lambda x: 'hello {0}!'.format(x)


def my_func(name):
    return print(name)


print(my_func('world'))

del print


for i in range(10):
    x = 2 * i
    print(x)
print('x:', x)
