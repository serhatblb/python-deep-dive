import ctypes
import sys
from weakref import ref

a = [1, 2, 3]

print(id(a))

print(sys.getrefcount(a))


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


# print(ref_count(id(a)))
# print(ref_count(140260874584256))

b = a

print(id(b))

print(ref_count(id(a)))

c = a

print(ref_count(id(a)))

c = 10
print(ref_count(id(a)))
b = None
print(ref_count(id(a)))
a_id = id(a)
print(ref_count(id(a_id)))
a = None
print(ref_count(id(a_id)))
print(ref_count(id(a_id)))
print(ref_count(id(a_id)))
