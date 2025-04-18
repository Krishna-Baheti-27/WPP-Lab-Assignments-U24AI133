import numpy as np

def format_strings(arr):
    str_arr = np.array(arr, dtype=str)
    
    centered = np.array([s.center(15, '_') for s in str_arr])
    left_justified = np.array([s.ljust(15, '_') for s in str_arr])
    right_justified = np.array([s.rjust(15, '_') for s in str_arr])
    
    return centered, left_justified, right_justified

arr = np.array(["Hello", "World", "NumPy", "Python"])
centered, left_justified, right_justified = format_strings(arr)

print("Centered:")
print(centered)
print("\nLeft-Justified:")
print(left_justified)
print("\nRight-Justified:")
print(right_justified)
