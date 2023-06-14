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