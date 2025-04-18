numbers = list(range(1, 10001))

equivalence_classes = {i: [] for i in range(5)}
for num in numbers:
    equivalence_classes[num % 5].append(num)

union_of_classes = set()
for eq_class in equivalence_classes.values():
    union_of_classes.update(eq_class)

is_valid = set(numbers) == union_of_classes

print("Equivalence Classes (mod 5):")
for key, value in equivalence_classes.items():
    print(f"Class [{key}]: {value[:10]} ... {value[-10:]}")

print("\nValidity Check:", "Valid" if is_valid else "Invalid")
