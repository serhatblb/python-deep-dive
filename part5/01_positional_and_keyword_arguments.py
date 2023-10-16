from re import M


def my_func(a, b, c):
    print("a={}, b={}, c={}".format(a, b, c))


my_func(1, 2, 3)

print("\n")


def my_func(a=1, b=2, c=3):
    print("a={}, b={}, c={}".format(a, b, c))


my_func(10, 20, 30)
my_func(10, 20)
my_func(10)
my_func()

print("\n")


def my_func(a, b=2, c=3):
    print("a={}, b={}, c={}".format(a, b, c))


my_func(c=30, b=20, a=10)
