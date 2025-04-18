def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Example usage
num = int( input('Enter the number : '))
print(digital_root(num))  # Output: 2
