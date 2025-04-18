import sys

def utopian_tree(n):
    height = 1
    for cycle in range(n):
        if cycle % 2 == 0:
            height *= 2  # Monsoon (double the height)
        else:
            height += 1  # Summer (increase by 1 meter)
    return height

# Read input
t = int(sys.stdin.readline().strip())
results = []
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    results.append(str(utopian_tree(n)))

# Print all results after input is received
print("\n".join(results))
