import inspect
from inspect import isfunction, ismethod, isroutine


def my_func(a, b=2, c=3, *, kw1, kw2=2):
    pass


print(my_func.__name__)
print(my_func.__defaults__)
print(my_func.__kwdefaults__)


def my_func2(a, b=2, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b


print(my_func.__code__)

print('\n')

# inspect module


print('\n')
print('######################## CODE ########################')
print('\n')


# TODO: Fix this function
# currently does nothing, but should print the name of the function
def my_func(a, b=1, c=2, *args, kw1, kw2=100, kw3=200, **kwargs):
    i = 10
    j = 20


print(dir(my_func))
print(my_func.__name__)


def func_call(f):
    print(f.__name__)


print(id(my_func))

func_call(my_func)

print(my_func.__kwdefaults__)

print(my_func.__code__)
print(dir(my_func.__code__))
print(my_func.__code__.co_name)
print(my_func.__code__.co_varnames)
print(my_func.__code__.co_argcount)

print('\n')

a = 10

print(isfunction(a))
print(isfunction(my_func))
print(ismethod(my_func))
print(isroutine(my_func))

print('\n')


class MyClass:
    def f(self):
        pass


print(isfunction(MyClass.f))

my_obj = MyClass()
f = my_func
print(isfunction(my_obj.f))
print(ismethod(my_obj.f))
print(isroutine(my_obj.f))
print(inspect.getsource(my_func))
print(inspect.getsource(f))


print(inspect.getmodule(print))

print(inspect.getcomments(my_func))

print(inspect.signature(my_func))

print('\n')

sig = inspect.signature(my_func)

print(sig)
print(sig.parameters)

for k, param in sig.parameters.items():
    print('Name:', param.name)
    print('Default:', param.default)
    print('Annotations:', param.annotation)
    print('Kind:', param.kind)
    print('----------------------------------------')

print('\n')

print(divmod(4, 3))
