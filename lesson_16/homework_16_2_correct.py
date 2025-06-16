from abc import ABC, abstractmethod

class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Figure):

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return (self.__length + self.__width) * 2

class Trapeze(Figure):

    def __init__(self, length, width, height):
        self.__length = length
        self.__width = width
        self.__height = height

    def area(self):
        return (((self.__length * self.__width) / 2) * self.__height)

    def perimeter(self):
        return ((self.__length * 2) + (self.__width * 2))

class RightTriangle (Figure):
    def __init__(self, first_side, second_side, third_side):
        self.__first_side = first_side
        self.__second_side = second_side
        self.__third_side = third_side

    def area(self):
        return (self.__first_side * self.__second_side) / 2

    def perimeter(self):
        return (self.__first_side + self.__second_side + self.__third_side)


rectangle = Rectangle(5,10)
trapeze = Trapeze(10,7, 5)
right_triangle = RightTriangle(3,4, 6)
print(rectangle.area())            #50
print(rectangle.perimeter())       #30
print(trapeze.area())              #175
print(trapeze.perimeter())         #34
print(right_triangle.area())       #6
print(right_triangle.perimeter())  #13
