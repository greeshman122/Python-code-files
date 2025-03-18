# Base class
class Polygon:
    def __init__(self):
        pass

    def area(self):
        pass  # This will be overridden in the derived classes

# Derived class for Rectangle
class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

# Derived class for Triangle
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Derived class for Circle
class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

# Derived class for Square
class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Example usage
rectangle = Rectangle(12, 8)
triangle = Triangle(5, 10)
circle = Circle(7)
square = Square(6)

print(f"Rectangle Area: {rectangle.area()}")  # Output: 96
print(f"Triangle Area: {triangle.area()}")    # Output: 25.0
print(f"Circle Area: {circle.area():.2f}")    # Output: 153.94
print(f"Square Area: {square.area()}")        # Output: 36
