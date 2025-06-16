from abc import ABC, abstractmethod

class Figure(ABC):

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Figure):

    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.get_length() * self.get_width()

    def perimeter(self):
        return (self.get_length() + self.get_width()) * 2

class Trapeze(Figure):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def area(self):
        return (((self.get_length() * self.get_width()) / 2) * self.height)

    def perimeter(self):
        return ((self.get_length() * 2) + (self.get_width() * 2))

class RightTriangle (Figure):
    def __init__(self, length, width, third_side):
        super().__init__(length, width)
        self.third_side = third_side

    def area(self):
        return (self.get_length() * self.get_width()) / 2

    def perimeter(self):
        return (self.get_length() + self.get_width() + self.third_side)


rectangle = Rectangle(5,10)
trapeze = Trapeze(10,7, 5)
right_triangle = RightTriangle(3,4, 6)
print(rectangle.area())            #50
print(rectangle.perimeter())       #30
print(trapeze.area())              #175
print(trapeze.perimeter())         #34
print(right_triangle.area())       #6
print(right_triangle.perimeter())  #13
