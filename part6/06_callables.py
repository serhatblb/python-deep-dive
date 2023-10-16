from decimal import Decimal

print(callable(print))
print(callable('abc'.upper))
print(callable(str.upper))
print(callable(10))


print(callable(Decimal))

a = Decimal('10.5')
print(a)


class MyClass:
    def __init__(self, x=0):
        print('initializing...')
        self.counter = x


print(callable(MyClass))
a = MyClass(100)
print(a)
print(a.counter)
print(callable(a))


class MyClass2:
    def __init__(self, x=0):
        print('initializing...')
        self.counter = x

    def __call__(self, x=1):
        print('updating counter...')
        self.counter += x


b = MyClass2(100)
print(b)

print(MyClass2.__call__(b, 10))

print(b.counter)
print(callable(b))
