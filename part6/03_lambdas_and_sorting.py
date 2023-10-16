# help(sorted)

l = [1, 5, 7, 2, 3, 4, 6, 9, 8]
print(sorted(l))

l = ['c', 'B', 'D', 'a']
print(sorted(l))
print(ord('a'))
print(ord('A'))

print(sorted(l, key=lambda s: s.upper()))

# dicts

d = {'def': 300, 'abc': 200, 'ghi': 400}
print(d)
for e in d:
    print(e)
print(sorted(d))

print(sorted(d, key=lambda e: d[e]))

print('\n')


def dist_sq(x):
    return (x.real) ** 2 + (x.imag) ** 2


print(dist_sq(1 + 1j))

l = [1 + 1j, 2 + 2j, 3 + 3j, 4 + 4j, 5 + 5j, 0, 1, 2, 3, 4, 5]
# print(sorted(l)) # TypeError: '<' not supported between instances of 'complex' and 'complex'
print(sorted(l, key=dist_sq))
print(sorted(l, key=lambda x: (x.real) ** 2 + (x.imag) ** 2))


print('\n')

l = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Jones']
print(sorted(l))
print(sorted(l, key=lambda s: s[-1]))
