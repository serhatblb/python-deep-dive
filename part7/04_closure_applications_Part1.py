from itertools import count


class Averager:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count


a = Averager()

a.add(10)
print(a.add(10))
a.add(20)
print(a.add(20))
a.add(30)
print(a.add(30))

b = Averager()

b.add(10)
print(b.add(10))

print('\n', '*' * 50, '\n')


def averager():
    numbers = []

    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count

    return add


a = averager()
print(a(10))
print(a(20))
b = averager()
print(b(10))
print(a.__closure__)
print(b.__closure__)

print('\n', '*' * 50, '\n')


def averager():
    total = 0
    count = 0

    def add(number):
        nonlocal total
        nonlocal count

        total = total + number
        count = count + 1
        return total / count

    return add


a = averager()
print(a.__closure__)
print(a.__code__.co_freevars)

print(a(10))
print(a(20))
