i = 0
while i < 5:
    print(i)
    i += 1

i = 5
while True:
    print(i)
    if i >= 5:
        break

#################################################

# min_length = 2

# name = input('Enter your name: ')

# while not (len(name) > min_length and name.isalpha() and name.isprintable()):
#     print('Invalid name')
#     name = input('Enter your name: ')

# print('Hello, {0})'.format(name))

# kodun daha kisa yazilabilmesi icin

min_length = 2
while True:
    name = input('Enter your name: ')
    if len(name) > min_length and name.isalpha() and name.isprintable():
        print('Hello, {0})'.format(name))
        break
    else:
        print('Invalid name')

# continue

a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

#################################################

l = [1, 2, 3]
val = 10

found = False
idx = 0
while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1
if not found:
    l.append(val)
print(l)


l = [1, 2, 3]
val = 10

idx = 0

while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else:
    l.append(val)
print(l)
