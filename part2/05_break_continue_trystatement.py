a = 10
b = 1

try:
    a / b
except ZeroDivisionError:
    print('division by zero')
finally:
    print('this always executes')

#################################################

a = 10
b = 0
try:
    a / b
except ZeroDivisionError:
    print('division by 0')
finally:
    print('this always executes')

#################################################

a = 0
b = 2

while a < 3:
    print('-----------------')
    a += 1
    b -= 1
    try:
        res = a / b
    except ZeroDivisionError:
        print('{0}, {1} - devision by 0'.format(a, b))
        res = 0
        continue
    finally:
        print('{0}, {1} - this always executes'.format(a, b))

    print('{0}, {1} - main loop'.format(a, b))

#################################################

a = 0
b = 2

while a < 3:
    print('-----------------')
    a += 1
    b -= 1
    try:
        res = a / b
    except ZeroDivisionError:
        print('{0}, {1} - devision by 0'.format(a, b))
        res = 0
        continue
    finally:
        print('{0}, {1} - this always executes'.format(a, b))

    print('{0}, {1} - main loop'.format(a, b))
else:
    print('Code executed without a zero division error')
