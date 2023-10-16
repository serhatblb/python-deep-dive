from __future__ import annotations


def fact(n):
    '''Calculates n! (factorial function)

    Inputs:
        n: non-negative integer
    Returns:
        the factorial of n
    '''

    if n < 0:
        '''Note that this is not part of the docstring!'''
        return 1
    else:
        return n * fact(n - 1)


print(fact.__doc__)  # coklu yorum satirini gostermek icin kullanilir.


# def my_fonc(a: 'a string', b: 'a positive integer') -> 'a string':
#     return a * b


def my_func(a: str, b: 'int > 0') -> str:
    return a * b


# def my_func(a: int = 0, *args: 'additional args'):
#     print(a, args)


print(my_func.__annotations__)
