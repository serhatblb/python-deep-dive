from ast import arguments
from turtle import right

l = [10, 20, 30]


def func1(*l):
    print(l)
    print(type(l))
    print(l[0])
    print(l[1])
    print(l[2])
    print("\n")


func1(*l)
print("\n")

a, b, *c = 10, 20, 'a', 'b'


def func2(a, b, *args):
    print(a)
    print(b)
    print(args)
    print("\n")


func2(a, b)
func2(10, 20, 1, 2, 4)
print("\n")


def avg(*args):
    count = len(args)
    total = sum(args)
    return count and total / count
    # if count == 0:
    #     return 0
    # else:
    #     return total / count


print(avg(2, 2, 4, 8))
print(avg())


def func3(a, b, c, *args):
    print(a)
    print(b)
    print(c)
    print(args)


l = [10, 20, 30, 40, 50, 60]

func3(l, 'x', 'y')
func3(*l)
