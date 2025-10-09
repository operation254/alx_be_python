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

    def area(self):
        area = self.length * self.width
        # If it's a whole number (e.g., 50.0), return an int so it prints as 50
        return int(area) if float(area).is_integer() else area


class Circle(Shape):
    def __init__(self, radius):
        self.radius = float(radius)

    def area(self) -> float:
        return math.pi * (self.radius ** 2)
