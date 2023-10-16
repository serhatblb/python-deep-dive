import time


def time_it(fn, *args, **kwargs):
    print(args, kwargs)


time_it(print, 1, 2, 4, sep=' - ', end=' *** ')

print('\n')


def time_it(fn, *args, rep=1, **kwargs):
    for i in range(rep):
        fn(*args, **kwargs)


time_it(print, 1, 2, 4, sep=' - ', end=' ***\n', rep=10)

print('\n')


def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    print((end - start) / rep)
    return (end - start) / rep


time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5)

print('\n')


def compute_powers_1(n, *, start=1, end):
    # using a for loop
    results = []
    for i in range(start, end):
        results.append(n**i)
    print(results)
    return results


compute_powers_1(2, end=5)

print('\n')


def compute_powers_2(n, *, start=1, end):
    # using a list comprehension
    print([n**i for i in range(start, end)])
    return [n**i for i in range(start, end)]


compute_powers_2(2, end=5)

print('\n')


def compute_powers_3(n, *, start=1, end):
    # using a generator expression
    print(list(n**i for i in range(start, end)))  # list() is used to convert the generator to a list
    return (n**i for i in range(start, end))


compute_powers_3(2, end=5)

print('\n')

# time_it(compute_powers_2, 2, start=0, rep=5, end=20000) # this will take a long time to run
time_it(compute_powers_2, 2, end=20000, rep=4)  # this will take a long time to run
