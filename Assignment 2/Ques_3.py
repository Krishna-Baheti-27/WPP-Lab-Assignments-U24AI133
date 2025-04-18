def find_digits(N):
    count = 0
    N_str = str(N)
    for digit in N_str:
        if digit != '0' and N % int(digit) == 0:
            count += 1
    return count

T = int(input())  # Read the number of test cases

# Initialize a list to store results
results = []

# Loop through each test case
for _ in range(T):
    # Read the number N for the test case
    N = int(input())
    # Store the result in the list
    results.append(find_digits(N))

# Print all the results after all inputs are processed
for result in results:
    print(result)
