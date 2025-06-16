import pytest
from lesson_16.homework_16_2_correct import *

class TestFigure:

    rectangle_for_testing = Rectangle(7, 6)                       # a=42, p=26
    trapeze_for_testing = Trapeze(12, 10, 8)               # a=480, p=44
    right_triangle_for_testing = RightTriangle(4, 2, 7)  # a=4, p=13

    @classmethod
    def test_rectangle_area(cls):
        assert cls.rectangle_for_testing.area() == 42

    @classmethod
    def test_rectangle_perimeter(cls):
        assert cls.rectangle_for_testing.perimeter() == 26

    @classmethod
    def test_trapeze_area(cls):
        assert cls.trapeze_for_testing.area() == 480

    @classmethod
    def test_trapeze_perimeter(cls):
        assert cls.trapeze_for_testing.perimeter() == 44

    @classmethod
    def test_right_triangle_area(cls):
        assert cls.right_triangle_for_testing.area() == 4

    @classmethod
    def test_right_triangle_perimeter(cls):
        assert cls.right_triangle_for_testing.perimeter() == 13