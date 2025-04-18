def bigger_is_greater(w):
    w = list(w)
    i = len(w) - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1
    if i == -1:
        return "no answer"
    
    j = len(w) - 1
    while w[j] <= w[i]:
        j -= 1
    
    w[i], w[j] = w[j], w[i]
    w = w[:i + 1] + sorted(w[i + 1:])
    
    return "".join(w)

# Read inputs for Bigger is Greater
t = int(input())
words = [input().strip() for _ in range(t)]
results = [bigger_is_greater(w) for w in words]

for result in results:
    print(result)
