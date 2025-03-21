# Base class Polygon
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def get_sides(self):
        return self.sides

    def calculate_area(self):
        raise NotImplementedError("This method should be overridden in subclasses")

# Subclass for Triangle
class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__(3)
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

# Subclass for Rectangle
class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Subclass for Square
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

# Subclass for Circle
class Circle(Polygon):
    def __init__(self, radius):
        super().__init__(0)  # Circle has no sides
        self.radius = radius

    def calculate_area(self):
        import math
        return math.pi * self.radius**2

# Main program to demonstrate functionality
shapes = [
    Triangle(10, 5),
    Rectangle(4, 6),
    Square(4),
    Circle(7)
]

for shape in shapes:
    print(f"{shape.__class__.__name__}: Area = {shape.calculate_area()}")
