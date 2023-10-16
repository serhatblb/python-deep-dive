# int
import sys
import time

example = 0, 10, -100, 23000

print(type(example))

print(sys.getsizeof(0))
print(sys.getsizeof(10))
print(sys.getsizeof(2**1000))
print(2**1000)
print(2**10000)


def calc(a):
    for i in range(10000000):
        a * 2


start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(end - start)

print("#############################################")

start = time.perf_counter()
calc(2**1000)
end = time.perf_counter()
print(end - start)

print("#############################################")

start = time.perf_counter()
calc(2**10000)
end = time.perf_counter()
print(end - start)
