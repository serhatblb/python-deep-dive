# import time


# def ornek_decarator(asd):
#     def ic_deco():
#         print('giris ')
#         asd()
#         print('cikis ')

#     return ic_deco


# @ornek_decarator
# def fonk88():
#     print('orta')


# fonk88()

# print('\n', '*' * 50, '\n')


# def zaman_hesapla(fonk):
#     def wrapper(*args, **kwargs):
#         baslangic = time.time()
#         fonk(*args, **kwargs)
#         bitis = time.time()
#         print(f"Fonk çalisma suresi: {bitis-baslangic} saniye surdu.")

#     return wrapper


# @zaman_hesapla
# def kareleri_al(liste):
#     for i in liste:
#         print(i * i)


# @zaman_hesapla
# def kupleri_al(liste):
#     for i in liste:
#         print(i**3)


# @zaman_hesapla
# def topla(a, b):
#     time.sleep(1)
#     print(a + b)


# # kareleri_al(range(100))
# # kupleri_al(range(100))

# topla(10, 20)

############## deep dive bolumu
import inspect
from functools import wraps


def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)

    return inner


def add(a, b=0):
    """
    returns the sum of a and b
    """
    return a + b


# help(add)
print(id(add))

add = counter(add)

print(id(add))
print(add(1, 2))
print(add(2, 2))


@counter
def mult(a: float, b: float = 1, c: float = 1) -> float:
    return a * b * c


print(mult(2, 3, 4))
print(mult(2, 2, 2))
print(add.__name__)
print(mult.__name__)


print(inspect.getsource(add))
print(inspect.signature(add))
print(inspect.getsource(mult))
print(inspect.signature(mult))

print(
    '\n',
    '*' * 50,
    '\n',
)


def counter(fn):
    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{0} was called {1} times".format(fn.__name__, count))

    return inner


@counter
def add(a: int, b: int = 10) -> int:
    """
    returns sum of two integers
    """
    return a + b


print(add(1, 2))
