import sys

def is_fibonacci(n):
    a, b = 0, 1
    while b <= n:
        if b == n:
            return "IsFibo"
        a, b = b, a + b
    return "IsNotFibo"

# Read input
t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    results.append(is_fibonacci(n))

# Print all results after input is received
print("\n".join(results))
