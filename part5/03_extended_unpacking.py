# l = [1, 2, 3, 4, 5, 6]

# a = l[0]
# b = l[1:]
# print(a)
# print(b)
# print(a, b)

# print("\n")

# a, *b = [-10, 5, 2, 100]
# print(a)
# print(b)
# print("\n")

# a, *b, c = [-10, 5, 2, 100]
# print(a)
# print(b)
# print(c)

# a, *b = (-10, 5, 2, 100)  # tupple olsada list seklinde yaziyor * oldugunda
# print(a)
# print(b)
# print("\n")

# a, *b = 'XYZ'
# print(a)
# print(b)
# print("\n")

# a, b, *c = 1, 2, 3, 4, 5
# print(a, "\n", b, "\n", c)
# print("\n")

# a, b, *c, d = 1, 2, 3, 4, 5
# print(a, "\n", b, "\n", c, "\n", d)
# print("\n")

# a, b, *c, d = 'python'
# print(a, "\n", b, "\n", c, "\n", d)
# print("\n")

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l = [*l1, *l2]
# print(l)
# print("\n")


# l1 = [1, 2, 3]
# l2 = 'XYZ'
# l = [*l1, *l2]
# print(l)
# print("\n")

# d1 = {'p': 1, 'y': 2}
# d2 = {'t': 3, 'h': 4}
# d3 = {'h': 5, 'o': 6, 'n': 7}

# l = [*d1, *d2, *d3]
# print(l)
# s = {*d1, *d2, *d3}
# print(s)
# d = {**d1, **d2, **d3}
# print(d)
# print("\n")

# l = [1, 2, [3, 4]]
# a, b, c = l
# print(a, "\n", b, "\n", c)
# d, e = c
# print(d, "\n", e)
# a, b, (c, d) = l
# print(d)


print("###################################-CODE-############################################")

s = 'python'

a, b, c, d = s[0], s[1], s[2:-1], s[-1]
print(a)
print(b)
print(list(c))
print(d)
print("\n")

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]
print(l)
print("\n")

l1 = [1, 2, 3]
s = 'abc'
l = [*l1, *s]
print(l)
print("\n")

l1 = [1, 2, 3]
s1 = {'x', 'y', 'z'}  # farklı sirayla geliyor
l = [*l1, *s1]
print(l)
print("\n")

s1 = 'abc'
s2 = 'cde'
l1 = [*s1, *s2]
s = {*s1, *s2}  # set oldugu zaman aynı karakteri yazmıyor
print(l1)
print(s)
print("\n")

s = {3, -99, 's', 10}

for i in s:
    print(i)

a, b, c, d = s
print(a, b, c, d)

a, b, *c = s
print(a)
print(b)
print(c)
print("\n")

print(s)
print(list(s))

(*c,) = s
print(c)
print("\n")

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s = {*s1, *s2}
print(s)
print(s1.union(s2))
print("\n")

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
s4 = {7, 8, 9}
print(s1.union(s2).union(s3).union(s4))
print(s1.union(s2, s3, s4))
print([*s1, *s2, *s3, *s4])
print({*s1, *s2, *s3, *s4})
print("\n")

d1 = {'key1': 1, 'key2': 2}
d2 = {'key2': 3, 'key4': 4}

print({*d1, *d2})
print({**d1, **d2})  # d1 in uzerine d2 yazildigi icin key2 degeri 3 oluyor
print({**d2, **d1})  # d2 in uzerine d1 yazildigi icin key2 degeri 2 oluyor
a = {'a': 1, 'b': 2, **d1, 'c': 3}
print(a)
print("\n")

# Nested unpacking

a, b, e = [1, 2, 'XY']
print(a)
print(b)
print(e)
print("\n")

a, b, (c, d) = [1, 2, 'XY']
print(a)
print(b)
print(c)
print(d)
print("\n")

a, b, (c, d, *e) = [1, 2, 'python']
print(a)
print(b)
print(c)
print(d)
print(e)
print("\n")

l = [1, 2, 3, 4, 'python']
a, *b, (c, d, *e) = l
print(a, b, c, d, e)
print(l[0], l[1:-1], l[-1])
