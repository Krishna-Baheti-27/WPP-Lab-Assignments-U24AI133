import random

def find_longest_run_of_zeros(arr):
    max_run = 0
    current_run = 0

    for num in arr:
        if num == 0:
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0

    return max_run

# Generate 100 random integers (0 or 1)
random_numbers = [random.randint(0, 1) for _ in range(100)]

longest_run = find_longest_run_of_zeros(random_numbers)

print("Random numbers:", random_numbers)
print("Longest run of zeros:", longest_run)
