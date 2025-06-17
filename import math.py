import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

try:
    user_radius = float(input("Enter the radius of the circle: "))
    circle = Circle(user_radius)

    print(f"Area of the circle: {circle.area():.2f}")
    print(f"Perimeter of the circle: {circle.perimeter():.2f}")
except ValueError:
    print("Please enter a valid number for radius.")
