# Define a class named Cylinder. 
# Define:
# - the init() method to initialize instances of the Cylinder class with two parameters: height and radius, both defaulting to 1.
# - a method named volume() that calculates and returns the volume of the cylinder using the formula  π∗r2∗h 
# - a method named surface_area() that calculates and returns the surface area of the cylinder.
# Calculate:
# - the area of each circular base using the formula  π∗r2 
# - the lateral surface area using the formula  2∗π∗r∗h

import math
 
class Cylinder:

  pi = math.pi

  def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

  def volume(self):
      return self.pi * self.radius ** 2 * self.height

  def surface_area(self):
      return (2 * (self.pi * self.radius ** 2) + (2 * self.pi * self.radius * self.height))
      

c = Cylinder(2,3)

print("Volume of cylinder: ", c.volume())
print("Surface area: ", c.surface_area())
