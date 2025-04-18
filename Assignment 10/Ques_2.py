import random

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col):
    if col >= len(board):
        return True

    rows = list(range(len(board)))
    random.shuffle(rows)

    for i in rows:
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1):
                return True
            board[i][col] = 0

    return False

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False

    print_board(board)
    return True

def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()

if __name__ == "__main__":
    n = 8  # You can change the size of the board here
    solve_n_queens(n)