
'''
class TableClass:

    legs = 0

    def set_param(self, color):
        self.color = color

    def change_legs(self, legs):
        self.legs = legs

redT = TableClass()
redT.set_param('red')
print(redT.legs)
print(redT.color)

redT.change_legs(5)
print(redT.legs)

bluT = TableClass()
bluT.set_param('red')
print(bluT.legs)
print(bluT.color)'''


'''
class TableClass:

    legs = 0

    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

redT = TableClass('red', 5)
print(redT.legs)
print(redT.color)'''

'''
class TableClass:
    __legs = 0

    def init(self, legs, color=''):
        self.__color = color
        self.legs = legs


    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    @staticmethod
    def testStaticMet(color):
        if color == 'red':
            print('Red')
        else:
            print('No red')

    @classmethod
    def change_legs(cls):
        cls.legs = 5

    @classmethod
    def testClsMet(cls, legs, color):
        tmp = cls(legs, color)
        return tmp

redT = TableClass()
print(redT.__color)'''

'''class TableClass:

    _mat = 'no mat'

    def __init__(self, color, height):
        self.height = height
        self.color = color

class RollTableClass(TableClass):

    def __init__(self,color,height,roll):
        super().__init__(color, height)
        self.roll = roll

test = RollTableClass('white',5, 100)
print(test.color)
print(test.height)
print(test.roll)'''


'''class powered():

    def __init__(self, x, n):
        self.x = x
        self.n = n

    def pow(self):
        return self.x ** self.n

    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def dif(a, b):
        return a - b


heatStation = powered(2, 10)
print(heatStation.pow())

print(powered.sum(15, 7))
print(powered.dif(15, 7))'''

'''class Color:

    def __int__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    def toHex(self):
        return '#02x%02x%02x' % (self.red, self.green. self.blue)

    def stats(self):
        return self.red + self.green + self.blue

class ColorAlpha(Color):
    alpha = 1

    def __init__(self, r, g, b, a):
        super().__init__(r, g, b)
        self.alpha = a

    def stats(self):
        return super().stats()+ self.alpha

test = ColorAlpha('r', 'g','b', 'a')
print(test.stats())
'''

'''
class Color:

    # red = 0
    # green = 0
    # blue = 0

    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

    def toHex(self):
        return '#%02x%02x%02x' % (self.red, self.green, self.blue)

l

    def stats(self):
        print(f"Red is {self.red}")
        print(f"Green is {self.green}")
        print(f"Blue is {self.blue}")

l


    def stats(self):
        return [f"Red is {self.red}", f"Green is {self.green}", f"Blue is {self.blue}"]


class ColorAlpha(Color):
    alpha = 1

    def __init__(self, r, g, b, a):
        super().__init__(r, g, b)
        self.alpha = a

    def stats(self):
        return super().stats()


gray = Color(80, 80, 80)

print(gray.toHex())

ted = ColorAlpha(255, 0, 0, 0.5)
print(ted.stats())'''

from math import pi

class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def doesExist(self):
        maxim = max(self.a,self.b,self.c)
        if(self.a + self.b + self.c - maxim > maxim):
            return True
        else:
            return False

circleOne = Circle(5)
print(circleOne.perimeter())
circleTwo = Circle(13443434)
print(circleTwo.perimeter())
