import operator
from functools import reduce
from operator import is_
from textwrap import shorten

# print(dir(operator))

print(operator.add(1, 2))
print(operator.sub(1, 2))
print(operator.mul(1, 2))
print(operator.truediv(3, 2))
print(operator.floordiv(13, 2))


print(
    reduce(
        lambda x, y: x * y,
        [
            1,
            2,
            3,
            4,
        ],
    )
)
print(reduce(operator.mul, [1, 2, 3, 4]))
print(operator.lt(10, 3))
print(operator.lt(1, 3))


print(is_('abc', 'abc'))
print(is_('abc', 'abcd'))

print(operator.truth([]))
print(operator.truth([1, 2, 3]))

print('\n')

my_list = [1, 2, 3, 4]
print(my_list[1])

print(operator.getitem(my_list, 1))

my_list[1] = 100
print(my_list)
del my_list[3]
print(my_list)

print('\n')
my_list2 = [1, 2, 3, 4]
print(operator.setitem(my_list2, 1, 100))
print(my_list2)
print(operator.delitem(my_list2, 1))
print(my_list2)

print('\n')

f = operator.itemgetter(2)
print(type(f))
my_list3 = [1, 2, 3, 4]

print(f(my_list3))  # 3 sonucunu veriyor cunku f i 2. indexe olarak verdik

s = 'python'
print(f(s))  # 2. indexe olan 't' karakterini veriyor

print('\n')

f = operator.itemgetter(2, 3)
print(f(my_list3))  # [3, 4] sonucunu veriyor cunku f i 2. ve 3. indexe olarak verdik
print(f(s))  # ['t', 'h'] sonucunu veriyor cunku f i 2. ve 3. indexe olarak verdik


print('\n', '###', '\n')


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print('test method running...')


obj = MyClass()
print(obj)
print(obj.a)
print(obj.b)
print(obj.test())
prop_a = operator.attrgetter('a')
print(prop_a(obj))
my_var = 'b'
prop_b = operator.attrgetter(my_var)
print(prop_b(obj))
my_var = 'c'
print(prop_b(obj))  # c degerini vermiyor
print(operator.attrgetter('a', 'b')(obj))

a, b, test = operator.attrgetter('a', 'b', 'test')(obj)
print(a, b, test())

print('\n')

a = 5 + 10j
print(a)
print(a.real)


l = [5 - 10j, 3 + 3j, 2 - 100j]
print(sorted(l, key=lambda x: x.real))
print(sorted(l, key=operator.attrgetter('real')))  # ustteki ile aynı

l = [(2, 3, 4), (1, 2, 3), (4,), (3, 4)]
print(sorted(l, key=lambda x: x[0]))
print(sorted(l, key=operator.itemgetter(0)))

print('\n', '###', '\n')

x = 'python'
print(x.upper())
print(operator.attrgetter('upper')(x)())


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    def do_something(self, c):
        print(self.a, self.b, c)


obj = MyClass()

print(obj.do_something(100))

print(operator.methodcaller('do_something', 100)(obj))


class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20

    def do_something(self, *, c):
        print(self.a, self.b, c)


print(obj.do_something(c=100))
print(operator.methodcaller('do_something', c=100)(obj))
