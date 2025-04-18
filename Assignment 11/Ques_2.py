import pandas as pd

s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

upper_case = s.str.upper()
lower_case = s.str.lower()
string_length = s.str.len()

print("Upper Case:\n", upper_case)
print("\nLower Case:\n", lower_case)
print("\nString Length:\n", string_length)
