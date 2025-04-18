import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

points = []
print("Enter 10 points in 3D space (x, y, z):")
for i in range(10):
    x, y, z = map(float, input(f"Enter coordinates of point {i+1}: ").split())
    points.append((x, y, z))

nearest_neighbors = []
for i in range(len(points)):
    min_distance = float('inf')
    nearest_point = None
    for j in range(len(points)):
        if i != j:  # Avoid comparing the point with itself
            dist = euclidean_distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                nearest_point = points[j]
    nearest_neighbors.append((points[i], nearest_point))

print("\nPoint -> Nearest Neighbor")
for point, neighbor in nearest_neighbors:
    print(f"{point} -> {neighbor}")
