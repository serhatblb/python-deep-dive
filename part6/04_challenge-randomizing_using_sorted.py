import random

print(random.random())

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sorted(l, key=lambda x: random.random()))
print(random.choice(l))

print(sorted('abcdefg', key=lambda x: random.random()))
