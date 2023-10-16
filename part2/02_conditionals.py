a = 9

if a < 5:
    print("a < 5")
    print("a is less than 5")
else:
    print("a > 5")
    print("a is equal or greater than 5")
    if a < 10:
        print("5 <= a < 10")
        print("a is equal or greater than 5 or less than 10")
    else:
        print("a >= 10")
        print("a is equal or greater than 10")


b = 16

if b < 5:
    print('b < 5')
elif b < 10:
    print('5 <= b < 10')
elif b < 15:
    print('10 <= b < 15')
elif b < 20:
    print('15 <= b < 20')
else:
    print('b >= 20')

# X if (condition) else Y

c = 5

res = 'c < 10' if c < 10 else 'c >= 10'

print(res)


def merhaba():
    print('merhaba!')


def baybay():
    print('baybay!')


d = 10
merhaba() if d < 10 else baybay()
