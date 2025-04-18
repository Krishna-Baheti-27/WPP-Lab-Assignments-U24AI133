import numpy as np

N = 10

cartesian_points = np.random.rand(N, 2) * 10

x, y = cartesian_points[:, 0], cartesian_points[:, 1]
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)

polar_points = np.column_stack((r, theta))

print("Cartesian Points:")
print(cartesian_points)
print("\nPolar Coordinates:")
print(polar_points)
