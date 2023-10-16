import re
from tkinter import PIESLICE


class Rectagle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


r1 = Rectagle(10, 20)

print(r1.width)

r1.width = 300
print(r1.width)

###########################################################
print('###########################################################')


class Rectagle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


r1 = Rectagle(10, 20)
print(r1.area())
print(r1.perimeter())
print(str(r1))
print(hex(id(r1)))

###########################################################


class Rectagle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return 'Rectangle (width={0}, height={1})'.format(self.width, self.height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, serhat):
        if isinstance(serhat, Rectagle):
            return self.width == serhat.width and self.height == serhat.height
        else:
            return False


r1 = Rectagle(10, 20)
print(str(r1))

print(r1)

r2 = Rectagle(10, 20)
print(r1 is not r2)
print(r1 == r2)

r1.height = 30

###########################################################
print('###########################################################')


class Rectagle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        self._height = height

    def __str__(self):
        return 'Rectangle (width={0}, height={1})'.format(self._width, self._height)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self._width, self._height)

    def __eq__(self, serhat):
        if isinstance(serhat, Rectagle):
            return self._width == serhat._width and self._height == serhat._height
        else:
            return False


r1 = Rectagle(-30, 20)
print(r1.width)
r1.width = -30
print(r1.width)
###########################################################
print('###########################################################')


class Rectangle:
    def __init__(self, width, height):
        self._width = None
        self._height = None
        # now we call our accessor methods to set the width and height
        self.width = width
        self.height = height

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        self._height = height


r1 = Rectagle(-30, 20)
print(r1.width)
r1.width = -30
print(r1.width)
