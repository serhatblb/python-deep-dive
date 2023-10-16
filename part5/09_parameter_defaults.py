from audioop import add
from datetime import datetime
from functools import cache

print(datetime.utcnow())


def log(msg, *, dt=datetime.utcnow()):
    print("{} {}".format(dt, msg))


log("Hello", dt="2001-01-01 00:00:00.000")
log("Hello 2")
log("Hello 3")
log("Hello 3")


def log(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    # if not dt:
    #     dt = datetime.utcnow()
    print("{} {}".format(dt, msg))


log('message 1')
log('message 2')
log('message 3')

print('\n')

my_list = [1, 2, 3, 4, 5]


def func(x=my_list):
    print(x)


func()
func(['a', 'b', 'c'])
my_list.append(88)
print(my_list)
func()

print('\n')
print("################################ 2. PART ##############################################")
print('\n')


def add_item(name, quantity, unit, grocery_list):
    grocery_list.append("{} ({} {})".format(name, quantity, unit))
    print(grocery_list)
    return grocery_list


store1 = []
store2 = []

add_item("banana", 3, "units", store1)
add_item("orange", 5, "units", store1)
add_item("milk", 1, "liters", store1)

add_item("python", 1, "medium-rare", store2)

print(store1 is store2)


def add_item(name, quantity, unit=1, grocery_list=None):
    if not grocery_list:
        grocery_list = []
    grocery_list.append("{} ({} {})".format(name, quantity, unit))
    print(grocery_list)
    return grocery_list


print('\n')


# write factorial function


def factorial(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        result = n * factorial(n - 1)
        cache[n] = result
        return result


cache = {}
factorial(5, cache=cache)
print(cache)
factorial(6, cache=cache)
