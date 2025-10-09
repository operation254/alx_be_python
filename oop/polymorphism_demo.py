# oop/polymorphism_demo.py
import math


class Shape:
    """Base shape: subclasses must implement area()."""
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def area(self) -> float:
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = float(radius)

    def area(self) -> float:
        return math.pi * (self.radius ** 2)
