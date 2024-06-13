# Create a Rectangle class with the following specifications:
# - it should have two attributes: width and height, both initialized to 1 by default.
# - it should have an __init__ method that takes width and height as parameters and sets the attributes accordingly.
# - it should have a method named area that calculates and returns the area of the rectangle.
# - it should have a method named perimeter that calculates and returns the perimeter of the rectangle.
# - it should have a method named is_square that returns True if the rectangle is a square (i.e., width equals height), and False otherwise.

class Rectangle:

    def __init__(self, width=1, length=1):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def is_square(self):
      return self.width == self.length

r = Rectangle(4, 6)

print("Area of rectangle: ", r.area())
print("Perimeter of rectangle: ", r.perimeter())
print("Is rectangle a square? ", r.is_square())