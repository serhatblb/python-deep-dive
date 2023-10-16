a = 10
b = 10

print(hex(id(a)))
print(hex(id(b)))


print('a is b:', a is b)
print("a == b:", a == b)

# listelerde farkli

a = [1, 2, 3]
b = [1, 2, 3]

print(hex(id(a)))
print(hex(id(b)))

print('a is b:', a is b)
print("a == b:", a == b)

print('##############################################################################')

a = 10
b = 10.0

print(type(a))
print(type(b))

print('a is b:', a is b)
print("a == b:", a == b)


c = 10 + 0j
print(type(c))

print('a is c', a is c)
print("a == b:", a == b)

# None
print('#############################  None  #########################################')


print(None)

print(hex(id(None)))
print(type(None))


a = None
b = None

print(a is b)
print(a is None)
