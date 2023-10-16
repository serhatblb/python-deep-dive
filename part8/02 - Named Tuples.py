from collections import namedtuple


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


Point2D = namedtuple('Point2D', ['x', 'y'])
pt1 = Point2D(10, 20)
print(pt1)

print('\"')

pt3d_1 = Point3D(10, 20, 30)

print(pt3d_1)

Point2D = namedtuple('Pt2D', ('x', 'y'))

pt2 = Point2D(10, 20)
print(pt2)

Pt3D = Point3D

p = Pt3D(10, 20, 30)
print(p)
print(p.x)
print(p.y)

p = Point2D(x=10, y=20)

print(p)

print(isinstance(p, tuple))
p = Point3D(x=10, y=20, z=30)
print(isinstance(p, tuple))

print('\n')

a = (10, 20)
b = (10, 20)

print(a is b)

print(a == b)

print('\n')

pt1 = Point2D(10, 20)
pt2 = Point2D(10, 20)

print(pt1 is pt2)
print(pt1 == pt2)

print('\n')

pt1 = Point3D(10, 20, 30)
pt2 = Point3D(10, 20, 30)

print(pt1 is pt2)
print(pt1 == pt2)
