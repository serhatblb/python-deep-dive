def dis_fonksiyon():
    x = 'hello'

    def ic_fonksiyon():
        print(x)

    ic_fonksiyon()


dis_fonksiyon()

print('\n')


def outer_func():
    x = 'hello'

    def inner1():
        def inner2():
            print(x)

        inner2()

    inner1()


outer_func()

print('\n')

# nonlocal ile degiskenleri degistirme
def outer():
    x = 'hello'

    def inner():
        nonlocal x
        x = 'world'

    inner()
    print(x)


outer()

print('\n')


def outer():
    x = 'hello'

    def inner1():
        def inner2():
            nonlocal x
            x = 'python'

        inner2()

    inner1()
    print(x)


outer()

print('\n')


def dis():
    x = 'hello'

    def ic1():
        x = 'ic 1'

        def ic2():
            x = 'ic 2'

            def ic3():
                x = 'ic 3'

            print(x)
            ic3()

        print(x)
        ic2()

    print(x)
    ic1()
    print(x)


dis()

print('\n')


def outer():
    x = 'hello'

    def inner1():
        nonlocal x
        x = 'python'

        def inner2():
            nonlocal x
            x = 'monty'

        print('inner1 (before):', x)
        inner2()
        print('inner1 (after):', x)

    inner1()
    print('outer:', x)


outer()
