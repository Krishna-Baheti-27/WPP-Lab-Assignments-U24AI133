import math

def count_square_integers(a, b):
    # Find the smallest integer whose square is >= a
    start = math.ceil(math.sqrt(a))
    # Find the largest integer whose square is <= b
    end = math.floor(math.sqrt(b))
    # Count the integers in this range
    return max(0, end - start + 1)

t = int(input())  # Number of test cases
results = []
for _ in range(t):
    a, b = map(int, input().split())
    results.append(count_square_integers(a, b))

for result in results:
    print(result)
