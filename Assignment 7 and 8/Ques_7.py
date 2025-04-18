import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def rotation(self):
        return math.degrees(math.atan2(self.y, self.x))

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def cross_product(self, other):
        return self.x * other.y - self.y * other.x

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

print("Select vector type:")
print("1. 2D Vector")
print("2. 3D Vector")
choice = int(input("Enter your choice: "))

if choice == 1:
    x1, y1 = map(float, input("Enter first 2D vector (x y): ").split())
    x2, y2 = map(float, input("Enter second 2D vector (x y): ").split())
    vec2d_1 = Vector2D(x1, y1)
    vec2d_2 = Vector2D(x2, y2)
    print(f"2D Magnitude: {vec2d_1.magnitude()}")
    print(f"2D Rotation: {vec2d_1.rotation()} degrees")
    print(f"2D Distance: {vec2d_1.distance(vec2d_2)}")
    print(f"2D Dot Product: {vec2d_1.dot_product(vec2d_2)}")
    print(f"2D Cross Product: {vec2d_1.cross_product(vec2d_2)}")

elif choice == 2:
    x1, y1, z1 = map(float, input("Enter first 3D vector (x y z): ").split())
    x2, y2, z2 = map(float, input("Enter second 3D vector (x y z): ").split())
    vec3d_1 = Vector3D(x1, y1, z1)
    vec3d_2 = Vector3D(x2, y2, z2)
    print(f"3D Magnitude: {vec3d_1.magnitude()}")
    print(f"3D Dot Product: {vec3d_1.dot_product(vec3d_2)}")
    cross_prod = vec3d_1.cross_product(vec3d_2)
    print(f"3D Cross Product: ({cross_prod.x}, {cross_prod.y}, {cross_prod.z})")
else:
    print("Invalid choice.")