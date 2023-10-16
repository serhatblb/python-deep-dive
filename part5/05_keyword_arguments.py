from this import d


def func(a, b, c):
    print(a, b, c)


func(1, 2, 3)

func(1, c=3, b=2)
func(c=3, b=2, a=1)


def func1(a, b, *args):
    print(a, b, args)


func1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def func1(a, b, *args, d):
    print(a, b, args, d)


func1(1, 2, 3, 4, 5, 6, 7, 8, 9, d=10)


def func1(*args, d):
    print(args, d)


func1(1, 2, 3, 4, 5, d='a')
func1(d='a')

print("\n")


def func(*, d):
    print(d)


func(d=100)


def func(a, b, *, d):
    print(a, b, d)


func(1, 2, d=3)

print("\n")


def func2(a, b=2, *args, d):
    print(a, b, args, d)


func2(1, 44, 3, 4, 2, d='a')

print("\n")


def func(a, b=20, *args, d=0, e):
    print(a, b, args, d, e)


func(1, 2, 3, 4, 5, 6, d=7, e='aaaa')
func(0, 600, d='hello', e='world')
