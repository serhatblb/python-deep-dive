london = ('London', 'UK', 8.9)

city = london[0]
print(city)
country = london[1]
print(country)
population = london[2]
print(population)

cities = [(london, 'UK', 8.9), ('Paris', 'France', 2.3), ('Berlin', 'Germany', 3.5)]

total_population = 0
for city in cities:
    total_population += city[2]

print(total_population)

city, country, population = ('New York', 'USA', 8.9)
city, country, population = 'New York', 'USA', 8.9

print('\n')

city, _, population = ('Beijing', 'China', 13.5)


print('\n', '#' * 30, 'CODE', '#' * 30, '\n')


(10, 20, 30)
a = (10, 20, 30)
b = 10, 20, 30

print(type(a))
print(type(b))


def print_tuple(t):
    for e in t:
        print(e)


print_tuple((10, 20, 30))


a = 'a', 10, 20
print(a[0])
print(a[1])

a = 1, 2, 3, 4, 5, 6
print(type(a))
print(a[2:5])

for i in a:
    print(i)


a = 'a', 10, 20

x, y, z = a

print(x)
print(z)

a = 1, 2, 3, 4, 5, 6

x, *other, y, z = a

print(x)
print(y)
print(z)
print(other)

print('\n')

x, *_, y, z = a

print(x)
print(y)
print(z)
print(_)

print('\n', '\n')


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.__class__.__name__}({self.x},{self.y})'


pt = Point2D(10, 20)

Point2D(x=10, y=20)

print(id(pt))

pt.x = 100
print(pt)
print(id(pt))

print('\n')

a = 1, 2, 3

print(id(a))

a += (4, 5, 6)
print(a)
print(id(a))
a = a + (4, 5, 6)
print(a)
print(id(a))


print('\n')

london = 'London', 'UK', 8.9
new_york = 'New York', 'USA', 8.9
beijing = 'Beijing', 'China', 13.5

cities = [london, new_york, beijing]

total = 0

for city in cities:
    total += city[2]

print(total)

print([city[2] for city in cities])

total = sum([city[2] for city in cities])

print(total)

print('\n')

record = 'DJIA', 2018, 1, 19, 25_987, 26_072, 25_942, 26_072

symbol, year, month, day, open_, high, low, close = record

print(symbol)

symbol, year, *_, close = record

print(_)
