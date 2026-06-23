import math


class Shape:

    def __init__(self, color):
        self.color = color

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter()")

    def describe(self):
        return f"A {self.color} {type(self).__name__} with area {self.area():.2f}"


class Circle(Shape):

    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):

    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):

    def __init__(self, color, a, b, c):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(
            s * (s - self.a) * (s - self.b) * (s - self.c)
        )

    def perimeter(self):
        return self.a + self.b + self.c