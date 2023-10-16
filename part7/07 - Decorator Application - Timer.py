from functools import reduce


def timed(fn):
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)
        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__, args_str, elapsed))
        return result

    return inner


# Fibonacci Numbers

# Using Recursion


def calc_recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return calc_recursive_fib(n - 1) + calc_recursive_fib(n - 2)


print(calc_recursive_fib(3))
print(calc_recursive_fib(6))


@timed
def fib_recursed(n):
    return calc_recursive_fib(n)


print(fib_recursed(33))


# Using a Loop


@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n + 1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2


print(fib_loop(33))
print(fib_loop(35))


# Using Reduce


@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n - 1)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), dummy, initial)
    return fib_n[0]


print(fib_reduce(33))


print('\n')

print(fib_recursed(35))
print(fib_loop(35))
print(fib_reduce(35))
