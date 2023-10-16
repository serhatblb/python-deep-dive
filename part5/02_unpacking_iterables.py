# # tuple
# t = (1, 2, 3)

# # list
# l = [1, 2, 3]

# # string
# s = 'python'

# # set
# set1 = {1, 2, 3}

# # dict
# d = {'a': 1, 'b': 2, 'c': 3}

# a, b, c = [1, 2, 3]
# print(
#     a,
# )

# a, b, c = 10, 20, "python"
# print(a, b, c)

# a, b, c = "XYZ"
# print(a, b, c)

# s = {'p', 'y', 't', 'h', 'o', 'n'}
# for c in s:
#     print(c)

# a, b, c, d, e, f = s

# print(a, b, c, d, e, f)

print('################################# CODE  ##############################################')

a = (1, 2, 3)  # tuple
print(type(a))

a = 1, 2, 3  # tuple
print(type(a))
print(a)

a = 1  # a is an integer
print(type(a))
a = 'a'  # string
print(type(a))

a = (1,)  # tuple
print(type(a))
print(a)
a = (10,)  # tuple
print(type(a))

a = ()  # empty tuple
print(type(a))

a, b, c = [1, 'a', 3.14]
print(a, type(a))
print(b, type(b))
print(c, type(c))

(a, b, c) = [1, 2, 3]
print(a, b, c)

(a, b, c) = (1, 2, 3)
print(a)

a, b, c = 1, 2, 30
print(a, b, c)

print('###############################################################################')

a, b, c = 10, {1, 2, 3}, ['a', 'b', 'c']
print(a, type(a))
print(b, type(b))
print(c, type(c))


a, b = 10, 20
print(a, b)

a, b = b, a
print(a, b)


s = 'XYZ'
print(s[0])
print(s[1])

s = {'p', 'y', 't', 'h', 'o', 'n'}
print(s)

for c in s:
    print(c)

a, b, c, d, e, f = s

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print("\n")

d = {'a': 1, 'b': 2, 'c': 3}
for e in d:
    print(e)

a, b, c = d
print(a)
print(b)
print(c)
print(d)

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for e in d:
    print(e)

for e in d.values():
    print(e)

a, b, c, d = d.values()
print(a)
print(b)
print(c)
print(d)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for e in dict1.items():
    print(e)

print("\n")

dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for e in dict2.items():
    a, b = e
    print('key: {}, value: {}'.format(a, b))

print("\n")

dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for a, b in dict2.items():
    print('key: {}, value: {}'.format(a, b))
