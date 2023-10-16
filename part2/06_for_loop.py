for i in range(5):
    print(i)
for i in [1, 2, 3, 4, 5]:
    print(i)
for c in "Hello":
    print(c)

for x in (1, 2, 3, 4, 5):
    print(x)

for x in [(1, 2), (3, 4), (5, 6)]:
    print(x)

for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)

for i in range(5):
    if i == 2:
        continue
    print(i)
print('******************************************')
for i in range(1, 54):
    if i == 7:
        continue
    print(i)
    if i % 7 == 0:
        print('Found a multiple of 7 = ', i)
        break
else:
    print('No multiple of 7 found')

print('******************************************')

for i in range(5):
    print('-------------------')
    try:
        10 / (i - 3)
    except ZeroDivisionError:
        print('devide by zero')
    finally:
        print('always run')
    print(i)
############################################################
s = 'hello'
for c in s:
    print(c)


s = 'hello'
i = 0

for c in s:
    print(i, c)
    i += 1

s = 'hello'
for i in range(len(s)):
    print(i, s[i])

s = 'hello'
for i, c in enumerate(s):
    print(i, c)
