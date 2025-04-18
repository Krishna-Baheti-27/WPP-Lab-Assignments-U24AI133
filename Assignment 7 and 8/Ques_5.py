import math

class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

print("Choose shape:")
print("1. Rectangle")
print("2. Circle")
choice = int(input("Enter your choice: "))

if choice == 1:
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    rect = Rectangle(length, width)
    print(f"Rectangle Area: {rect.area()}")
    print(f"Rectangle Perimeter: {rect.perimeter()}")

elif choice == 2:
    radius = float(input("Enter radius of circle: "))
    circ = Circle(radius)
    print(f"Circle Area: {circ.area()}")
    print(f"Circle Perimeter: {circ.perimeter()}")
else:
    print("Invalid choice.")