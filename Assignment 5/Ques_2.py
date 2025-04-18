def halloween_party(k):
    return (k // 2) * (k - (k // 2))

# Read inputs for Halloween Party
t = int(input())
k_values = list(map(int, input().split()))
for k in k_values:
    print(halloween_party(k))
