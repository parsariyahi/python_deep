class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    #We can name the 'self' everything we want

    def some_method(the_instance):
        return the_instance.width


r = Rectangle(10, 100)

print(r.area())
print(r.perimeter())
print(r.some_method())

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle width={self.width}, height={self.height}"

    def __repr__(self):
        return f"Rectange({self.width}, {self.height})"

    def __eq__(self, other: Rectangle) -> bool:
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return False

    def __lt__(self, other: Rectangle) :
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

r1 = Rectangle(10, 100)
r2 = Rectangle(10, 100)
r3 = Rectangle(20, 110)

print(r1 == r2)

print(r1 < r3)

print(r1)

print(repr(r1)) #The representation of that class


class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def __str__(self):
        return f"Rectangle width={self._width}, height={self._height}"

    def __repr__(self):
        return f"Rectange({self._width}, {self._height})"

# Pythonic way to write getter and setter

class Rectangle:

    # Each time we run self.width or self.height,
    # We run the getter and setter method.

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be positive")
        else:
            self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("Height must be positive")
        else:
            self._height = height

    def __str__(self):
        return f"Rectangle width={self._width}, height={self._height}"

    def __repr__(self):
        return f"Rectange({self._width}, {self._height})"