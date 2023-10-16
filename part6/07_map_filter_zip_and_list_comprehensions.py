def fact(n):
    return 1 if n < 2 else n * fact(n - 1)


print(fact(5))

results = list(map(fact, range(6)))

print(results)


l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]
l3 = [100, 200, 300, 400]

results = list(map(lambda x, y, z: x + y + z, l1, l2, l3))
print(results)

print('###### filter ######')

x = range(25)
print(x)
print(list(filter(lambda x: x % 3 == 0, range(25))))
print(list(filter(None, [1, 0, 4, 'a', '', None, True, False])))

print('###### zip ######')

l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]
l3 = 'python'

results = list(zip(l1, l2, l3))

for x in results:
    print(x)

print(list(zip(range(100000), 'python')))


print('\n')

l = range(10)
print(list(l))

print(list(map(fact, l)))
results = [fact(n) for n in range(10)]
print(results)

print('\n')

l1 = [1, 2, 3, 4, 5, 6]
l2 = [10, 20, 30, 40]

print(list(map(lambda x, y: x + y, l1, l2)))
print([x + y for x, y in zip(l1, l2)])
print(list(filter(lambda x: x % 2 == 0, (map(lambda x, y: x + y, l1, l2)))))
print([x + y for x, y in zip(l1, l2) if (x + y) % 2 == 0])
