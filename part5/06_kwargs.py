def func(*, d, **kwargs):
    print(d, kwargs)


func(d=11, a=1, b=2, c=3)
func(d=1)


def func(**kwargs):
    print(kwargs)


func(a=1, b=2, c=3)


def func(*args, **kwargs):
    print(args, kwargs)


func(1, 2, 3, a=1, b=2, c=3)
func()
print('\n')
print("############################################### CODE ###############################################")


def func(**others):
    print(others)


func(a=1, b=2, c=3)

print('\n')


def func(*args, **kwargs):
    print(args)
    print(kwargs)


func(1, 2, 3, a=1, b=2, c=3)

print('\n')


def func(a, b, *, d, **kwargs):
    print(a)
    print(b)
    print(d)
    print(kwargs)


func(1, 2, d=3, x=1, y=2, z=3)

print('\n')

print("############################################### EXAMPLE ###############################################")


def ProperCalorie(**fruits):
    for fruitName, fruitCal in fruits.items():
        if fruitCal <= 50:
            print(f"{fruitName}: {fruitCal}")


myFruits = {'Apple': 100, 'Banana': 20, 'Orange': 50, 'Ananas': 300, 'Pineapple': 40}

ProperCalorie(**myFruits)
