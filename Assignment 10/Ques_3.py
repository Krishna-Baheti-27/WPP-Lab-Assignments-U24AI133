import numpy as np

def generate_magic_square(n):
    if n % 2 == 1:
        magic_square = np.zeros((n, n), dtype=int)
        i, j = 0, n // 2
        for num in range(1, n * n + 1):
            magic_square[i, j] = num
            new_i, new_j = (i - 1) % n, (j + 1) % n
            if magic_square[new_i, new_j]:
                i += 1
            else:
                i, j = new_i, new_j
    elif n % 4 == 0:
        magic_square = np.arange(1, n * n + 1).reshape(n, n)
        mask = np.array([[((i % 4 == j % 4) or ((i % 4 + j % 4) == 3)) for j in range(n)] for i in range(n)])
        magic_square[mask], magic_square[~mask] = magic_square[~mask], magic_square[mask]
    else:
        half_n = n // 2
        sub_square_size = half_n * half_n
        sub_square = generate_magic_square(half_n)
        magic_square = np.zeros((n, n), dtype=int)
        magic_square[:half_n, :half_n] = sub_square
        magic_square[half_n:, half_n:] = sub_square + sub_square_size
        magic_square[:half_n, half_n:] = sub_square + 2 * sub_square_size
        magic_square[half_n:, :half_n] = sub_square + 3 * sub_square_size
        mid_cols = n // 4
        for i in range(half_n):
            for j in range(mid_cols):
                if j == 0 and i == half_n // 2:
                    continue
                magic_square[i, j], magic_square[i + half_n, j] = magic_square[i + half_n, j], magic_square[i, j]
                magic_square[i, j + half_n + mid_cols], magic_square[i + half_n, j + half_n + mid_cols] = (
                    magic_square[i + half_n, j + half_n + mid_cols], magic_square[i, j + half_n + mid_cols]
                )
    return magic_square

sizes = [4, 5, 6, 7, 8]
for n in sizes:
    print(f"Magic Square for N={n}:")
    print(generate_magic_square(n))
    print("\n")
