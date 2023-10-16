import math
import sys
import time
from decimal import Decimal

a = 3.12345
b = Decimal('3.12345')

print(sys.getsizeof(a))
print(sys.getsizeof(b))  # decimal sayılar çok fazla yer kaplar.


def run_float(n=1):
    for i in range(n):
        a = 3.1415


def run_decimal(n=1):
    for i in range(n):
        a = Decimal('3.1415')


n = 10000000
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end - start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end - start)


print("#" * 80)


def run_float(n=1):
    a = 3.1415
    for i in range(n):
        a + a


def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a + a


start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end - start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end - start)


print("############# with math modul #############")

n = 5000000


def run_float(n=1):
    a = 3.1415
    for i in range(n):
        math.sqrt(a)


def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a.sqrt()


start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end - start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end - start)
