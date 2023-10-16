def func(a, b=10):
    pass


def func2(a, b, *args):
    print(a, b, args)


func2(1, 2, 'a', 'b', 'c')

print('\n')


def func3(a, b, *args, kw1, kw2=100):
    pass


def func4(a, b=10, *, kw1, kw2=100):
    pass


def func5(a, b=10, *args, kw1, kw2=100, **kwargs):
    pass


def func6(a, b=10, *, kw1, kw2=100, **kwargs):
    pass


def func7(*args):
    pass


def func8(**kwargs):
    pass


def func9(*args, **kwargs):
    pass


print('\n')
print("#################################### CODE ###########################################")
print('\n')


def func(a, b, *args):
    print(a, b, args)


func(1, 2, 'a', 'b', 'c')

print('\n')


def func(a, b=2, c=3, *args):
    print(a, b, c, args)


func(1, 2, 3, 4, 5, 6, 'a', 'b', 'c')
func(1, 5, 'x', 'y')


def func(a, b=2, *args, c=3, d):
    print(a, b, args, c, d)


func(10, 20, 'x', 'y', c=40, d=50)
func(1, 2, 'x', 'y', d=60)  # c defaults to 3

print('\n')


def func(a, b, *args, c=50, d=100, **kwargs):
    print(a, b, args, c, d, kwargs)


func(1, 2, 'x', 'y', c=5000, d=60, e=70, f=8.0, g=9.0)

print('\n')

print(1, 2, 3)
print(1, 2, 3, sep='-*-', end=" *** ")
print(4, 5, 6, sep='-*-')

print('\n')


def calc_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = min(args) if len(args) > 0 else 0
    avg = (hi + lo) / 2
    if log_to_console:
        # print('hi:', hi, 'lo:', lo, 'avg:', avg)
        print("high:{}, low:{}, avg:{}".format(hi, lo, avg))
    return avg


is_debug = True

ortalama = calc_hi_lo_avg(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, log_to_console=is_debug)
print(ortalama)
