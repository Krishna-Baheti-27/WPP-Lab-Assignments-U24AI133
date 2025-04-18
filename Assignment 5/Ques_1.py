import math

def maximize_xor(l, r):
    max_xor = 0
    for a in range(l, r + 1):
        for b in range(a, r + 1):
            max_xor = max(max_xor, a ^ b)
    return max_xor

# Read inputs for maximizing XOR
l = int(input())
r = int(input())
print(maximize_xor(l, r))
